# Metadata and Filtering: Organizing Your AI Data 🔍

Master the art of organizing and finding your data using Dataloop's powerful metadata and filtering capabilities.

## Working with Metadata 📝

### 1. Adding Metadata

```python
import dtlpy as dl

# Add metadata to an item
item = dataset.items.get(item_id='your-item-id')
item.metadata['user'] = {
    'photographer': 'John Doe',
    'location': 'New York',
    'camera': {
        'model': 'Canon EOS R5',
        'settings': {
            'iso': 100,
            'aperture': 'f/2.8',
            'shutter_speed': '1/1000'
        }
    },
    'tags': ['outdoor', 'daylight']
}
item = item.update()

# Add metadata during upload
item = dataset.items.upload(
    local_path='/path/to/image.jpg',
    metadata={
        'user': {
            'project_id': 'PRJ-123',
            'batch': 'B-001'
        }
    }
)
```

### 2. Updating Metadata

```python
# Update specific fields
item.metadata['user']['status'] = 'reviewed'
item.metadata['user']['last_modified'] = '2024-03-20'
item = item.update()

# Batch update metadata
filters = dl.Filters(field='dir', values='/batch1')
dataset.items.update(
    filters=filters,
    update_values={
        'user.status': 'processed',
        'user.batch': 'B-001'
    }
)
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
# Create filters
filters = dl.Filters()

# Filter by filename
filters.add(field='filename', values='*.jpg')

# Filter by directory
filters.add(field='dir', values='/raw-data')

# Filter by created date
filters.add(field='createdAt', values="2024-03-*")

# Get filtered items
pages = dataset.items.list(filters=filters)
```

### 2. Metadata Filters

```python
# Filter by metadata fields
filters = dl.Filters()

# Exact match
filters.add(field='metadata.user.status', values='reviewed')

# Multiple values
filters.add(field='metadata.user.tags', values=['outdoor', 'daylight'], operator=dl.FiltersOperations.IN)

# Larger than, smaller than
filters.add(field='metadata.user.camera.settings.iso', 
           values=100,
           operator=dl.FiltersOperations.GREATER_THAN)

# Nested field exists
filters.add(field='metadata.user.camera', 
           operator=dl.FiltersOperations.EXISTS)
```

### 3. Complex Queries

```python
# Combining multiple filters
filters = dl.Filters(resource=dl.FiltersResource.ITEM)

# AND operation (default)
filters.add(field='metadata.user.status', values='reviewed')
filters.add(field='metadata.user.quality', values=5)

# OR operation
filters.add(field='metadata.user.tags', values=['important', 'urgent'],
           operator=dl.FiltersOperations.OR)

# NOT operation
filters.add_join(field='label', values='rejected',
                operator=dl.FiltersOperations.NOT)
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