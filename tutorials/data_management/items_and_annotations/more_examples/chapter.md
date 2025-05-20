# Advanced Item and Annotation Examples 🎓

Welcome to our advanced guide for working with items and annotations! Here you'll find detailed examples and advanced techniques for managing your data in Dataloop.

## Advanced Item Examples and Operations 🎯

### Advanced Upload Scenarios 🚀

#### Batch Upload with Metadata and Annotations

Want to upload multiple items with their metadata and annotations? Here's how to use a Pandas DataFrame:

```python
import pandas as pd
import dtlpy as dl

# Prepare your data
upload_data = [
    {
        'local_path': r"E:\TypesExamples\000000000064.jpg",
        'local_annotations_path': r"E:\TypesExamples\000000000776.json",
        'remote_path': '/first',
        'remote_name': 'f.jpg',
        'item_metadata': {'user': {'category': 'first'}}
    },
    {
        'local_path': r"E:\TypesExamples\000000000776.jpg",
        'local_annotations_path': r"E:\TypesExamples\000000000776.json",
        'remote_path': "/second",
        'remote_name': 's.jpg',
        'item_metadata': {'user': {'category': 'second'}}
    }
]

# Create DataFrame
df = pd.DataFrame(upload_data)

# Upload with DataFrame
dataset = dl.datasets.get(dataset_id='your-dataset-id')
items = dataset.items.upload(
    local_path=df,
    overwrite=True
)
```

### Working with Different File Types 📁

#### Image Arrays with OpenCV

```python
import cv2
import numpy as np

# Create or load your array
img_array = cv2.imread('path/to/image.jpg')
# Or create a random array
random_array = np.random.rand(100, 100, 3) * 255
random_array = random_array.astype(np.uint8)

# Upload array (remember to specify remote_name!)
item = dataset.items.upload(
    local_path=random_array,
    remote_name='generated_image.jpg'  # Only .jpg or .png formats are supported!
)

# Download as array
buffer = item.download(
    save_locally=False,  # Returns a buffer instead of saving to disk
    to_array=True       # Converts the buffer directly to a numpy array
)
```

**Important Notes:**
- Use `save_locally=False` to get a buffer instead of saving to disk
- Use `to_array=True` to get the buffer as a numpy array

#### Image Arrays with PIL

```python
from PIL import Image
import numpy as np

# Load with PIL
pil_image = Image.open('path/to/image.jpg')
np_array = np.asarray(pil_image)

# Upload the array
item = dataset.items.upload(
    local_path=np_array,
    remote_name='pil_image.jpg'
)
```

#### Json files

```python
import json

# Open the json file as dictionary
with open('path/to/json_file.json', 'r') as f:
    json_data = json.load(f)

# Upload the json
item = dataset.items.upload(
    local_path=json.dumps(json_data).encode(),
    remote_name='json_file.json'
)

# Download and open the json as dictionary
item = dl.items.get(item_id="item_id")
json_data = json.loads(item.download(save_locally=False).getvalue())
```

### Advanced Metadata Operations 📊

#### Complex Metadata Structure

```python
# Prepare complex metadata
metadata = {
    'user': {
        'categories': ['dog', 'cat'],
        'attributes': {
            'size': 'large',
            'colors': ['brown', 'white'],
            'age': 3
        },
        'validation': {
            'verified': True,
            'verified_by': 'john.doe@example.com',
            'verified_date': '2024-01-01'
        }
    }
}

# Upload with complex metadata
item = dataset.items.upload(
    local_path='path/to/image.jpg',
    remote_name='pet.jpg',
    item_metadata=metadata
)
```

#### Batch Metadata Update

```python
# Update metadata for multiple items
filters = dl.Filters()
filters.add(field='dir', values='/pets')

update_values = {
    'user': {
        'batch_processed': True,
        'process_date': '2024-01-01'
    }
}

dataset.items.update(
    filters=filters,
    update_values=update_values
)
```

## Working with Large Datasets 🗄️

### Progress Tracking

```python
import tqdm

# Get all items
filters = dl.Filters()
pages = dataset.items.list(filters=filters)

# Create progress bar
pbar = tqdm.tqdm(total=pages.items_count)

# Process items with progress
for item in pages.all():
    # Your processing logic here
    process_item(item)
    pbar.update()
```

### Parallel Processing

```python
from concurrent.futures import ThreadPoolExecutor
import tqdm

def process_item(item):
    # Your processing logic here
    return True

# Create progress bar
pbar = tqdm.tqdm(total=pages.items_count)

# Process in parallel
with ThreadPoolExecutor(max_workers=32) as executor:
    futures = []
    for item in pages.all():
        future = executor.submit(process_item, item)
        futures.append(future)

    # Track progress
    for future in futures:
        future.result()
        pbar.update()
```

## Advanced Annotation Examples and Operations 🎯

Welcome to our advanced guide for working with annotations! Here you'll find detailed examples and techniques for managing complex annotation scenarios in Dataloop.

### Working with Different Formats 📦

#### Converting from COCO Format

