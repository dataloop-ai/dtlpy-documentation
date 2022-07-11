# Using Custom AI Tracker
Based on [this](https://learnopencv.com/object-tracking-using-opencv-cpp-python) OpenCV example.

This is an example for using your own tracker on video.  
The tracker is a Dataloop FaaS that receives the frame and bounding box from the UI when a user enables the AI tracker.
The returned results is taken by the UI and shows the annotations oin the Annotation Studio.

NOTE you need to have opencv version (4.5.2.54 or similar) in order to read the video stream directly

## Function inputs:

item_stream_url: the url of the video. we need to stream it to avoid downloading each time   
bbs: a dictionary of the bounding box to be tracked. keys are annotation ids, values are the Dataloop annotations. for
example, for dl.Box tracker in will be `[{"x": x, "y":y}, {"x": x, "y":y}]`.     
start_frame: frame number to start the track from. the annotation should be for this frame.  
frame_duration: number of frames to track  
progress: dl.Progress object

## Function outputs:

A dictionary with the following format:

```
{annotation_id: {frame_num: bb_coordinated}}
```

## Open Issues:

1. need to change the name of the tracker (not the default Ai Tracker)
1. need to add the tracker slot to WOZ (not in the recipe)
1. "dl" is a required input (shouldn't be) and is None in the run (why?)

## Deploying the function

As usual, we need to push the package and deploy the function:

```python
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
```

## Setting the recipe to use this tracker

This is required to make the current Dataset and Recipe point the custom tracker:

```python
dataset = project.datasets.get("custom tracker")
recipe = dataset.recipes.list()[0]
recipe.metadata["system"]["trackerSettings"] = {"serviceName": tracker_service.name,
                                                "projectId": tracker_service.project_id,
                                                "maxAnnotations": 50
                                                }
recipe.update(True)
```

