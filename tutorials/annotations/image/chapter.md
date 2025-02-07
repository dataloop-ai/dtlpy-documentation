# 🎨 Image Annotations - Your Visual Data Toolkit!

Welcome to the world of image annotations! Whether you're training an AI model, analyzing medical images, or cataloging your photo collection, annotations are your tools for marking, labeling, and understanding visual data. Let's dive into the exciting possibilities!

# 📋 Classification - Simple Yet Powerful

## Single Item Classification
Need to label an entire image? Here's how to add a simple classification:

```python
# Get item from the platform
item = dataset.items.get(filepath='/your-image-file-path.jpg')
# Create a builder instance
builder = item.annotations.builder()
# Add classification label
builder.add(annotation_definition=dl.Classification(label=label))
# Save to platform
item.annotations.upload(builder)
```

## Batch Classification
Got multiple images to classify? Let's do it efficiently:

```python
# Create a filter for batch processing
filters = dl.Filters()
# Add filter - only files
filters.add(field='type', values='file')
# Get filtered items
pages = dataset.items.list(filters=filters)
# Process each item
for page in pages:
    for item in page:
        builder = item.annotations.builder()
        builder.add(annotation_definition=dl.Classification(label='your-label'))
        item.annotations.upload(builder)
```

# 📍 Points & Poses - Precision Marking

## Point Annotations
Perfect for marking specific locations in your image:

```python
# Get your canvas ready
item = dataset.items.get(filepath='/your-image-file-path.jpg')
builder = item.annotations.builder()
# Add a point with attributes
builder.add(annotation_definition=dl.Point(x=100,
                                         y=100,
                                         label='my-label',
                                         attributes={'color': 'red'}))
# Save your work
item.annotations.upload(builder)
```

## Pose Annotations - Digital Skeletons
Create pose templates for tracking key points on subjects:

```python
# Get your pose template ID
template_id = recipe.get_annotation_template_id(template_name="my_template_name")

# Create the parent pose annotation
parent_annotation = item.annotations.upload(
    dl.Annotation.new(annotation_definition=dl.Pose(
        label='my_parent_label',
        template_id=template_id,
        instance_id=None  # Optional for tracking specific instances
    ))
)[0]

# Add the skeleton points
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Point(x=x,
                                         y=y,
                                         label='my_point_label'),
           parent_id=parent_annotation.id)
builder.upload()
```

# 📦 Boxes & Cuboids - Defining Regions

## Bounding Box
The classic way to mark regions of interest:

```python
# Create a simple box
builder.add(annotation_definition=dl.Box(top=10,
                                       left=10,
                                       bottom=100,
                                       right=100,
                                       label='my-label'))
```

## 3D Cuboid
Working in 3D? Choose your preferred method:

```python
# Method 1: Using front and back rectangles
builder.add(annotation_definition=dl.Cube.from_boxes_and_angle(
    label="label",
    front_top=100,
    front_left=100,
    front_right=300,
    front_bottom=300,
    back_top=200,
    back_left=200,
    back_right=400,
    back_bottom=400,
    angle=0
))

# Method 2: Using 8 corner points
builder.add(annotation_definition=dl.Cube(
    label="label",
    front_tl=[200, 200],  # Front top left
    front_tr=[500, 250],  # Front top right
    front_br=[500, 550],  # Front bottom right
    front_bl=[200, 500],  # Front bottom left
    back_tl=[300, 300],   # Back top left
    back_tr=[600, 350],   # Back top right
    back_br=[600, 650],   # Back bottom right
    back_bl=[300, 600]    # Back bottom left
))
```

# 🔷 Advanced Shapes - Creative Freedom

## Ellipse Annotations
Perfect for circular or oval regions:

```python
builder.add(annotation_definition=dl.Ellipse(
    x=center_x,
    y=center_y,
    rx=radius_x,
    ry=radius_y,
    angle=rotation_angle,
    label=label
))
```

## Polygons & Polylines
For when predefined shapes won't cut it:

```python
# Create a polygon
builder.add(annotation_definition=dl.Polygon(
    geo=[[100, 50], [80, 120], [110, 130]],
    label='my-label'
))

# Create a polyline
builder.add(annotation_definition=dl.Polyline(
    geo=[[100, 50], [80, 120], [110, 130]],
    label='my-label'
))
```

# 🎭 Segmentation - Pixel-Perfect Precision

## Basic Segmentation
Create a binary mask for your annotations:

```python
# Create a mask
mask = np.zeros(shape=(item.height, item.width), dtype=np.uint8)
mask[50:100, 200:250] = 1  # Mark region of interest

# Add segmentation annotation
builder.add(annotation_definition=dl.Segmentation(
    geo=mask,
    label='my-label'
))
```

## Converting Between Formats

### Mask to Polygon
```python
# Convert segmentation to polygon
builder.add(dl.Polygon.from_segmentation(
    mask=mask_annotation.geo,
    label=mask_annotation.label,
    max_instances=None
))
```

### Polygon to Mask
```python
# Convert polygon to segmentation
builder.add(dl.Segmentation.from_polygon(
    geo=polygon_annotation.geo,
    label=annotation.label,
    shape=img.size[::-1]  # (height, width)
))
```

## Segmentation from Instance Mask
Create segmentation from instance masks:

```python
# Create random instance mask
mask = np.random.randint(low=0, high=2, size=(item.height, item.width))
instance_map = {"background": 0, "foreground": 1}

# Convert to segmentation annotations
builder.from_instance_mask(mask=mask, instance_map=instance_map)
```

