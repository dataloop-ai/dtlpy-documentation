# Working with Items and Annotations in Dataloop 📦

Welcome to your guide to working with items and annotations in Dataloop! Whether you're uploading files, managing metadata, or organizing your data, we've got you covered. Let's dive in!

## Understanding Items 📚

In Dataloop, an item can be any type of data - images, videos, text files, and more. Think of items as the building blocks of your datasets. Each item can have:
- Metadata
- Annotations
- Custom attributes
- And more!

### Basic Item Operations 🛠️

### Uploading Individual Files

Let's start with the basics - uploading specific files to your dataset:

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()

# Get your project and dataset
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')

# Upload specific files
local_path = [
    r'C:/home/project/images/John Morris.jpg',
    r'C:/home/project/images/John Benton.jpg',
    r'C:/home/project/images/Liu Jinli.jpg'
]
remote_path = '/folder_name'  # Optional: files go to root directory by default

# Upload the files
dataset.items.upload(
    local_path=local_path,
    remote_path=remote_path
)
```

### Uploading Entire Folders

Need to upload all files from a folder? Here's how:

```python
# Specify your folder path
local_path = r'C:/home/project/images'
remote_path = '/folder_name'

# Upload everything in the folder
dataset.items.upload(
    local_path=local_path,
    remote_path=remote_path
)
```

### Working with URLs

You can also add items using their URL links:

```python
# Prepare your URL
url_path = 'http://ww.some_website/beautiful_flower.jpg'
file_name = 'flower.jpg'

# Create a URL link
link = dl.UrlLink(
    ref=url_path,
    mimetype='image',
    name=file_name
)

# Upload the link
item = dataset.items.upload(local_path=link)

# View the item in the platform
item.open_in_web()
```

### Working with Metadata 📝

Think of metadata as your data's personal diary - you can attach any information you want to both items and annotations. It's perfect for organizing, filtering, and finding your data later.

> ⚠️ **Note**: When adding new metadata to an item, it might overwrite existing metadata, so be careful to preserve existing data when needed.

#### Metadata Types

Metadata supports various data types:

1. 📝 **Strings**
```python
item.metadata['user'] = {'message': 'Hello, World!'}
annotation.metadata['user'] = {'mood': 'Happy'}
```

2. 🔢 **Numbers**
```python
item.metadata['user'] = {'lucky_number': 42}
annotation.metadata['user'] = {'confidence_score': 0.95}
```

3. ✅ **Booleans**
```python
item.metadata['user'] = {'is_verified': True}
annotation.metadata['user'] = {'needs_review': False}
```

4. 👻 **Null**
```python
item.metadata['user'] = {'secret': None}
```

#### Basic Metadata Upload

Here's how to upload items with metadata:

```python
# Prepare item information
item_info = {
    'local_path': 'path/to/image.jpg',
    'remote_path': '/destination',
    'remote_name': 'new_name.jpg',
    'item_metadata': {
        'user': {
            'category': 'flower',
            'color': 'red'
        }
    }
}

# Upload with metadata
item = dataset.items.upload(**item_info)
```

#### Updating Existing Item Metadata

```python
# Get your item
item = dataset.items.get(item_id='your-item-id')

# Add or update metadata
if 'user' not in item.metadata:
    item.metadata['user'] = dict()
item.metadata['user']['mood'] = 'fantastic'

# Save the changes
item = item.update()
```

#### Finding Items by Metadata

Want to find all items with specific metadata? Here's how:

```python
# Create filters
filters = dl.Filters(resource=dl.FiltersResource.ITEM)
filters.add(field='metadata.user.mood', values='fantastic')

# Find matching items
pages = dataset.items.list(filters=filters)
for page in pages:
    for item in page:
        print(f"Found item: {item.name} with mood: {item.metadata['user']['mood']}")
```

### Working with Arrays 🔢a

Need to upload numpy arrays directly? Here's how:

```python
import cv2
import numpy as np
from PIL import Image

# Load image with cv2
img_cv2 = cv2.imread("/home/tmp/saturn.jpg")

# Or load with PIL
img_pil = np.asarray(Image.open("/home/tmp/saturn.jpg"))

# Upload array (remote_name is required!)
item = dataset.items.upload(
    local_path=img_cv2,
    remote_name='saturn.jpg'
)

# View in platform
item.open_in_web()
```

### Working with Modalities 🎭

Modalities are multiple layers representing the same reality or scene. For example, you might have multiple sensors capturing the same object, or different views of the same item. In Dataloop, you can link these related items as modality layers.

#### Adding a Single Modality

Here's how to set one item as a modality of another:

```python
# Get your main item
main_item = dataset.items.get(item_id='main-item-id')

# Get the modality item
modality_item = dataset.items.get(item_id='modality-item-id')

# Create the modality link
main_item.modalities.create(
    name='thermal_view',  # Give your modality a descriptive name
    modality_type=dl.ModalityTypeEnum.OVERLAY,
    ref=modality_item.id
)

# Update the main item to apply changes
main_item.update()
```

#### Working with Multiple Modalities

For multiple modalities, you can use a JSON layout to organize your items:

```python
# Example modalities layout
modalities_layout = {
    "main_image.jpg": [  # Main item path or URL
        "thermal_view.jpg",  # Modality 1
        "depth_map.png"     # Modality 2
    ],
    "https://example.com/main.jpg": [  # Main item URL
        "https://example.com/thermal.jpg",
        "https://example.com/depth.png"
    ]
}

