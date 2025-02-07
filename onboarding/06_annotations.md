# Data Annotation: Labeling Your Way to Success 🎯

Learn how to create, manage, and organize annotations in Dataloop - your key to building high-quality training data.

## Annotation Basics 🎨

### 1. Creating Annotations

```python
import dtlpy as dl

# Get your item
item = dataset.items.get(item_id='your-item-id')

# Create an annotation builder
builder = item.annotations.builder()

# Add a box annotation
builder.add(annotation_definition=dl.Box(
    top=100,
    left=100,
    bottom=200,
    right=200,
    label='car'
))

# Add a classification
builder.add(annotation_definition=dl.Classification(
    label='sedan',
))

# Upload annotations
item.annotations.upload(builder)
```

### 2. Annotation Types

```python
# Point annotation
builder.add(annotation_definition=dl.Point(
    x=100,
    y=100,
    label='landmark'
))

# Polygon annotation
builder.add(annotation_definition=dl.Polygon(
    geo=[[100, 100], [200, 100], [200, 200], [100, 200]],
    label='building'
))

# Segmentation annotation
builder.add(annotation_definition=dl.Segmentation(
    geo=[[100, 100], [200, 100], [200, 200]],
    label='road'
))

# Polyline annotation
builder.add(annotation_definition=dl.Polyline(
    geo=[[100, 100], [200, 200], [300, 300]],
    label='lane'
))
```

### 3. Advanced Annotation Properties

```python
# Add attributes
builder.add(annotation_definition=dl.Box(
    top=100,
    left=100,
    bottom=200,
    right=200,
    label='car',
    attributes={
        'color': 'red',
        'model': 'sedan',
        'damaged': True
    }
))

# Add metadata
builder.add(annotation_definition=dl.Box(
    top=100,
    left=100,
    bottom=200,
    right=200,
    label='car'
),
    metadata = {
        'confidence': 0.95,
        'reviewer': 'John'
    }
)
```

## Managing Annotations 📋

### 1. Querying Annotations

```python
# Get all annotations for an item
annotations = item.annotations.list()
for annotation in annotations:
    print(f"Found {annotation.label} at {annotation.coordinates}")

# Filter annotations by label
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
filters.add(field='label', values='car')
car_annotations = item.annotations.list(filters=filters)
```

### 2. Updating Annotations

```python
# Get specific annotation
annotation = item.annotations.get(annotation_id='annotation-id')

# Update properties
annotation.label = 'truck'
annotation.attributes['color'] = 'blue'
annotation.update()

# Update coordinates (for box)
if isinstance(annotation, dl.Box):
    annotation.top = 150
    annotation.bottom = 250
    annotation.update()
```

### 3. Batch Operations

```python
# Delete all annotations of a specific label
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
filters.add(field='label', values='car')
item.annotations.delete(filters=filters)

# Copy annotations between items
source_item = dataset.items.get(item_id='source-id')
target_item = dataset.items.get(item_id='target-id')

annotations = source_item.annotations.list()
target_item.annotations.upload(annotations)
```

## Working with Tasks 📝

### 1. Creating Tasks

```python
# Create an annotation task
task = dataset.tasks.create(
    task_name='Annotate Cars',
    assignee_ids=['annotator@company.com'],
    filters=dl.Filters(field='dir', values='/folder/to/annotate')
)

# Add specific items to task
task.add_items(
    item_ids=['item1-id', 'item2-id'],
    assignee_ids=['annotator@company.com']
)
```

### 2. Task Management

```python
# Get task by ID
task = dataset.tasks.get(task_id='task-id')

# Update task status
task.set_status(status='completed')

# Get task items
items = task.items.list()
for item in items:
    print(f"Item: {item.name}, Status: {item.status}")
```

## Quality Assurance 🔍

### 1. Annotation Review

```python
# Create a review task
review_task = dataset.tasks.create_qa_task(
    task=task, # Original task
    assignee_ids=['reviewer@company.com'],
    filters=dl.Filters(field='annotated', values=True)
)
```

### 2. Consensus Annotations

```python
# Get all annotations for comparison
annotations_a = item.annotations.list(filters=dl.Filters(field='creator', values='annotator1@company.com', resource=dl.FiltersResource.ANNOTATION))
annotations_b = item.annotations.list(filters=dl.Filters(field='creator', values='annotator2@company.com', resource=dl.FiltersResource.ANNOTATION))

# Calculate IoU for box annotations
def calculate_iou(box_a, box_b):
    if not (isinstance(box_a, dl.Box) and isinstance(box_b, dl.Box)):
        return 0
    # IoU calculation logic here
    pass
```

## Best Practices 👑

### 1. Annotation Guidelines

- Create clear labeling instructions
- Define label hierarchies
- Establish quality criteria
- Document edge cases

### 2. Workflow Optimization

```python
# Create annotation template
template = {
    'attributes': {
        'color': ['red', 'blue', 'green'],
        'size': ['small', 'medium', 'large'],
        'damaged': [True, False]
    }
}

# Apply template to new annotations
builder.add(annotation_definition=dl.Box(
    top=100,
    left=100,
    bottom=200,
    right=200,
    label='car',
    attributes=template['attributes']
))
```

### 3. Error Prevention

```python
def validate_annotation(annotation):
    """Validate annotation properties"""
    try:
        # Check required fields
        assert annotation.label, "Missing label"
        if isinstance(annotation, dl.Box):
            assert annotation.top < annotation.bottom, "Invalid box coordinates"
        return True
    except AssertionError as e:
        print(f"Validation failed: {str(e)}")
        return False
```


Ready to explore metadata and filtering? Let's move on to the next chapter! 🚀
