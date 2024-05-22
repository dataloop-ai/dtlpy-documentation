# Segmentation  
## Init Segmentation  
Each annotation init receives the coordinates for the specific type, label, and optional attributes. A binary mask should be exactly the same dimensions as the image item, with 0 for background and 1 for the annotation.  
  
  

```python
annotations_definition = dl.Segmentation(geo=mask, label=label)
```
## Create a Semantic Segmentation Annotation  
  
  

```python
# Get item from the platform
item = dataset.items.get(filepath='/your-image-file-path.jpg')
# Create a builder instance
builder = item.annotations.builder()
# Create semantic segmentation mask with label and attribute
mask = np.zeros(shape=(item.height, item.width), dtype=np.uint8)
# mark some part in the middle
mask[50:100, 200:250] = 1
# Add annotations of type segmentation
builder.add(annotation_definition=dl.Segmentation(geo=mask,
                                                  label='my-label'))
# Optional: Plot all of the annotations you created before uploading them to the platform
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(builder.show())
for annotation in builder:
    plt.figure()
    plt.imshow(annotation.show())
    plt.title(annotation.label)
# Upload semantic segmentation to the item
item.annotations.upload(builder)
```
## Convert Mask to Polygon  
The Dataloop SDK includes a function to convert a semantic mask to a polygon annotation, which is often easier to edit and work with in the UI.  
The following example filters for items with semantic mask annotations, and converts them into Polygon annotations.  
  

```python
filters = dl.Filters()
# set resource
filters.resource = 'items'
# add filter - only files
filters.add(field='type', values='file')
# add annotation filters - only items with 'binary' annotations
filters.add_join(field='type', values='binary')
# get results
pages = dataset.items.list(filters=filters)
# run over all items in page
for page in pages:
    for item in page:
        print('item=' + item.id)
        annotations = item.annotations.list()
        builder = item.annotations.builder()
        # run over all annotation in item
        for annotation in annotations:
            # print(annotation)
            if annotation.type == 'binary':
                print("Found binary annotation - id:", annotation.id)
                builder.add(dl.Polygon.from_segmentation(mask=annotation.annotation_definition.geo,
                                                         # binary mask of the annotation
                                                         label=annotation.label,
                                                         max_instances=None))
                annotation.delete()
        item.annotations.upload(annotations=builder)
```
## Convert Polygon to Mask  
The Dataloop SDK also includes a function to convert a Polygon annotation into semantic mask annotation.  
The following example filters for items with Polygon annotations, and converts them into semantic mask annotations.  
This script uses module CV2, please make sure it is installed.  
  
  
  

```python
from PIL import Image
filters = dl.Filters()
# set resource
filters.resource = 'items'
# add filter - only files
filters.add(field='type', values='file')
# add annotation filters - only items with polygon annotations
filters.add_join(field='type', values='segment')
# get results
pages = dataset.items.list(filters=filters)
# run over all items in page
for page in pages:
    for item in page:
        print('item=' + item.id)
        annotations = item.annotations.list()
        item = dataset.items.get(item_id=item.id)
        buffer = item.download(save_locally=False)
        img = Image.open(buffer)
        builder = item.annotations.builder()
        # run over all annotation in item
        for annotation in annotations:
            # print(annotation)
            if annotation.type == 'segment':
                print("Found polygon annotation - id:", annotation.id)
                builder.add(dl.Segmentation.from_polygon(geo=annotation.annotation_definition.geo,
                                                         # binary mask of the annotation
                                                         label=annotation.label,
                                                         shape=img.size[::-1]  # (h,w)
                                                         ))
                annotation.delete()
        item.annotations.upload(annotations=builder)
```
## Create Semantic Segmentation from Image Mask and Upload  
The following script creates a semantic mask based on RGB colors of an image item and upload them to the Dataloop platform  
Please notice that directory paths look different in OS and Linux and does not require "r" at the beginning  
Make sure to use install OpenCV package to version 3.4.8.x with the script  
**pip install opencv-python == 3 .4.8.latest**  
  
  

