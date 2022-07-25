## Copy Annotations Between Items  
By setting annotations entity from one item, and uploading it into another, we can copy annotations between items. Running through all items in a filter allows us to copy from one item into multiple items, for example video snapshots with the same object.  
  

```python
# Set the source item with the annotations we want to copy
project = dl.projects.get(project_name='second-project_name')
dataset = project.datasets.get(dataset_name='second-dataset_name')
item = dataset.items.get(item_id='first-id-number')
annotations = item.annotations.list()
# Set the target item where we want to copy to. If located on a different Project or Dataset, set these accordingly
item = dataset.items.get(item_id='second-id-number')
item.annotations.upload(annotations=annotations)
# Copy the annotation into multiple items, based on a filter entity. In this example, the filter is based on directory
filters = dl.Filters()
filters.add(field='filename', values='/fighting/**')  # take files from the directory only (recursive)
filters.add(field='type', values='file')  # only files
pages = dataset.items.list(filters=filters)
for page in pages:
    for item in page:
        # upload annotations
        item.annotations.upload(annotations=annotations)
```
## Show Images & Annotations  
This script uses module CV2, please use this page to install it.  
  

```python
from PIL import Image
# Get item
item = dataset.items.get(item_id='write-your-id-number')
# download item as a buffer
buffer = item.download(save_locally=False)
# open image
image = Image.open(buffer)
# download annotations
annotations = item.annotations.show(width=image.size[0],
                                    height=image.size[1],
                                    thickness=3)
annotations = Image.fromarray(annotations.astype(np.uint8))
# show the annotations and the image separately
annotations.show()
image.show()
# Show the annotations with the image
image.paste(annotations, (0, 0), annotations)
image.show()
```
## Show Annotations from JSON file (Dataloop format)  
  
Please notice that directory paths look different in OS and Linux and does not require "r" at the beginning  
  
  

```python
from PIL import Image
import json
with open(r'C:/home/project/images/annotation.json', 'r') as f:
    data = json.load(f)
for annotation in data['annotations']:
    annotations = dl.Annotation.from_json(annotation)
    mask = annotations.show(width=640,
                            height=480,
                            thickness=3,
                            color=(255, 0, 0))
    mask = Image.fromarray(mask.astype(np.uint8))
    mask.show()
```
## Count total number of annotations  
The following script counts the number of annotations in a filter. The filter can be set to any context - Dataset, folder or any specific criteria. In the following example, it is set to a dataset.  

```python
# Create annotations filters instance
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
filters.page_size = 0
# Count the annotations
annotations_count = dataset.annotations.list(filters=filters).items_count
```
## Parenting Annotations  
  
Parenting establishes a relation between 2 annotations, executed by setting the parent_id parameter. The Dataloop system will reject an attempt to set circular parenting.  
The following script demonstrate setting parenting relation while uploading/creating annotations  
  
  

```python
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Box(top=10, left=10, bottom=100, right=100,
                                         label='my-parent-label'))
# upload parent annotation
annotations = item.annotations.upload(annotations=builder)
# create the child annotation
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Box(top=10, left=10, bottom=100, right=100,
                                         label='my-child-label'),
            parent_id=annotations[0].id)
# upload annotations to item
item.annotations.upload(annotations=builder)
```
  
The following script demonstrate setting parenting relation on existing annotations:  

```python
# create and upload parent annotation
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Box(top=10, left=10, bottom=100, right=100,
                                         label='my-parent-label'))
parent_annotation = item.annotations.upload(annotations=builder)[0]
# create and upload child annotation
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Box(top=10, left=10, bottom=100, right=100,
                                         label='my-child-label'))
child_annotation = item.annotations.upload(annotations=builder)[0]
# set the child parent ID to the parent
child_annotation.parent_id = parent_annotation.id
# update the annotation
child_annotation.update(system_metadata=True)
```
  
## Change Annotations’ Label  
The following example creates a new label in the recipe (an optional step, you can also use an existing label), then applies it to all annotations in a certain filter.  
  

```python
# Create a new label
dataset.add_label(label_name='newLabel', color=(2, 43, 123))
# Filter annotations with the "oldLabel" label.
filters = dl.Filters()
filters.resource = dl.FiltersResource.ANNOTATION
filters.add(field='label', values='oldLabel')
pages = dataset.annotations.list(filters=filters)
# Change the Label of the Annotations - For every annotation we filtered out, Change it's Label to the "newLabel".
for annotation in pages.all():
    annotation.label = 'newLabel'
    annotation.update()
```