# Function to upload and link modalities
def upload_with_modalities(dataset, source, modalities):
    # Upload main item (handle both local files and URLs)
    if not os.path.isfile(source):
        source = dl.UrlLink(ref=source)
    main_item = dataset.items.upload(local_path=source)
    
    # Upload modalities
    modalities = [
        mod if os.path.isfile(mod) else dl.UrlLink(ref=mod) 
        for mod in modalities
    ]
    modality_items = dataset.items.upload(
        local_path=modalities,
        remote_path='/modalities'
    )
    
    # Create modality links
    for mod_item in modality_items:
        main_item.modalities.create(
            modality_type=dl.ModalityTypeEnum.OVERLAY,
            ref=mod_item.id,
            name=f'{mod_item.name}:{mod_item.id}'
        )
    main_item.update(system_metadata=True)

# Process all items with modalities in parallel
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=32) as executor:
    for source, modalities in modalities_layout.items():
        executor.submit(
            upload_with_modalities,
            dataset=dataset,
            source=source,
            modalities=modalities
        )
```

## Working with Annotations in Dataloop 🎨

Welcome to your guide to working with annotations in Dataloop! Whether you're creating labels, managing metadata, or organizing your annotations, we've got you covered. Let's dive in!

### Understanding Annotations 📚

In Dataloop, annotations are the building blocks of your labeled data. Each annotation can have:
- Labels
- Attributes
- Metadata
- Task and Recipe context
- And more!

### Basic Annotation Operations 🛠️

### Adding Simple Annotations

Let's start with the basics - adding annotations to an item:

```python
import dtlpy as dl
item = dl.items.get(item_id="your-item-id")

# Create an annotation collection
collection = item.annotations.builder()

# Add a classification
collection.add(
    annotation_definition=dl.Classification(label="Komodo Dragon"),
    metadata={"type": "reptile"}
)

# Upload the annotations
item.annotations.upload(annotations=collection)
```

### Working with Metadata

Need to update annotation metadata? Here's how:

```python
# Get an existing annotation
annotation = item.annotations.get(annotation_id="your-annotation-id")

# Update metadata
annotation.metadata["user"] = True
annotation.update()
```

### Setting Attributes 🏷️

#### Free Text Attribute

```python
annotation.attributes.update({"ID of the attribute": "value of the attribute"})
annotation = annotation.update(True)
```

#### Range Attributes (Slider in UI)

```python
annotation.attributes.update({"<attribute-id>": number_on_range})
annotation = annotation.update(system_metadata=True)
```

#### CheckBox Attribute (Multiple Choice)

```python
annotation.attributes.update({"<attribute-id>": ["selection1", "selection2"]})
annotation = annotation.update(system_metadata=True)
```

#### Radio Button Attribute (Single Choice)

```python
annotation.attributes.update({"<attribute-id>": "selection"})
annotation = annotation.update(system_metadata=True)
```

#### Yes/No Attribute

```python
annotation.attributes.update({"<attribute-id>": True})  # or False
annotation = annotation.update(system_metadata=True)
```

### Task and Recipe Context 📋

Want to add task context to your annotations? Here's how:

```python
# Get the entities
assignment = dl.assignments.get(assignment_id="your-assignment-id")
task = dl.tasks.get(task_id="your-task-id")
# OR
task = assignment.task
recipe = dl.recipes.get(recipe_id="your-recipe-id")
# OR
recipe = dl.recipes.get(recipe_id=task.recipe_id)

# Create context dictionary
context = {
    "taskId": task.id,
    "assignmentId": assignment.id,
    "recipeId": recipe.id
}

# Add annotation with context
collection = item.annotations.builder()
collection.add(
    annotation_definition=dl.Classification(label="Komodo Dragon"),
    metadata={"system": context}
)
item.annotations.upload(annotations=collection)

# Or update existing annotation
annotation = item.annotations.get(annotation_id="your-annotation-id")
annotation.metadata["system"].update(context)
annotation.update(system_metadata=True)
```

### Visualizing Annotations 👁️

#### Show Individual Annotations

```python
# Use the show function for specific annotation types
box = dl.Box()
box.show(
    image="path/to/image",
    thickness=2,
    with_text=True,
    height=None,  # Optional
    width=None,   # Optional
    annotation_format="dl.ViewAnnotationOptions.*",
    color=(0, 255, 0)  # RGB format
)
```

#### Show All Item Annotations

```python
# Show all annotations on an item
annotation.show(
    image="path/to/image",
    height=None,  # Optional
    width=None,   # Optional
    annotation_format="dl.ViewAnnotationOptions.*",
    thickness=2,
    with_text=True
)
```

## Best Practices 💡

### Data Organization and Structure 📂
1. **Organize Your Data**: Use clear folder structures with meaningful names
2. **Organize Your Annotations**: Use clear labels and consistent naming
3. **Keep Metadata Clean**: Use structured metadata for better organization

### Workflow Optimization 🔄
4. **Use Batch Operations**: Upload multiple items and annotations at once when possible
5. **Monitor Progress**: Use progress bars for large uploads
6. **Check File Types**: Ensure your files are in supported formats

### Quality and Context 🎯
7. **Add Metadata**: Include relevant metadata during upload for better organization
8. **Add Context**: Include task and recipe context when relevant for annotations
9. **Use Attributes**: Leverage attributes for additional information in annotations
10. **Validate Visually**: Always check your annotations visually after upload

## Need More Help? 🤔

- Check out our [Python SDK Documentation](https://sdk-docs.dataloop.ai/en/latest/entities.html)
- Explore [Advanced Examples](tutorials/data_management/items_and_annotations/more_examples/chapter.md)
- Visit our [Community Forum](https://dataloop.ai/community) for more tips

Happy working with Dataloop! 🚀
