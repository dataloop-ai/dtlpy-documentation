Create and Deploy a Sample Function
Below is an image-manipulation function in Python to use for converting an RGB image to a grayscale image. The function receives a single item, which later can be used as a trigger to invoke the function:
```
import cv2
import numpy as np
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
    bgr_equalized_item = item.dataset.items.upload(local_path=gray,
                                                   remote_path='/gray' + item.dir,
                                                   remote_name=item.filename)
    # add modality
    item.modalities.create(name='gray',
                           ref=bgr_equalized_item.id)
    item.update(system_metadata=True)
```
You can now deploy the function as a service using Dataloop SDK. Once the service is ready, one may execute the available function on any input:
```
service = project.services.deploy(func=rgb2gray, service_name='greyscale-item-service')
```
Execute the function
An execution is a run of the function on a service with specific inputs (arguments). The execution input will be provided to the function that the execution runs.

Now when the service is up, it can be executed manually (on demand) or automatically, based on a set trigger (time/criteria). As part of this chapter, we will demonstrate how to manually run the Grayscale function.

Click here to see the picture before the transformation:
Button

Let’s execute the function and watch the results (display the image):

```
...
```
