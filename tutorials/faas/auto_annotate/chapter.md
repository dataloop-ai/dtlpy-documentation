## Step-by-step: Setting up auto-annotation model  
This tutorial explains step-by-step how to upload your model to the Dataloop platform and use it for auto annotate any item  
  
### Your Model  
Following this example you can use your own model, or the sample one presented below.  
It uses CV2 and Caffe for basic face detection.  

```python
import numpy as np
import os
import cv2
import dtlpy as dl
class ServiceRunner:
    def __init__(self,
                 model_filename: str,
                 prototxt_filename: str,
                 min_confidence: float):
        prototxt = os.path.join(os.getcwd(), prototxt_filename)
        weights = os.path.join(os.getcwd(), model_filename)
        print("[INFO] loading model...")
        self.net = cv2.dnn.readNetFromCaffe(prototxt, weights)
        self.min_confidence = min_confidence
    def detect(self, item: dl.Item):
        print("[INFO] downloading image...")
        filename = item.download()
        try:
            # load the input image and construct an input blob for the image
            # by resizing to a fixed 300x300 pixels and then normalizing it
            print("[INFO] opening image...")
            image = cv2.imread(filename)
            (h, w) = image.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(image,
                                                    (300, 300)), 1.0,
                                         (300, 300),
                                         (104.0, 177.0, 123.0))
            # pass the blob through the network and obtain the detections and
            # predictions
            print("[INFO] computing object detections...")
            self.net.setInput(blob)
            detections = self.net.forward()
            # create annotation builder to add annotations to item
            print("[INFO] uploading annotations...")
            builder = item.annotations.builder()
            # loop over the detections
            for i in range(0, detections.shape[2]):
                # extract the confidence (i.e., probability) associated with the
                # prediction
                confidence = detections[0, 0, i, 2]
                # filter out weak detections by ensuring the `confidence` is
                # greater than the minimum confidence
                if confidence > self.min_confidence:
                    # compute the (x, y)-coordinates of the bounding box for the
                    # object
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    # draw the bounding box of the face along with the associated
                    # probability
                    builder.add(
                        annotation_definition=dl.Box(
                            top=startY,
                            left=startX,
                            right=endX,
                            bottom=endY,
                            label='person'
                        ),
                        model_info={
                            'name': 'Caffe',
                            'confidence': confidence
                        }
                    )
                    # upload annotations
            builder.upload()
            print("[INFO] Done!")
        finally:
            os.remove(filename)
```
### Define the module  
In this example, we load the model in the init method.  
This method runs only once at deployment time. This can save us time by avoiding to load the model at each execution.  
The init inputs are attributes that we want the service to include for its entire lifetime.  
In this case, it's the model and weights files we want the service to use and the confidence limit of which to accept detections.  
  

```python
module = dl.PackageModule(
    init_inputs=[
        dl.FunctionIO(name='model_filename', type=dl.PackageInputType.JSON),
        dl.FunctionIO(name='prototxt_filename', type=dl.PackageInputType.JSON),
        dl.FunctionIO(name='min_confidence', type=dl.PackageInputType.JSON)
    ],
    functions=[
        dl.PackageFunction(
            name='detect',
            description='OpenCV face detection using Caffe model',
            inputs=[
                dl.FunctionIO(name='item', type=dl.PackageInputType.ITEM)
            ]
        )
    ]
)
```

```python
...
```
### Weights File  
  
The function uses 2 files that hold the model and weight to run the detection.  
We need to have these files at the same folder as the entry point.  
To get these files please download them here.  

```python
...
# numpy == 1.18
# .1
# opencv - python == 3.4
# .2
# .17
```
### Package Requirements  
  
Our package's codebase uses 2 Python libraries that are not standard libraries.  
Therefore, we need to make sure they are pre-installed before running the entry point.  
One way to do so is to use a custom Docker Image (information on this process can be found here.  
The other way is to add a requirements.txt file to the package codebase.  
To do so, simply add the following requirements.txt file in the same folder of the entry point (main.py):  

```python
package = project.packages.push(
    src_path='<path to folder containing the codebase>',
    package_name='face-detector',
    modules=[module]
)
```
### Push The Package  
Now we have all our files in one place:  
- main.py  
- requirements.txt  
- res10_300x300_ssd_iter_140000.caffemodel  
- deploy.prototxt.txt  
  
Time to push the package:  
  

```python
service = package.deploy(
    service_name='face-detector',
    init_input=[
        dl.FunctionIO(name='model_filename',
                      type=dl.PackageInputType.JSON,
                      value='res10_300x300_ssd_iter_140000.caffemodel'),
        dl.FunctionIO(name='prototxt_filename',
                      type=dl.PackageInputType.JSON,
                      value='deploy.prototxt.txt'),
        dl.FunctionIO(name='min_confidence',
                      type=dl.PackageInputType.JSON,
                      value=0.5)
    ],
    runtime=dl.KubernetesRuntime(concurrency=1)
)
```
### Deploy A Service  
The package is now ready to be deployed to the Dataloop Platform.  
The runtime argument here is the service configuration. Concurrency=1 means that only one execution can run at a time (no parallel executions).  
  

```python
filters = dl.Filters(resource=dl.FiltersResource.ITEM)
filters.add(field='metadata.system.mimetype', values='image*')
trigger = service.triggers.create(
    name='face-detector',
    function_name="detect",
    resource=dl.TriggerResource.ITEM,
    actions=dl.TriggerAction.CREATED,
    filters=filters
)
```
### Model Weights As Artifacts  
When working with AI, we have the package with the model code on one hand and the weight file (the results of training the model) on the other hand.  
The model needs to load the weight file to be able to identify the data.  
When writing FaaS (Function as a Service), we create a package with our code. Since the weight file can be very large, we do not want to push such a large file into the package; therefore, we use data objects called artifacts.  
See this example how to upload model weights as artifacts.  
  