# 📝 Metadata & Description

## Item Description
Add context to your images:

```python
# Add or update item description
item.set_description(text="Detailed description of the image")
```

## Working with Attributes
Enrich your annotations with metadata:

```python
builder.add(annotation_definition=dl.Box(...),
           attributes={
               'confidence': 0.95,
               'category': 'vehicle',
               'condition': 'new'
           })
```

# 🚀 Advanced Tutorials

## Copying Annotations Between Items
Want to reuse annotations across different images? Here's how to copy them between items:

```python
# Set the source item with the annotations we want to copy
project = dl.projects.get(project_name='second-project_name')
dataset = project.datasets.get(dataset_name='second-dataset_name')
item = dataset.items.get(item_id='first-id-number')
annotations = item.annotations.list()

# Set the target item where we want to copy to
item = dataset.items.get(item_id='second-id-number')
item.annotations.upload(annotations=annotations)

# Want to copy to multiple items? Use filters!
filters = dl.Filters()
filters.add(field='filename', values='/fighting/**')  # Get files from directory (recursive)
filters.add(field='type', values='file')             # Only files
pages = dataset.items.list(filters=filters)

# Copy annotations to all filtered items
for page in pages:
    for item in page:
        item.annotations.upload(annotations=annotations)
```

## Visualizing Images & Annotations
Want to see your annotations? Here's how to visualize them:

```python
from PIL import Image

# Get your item
item = dataset.items.get(item_id='write-your-id-number')

# Download and open the image
buffer = item.download(save_locally=False)
image = Image.open(buffer)

# Get annotations as an image overlay
annotations = item.annotations.show(
    width=image.size[0],
    height=image.size[1],
    thickness=3
)
annotations = Image.fromarray(annotations.astype(np.uint8))

# View annotations and image separately
annotations.show()
image.show()

# Or view them combined!
image.paste(annotations, (0, 0), annotations)
image.show()
```

## Working with JSON Annotations
Need to load annotations from a JSON file? We've got you covered:

```python
from PIL import Image
import json

# Read annotations from JSON
with open(r'C:/home/project/images/annotation.json', 'r') as f:
    data = json.load(f)

# Display each annotation
for annotation in data['annotations']:
    annotations = dl.Annotation.from_json(annotation)
    mask = annotations.show(
        width=640,
        height=480,
        thickness=3,
        color=(255, 0, 0)
    )
    mask = Image.fromarray(mask.astype(np.uint8))
    mask.show()
```

## Counting Annotations
Need to know how many annotations you have? Here's a quick way:

```python
# Create annotation filters
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
filters.page_size = 0

# Get the total count
annotations_count = dataset.annotations.list(filters=filters).items_count
```

## Working with Parent-Child Relationships
Create hierarchical relationships between annotations:

### Creating Parent-Child While Uploading
```python
# Create parent box
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Box(
    top=10, left=10, bottom=100, right=100,
    label='my-parent-label'
))
# Upload parent and get its ID
annotations = item.annotations.upload(annotations=builder)

# Create child box linked to parent
builder = item.annotations.builder()
builder.add(
    annotation_definition=dl.Box(
        top=10, left=10, bottom=100, right=100,
        label='my-child-label'
    ),
    parent_id=annotations[0].id
)
# Upload the complete family
item.annotations.upload(annotations=builder)
```

### Linking Existing Annotations
```python
# Create and upload parent
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Box(
    top=10, left=10, bottom=100, right=100,
    label='my-parent-label'
))
parent_annotation = item.annotations.upload(annotations=builder)[0]

# Create and upload child
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Box(
    top=10, left=10, bottom=100, right=100,
    label='my-child-label'
))
child_annotation = item.annotations.upload(annotations=builder)[0]

# Link child to parent
child_annotation.parent_id = parent_annotation.id
child_annotation.update(system_metadata=True)
```

## Bulk Label Updates
Need to change labels across multiple annotations? Here's how:

```python
# Create a new label (optional)
dataset.add_label(label_name='newLabel', color=(2, 43, 123))

# Find all annotations with the old label
filters = dl.Filters()
filters.resource = dl.FiltersResource.ANNOTATION
filters.add(field='label', values='oldLabel')
pages = dataset.annotations.list(filters=filters)

# Update each annotation's label
for annotation in pages.all():
    annotation.label = 'newLabel'
    annotation.update()
```

# 💡 Pro Tips & Best Practices

## Annotation Quality
- Double-check coordinates and dimensions
- Use consistent labeling schemes
- Verify segmentation masks match image dimensions
- Keep attributes consistent across similar annotations

## Performance Optimization
- Use batch operations for multiple items
- Convert between formats efficiently
- Consider memory usage with large masks
- Cache frequently used templates

## Workflow Tips
- Create templates for common annotation patterns
- Use filters for batch operations
- Implement quality control checks
- Document your annotation guidelines

# 🔧 Troubleshooting Common Issues

## Coordinate Systems
- Remember: (0,0) is top-left corner
- Verify coordinate ranges match image dimensions
- Check angle calculations for rotated shapes
- Validate polygon point sequences

## Data Validation
- Verify mask dimensions match image size
- Check for closed polygons
- Validate attribute formats
- Test annotation visibility

Need help? Check out our other tutorials or reach out to our support team. Happy annotating! 🎨✨

