def section1():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    item = dataset.items.get(filepath='/my_item.mp4')


def section2():
    annotation = dl.Annotation.new(item=item)
    # Span the annotation over 100 frames. Change this or use a different approach based on your context
    for i_frame in range(100):
        # go over 100 frame
        annotation.add_frame(annotation_definition=dl.Box(top=2 * i_frame,
                                                          left=2 * (i_frame + 10),
                                                          bottom=2 * (i_frame + 50),
                                                          right=2 * (i_frame + 100),
                                                          label="my-label"),
                             frame_num=i_frame,  # set the frame for the annotation
                             )
    # upload to platform
    annotation.upload()


def section3():
    # create annotation builder
    builder = item.annotations.builder()
    for i_frame in range(100):
        # go over 100 frames
        for i_detection in range(10):
            # for each frame we have 10 different detections (location is just for the example)
            builder.add(annotation_definition=dl.Box(top=2 * i_frame,
                                                     left=2 * i_detection,
                                                     bottom=2 * i_frame + 10,
                                                     right=2 * i_detection + 100,
                                                     label="my-label"),
                        # set the frame for the annotation
                        frame_num=i_frame,
                        # need to input the element id to create the connection between frames
                        object_id=i_detection + 1,
                        )
    # Upload the annotations to platform
    item.annotations.upload(builder)


def section4():
    for annotation in item.annotations.list():
        print(annotation.object_id)
        for key in annotation.frames:
            frame = annotation.frames[key]
            print(frame.left, frame.right, frame.top, frame.bottom)


def section5():
    dl.utilities.Videos.video_snapshots_generator(item=item, frame_interval=30)


def section6():
    from dtlpy.utilities.videos.video_player import VideoPlayer
    VideoPlayer(project_name=project_name,
                dataset_name=dataset_name,
                item_filepath=item_filepath)


def section7():
    import matplotlib.pyplot as plt
    # Get from platform
    annotations = item.annotations.list()
    # Plot the annotations in frame 55 of the created annotations
    frame_annotation = annotations.get_frame(frame_num=55)
    plt.figure()
    plt.imshow(frame_annotation.show())
    plt.title(frame_annotation.label)
    # Play video with the Dataloop video player
    annotations.video_player()