```python
from PIL import Image
import numpy as np
import dtlpy as dl
# Get project and dataset
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
# image filepath
image_filepath = r'C:/home/images/with_family.png'
# annotations filepath - RGB with color for each label
annotations_filepath = r'C:/home/masks/with_family.png'
# upload item to root directory
item = dataset.items.upload(local_path=image_filepath,
                            remote_path='/')
# read mask from file
mask = np.array(Image.open(annotations_filepath))
# get unique color (labels)
unique_colors = np.unique(mask.reshape(-1, mask.shape[2]), axis=0)
# init dataloop annotations builder
builder = item.annotations.builder()
# for each label - create a dataloop mask annotation
for i, color in enumerate(unique_colors):
    print(color)
    if i == 0:
        # ignore background
        continue
    # get mask of same color
    class_mask = np.all(color == mask, axis=2)
    # add annotation to builder
    builder.add(annotation_definition=dl.Segmentation(geo=class_mask,
                                                      label=str(i)))
    # upload all annotations
    item.annotations.upload(builder)
```
## Create Semantic Segmentation annotations from an Instance Mask  
The following script creates semantic segmentation annotations based on the given instance mask and  
the instance map, and then upload them to the Dataloop platform.  
Please notice that the instance map should be ordered by the mask values.  
  

```python
import dtlpy as dl
import numpy as np
# Get project, dataset and item
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
item = dataset.items.get(filepath='file_path')
# Create a builder instance
builder = item.annotations.builder()
# Create a random mask
mask = np.random.randint(2, size=(item.height, item.width))
instance_map = ["background", "foreground"]
# Add convert the instance mask to segmentation annotations
builder.from_instance_mask(mask=mask, instance_map=instance_map)
# Upload the annotations to the item
item.annotations.upload(annotations=builder)
```
## Convert and Merge Polygon Annotations to Segmentation Annotations  
The following script convert all the polygon annotations to segmentation annotations, merge them into one mask per  
label and then upload them to the Dataloop platform.  
Please notice the following things:  
1. When the item have more than 2 annotations with the same label merging is required, otherwise only the first  
existing/created annotation will be uploaded.  
2. There is an option to upload the converted polygons without merging them to existing masks by setting a unique  
object_id to each one of them.  
3. The script assumes that the item has only up to one instance of semantic segmentation annotation per label.  
  

```python
import dtlpy as dl
import numpy as np
# Get project, dataset and item
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
item = dataset.items.get(filepath='filepath')
# Get item semantic segmentation and polygon annotations
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
filters.add(field=dl.KnownFields.TYPE,
            values=[dl.AnnotationType.SEGMENTATION, dl.AnnotationType.POLYGON],
            operator=dl.FiltersOperations.IN)
annotations = item.annotations.list(filters=filters)
# Merge all the annotations into masks
final_masks = dict()
for annotation in annotations:
    # Get segmentation annotation mask and reference
    if annotation.type == dl.AnnotationType.SEGMENTATION:
        mask = annotation.geo
        segmentation_ref = annotation
    # Convert the polygon to segmentation and get its mask
    else:
        mask = dl.Segmentation.from_polygon(geo=annotation.geo,
                                            label=annotation.label,
                                            shape=(item.height, item.width)).geo
        segmentation_ref = None
    # Merge the masks
    if annotation.label not in list(final_masks.keys()):
        final_masks[annotation.label] = {"mask": mask, "segmentation_ref": segmentation_ref}
    else:
        final_masks[annotation.label]["mask"] = np.logical_or(final_masks[annotation.label]["mask"], mask)
        if segmentation_ref is not None:
            final_masks[annotation.label]["segmentation_ref"] = segmentation_ref
# Upload masks to the item
builder = item.annotations.builder()
for label, mask in final_masks.items():
    annotation = mask["segmentation_ref"]
    if annotation is None:
        builder.add(annotation_definition=dl.Segmentation(geo=mask["mask"], label=label))
    else:
        annotation.geo = mask["mask"]
        annotation.update()
if len(builder) > 0:
    builder.upload()
    # Delete all the polygon annotations
    polygon_filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
    polygon_filters.add(field=dl.KnownFields.TYPE, values=dl.AnnotationType.POLYGON)
    item.annotations.delete(filters=polygon_filters)
```
