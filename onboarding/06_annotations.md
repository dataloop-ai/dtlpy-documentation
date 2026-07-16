# Data Annotation: Labeling Your Way to Success 🎯

Learn how to create, manage, and organize annotations in Dataloop - your key to building high-quality training data.

## Project Setup ⚙️

### Dataloop Login 🔐

> ```python
> import dtlpy as dl
>
> # Interactive login — opens a browser window
> if dl.token_expired():
>     dl.login()
> ```

### Project and Dataset Setup

> ```python
> # Set your project and dataset names
> project_name = "onboarding-project"
> dataset_name = "onboarding-dataset"
>
> try:
>     # Try to get existing project
>     project = dl.projects.get(project_name=project_name)
>     print(f"Project '{project_name}' already exists")
> except dl.exceptions.NotFound:
>     project = dl.projects.create(project_name=project_name)
>     # Create project if it doesn't exist
>     print(f"Created project '{project_name}'")
>
> try:
>     # Try to get existing dataset
>     dataset = project.datasets.get(dataset_name=dataset_name)
>     print(f"Dataset '{dataset_name}' already exists")
>
> except dl.exceptions.NotFound:
>     # Create dataset if it doesn't exist
>     dataset = project.datasets.create(dataset_name=dataset_name)
>     print(f"Created dataset '{dataset_name}'")
> ```

### Dataset Items Setup

> ```python
> # Ensure the dataset has items — if empty, upload sample files
> if dataset.items.list().items_count == 0:
>     print("Dataset is empty. Please upload some image files before proceeding.")
>     print("You can upload items by running: dataset.items.upload(local_path='path/to/your/images')")
> else:
>     print(f"Dataset has {dataset.items.list().items_count} items")
> ```

## Annotation Basics 🎨

### 1. Creating Annotations

> ```python
> item = dataset.items.list().items[0]
> first_item_id = item.id
>
> # Get your item
> item = dataset.items.get(item_id=first_item_id)
>
> # Create an annotation builder
> builder = item.annotations.builder()
>
> # Add a box annotation
> builder.add(annotation_definition=dl.Box(
>     top=100,
>     left=100,
>     bottom=200,
>     right=200,
>     label='car'
> ))
>
> # Add a classification
> builder.add(annotation_definition=dl.Classification(
>     label='sedan',
> ))
>
> # Upload annotations
> item.annotations.upload(builder)
> ```

> ```python
> # Explore the added annotations in your item
> item.open_in_web()
> ```

### 2. Annotation Types

> ```python
> # Point annotation
> builder.add(annotation_definition=dl.Point(
>     x=100,
>     y=100,
>     label='landmark'
> ))
>
> # Polygon annotation
> builder.add(annotation_definition=dl.Polygon(
>     geo=[[100, 100], [200, 100], [200, 200], [100, 200]],
>     label='building'
> ))
>
> # Segmentation annotation (geo must be a binary mask)
> import numpy as np
> mask = np.zeros(shape=(item.height, item.width), dtype=np.uint8)
> mask[100:200, 100:200] = 1
> builder.add(annotation_definition=dl.Segmentation(
>     geo=mask,
>     label='road'
> ))
>
> # Polyline annotation
> builder.add(annotation_definition=dl.Polyline(
>     geo=[[100, 100], [200, 200], [300, 300]],
>     label='lane'
> ))
> ```

### 3. Advanced Annotation Properties

> ```python
> # Add attributes
> builder.add(annotation_definition=dl.Box(
>     top=100,
>     left=100,
>     bottom=200,
>     right=200,
>     label='car',
>     attributes={
>         'color': 'red',
>         'model': 'sedan',
>         'damaged': True
>     }
> ))
>
> # Add metadata
> builder.add(annotation_definition=dl.Box(
>     top=100,
>     left=100,
>     bottom=200,
>     right=200,
>     label='car'
> ),
>     metadata = {
>         'confidence': 0.95,
>         'reviewer': 'John'
>     }
> )
> ```

## Managing Annotations 📋

### 1. Querying Annotations

> ```python
> # Get all annotations for an item
> annotations = item.annotations.list()
> for annotation in annotations:
>     print(f"Found {annotation.label} at {annotation.coordinates}")
>
> # Filter annotations by label
> filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
> filters.add(field='label', values='car')
> car_annotations = item.annotations.list(filters=filters)
> ```

### 2. Updating Annotations

> ```python
> annotations.print()
> annotation_id = annotations[0].id
> print(f"annotation id: {annotation_id} ")
> ```

> ```python
> # Get specific annotation
> annotation = item.annotations.get(annotation_id=annotation_id)
>
> # Update properties
> annotation.label = 'truck'
> annotation.attributes['color'] = 'blue'
> annotation.update()
>
> # Update coordinates (for box)
> annotation.top = 150
> annotation.bottom = 250
> annotation.update()
> ```

> ```python
> # Explore the item with updated annotations
> item.open_in_web()
> ```

### 3. Batch Operations

> ```python
> # Delete all annotations of a specific label
> filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
> filters.add(field='label', values='car')
> item.annotations.delete(filters=filters)
>
> source_id = first_item_id
>
> # Ensure your dataset has at least 2 items
> target_id = dataset.items.list().items[1].id
> # Copy annotations between items
> source_item = dataset.items.get(item_id=source_id)
> target_item = dataset.items.get(item_id=target_id)
>
> annotations = source_item.annotations.list()
> target_item.annotations.upload(annotations)
> ```

Ready to explore task management? Let's move on to the next chapter! 🚀
