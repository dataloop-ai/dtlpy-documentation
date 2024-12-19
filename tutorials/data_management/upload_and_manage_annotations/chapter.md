# Upload & Manage Annotations  

```python
import dtlpy as dl
item = dl.items.get(item_id="")
annotation = item.annotations.get(annotation_id="")
annotation.metadata["user"] = True
annotation.update()
```
## Upload User Metadata  
To upload annotations from JSON and include the user metadata, add the parameter local_annotation_path to the dataset.items.upload function, like so:  

```python
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
dataset.items.upload(local_path=r'<items path>',
                     local_annotations_path=r'<annotation json file path>',
                     item_metadata=dl.ExportMetadata.FROM_JSON,
                     overwrite=True)
```
## Upload with Task and Recipe Context  
  
Annotation can be uploaded or edited with a context. The Recipe, Task and Assignment IDs can be add to the system metadata:  
  

```python
import dtlpy as dl
item = dl.items.get(item_id="")
# Get the entities to add to the context
assignment = dl.assignments.get(assignment_id="")
task = dl.tasks.get(task_id="")
# OR
task = assignment.task
recipe = dl.recipes.get(recipe_id="")
# OR
recipe = dl.recipes.get(recipe_id=task.recipe_id)
# Context dictionary
context = {'taskId': task.id,
           'assignmentId': assignment.id,
           'recipeId': recipe.id}
# Create the annotation
collection = item.annotations.builder()
collection.add(annotation_definition=dl.Classification(label='Komodo Dragon'),
               metadata={'system': context})
item.annotations.upload(annotations=collection)
# Or Update existing one
annotation = item.annotations.get(annotation_id="")
annotation.metadata["system"].update(context)
annotation.update(system_metadata=True)
```
## Convert Annotations from COCO Format  
  

```python
converter = dl.Converter()
converter.upload_local_dataset(
    from_format=dl.AnnotationFormat.COCO,
    dataset=dataset,
    local_items_path=r'C:/path/to/items',
    # Please make sure the names of the items are the same as written in the COCO JSON file
    local_annotations_path=r'C:/path/to/annotations/file/coco.json'
)
```
## Upload Entire Directory and their Corresponding  Dataloop JSON Annotations  
  

```python
# Local path to the items folder
# If you wish to upload items with your directory tree use : r'C:/home/project/images_folder' 
local_items_path = r'C:/home/project/images_folder/*'
# Local path to the corresponding annotations - make sure the file names fit
local_annotations_path = r'C:/home/project/annotations_folder'
dataset.items.upload(local_path=local_items_path,
                     local_annotations_path=local_annotations_path)
```
## Upload Annotations To Video Item  
Uploading annotations to video items needs to consider spanning between frames, and toggling visibility (occlusion). In this example, we will use the following CSV file.  
In this file there is a single 'person' box annotation that begins on frame number 20, disappears on frame number 41, reappears on frame number 51 and ends on frame number 90.  
  
