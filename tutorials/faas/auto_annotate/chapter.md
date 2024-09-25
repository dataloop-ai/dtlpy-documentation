# Example: Model Annotations Service  
This tutorial demonstrates creating and deploying a service that pre-annotates an items before manual annotation work is performed, as part of active-learning process.  
  
## Service Code  
Your code can perform any action you need toe execute as part of pre-annotating items for example:  
- Access a remote server/API to retrieve annotations  
- Run your algorithm or ML model as a service in Dataloop FaaS  
  
In this example we use a simple face detection algorithm that uses Cv2 and Caffe model  
  

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
## Define the module  
In this example, we load the model in the init method, which runs only once at deployment time, saving us time bu not loading on each execution/  
This can inputs are attributes that we want the service to include for its entire lifetime. In this case, it's the model and weights files we want the service to use and the confidence limit for accepting detections.  
  

```python
module = dl.PackageModule(
    init_inputs=[
        dl.FunctionIO(name='model_filename', type=dl.PackageInputType.STRING),
        dl.FunctionIO(name='prototxt_filename', type=dl.PackageInputType.STRING),
        dl.FunctionIO(name='min_confidence', type=dl.PackageInputType.FLOAT)
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
numpy == 1.18
opencv - python == 3.4
```
## Model and weights files  
The function uses 2 files containing the model and its weights for inferencing detections. We need to have these files at the same folder as the entry point.  
To get these files please download them here.  
https://storage.googleapis.com/dtlpy/model_assets/faas-tutorial/model_weights.zip  
  
##Package Requirements  
Our package's codebase uses 2 Python libraries that are not standard ones. Therefore, we need to make sure they are pre-installed before running the entry point. One way to do so is to use a custom Docker Image (information on this process can be found here. The other way is to add a requirements.txt file to the package codebase. To do so, simply add the following requirements.txt file in the same folder of the entry point (main.py):  
https://docs.dataloop.ai/docs/service-runtime#customimage  

```python
package = project.packages.push(
    src_path='<path to folder containing the codebase>',
    package_name='face-detector',
    modules=[module]
)
```
## Push the Package  
Make sure you have the following files in one directory:  
- main.py  
- requirements.txt  
- res10_300x300_ssd_iter_140000.caffemodel  
- deploy.prototxt.txt  
  
Run this to push your package:  

```python
service = package.deploy(
    service_name='face-detector',
    init_input=[
        dl.FunctionIO(name='model_filename',
                      type=dl.PackageInputType.STRING,
                      value='res10_300x300_ssd_iter_140000.caffemodel'),
        dl.FunctionIO(name='prototxt_filename',
                      type=dl.PackageInputType.STRING,
                      value='deploy.prototxt.txt'),
        dl.FunctionIO(name='min_confidence',
                      type=dl.PackageInputType.FLOAT,
                      value=0.5)
    ],
    runtime=dl.KubernetesRuntime(concurrency=1)
    # The runtime argument Concurrency=1 means that only one execution can run at a time (no parallel executions).
)
```
## Deploy The  Service  
The package is now ready to be deployed as a service in the Dataloop Platform.  
Whenever executed, your package will run as a service on default instance type. Review the service configuration to configure it to your needs, for example  
- Change instance-type to use stronger instances with more memory, CPU and GPU  
- Increase auto-scaling to handle larger loads  
- Increase timeouts to allow longer execution time  
  
  

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
## Trigger the Service  
Once the service is deployed, we can create a trigger to run it automatically when a certain event occurs.  
In our example we trigger the face-detection service whenever an item is uploaded to the platform.  
Consider using other triggers or different ways to run you service:  
- Add the services to a FaaS-node in a pipeline, before annotation tasks  
- Use DQL trigger to run only on specific datasets, or in specific tasks  
- Run the service when an item is updated  

```python
self.package.artifacts.download(artifact_name=artifact_filename,
                                local_path=full_weight_path)
```
## Uploading Model Weights as Artifacts  
Large data files such as ML model weights can be too big to include in a package. These and other large files can be uploaded as artifact.  
  
