# Using Custom AI Tracker

Based on [this](https://learnopencv.com/object-tracking-using-opencv-cpp-python) OpenCV example.

This is an example for using your own tracker on video.  
The tracker is a Dataloop FaaS that receives the frame and bounding box from the UI when a user enables the AI
tracker.  
The returned results is taken by the UI and shows the annotations in the Annotation Studio.

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

## Deploying the function

Create a `dataloop.json` manifest in this directory (see the one in the repo). Then from the script directory:

```python
import os
import dtlpy as dl

project_name = "Frog Tracking"
project = dl.projects.get(project_name=project_name)

script_dir = os.path.dirname(os.path.abspath(__file__))
dpk = project.dpks.publish(
    manifest_filepath=os.path.join(script_dir, 'dataloop.json'),
    local_path=script_dir
)
app = project.apps.install(dpk=dpk)

tracker_service = project.services.get(service_name="custom-tracker")
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

