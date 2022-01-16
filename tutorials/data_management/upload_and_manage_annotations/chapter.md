
# Upload & Manage Annotations

```
item = dl.items.get(item_id="")
annotation = item.annotations.get(annotation_id="")
annotation.metadata["user"] = True
annotation.update()
```

## Convert Annotations To COCO Format

```
import dtlpy as dl
dataset = project.datasets.get(dataset_name='dataset_name')
converter = dl.Converter()
converter.upload_local_dataset(
    from_format=dl.AnnotationFormat.COCO,
    dataset=dataset,
    local_items_path=r'C:/path/to/items', # Please make sure the names of the items are the same as written in the COCO JSON file
    local_annotations_path=r'C:/path/to/annotations/file/coco.json'
)
```

## Upload Entire Directory and their Corresponding  Dataloop JSON Annotations

```
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
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

```
import dtlpy as dl
import pandas as pd
project = dl.projects.get(project_name='my_project')
dataset = project.datasets.get(dataset_id='my_dataset')
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
                    object_visible=row['visible'], # Support hidden annotations on the visible row
                    object_id=row['annotation id'], # Numbering system that separates different annotations
                    frame_num=row['frame'])
# Upload all created annotations
item.annotations.upload(annotations=builder)
```

# Show Annotations Over Image
After uploading items and annotations with their metadata, you might want to see some of them and perform visual validation.

To see only the annotations, use the annotation type *show* option.

```
# Use the show function for all annotation types
box = dl.Box()
# Must provide all inputs
box.show(image='', thickness='', with_text='', height='', width='', annotation_format='', color='')
```

To see the item itself with all annotations, use the Annotations option.

```
# Must input an image or height and width
annotation.show(image='', height='', width='', annotation_format='dl.ViewAnnotationOptions.*', thickness='', with_text='')
```

# Download Data, Annotations & Metadata
The item ID for a specific file can be found in the platform UI - Click BROWSE for a dataset, click on the selected file, and the file information will be displayed in the right-side panel. The item ID is detailed, and can be copied in a single click.

## Download Items and Annotations
Download dataset items and annotations to your computer folder in two separate folders.
See all annotation options [here](https://dataloop.ai/docs/sdk-download#annotation-options).


```
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
dataset.download(local_path=r'C:/home/project/images', # The default value is ".dataloop" folder
                annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON) 
```

## Multiple Annotation Options
See all annotation options [here](https://dataloop.ai/docs/sdk-download#annotation-options).


```
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
dataset.download(local_path=r'C:/home/project/images', # The default value is ".dataloop" folder
                annotation_options=[dl.VIEW_ANNOTATION_OPTIONS_MASK, dl.VIEW_ANNOTATION_OPTIONS_JSON, dl.ViewAnnotationOptions.INSTANCE])
```

## Filter by Item and/or Annotation
* **Items filter** - download filtered items based on multiple parameters, like their directory.
You can also download items based on different filters. Learn all about item filters [here](https://dataloop.ai/docs/sdk-sort-filter).
* **Annotation filter** - download filtered annotations based on multiple parameters like their label.
You can also download items annotations based on different filters, learn all about annotation filters [here](https://dataloop.ai/docs/sdk-sort-filter-annotation).
This example will download items and JSONS from a dog folder of the label 'dog'.


```
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
# Filter items from "folder_name" directory
item_filters = dl.Filters(resource='items',field='dir', values='/dog_name')
# Filter items with dog annotations
annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
dataset.download( # The default value is ".dataloop" folder
                local_path=r'C:/home/project/images',
                filters = item_filters, 
                annotation_filters=annotation_filters,
                annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)
```

## Filter by Annotations
* **Annotation filter** - download filtered annotations based on multiple parameters like their label. You can also download items annotations based on different filters, learn all about annotation filters [here](https://dataloop.ai/docs/sdk-sort-filter-annotation).


```
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
item = dataset.items.get(item_id="item_id") #Get item from dataset to be able to view the dataset colors on Mask
# Filter items with dog annotations
annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
item.download( # the default value is ".dataloop" folder
                local_path=r'C:/home/project/images',
                annotation_filters=annotation_filters,
                annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)
```

## Download Annotations in COCO Format

* **Items filter** - download filtered items based on multiple parameters like their directory. You can also download items based on different filters, learn all about item filters [here](https://dataloop.ai/docs/sdk-sort-filter).
* **Annotation filter** - download filtered annotations based on multiple parameters like their label. You can also download items annotations based on different filters, learn all about annotation filters [here](https://dataloop.ai/docs/sdk-sort-filter-annotation).

This example will download COCO from a dog items folder of the label 'dog'.


```
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
# Filter items from "folder_name" directory
item_filters = dl.Filters(resource='items',field='dir', values='/dog_name')
# Filter items with dog annotations
annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
converter = dl.Converter()
converter.convert_dataset(dataset=dataset, to_format='coco',
                        local_path=r'C:/home/coco_annotations', 
                filters = item_filters, 
                        annotation_filters=annotation_filters)
```
