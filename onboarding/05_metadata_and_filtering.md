# Metadata and Filtering: Organizing Your AI Data 🔍

Master the art of organizing and finding your data using Dataloop's powerful metadata and filtering capabilities.

## Project Setup ⚙️

### Dataloop Login 🔐

> ```python
> import dtlpy as dl
> from dotenv import load_dotenv
> import os
>
> # Load environment variables from .env file
> load_dotenv(override=True)
>
> # Access your API key securely
> api_key = os.getenv('DTLPY_API_KEY')
>
> # Initialize Dataloop with the API key
> dl.login_api_key(api_key=api_key)
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
> except Exception:
>     project = dl.projects.create(project_name=project_name)
>     # Create project if it doesn't exist
>     print(f"Created project '{project_name}'")
>
> try:
>     # Try to get existing dataset
>     dataset = project.datasets.get(dataset_name=dataset_name)
>     print(f"Dataset '{dataset_name}' already exists")
>
> except Exception:
>     # Create dataset if it doesn't exist
>     dataset = project.datasets.create(dataset_name=dataset_name)
>     print(f"Created dataset '{dataset_name}'")
> ```

## Working with Metadata 📝

### 1. Adding Metadata

> ```python
> # Print dataset items details
> dataset.items.list().print()
> # Print dataset items metadata
> for item in dataset.items.list().all():
>     print(item.metadata)
> ```

> ```python
> # Get first item id
> item = dataset.items.list().items[0]
> item_id = item.id
> ```

> ```python
> import dtlpy as dl
>
> # Add metadata to the first item
> item = dataset.items.get(item_id=item_id)
> item.metadata['user'] = {
>     'photographer': 'John Doe',
>     'location': 'New York',
>     'camera': {
>         'model': 'Canon EOS R5',
>         'settings': {
>             'iso': 120,
>             'aperture': 'f/2.8',
>             'shutter_speed': '1/1000'
>         }
>     },
>     'tags': ['outdoor', 'daylight']
> }
> item = item.update()
>
> print(item.metadata['user'])
> ```

> ```python
> # Set the item_id from the list above
> local_image_path = '/path/to/image.jpg'
>
> # Add metadata during upload
> item = dataset.items.upload(
>     local_path=local_image_path,
>     item_metadata={
>         'user': {
>             'project_id': 'PRJ-123',
>             'batch': 'B-001'
>         }
>     }
> )
>
> for item in dataset.items.list().all():
>     print(item.metadata)
> ```

### 2. Updating Metadata

> ```python
> dataset.items.list().print()
> ```

> ```python
> # Update specific fields
> item.metadata['user']['status'] = 'reviewed'
> item.metadata['user']['last_modified'] = '2024-03-20'
> item = item.update()
>
> # Batch update metadata, set filter dir values
> filters = dl.Filters(field='dir', values='/my-folder/news/')
> dataset.items.update(
>     filters=filters,
>     update_values={
>         'user.status': 'processed',
>         'user.batch': 'B-001'
>     }
> )
> ```

> ```python
> for item in dataset.items.list().all():
>     print(item.metadata)
> ```

### 3. Metadata Schema

> ```python
> # Define a metadata schema
> schema = {
>     "type": "object",
>     "properties": {
>         "user": {
>             "type": "object",
>             "properties": {
>                 "status": {
>                     "type": "string",
>                     "enum": ["new", "in-progress", "reviewed"]
>                 },
>                 "quality": {
>                     "type": "integer",
>                     "minimum": 1,
>                     "maximum": 5
>                 }
>             }
>         }
>     }
> }
>
> # Apply schema to dataset
> dataset.metadata_schema = schema
> dataset.update()
> ```

## Advanced Filtering 🎯

### 1. Basic Filters

> ```python
> dataset.items.list().print()
> ```

> ```python
> # Create filters
> filters = dl.Filters()
>
> # Filter by filename
> filters.add(field='filename', values='*.jpg')
>
>
> # Filter by directory, set filter dir values
> filters.add(field='dir', values='/my-folder/news/')
>
> # filter by created date, set filter date value
> filters.add(field='createdAt', values='2026-05-23' , operator=dl.FiltersOperations.GREATER_THAN)
>
> dataset.items.list(filters=filters).print()
> ```

### 2. Metadata Filters

> ```python
> for item in dataset.items.list().all():
>     print(item.metadata)
> ```

> ```python
> # Filter by metadata fields
> filters = dl.Filters()
>
> # Exact match
> filters.add(field='metadata.user.location', values='New York')
>
> # Error:  Cannot query on key 'metadata.user.tags' - no items contain the specified key, or the key is unsearchable
> # error on filtering an array field
> # filters.add(field='metadata.user.tags', values=['outdoor', 'daylight'], operator=dl.FiltersOperations.IN)
>
> # Larger than, smaller than
> filters.add(field='metadata.user.camera.settings.iso',
>            values=100,
>            operator=dl.FiltersOperations.GREATER_THAN_OR_EQUAL)
>
> dataset.items.list(filters=filters).print()
> for item in dataset.items.list(filters=filters).all():
>     print(item.metadata)
> ```

