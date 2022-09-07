# Multiple Functions and Modules  
## Multiple Functions  
### Create and Deploy a Package of Several Functions  
First, login to the Dataloop platform:  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
```
Let’s define the project and dataset you will work with in this tutorial.  
To create a new project and dataset:  

```python
project = dl.projects.create(project_name='project-sdk-tutorial')
project.datasets.create(dataset_name='dataset-sdk-tutorial')
```
To use an existing project and dataset:  

```python
project = dl.projects.get(project_name='project-sdk-tutorial')
dataset = project.datasets.get(dataset_name='dataset-sdk-tutorial')
```
### Write your code  
The following code consists of two image-manipulation methods:  
* RGB to grayscale over an image  
* CLAHE Histogram Equalization over an image - Contrast Limited Adaptive Histogram Equalization (CLAHE) to equalize images  
  
To proceed with this tutorial, copy the following code and save it as a main.py file.  

```python
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
### Define the module  
Multiple functions may be defined in a single package under a “module” entity. This way you will be able to use a single codebase for various services.  
  
Here, we will create a module containing the two functions we discussed. The “main.py” file you downloaded is defined as the module entry point. Later, you will specify its directory file path.  

```python
modules = [dl.PackageModule(name='image-processing-module',
                            entry_point='main.py',
                            class_name='ImageProcess',
                            functions=[dl.PackageFunction(name='rgb2gray',
                                                          description='Converting RGB to gray',
                                                          inputs=[dl.FunctionIO(type=dl.PackageInputType.ITEM,
                                                                                name='item')]),
                                       dl.PackageFunction(name='clahe_equalization',
                                                          description='CLAHE histogram equalization',
                                                          inputs=[dl.FunctionIO(type=dl.PackageInputType.ITEM,
                                                                                name='item')])
                                       ])]
```
### Push the package  
When you deployed the service in the previous tutorial (“Single Function”), a module and a package were automatically generated.  
  
Now we will explicitly create and push the module as a package in the Dataloop FaaS library (application hub). For that, please specify the source path (src_path) of the “main.py” file you downloaded, and then run the following code:  

```python
src_path = 'functions/opencv_functions'
project = dl.projects.get(project_name='project-sdk-tutorial')
package = project.packages.push(package_name='image-processing',
                                modules=modules,
                                src_path=src_path)
```
### Deploy a service  
Now that the package is ready, it can be deployed to the Dataloop platform as a service.  
To create a service from a package, you need to define which module the service will serve. Notice that a service can only contain a single module. All the module functions will be automatically added to the service.  
  
Multiple services can be deployed from a single package. Each service can get its own configuration: a different module and settings (computing resources, triggers, UI slots, etc.).  
  
In our example, there is only one module in the package. Let’s deploy the service:  

```python
service = package.services.deploy(service_name='image-processing',
                                  runtime=dl.KubernetesRuntime(concurrency=32),
                                  module_name='image-processing-module')
```
### Trigger the service  
Once the service is up, we can configure a trigger to automatically run the service functions. When you bind a trigger to a function, that function will execute when the trigger fires. The trigger is defined by a given time pattern or by an event in the Dataloop system.  
  
Event based trigger is related to a combination of resource and action. A resource can be any entity in our system (item, dataset, annotation, etc.) and the associated action will define a change in the resource that will prompt the trigger (update, create, delete). You can only have one resource per trigger.  
  
  
The resource object that triggered the function will be passed as the function's parameter (input).  
  
Let’s set a trigger in the event a new item is created:  

```python
filters = dl.Filters()
filters.add(field='datasetId', values=dataset.id)
trigger = service.triggers.create(name='image-processing2',
                                  function_name='clahe_equalization',
                                  execution_mode=dl.TriggerExecutionMode.ONCE,
                                  resource=dl.TriggerResource.ITEM,
                                  actions=dl.TriggerAction.CREATED,
                                  filters=filters)
```
In the defined filters we specified a dataset. Once a new item is uploaded (created) in this dataset, the CLAHE function will be executed for this item. You can also add filters to specify the item type (image, video, JSON, directory, etc.) or a certain format (jpeg, jpg, WebM, etc.).  
  
A separate trigger must be set for each function in your service.  
Now, we will define a trigger for the second function in the module rgb2gray. Each time an item is updated, invoke the rgb2gray function:  

```python
trigger = service.triggers.create(name='image-processing-rgb',
                                  function_name='rgb2gray',
                                  execution_mode=dl.TriggerExecutionMode.ALWAYS,
                                  resource=dl.TriggerResource.ITEM,
                                  actions=dl.TriggerAction.UPDATED,
                                  filters=filters)
```
To trigger the function only once (only on the first item update), set TriggerExecutionMode.ONCE instead of TriggerExecutionMode.ALWAYS.  
  
### Execute the function  
Now we can upload (“create”) an image to our dataset to trigger the service. The function clahe_equalization will be invoked:  

```python
item = dataset.items.upload(
    local_path=['https://github.com/dataloop-ai/dtlpy-documentation/raw/main/assets/images/hamster.jpg'])
# Remote path is optional, images will go to the main directory by default
```
To see the original item, please click [here](https://raw.githubusercontent.com/dataloop-ai/dtlpy-documentation/main/assets/images/hamster.jpg).  
  
### Review the function's logs  
You can review the execution log history to check that your execution succeeded:  

```python
service.log()
```
The transformed image will be saved in your dataset.  
Once you see in the log that the execution succeeded, you may open the item to see its transformation:  

```python
item.open_in_web()
```
### Pause the service:  
We recommend pausing the service you created for this tutorial so it will not be triggered:  

```python
service.pause()
```
Congratulations! You have successfully created, deployed, and tested Dataloop functions!  
  
## Multiple Modules  
You can define multiple different modules in a package. A typical use-case for multiple-modules is to have a single code base that can be used by a number of services (for different applications). For example, having a single YoloV4 codebase, but creating different modules for training, inference, etc.  
  
When creating a service from that package, you will need to define which module the service will serve (a service can only serve a single module with all its functions). For example, to push a 2 module package, you will need to have 2 entry points, one for each module, and this is how you define the modules:  
  

```python
modules = [
    dl.PackageModule(
        name='first-module',
        entry_point='first_module_main.py',
        functions=[
            dl.PackageFunction(
                name='run',
                inputs=[dl.FunctionIO(name='item',
                                      type=dl.PackageInputType.ITEM)]
            )
        ]
    ),
    dl.PackageModule(
        name='second-module',
        entry_point='second_module_main.py',
        functions=[
            dl.PackageFunction(
                name='run',
                inputs=[dl.FunctionIO(name='item',
                                      type=dl.PackageInputType.ITEM)]
            )
        ]
    )
]
```
Create the package with your modules  

```python
package = project.packages.push(package_name='two-modules-test',
                                modules=modules,
                                src_path='<path to where the entry point is located>'
                                )
```
You will pass these modules as a param to packages.push()  
After that, when you deploy the package, you will need to specify the module name:  
Note: A service can only implement one module.  
  

```python
service = package.deploy(
    module_name='first-module',
    service_name='first-module-test-service'
)
```
