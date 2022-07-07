import dtlpy as dl
import numpy as np
import logging
import cv2

logger = logging.getLogger("Tracker")

logging.getLogger("filelock").setLevel("WARNING")


class Tracker(dl.BaseServiceRunner):
    """
    Service runner class

    """

    def __init__(self):
        """
        Here is the place to load everything we need in when the process starts
        """
        logger.info(f"tracker loaded, opencv version: {cv2.__version__}")

    def run(self, dl, item_stream_url, bbs, start_frame, frame_duration=60, progress=None):
        """
        The function that will be called by the UI when the tracker is

        :param item_stream_url: the url of the video. we need to stream it to avoid downloading each time
        :param bbs: a dictionary of the bounding box to be tracked. keys are annotation ids, values are the Dataloop annotations.
                    for example, for dl.Box tracker in will be [{"x": x, "y":y}, {"x": x, "y":y}]
        :param start_frame: frame number to start the track from. the annotation should be for this frame.
        :param frame_duration: number of frames to track.
        :param progress: dl.Progress object
        :return:
        """
        # open issue
        if dl is None:
            import dtlpy as dl

        try:
            if not isinstance(bbs, dict):
                raise ValueError("input 'bboxs' must be a dictionary of {id:bbox}")
            logger.info("Starting...")
            logger.info("Video url: {}".format(item_stream_url))
            # stream the video without downloading it
            cap = cv2.VideoCapture("{}?jwt={}".format(item_stream_url, dl.token()))
            logger.info("video loaded! video url: {}".format(item_stream_url))
            if not cap.isOpened():
                raise ValueError("cant open video stream. item id: {}".format(item_stream_url))

            # set the frame number to start from
            cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

            output_annotations_dict = dict()
            # the the first frame of each annotation to start the track from
            for ann_id, bb in bbs.items():
                output_annotations_dict[ann_id] = {start_frame: bb}

            # tracker for each annotations
            trackers = dict()

            # start the track! going frame by frame from start_frame
            for i_frame in range(0, frame_duration):
                logger.info("processing frame #{}".format(start_frame + i_frame))
                ret, frame = cap.read()
                if not ret:
                    break

                # for each frame - going over all boxes
                for bbox_id, frames in output_annotations_dict.items():
                    if i_frame == 0:
                        # first frame - init tracker
                        trackers[bbox_id] = cv2.TrackerKCF_create()
                        bb = frames[start_frame]
                        track_bb = np.asarray([bb[0]["x"], bb[0]["y"],
                                               bb[1]["x"] - bb[0]["x"], bb[1]["y"] - bb[0]["y"]]).astype("int")
                        ok = trackers[bbox_id].init(frame, track_bb)

                    else:
                        # other that first frame - do the track
                        ok, bbox = trackers[bbox_id].update(frame)
                        if not ok:
                            # don't save the frame is the tracker was unable to track
                            continue
                        # save out BB (Dataloop format)
                        frames[start_frame + i_frame] = [
                            {"x": int(bbox[0]), "y": int(bbox[1])},
                            {"x": int(bbox[0] + bbox[2]), "y": int(bbox[1] + bbox[3])}
                        ]

            logger.info("finished.")

        except Exception:
            logger.exception("failed during track")
            raise
        return output_annotations_dict


def deploy():
    import dtlpy as dl
    # Set project name and service name
    package_name = "custom-tracker"
    project_name = "Frog Tracking"
    project = dl.projects.get(project_name=project_name)

    # Push package
    modules = [
        dl.PackageModule(name="default_module",
                         entry_point="main.py",
                         class_name="Tracker",
                         functions=[dl.PackageFunction(
                             name="run",
                             inputs=[dl.FunctionIO(type="Json", name="item_stream_url"),
                                     dl.FunctionIO(type="Json", name="bbs"),
                                     dl.FunctionIO(type="Json", name="start_frame"),
                                     dl.FunctionIO(type="Json", name="frame_duration"),
                                     dl.FunctionIO(type="Json", name="dl")],
                             outputs=[],
                             description="Custom BB tracker"),
                         ])]
    package = project.packages.push(package_name=package_name,
                                    modules=modules,
                                    src_path="functions/custom_tracker",
                                    requirements=[dl.PackageRequirement(name="opencv_python",
                                                                        version="4.5.2.54"),
                                                  dl.PackageRequirement(name="opencv-contrib-python",
                                                                        version="4.5.2.54")]
                                    )

    # Deploy service
    tracker_service = package.services.deploy(
        service_name=package.name,
        execution_timeout=60,
        max_attempts=1,
        module_name="default_module",
        runtime=dl.KubernetesRuntime(pod_type=dl.InstanceCatalog.REGULAR_XS,
                                     concurrency=10,
                                     autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                         min_replicas=1,
                                         max_replicas=1)
                                     )
    )

    # Add to datasets recipe
    dataset = project.datasets.get("custom tracker")
    recipe = dataset.recipes.list()[0]
    recipe.metadata["system"]["trackerSettings"] = {"serviceName": tracker_service.name,
                                                    "projectId": tracker_service.project_id,
                                                    "maxAnnotations": 50
                                                    }
    recipe.update(True)


def local_test():
    import dtlpy as dl

    # get item
    item = dl.items.get(item_id="626e65c69271799f1885e144")

    # init the tracker locally
    tracker = Tracker()

    # set the inputs
    item_stream_url = item.stream
    ann = item.annotations.list()[0]
    bbs = {ann.id: ann.to_json()["coordinates"]}
    start_frame = 0
    frame_duration = 90

    # make the call
    results = tracker.run(item_stream_url=item_stream_url,
                          bbs=bbs,
                          start_frame=start_frame,
                          frame_duration=frame_duration)

    # upload the results to the annotation
    for a_id, frames in results.items():
        annotation = item.annotations.get(a_id)
        for i_frame, box in frames.items():
            annotation.add_frame(frame_num=i_frame,
                                 annotation_definition=dl.Box(left=box[0]["x"],
                                                              right=box[1]["x"],
                                                              top=box[0]["y"],
                                                              bottom=box[1]["y"],
                                                              label=annotation.label))
        annotation.update(True)