### 3. Complex Queries

> ```python
> for item in dataset.items.list().all():
>     print(item.metadata)
> ```

> ```python
> # Combining multiple filters
> filters = dl.Filters(resource=dl.FiltersResource.ITEM)
>
> # AND operation (default)
> filters.add(field='metadata.user.status', values='reviewed')
> filters.add(field='metadata.user.batch', values='B-001')
>
>
> # NOT EQUAL operation
> filters.add(field='metadata.user.status', values='rejected', operator=dl.FiltersOperations.NOT_EQUAL)
>
> print(filters.prepare())
>
> dataset.items.list(filters=filters).print()
> for item in dataset.items.list(filters=filters).all():
>     print(item.metadata)
> ```

> ```python
> dataset.open_in_web()
> ```

### 4. Pagination and Sorting

> ```python
> # Get items with pagination
> filters = dl.Filters()
> pages = dataset.items.list(
>     filters=filters,
>     page_offset=0,
>     page_size=50
> )
>
> # Sort results
> filters.sort_by(field='metadata.user.quality', value=dl.FiltersOrderByDirection.ASCENDING)
> ```

## Practical Examples 💡

### 1. Quality Control Pipeline

> ```python
> def quality_control_pipeline(dataset):
>     """Filter and process high-quality items"""
>     # Get high-quality, reviewed items
>     filters = dl.Filters()
>     filters.add(field='metadata.user.quality', values=[4, 5])
>     filters.add(field='metadata.user.status', values='reviewed')
>
>     high_quality_items = dataset.items.list(filters=filters)
>
>     # Process items
>     for item in high_quality_items:
>         process_high_quality_item(item)
> ```

### 2. Data Organization

> ```python
> def organize_by_metadata(dataset):
>     """Organize items into folders based on metadata"""
>     filters = dl.Filters()
>     items = dataset.items.list(filters=filters)
>
>     for item in items:
>         # Get metadata values
>         category = item.metadata['user'].get('category', 'uncategorized')
>
>         # Create category folder
>         new_path = f'/{category}/{item.name}'
>
>         # Move item
>         dataset.items.move(item=item, new_path=new_path)
> ```

### 3. Batch Processing

> ```python
> def process_unreviewed_items(dataset):
>     """Find and process unreviewed items"""
>     # Create filter for unreviewed items
>     filters = dl.Filters()
>     filters.add(field='metadata.user.status', values='new')
>
>     # Get items in batches
>     page_size = 100
>     pages = dataset.items.list(
>         filters=filters,
>         page_size=page_size
>     )
>
>     for page in pages:
>         for item in page:
>             # Process item
>             process_item(item)
>
>             # Update status
>             item.metadata['user']['status'] = 'processed'
>             item.update()
> ```

## Best Practices 👑

### 1. Metadata Structure
- Use consistent naming conventions
- Keep metadata hierarchical
- Document metadata schema
- Validate metadata values

### 2. Query Optimization

> ```python
> # Use specific fields when possible
> filters.add(field='metadata.user.status', values='reviewed')  # ✅
>
> # Combine filters efficiently
> filters = dl.Filters(resource=dl.FiltersResource.ITEM)
> filters.add(field='dir', values='/dataset1')
> filters.add(field='metadata.user.status', values='reviewed')
> ```

### 3. Error Handling

> ```python
> def safe_metadata_update(item, updates):
>     """Safely update item metadata"""
>     try:
>         for key, value in updates.items():
>             item.metadata['user'][key] = value
>         return item.update()
>     except Exception as e:
>         print(f"Error updating metadata: {str(e)}")
>         return None
> ```

### 4. Filter Error Troubleshooting

> ```python
> # Filter by metadata fields
> filters = dl.Filters()
> filters.add(field='metadata.user.camera',
>            values=True,
>            operator=dl.FiltersOperations.EXISTS)
>
> dataset.items.list(filters=filters).print()
> ```

#### Troubleshooting Filter Error

If you encounter this error:
```
Cannot query on key 'your-key' - no items contain the specified key, or the key is unsearchable
```

This indicates that the key you're using in your filter is either not valid or cannot be queried. Since the dataset schema defines all filterable keys, use it to verify your filter:

**Open the dataset schema endpoint:**
```
https://gate.dataloop.ai/api/v1/datasets/<dataset_id>/schema
```

**Check for your key under:**
- **schema keys** – filtered keys
- **unsearchablePaths** – unsearchable paths


Ready to explore task management? Let's move on to the next chapter! 🚀
