# Create and Deploy a Sample Function
Below is an image-manipulation function in Python that runs a Greyscale method over an item (image). The function receives an item, which later can be used as a trigger:
```
def rgb2gray(item: dl.Item):
    # download item as a buffer
    buffer = item.download(save_locally=False)
    image = Image.open(buffer).convert("LA" if "png" in item.mimetype else "L")
    buffer = io.BytesIO()
    buffer.name = item.name
    image.save(buffer)
    # upload item
    new_item = item.dataset.items.upload(local_path=buffer,
                                         remote_path='/greyscale',
                                         overwrite=True)
    if item.annotations_count:
        new_item.annotations.upload(annotations=item.annotations.list())
```
Deploy the function using Dataloop SDK:
```
```
## Execute the function
Now when the service is up, we can either execute it manually (on-demand) or have it executed automatically, when a trigger we set (time/criteria) is met.

We will now execute the function manually, to transform a given picture into greyscales.
Click here to see the picture before the transformation:

Let’s execute the function and watch the results (view the pic & navigate to the dataset?):
```
```
