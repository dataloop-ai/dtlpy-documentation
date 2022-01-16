# Create and Deploy a package of several functions

## Write your code
The following code consists of two image-manipulation methods:
1. RGB to grayscale over an image
1. Histogram equalization over an image

You can either download it as a Python file from here main.py or copy it from our Git repository

```
import dtlpy as dl
import cv2
import numpy as np
class ImageProcess(dl.BaseServiceRunner):
    @staticmethod
    def rgb2gray(item: dl.Item):
        """
        Function to convert RGB image to GRAY
        Will also add a modality to the original item
        :param item: dl.Item to convert
        :return: None
        """
        buffer = item.download(save_locally=False)
        bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        gray_item = item.dataset.items.upload(local_path=gray,
                                              remote_path='/gray' + item.dir,
                                              remote_name=item.filename)
        # add modality
        item.modalities.create(name='gray',
                               ref=gray_item.id)
        item.update(system_metadata=True)
    @staticmethod
    def clahe_equalization(item: dl.Item):
        """
        Function to perform histogram equalization (CLAHE)
        Will add a modality to the original item
        Based on opencv https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
        :param item: dl.Item to convert
        :return: None
        """
        buffer = item.download(save_locally=False)
        bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
        # create a CLAHE object (Arguments are optional).
        lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
        lab_planes = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        lab_planes[0] = clahe.apply(lab_planes[0])
        lab = cv2.merge(lab_planes)
        bgr_equalized = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
        bgr_equalized_item = item.dataset.items.upload(local_path=bgr_equalized,
                                                       remote_path='/equ' + item.dir,
                                                       remote_name=item.filename)
        # add modality
        item.modalities.create(name='equ',
                               ref=bgr_equalized_item.id)
        item.update(system_metadata=True)
```
## Define the module
You can define multiple different modules in a package. One of the incentives is to have a single code base that can be used by a number of services (for different applications).

When creating a service from that package, you will need to define which module the service will serve (a service can only serve a single module with all its functions)
```
import dtlpy as dl
modules = [dl.PackageModule(name='image-processing-module',
                            entry_point='main.py',
                            class_name='ImageProcess',
                            functions=[dl.PackageFunction(name='rgb2gray',
                                                          description='Converting RGN to gray',
                                                          inputs=[dl.FunctionIO(type=dl.PackageInputType.ITEM,
                                                                                name='item')]),
                                       dl.PackageFunction(name='clahe_equalization',
                                                          description='CLAHE histogram equalization',
                                                          inputs=[dl.FunctionIO(type=dl.PackageInputType.ITEM,
                                                                                name='item')])
                                       ])]
```
## Push the package
Now we have all our files in one place and we can push the package:

```
project_name = 'MyProject'
src_path = 'functions/opencv_functions'
project = dl.projects.get(project_name=project_name)
package = project.packages.push(package_name='image-processing',
                                modules=modules,
                                src_path=src_path)
```
## Deploy a service
The package is now ready to be deployed to the Dataloop Platform:
```
service = package.services.deploy(service_name='image-processing',
                                  runtime=dl.KubernetesRuntime(concurrency=32),
                                  module_name='image-processing-module')
```
## Trigger the service
Once the service is up, we can configure a trigger to automatically run the image manipulation functions whenever a given criterion is met.
Let’s set the following trigger: “an item is uploaded to the platform”

```
trigger = service.triggers.create(name='image-processing',
                                  execution_mode=dl.TriggerExecutionMode.ONCE,
                                  resource=dl.TriggerResource.ITEM,
                                  actions=dl.TriggerAction.CREATED,
                                  filters=dl.Filters(field='dir', values='/incoming'))
```
## Execute the function
Now we can upload an image to a dataset to trigger our service:
```
execution = service.execute(execution_input=[dl.FunctionIO(type=dl.PackageInputType.ITEM,
                                                           name='item',
                                                           value='<item_id>')])
execution = execution.wait()
print(execution.status)
```
## Review the function's logs
We can also review the execution logs history:
```
execution.logs()
```
## Add a slot UI of the function to the UI platform

Assigning a function to UI slots creates a button in the Dataloop platform, allowing users to quickly
invoke the FaaS function when needed, in the dataset browser or studio.

To define a slot that will be displayed in the image studio, let's run this:

```
slots = [
    dl.PackageSlot(
        module_name='image-processing',
        function_name='rgb2gray',
        display_name='RGB2GRAY',
        post_action=dl.SlotPostAction(type=dl.SlotPostActionType.NO_ACTION),
        display_scopes=[
            dl.SlotDisplayScope(
                resource=dl.SlotDisplayScopeResource.ITEM,
                filters={}
            )
        ]
    ),
]
package.slots = slots
package.update()
service.package_revision = package.version
service.update()
```
