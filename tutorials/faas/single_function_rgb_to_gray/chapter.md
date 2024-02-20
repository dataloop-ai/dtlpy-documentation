# Basic Use Case: Single Function  
## Create and Deploy a Sample Function  
Below is an image-manipulation function in Python to use for converting an RGB image to a grayscale image. The function receives a single item, which later can be used as a trigger to invoke the function:  

```python
def rgb2gray(item: dl.Item):
    """
    Function to convert RGB image to GRAY
    Will also add a modality to the original item
    :param item: dl.Item to convert
    :return: None
    """
    import numpy as np
    import cv2
    buffer = item.download(save_locally=False)
    bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    bgr_equalized_item = item.dataset.items.upload(local_path=gray,
                                                   remote_path='/gray' + item.dir,
                                                   remote_name=item.name)
    # add modality
    item.modalities.create(name='gray',
                           ref=bgr_equalized_item.id)
    item.update(system_metadata=True)
```
You can now deploy the function as a service using Dataloop SDK. Once the service is ready, you may execute the available function on any input:  

```python
project = dl.projects.get(project_name='project-sdk-tutorial')
service = project.services.deploy(func=rgb2gray,
                                  service_name='grayscale-item-service')
```
## Execute the function  
An execution means running the function on a service with specific inputs (arguments). The execution input will be provided to the function that the execution runs.  
  
Now that the service is up, it can be executed manually (on-demand) or automatically, based on a set trigger (time/event). As part of this tutorial, we will demonstrate how to manually run the “RGB to Gray” function.  
  
To see the item we uploaded, run the following code:  

```python
item.open_in_web()
```
Let’s convert the item from RGB to grayscale, using the service we created:  

```python
execution = service.execute(project_id=project.id,
                            item_id=item.id,
                            function_name='rgb2gray')
execution.logs(follow=True)
execution = execution.wait()
print(execution.latest_status)
```
## Batch Execution  
For executing on multiple items (with a filter) use:  

```python
filters = dl.Filters(resource=dl.FiltersResource.ITEM,
                     field='dir',
                     values='/test',
                     context={'datasets': [dataset.id]})
command = service.execute_batch(
    filters=filters,
    function_name='rgb2gray')
```
The transformed image will be saved in your dataset in the folder specified.  
You may now open the item received upon execution:  

```python
item.open_in_web()
```