```python
converter = dl.Converter()
converter.upload_local_dataset(
    from_format=dl.AnnotationFormat.COCO,
    dataset=dataset,
    local_items_path=r"C:/path/to/items",
    # Make sure item names match the COCO JSON file
    local_annotations_path=r"C:/path/to/annotations/file/coco.json"
)
```

### Working with VTT Format

Perfect for video transcription annotations:

```python
# Local paths
local_item_path = r"/Users/local/path/to/item.png"
local_vtt_path = r"/Users/local/path/to/subtitles.vtt"

# Upload item
item = dataset.items.upload(local_path=local_item_path)

# Upload VTT file - wait for item upload to complete
builder = item.annotations.builder()
builder.from_vtt_file(filepath=local_vtt_path)
item.annotations.upload(builder)
```

### Video Annotations 🎥

#### Adding Time-Based Annotations

Here's how to handle annotations that span multiple frames with visibility changes:

```python
import pandas as pd

# Read annotation data from CSV
df = pd.read_csv(r"C:/file.csv")

# Get video item
item = dataset.items.get(item_id="video-item-id")
builder = item.annotations.builder()

# Add annotations frame by frame
for i_row, row in df.iterrows():
    builder.add(
        annotation_definition=dl.Box(
            top=row["top"],
            left=row["left"],
            bottom=row["bottom"],
            right=row["right"],
            label=row["label"]
        ),
        object_visible=row["visible"],  # Handle visibility
        object_id=row["annotation id"],  # Track same object across frames
        frame_num=row["frame"]
    )

# Upload all annotations
item.annotations.upload(annotations=builder)
```

### Audio Annotations 🎵

```python
# Get your audio file
item = dataset.items.get(filepath="/my_audio.mp4")

# Create annotations using builder
builder = item.annotations.builder()
builder.add(
    annotation_definition=dl.Subtitle(label="speech", text="Hello world"),
    start_time="00:00:01",
    end_time="00:00:05"
)

# Add multiple segments
builder.add(
    annotation_definition=dl.Subtitle(label="music", text="Background music"),
    start_time="00:00:06",
    end_time="00:00:10"
)

# Upload annotations
item.annotations.upload(builder)
```

### Batch Operations 📊

#### Copy Annotations Between Items

```python
# Get source and target items
source_item = dataset.items.get(item_id="source-id")
target_item = dataset.items.get(item_id="target-id")

# Copy all annotations
target_item.annotations.upload(source_item.annotations.list())
```

#### Upload from Local JSON

```python
# Load annotations from JSON file
annotations = dl.AnnotationCollection.from_json_file(
    filepath=r"/home/project/annotations.json"
)

# Upload to item
item = dataset.items.get(item_id="target-item-id")
item.annotations.upload(annotations=annotations)
```

### Downloading Annotations 📥

#### Multiple Format Downloads

You can download annotations in various formats:

```python
# Download in multiple formats
dataset.download(
    local_path=r"C:/downloads",
    annotation_options=[
        dl.VIEW_ANNOTATION_OPTIONS_MASK,
        dl.VIEW_ANNOTATION_OPTIONS_JSON,
        dl.ViewAnnotationOptions.INSTANCE
    ]
)
```

#### Filtered Downloads

Download specific annotations based on filters:

```python
# Filter for specific items
item_filters = dl.Filters(resource="items", field="dir", values="/specific_folder")

# Filter for specific annotations
annotation_filters = dl.Filters(
    resource=dl.FiltersResource.ANNOTATION,
    field="label",
    values="desired_label"
)

# Download with filters
dataset.download(
    local_path=r"C:/filtered_downloads",
    filters=item_filters,
    annotation_filters=annotation_filters,
    annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON
)
```

### Format Conversion 🔄

Want to convert annotations between different formats? We've got you covered! First, grab our handy converter toolkit:

