# Data Annotation: Labeling Your Way to Success 🎯

Learn how to create, manage, and organize annotations in Dataloop - your key to building high-quality training data.

## Project Setup ⚙️

### Dataloop Login 🔐

```python
import dtlpy as dl
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access your API key securely
api_key = os.getenv('DTLPY_API_KEY')

print(f"API key: {api_key[:20]}...  ")

# Initialize Dataloop with the API key
dl.login_api_key(api_key=api_key)
```

### Project and Dataset Setup

```python
# Create your project and dataset (or get if they already exist)

# Set your project and dataset names
project_name = "onboarding-project-1"
dataset_name = "onboarding-dataset-1"

try:
    # Try to get existing project
    project = dl.projects.get(project_name=project_name)
    print(f"Project '{project_name}' already exists")
except Exception:
    project = dl.projects.create(project_name=project_name)
    # Create project if it doesn't exist
    print(f"Created project '{project_name}'")

try:
    # Try to get existing dataset
    dataset = project.datasets.get(dataset_name=dataset_name)
    print(f"Dataset '{dataset_name}' already exists")

except Exception:
    # Create dataset if it doesn't exist
    dataset = project.datasets.create(dataset_name=dataset_name)
    print(f"Created dataset '{dataset_name}'")
```

## Annotation Basics 🎨

### 1. Creating Annotations

```python
import dtlpy as dl

item = dataset.items.list().items[0]
item_id = item.id

# Get your item
item = dataset.items.get(item_id=item_id)

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

```python
# explore the added annotations in your item
item.open_in_web()
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
annotations.print()
anottation_id = annotations[0].id   
print(f"annotation id: {anottation_id} ")
```

```python
# Get specific annotation
annotation = item.annotations.get(annotation_id=anottation_id)

# Update properties
annotation.label = 'truck'
annotation.attributes['color'] = 'blue'
annotation.update()

# Update coordinates (for box)
annotation.top = 150
annotation.bottom = 250
annotation.update()
```

```python
item.open_in_web()
```

```python
dataset.items.list().print()
```

### 3. Batch Operations

```python
# Delete all annotations of a specific label
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
filters.add(field='label', values='car')
item.annotations.delete(filters=filters)

print(item_id)

source_id = item_id

target_id = '6a15976a4617583bfe5351e6' 
# Copy annotations between items
source_item = dataset.items.get(item_id=source_id)
target_item = dataset.items.get(item_id=target_id)

annotations = source_item.annotations.list()
target_item.annotations.upload(annotations)
```

## Working with Tasks 📝

### 1. Creating Tasks

```python
# Create an annotation task
# Set your email
email_addr = 'yigal.pinhasi@dell.com'
# email = 'annotator@company.com'
task = dataset.tasks.create(
    task_name='Annotate Cars',
    assignee_ids=[email_addr],
    filters=dl.Filters(field='dir', values='/folder/to/annotate')
)

# Add specific items to task
task.add_items(
    items=[source_item, target_item],
    assignee_ids=[email_addr]
)

task_id = task.id
```

```python
# Get task by ID
task = project.tasks.get(task_id=task_id)
```

```python
task.open_in_web()
```

### 2. Task Management

```python

# Update task status
task.set_status(status='completed', operation='create', item_ids=[source_id, target_id])

# Get task items
items = task.get_items()
# for item in items:
#     print(f"Item: {item.name}, Status: {item.status(assignment_id="", task_id="")}")


items.print()
```

## Quality Assurance 🔍

### 1. Annotation Review

```python
# Create a review task
review_task = dataset.tasks.create_qa_task(
    task=task, # Original task
    assignee_ids=[email_addr],
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
        assert annotation.top < annotation.bottom, "Invalid box coordinates"
        return True
    except AssertionError as e:
        print(f"Validation failed: {str(e)}")
        return False
```

Ready to explore metadata and filtering? Let's move on to the next chapter! 🚀