[Video_annotations_example.CSV](https://cdn.document360.io/53f32fe9-1937-4652-8526-90c1bc78d3f8/Images/Documentation/video_annotation_example.csv)  
  

```python
import pandas as pd
# Read CSV file
df = pd.read_csv(r'C:/file.csv')
# Get item
item = dataset.items.get(item_id='my_item_id')
builder = item.annotations.builder()
# Read line by line from the csv file
for i_row, row in df.iterrows():
    # Create box annotation from csv rows and add it to a builder
    builder.add(annotation_definition=dl.Box(top=row['top'],
                                             left=row['left'],
                                             bottom=row['bottom'],
                                             right=row['right'],
                                             label=row['label']),
                object_visible=row['visible'],  # Support hidden annotations on the visible row
                object_id=row['annotation id'],  # Numbering system that separates different annotations
                frame_num=row['frame'])
# Upload all created annotations
item.annotations.upload(annotations=builder)
```
## Upload Annotations In VTT Format  
The Dataloop builder support VTT files, for uploading Web Text Tracks for video transcription.  
  

```python
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
# local path to item
local_item_path = r'/Users/local/path/to/item.png'
# local path to vtt
local_vtt_path = r'/Users/local/path/to/subtitles.vtt'
# upload item
item = dataset.items.upload(local_path=local_item_path)
# upload VTT file - wait until the item finishs uploading
builder = item.annotations.builder()
builder.from_vtt_file(filepath=local_vtt_path)
item.annotations.upload(builder)
```
## Upload Audio Annotation to an Audio File  
  

```python
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
item = dataset.items.get(filepath='/my_item.mp4')
# Using annotation builder
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Subtitle(label='<label>',
                                              text='<text>'),
            start_time='<start>',
            end_time='<end>')
```
## Set Attributes On Annotations  
  
You can set attributes on annotations in hte platform using the SDK. Since Dataloop deprecated a legacy attributes mechanism, attributes are refered to as '2.0' version and need to be set as such first.  
  
### Free Text Attribute  

```python
annotation.attributes.update({"ID of the attribute": "value of the attribute"})
annotation = annotation.update(True)
```
### Range Attributes (Slider in UI)  
  

```python
annotation.attributes.update({"<attribute-id>": number_on_range})
annotation = annotation.update(system_metadata=True)
```
### CheckBox Attribute (Multiple choice)  

```python
annotation.attributes.update({"<attribute-id>": ["selection", "selection"]})
annotation = annotation.update(system_metadata=True)
```
### Radio Button Attribute (Single Choice)  

```python
annotation.attributes.update({"<attribute-id>": "selection"})
annotation = annotation.update(system_metadata=True)
```
### Yes/No Attribute  

```python
annotation.attributes.update({"<attribute-id>": True / False})
annotation = annotation.update(system_metadata=True)
```
## Show Annotations Over Image  
After uploading items and annotations with their metadata, you might want to see some of them and perform visual validation.  
  
To see only the annotations, use the annotation type *show* option.  
  

```python
# Use the show function for all annotation types
box = dl.Box()
# Must provide all inputs
box.show(image='',
         thickness='',
         with_text='',
         height='',
         width='',
         annotation_format='',
         color='')
```
  
To see the item itself with all annotations, use the Annotations option.  
  

```python
# Must input an image or height and width
annotation.show(image='',
                height='', width='',
                annotation_format='dl.ViewAnnotationOptions.*',
                thickness='',
                with_text='')
```
  
# Download Data, Annotations & Metadata  
The item ID for a specific file can be found in the platform UI - Click BROWSE for a dataset, click on the selected file, and the file information will be displayed in the right-side panel. The item ID is detailed, and can be copied in a single click.  
  
## Download Items and Annotations  
Download dataset items and annotations to your computer folder in two separate folders.  
To list the download annotation option use `dl.ViewAnnotationOptions`:  
1. JSON: Download json files with the Dataloop annotation format.  
2. MASK: Save a PNG image file with the RGB annotation drawn.  
3. INSTANCE: Saves a PNG with the annotation label ID as the pixel value.  
4. ANNOTATION_ON_IMAGE: Saves a PNG with the annotation drawn on top of the image.  
5. VTT: Save `subtitle` annotation type in a VTT format.  
6. OBJECT_ID: Save a PNG with the object ID as the pixel value.  
  

```python
dataset.download(local_path=r'C:/home/project/images',  # The default value is ".dataloop" folder
                 annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)
```
NOTE: The annotation option can also be a list to download multiple options:  
  

```python
dataset.download(local_path=r'C:/home/project/images',  # The default value is ".dataloop" folder
                 annotation_options=[dl.VIEW_ANNOTATION_OPTIONS_MASK,
                                     dl.VIEW_ANNOTATION_OPTIONS_JSON,
                                     dl.ViewAnnotationOptions.INSTANCE])
```
  
## Filter by Item and/or Annotation  
* **Items filter** - download filtered items based on multiple parameters, like their directory.  
You can also download items based on different filters. Learn all about item filters [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/item_level/chapter.md/).  
* **Annotation filter** - download filtered annotations based on multiple parameters like their label.  
You can also download items annotations based on different filters, learn all about annotation filters [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/annotation_level/chapter.md/).  
This example will download items and JSONS from a dog folder of the label 'dog'.  
  
  

```python
# Filter items from "folder_name" directory
item_filters = dl.Filters(resource='items', field='dir', values='/dog_name')
# Filter items with dog annotations
annotation_filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION, field='label', values='dog')
dataset.download(local_path=r'C:/home/project/images',  # The default value is ".dataloop" folder
                 filters=item_filters,
                 annotation_filters=annotation_filters,
                 annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)
```
  
## Filter by Annotations  
* **Annotation filter** - download filtered annotations based on multiple parameters like their label. You can also download items annotations based on different filters, learn all about annotation filters [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/annotation_level/chapter.md/).  
  
  

```python
item = dataset.items.get(item_id="item_id")  # Get item from dataset to be able to view the dataset colors on Mask
# Filter items with dog annotations
annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
item.download(local_path=r'C:/home/project/images',  # the default value is ".dataloop" folder
              annotation_filters=annotation_filters,
              annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)
```
  
## Download Annotations in COCO/YOLO/VOC Format  
  
* **Items filter** - download filtered items based on multiple parameters like their directory. You can also download items based on different filters, learn all about item filters [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/item_level/chapter.md/).  
* **Annotation filter** - download filtered annotations based on multiple parameters like their label. You can also download items annotations based on different filters, learn all about annotation filters [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/annotation_level/chapter.md/).  
  
This example will download COCO from a dog items folder of the label 'dog' (edit the script to change to YOLO/VOC).  
  
  

```python
# Filter items from "folder_name" directory
item_filters = dl.Filters(resource='items', field='dir', values='/dog_name')
# Filter items with dog annotations
annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
converter = dl.Converter()
converter.convert_dataset(dataset=dataset,
                          # Use the converter of choice
                          # to_format='yolo',
                          # to_format='voc',
                          to_format='coco',
                          local_path=r'C:/home/coco_annotations',
                          filters=item_filters,
                          annotation_filters=annotation_filters)
```

```python
# Param export_version will be set to ExportVersion.V1 by default.
dataset.download(local_path='/path',
                 annotation_options='json',
                 export_version=dl.ExportVersion.V2)
```

```python
from PIL import Image
item = dl.items.get(item_id='my-item-id')
array = item.download(save_locally=False, to_array=True)
# Check out the downloaded Ndarray with these commands - optional
image = Image.fromarray(array)
image.save(r'C:/home/project/images.jpg')
```