1. Install our [dtlpy-converters](https://github.com/dataloop-ai-apps/dtlpy-converters) package 🛠️
```bash
pip install git+https://github.com/dataloop-ai-apps/dtlpy-converters
```

2. Let's start converting! 🚀

#### Converting TO Dataloop Format ⬇️

Here's how to bring your COCO/YOLO/VOC annotations into Dataloop:

```python
import dtlpy as dl
from dtlpyconverters.coco import CocoToDataloop
from dtlpyconverters.yolo import YoloToDataloop
from dtlpyconverters.voc import VocToDataloop


# 🎯 COCO to Dataloop
coco_dataset = dl.datasets.get(dataset_id="dataset_id")
converter = CocoToDataloop(
    dataset=coco_dataset,
    input_items_path=r"C:/path/to/coco/items",
    # Make sure item filenames match the COCO json! 🎯
    input_annotations_path=r"C:/path/to/coco/items/annotations",
    upload_items=True
)
converter.convert(
    coco_json_filename="annotations.json",
    annotation_options=[
        dl.AnnotationType.BOX,
        dl.AnnotationType.SEGMENTATION
    ],
    to_polygon=True
)

# 🎯 YOLO to Dataloop
yolo_dataset = dl.datasets.get(dataset_id="dataset_id")
converter = YoloToDataloop(
    dataset=yolo_dataset,
    input_items_path=r"C:/path/to/yolo/items",
    # Make sure item filenames match YOLO txt files! 🎯
    input_annotations_path=r"C:/path/to/yolo/items/annotations",
    upload_items=True,
    add_labels_to_recipe=True
)
converter.convert(
    labels_txt_filepath=r"C:/path/to/yolo/items/labels/labels.txt"
)

# 🎯 VOC to Dataloop
voc_dataset = dl.datasets.get(dataset_id='dataset_id')
converter = VocToDataloop(
    dataset=voc_dataset,
    input_items_path=r"C:/path/to/voc/items",
    # Make sure item filenames match VOC xml files! 🎯
    input_annotations_path=r"C:/path/to/voc/items/annotations",
    upload_items=True,
    add_labels_to_recipe=True
)
converter.convert()
```

#### Converting FROM Dataloop Format ⬆️

Need to export your Dataloop annotations to other formats? Here's how:

```python
import dtlpy as dl
from dtlpyconverters.coco import DataloopToCoco
from dtlpyconverters.yolo import DataloopToYolo
from dtlpyconverters.voc import DataloopToVoc

# Set up your filters (optional but powerful!) 🎯
filters = dl.Filters()
# Example: Get items from specific folder
filters.add(field=dl.FiltersKnownFields.DIR, values='/dog_name')
# Example: Filter for dog annotations
filters.add_join(field=dl.FiltersKnownFields.LABEL, values='dog')

# 🎯 Dataloop to COCO
coco_dataset = dl.datasets.get(dataset_id='')
converter = DataloopToCoco(
    dataset=coco_dataset,
    input_annotations_path=r'C:/input_coco',
    output_annotations_path=r'C:/output_coco',
    download_annotations=True,
    output_items_path=None,
    download_items=False,
    filters=filters,
    label_to_id_mapping=None
)
converter.convert()

# 🎯 Dataloop to YOLO
yolo_dataset = dl.datasets.get(dataset_id='')
converter = DataloopToYolo(
    dataset=yolo_dataset,
    input_annotations_path=r'C:/input_yolo',
    output_annotations_path=r'C:/output_yolo',
    download_annotations=True,
    output_items_path=None,
    download_items=False,
    filters=filters
)
converter.convert()

# 🎯 Dataloop to VOC
voc_dataset = dl.datasets.get(dataset_id='')
converter = DataloopToVoc(
    dataset=voc_dataset,
    input_annotations_path=r'C:/input_voc',
    output_annotations_path=r'C:/output_voc',
    download_annotations=True,
    output_items_path=None,
    download_items=False,
    filters=filters
)
converter.convert()
```

**Pro Tips! 💡**
- Always check that your item filenames match the annotation files
- Use filters to convert specific subsets of your data
- Remember that converter functions are async - use `asyncio.run()`!

## Best Practices for Large Scale Operations 🎯

### Error Handling  🛡️

**Error Handling**: Always include error handling for large operations
   ```python
   try:
       items = dataset.items.upload(local_path=large_batch)
   except dl.exceptions.PlatformException as e:
       print(f"Platform error: {e}")
   ```

### Performance Optimization 🚀

**Batch Processing**: Group operations for better performance
   ```python
   # Example: Batch upload with progress tracking
   items_batch = []
   with tqdm.tqdm(total=len(file_list)) as pbar:
       for i, file_path in enumerate(file_list):
           items_batch.append({
               'local_path': file_path,
               'remote_name': f'processed_{i}.jpg'
           })
           if len(items_batch) == 100:  # Process in batches of 100
               dataset.items.upload(local_path=pd.DataFrame(items_batch))
               items_batch = []
               pbar.update(100)
   ```

**Progress Tracking**: Use progress bars for long operations
   ```python
   # Track progress for any operation
   def process_with_progress(items):
       with tqdm.tqdm(total=len(items)) as pbar:
           for item in items:
               # Your processing logic here
               process_item(item)
               pbar.update(1)
   ```

### Parallel Processing 🔄

7. **Multi-threading**: Use parallel processing for large datasets
   ```python
   from concurrent.futures import ThreadPoolExecutor

   def process_in_parallel(items, max_workers=32):
       with ThreadPoolExecutor(max_workers=max_workers) as executor:
           futures = []
           for item in items:
               future = executor.submit(process_item, item)
               futures.append(future)

           # Wait for all tasks to complete
           for future in futures:
               future.result()
   ```

### Logging 📝

**Logging**: Maintain detailed logs for debugging
    ```python
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def process_with_logging(item):
        try:
            logger.info(f"Processing item: {item.id}")
            # Your processing logic here
            logger.info(f"Successfully processed item: {item.id}")
        except Exception as e:
            logger.error(f"Error processing item {item.id}: {str(e)}")
            raise
    ```

## Need More Help? 🤔

- Check out our [Python SDK Documentation](https://sdk-docs.dataloop.ai/en/latest/entities.html)
- Visit our [Community Forum](https://dataloop.ai/community)
- Explore our [Tutorials](https://docs.dataloop.ai/tutorials)

Happy coding! 🚀
