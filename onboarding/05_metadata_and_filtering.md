# Metadata and Filtering: Organizing Your AI Data 🔍

Master the art of organizing and finding your data using Dataloop's powerful metadata and filtering capabilities.

## Dataloop Login 🔐

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

# if dl.token_expired():
#     dl.login()
```

## Project and Dataset Setup

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

## Working with Metadata 📝

### 1. Adding Metadata

```python
def print_meta_data(filters=None):
    items = list(dataset.items.list(filters=filters).all())
    for item in items:
        print(item.metadata)
```

```python
# print datset items
dataset.items.list().print()
print_meta_data()
```

```python
#get first item id 
item = dataset.items.list().items[0]
item_id = item.id
```

```python
import dtlpy as dl

# Add metadata to an item
item = dataset.items.get(item_id=item_id)
item.metadata['user'] = {
    'photographer': 'John Doe',
    'location': 'New York',
    'camera': {
        'model': 'Canon EOS R5',
        'settings': {
            'iso': 120,
            'aperture': 'f/2.8',
            'shutter_speed': '1/1000'
        }
    },
    'tags': ['outdoor', 'daylight']
}
item = item.update()

print(item.metadata['user'])
```

```python
#set the item_id from the list above
local_image_path = '/path/to/image.jpg'

# Add metadata during upload
item = dataset.items.upload(
    local_path=local_image_path,
    item_metadata={
        'user': {
            'project_id': 'PRJ-123',
            'batch': 'B-001'
        }
    }
)

print_meta_data()
```

### 2. Updating Metadata

```python
dataset.items.list().print()
```

```python
# Update specific fields
item.metadata['user']['status'] = 'reviewed'
item.metadata['user']['last_modified'] = '2024-03-20'
item = item.update()

#set - fill filter dir 
filter_dir = '/my-folder/news/dogs2'

# Batch update metadata
filters = dl.Filters(field='dir', values=filter_dir)
dataset.items.update(
    filters=filters,
    update_values={
        'user.status': 'processed',
        'user.batch': 'B-001'
    }
)
```

```python
print_meta_data()
```

### 3. Metadata Schema

```python
# Define a metadata schema
schema = {
    "type": "object",
    "properties": {
        "user": {
            "type": "object",
            "properties": {
                "status": {
                    "type": "string",
                    "enum": ["new", "in-progress", "reviewed"]
                },
                "quality": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 5
                }
            }
        }
    }
}

# Apply schema to dataset
dataset.metadata_schema = schema
dataset.update()
```

## Advanced Filtering 🎯

### 1. Basic Filters

```python
dataset.items.list().print()
```

```python
# Create filters
filters = dl.Filters()

# Filter by filename
filters.add(field='filename', values='*.jpg')

# set filter dir 
filter_dir = "/my-folder/news/dogs2"
# Filter by directory
filters.add(field='dir', values=filter_dir)

#  Filter by created date
# #set filter date
filter_date = "2026-05-23"
filters.add(field='createdAt', values=filter_date, operator=dl.FiltersOperations.GREATER_THAN)

dataset.items.list(filters=filters).print()
```

### 2. Metadata Filters

```python
print_meta_data()
```

```python
# Filter by metadata fields
filters = dl.Filters()

# Exact match
filters.add(field='metadata.user.location', values='New York')

#YGP-ERROR:  Cannot query on key 'metadata.user.tags' - no items contain the specified key, or the key is unsearchable
# # Multiple values
# filters.add(field='metadata.user.tags', values=['outdoor', 'daylight'], operator=dl.FiltersOperations.IN)

# Larger than, smaller than
filters.add(field='metadata.user.camera.settings.iso', 
           values=100,
           operator=dl.FiltersOperations.GREATER_THAN_OR_EQUAL)

#YGP-ERROR: BadRequest error received: ('400', "Cannot query on key 'metadata.user.camera' - no items contain the specified key, or the key is unsearchable"
# filters.add(field='metadata.user.camera', 
#            values=True,
#            operator=dl.FiltersOperations.EXISTS)

dataset.items.list(filters=filters).print()
print_meta_data(filters)
```

### 3. Complex Queries

```python
print_meta_data()
```

```python
# Combining multiple filters
filters = dl.Filters(resource=dl.FiltersResource.ITEM)

# AND operation (default)
filters.add(field='metadata.user.status', values='reviewed')
filters.add(field='metadata.user.batch', values='B-001')


# NOT EQUAL operation
filters.add(field='metadata.user.status', values='rejected', operator=dl.FiltersOperations.NOT_EQUAL)

print(filters.prepare())

dataset.items.list(filters=filters).print()
print_meta_data(filters)
```

```python
dataset.open_in_web()   
```

### 2. Pagination and Sorting

```python
# Get items with pagination
filters = dl.Filters()
pages = dataset.items.list(
    filters=filters,
    page_offset=0,
    page_size=50
)

# Sort results
filters.sort_by(field='metadata.user.quality', value=dl.FiltersOrderByDirection.ASCENDING)
```

## Practical Examples 💡

### 1. Quality Control Pipeline

```python
def quality_control_pipeline(dataset):
    """Filter and process high-quality items"""
    # Get high-quality, reviewed items
    filters = dl.Filters()
    filters.add(field='metadata.user.quality', values=[4, 5])
    filters.add(field='metadata.user.status', values='reviewed')
    
    high_quality_items = dataset.items.list(filters=filters)
    
    # Process items
    for item in high_quality_items:
        process_high_quality_item(item)
```

### 2. Data Organization

```python
def organize_by_metadata(dataset):
    """Organize items into folders based on metadata"""
    filters = dl.Filters()
    items = dataset.items.list(filters=filters)
    
    for item in items:
        # Get metadata values
        category = item.metadata['user'].get('category', 'uncategorized')
        
        # Create category folder
        new_path = f'/{category}/{item.name}'
        
        # Move item
        dataset.items.move(item=item, new_path=new_path)
```

### 3. Batch Processing

```python
def process_unreviewed_items(dataset):
    """Find and process unreviewed items"""
    # Create filter for unreviewed items
    filters = dl.Filters()
    filters.add(field='metadata.user.status', values='new')
    
    # Get items in batches
    page_size = 100
    pages = dataset.items.list(
        filters=filters,
        page_size=page_size
    )
    
    for page in pages:
        for item in page:
            # Process item
            process_item(item)
            
            # Update status
            item.metadata['user']['status'] = 'processed'
            item.update()
```

## Best Practices 👑

### 1. Metadata Structure
- Use consistent naming conventions
- Keep metadata hierarchical
- Document metadata schema
- Validate metadata values

### 2. Query Optimization

```python
# Use specific fields when possible
filters.add(field='metadata.user.status', values='reviewed')  # ✅

# Combine filters efficiently
filters = dl.Filters(resource=dl.FiltersResource.ITEM)
filters.add(field='dir', values='/dataset1')
filters.add(field='metadata.user.status', values='reviewed')
```

### 3. Error Handling

```python
def safe_metadata_update(item, updates):
    """Safely update item metadata"""
    try:
        for key, value in updates.items():
            item.metadata['user'][key] = value
        return item.update()
    except Exception as e:
        print(f"Error updating metadata: {str(e)}")
        return None
```

Ready to explore task management? Let's move on to the next chapter! 🚀
