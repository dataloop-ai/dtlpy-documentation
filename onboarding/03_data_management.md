# Data Management Fundamentals 💾

Master the essentials of managing your data in Dataloop - from uploading files to organizing your datasets efficiently.

## Uploading Items 📤

### 1. Single Item Upload

```python
import dtlpy as dl

# Upload a single file
item = dataset.items.upload(
    local_path='/path/to/image.jpg',
    remote_path='/folder/in/dataset'  # Optional
)

# Upload with metadata
item = dataset.items.upload(
    local_path='/path/to/image.jpg',
    metadata={'photographer': 'John Doe',
              'location': 'New York'}
)
```

### 2. Batch Upload

```python
# Upload entire directory
dataset.items.upload(
    local_path='/path/to/folder',
    local_annotations_path='/path/to/annotations'  # Optional
)

# Upload multiple specific files
items = dataset.items.upload(
    local_path=['/path/1.jpg', '/path/2.jpg'],
    remote_path='/batch-upload'
)
```

## File Organization Strategies 📂

### 1. Directory Structure

```python
# Move items
item.move(
    new_path='/new/path/item.jpg'
)

# List directory contents
pages = dataset.items.list(filters=dl.Filters(field='dir', values='/folder'))
```

### 2. Item Management

```python
# Get item by ID or filename
item = dataset.items.get(item_id='item_id')
item = dataset.items.get(filepath='/images/item.jpg')

# Update item
item.filename = '/new_name.jpg' # The new filename must include the full path.
item.update(True)

# Delete items
dataset.items.delete(filters=dl.Filters(field='dir', values='/old/folder'))
```

### 3. Metadata Organization

```python
# Add metadata to item
item.metadata['user'] = {
    'status': 'reviewed',
    'quality': 'high',
    'tags': ['validated', 'ready']
}
item = item.update()

# Batch metadata update
filters = dl.Filters(field='dir', values='/folder')
dataset.items.update(
    filters=filters,
    update_values={'user.status': 'reviewed'}
)
```

## Batch Operations ⚡

### 1. Bulk Upload and Download

```python
# Bulk upload
dataset.items.upload(
    local_path='/path/to/folder',
    remote_path='/dataset/folder'
)

# Bulk download
dataset.items.download(
    local_path='/local/folder',
    filters=dl.Filters(field='dir', values='/dataset/folder')
)
```

### 2. Batch Processing

```python
# Process multiple items
filters = dl.Filters(field='dir', values='/folder')
pages = dataset.items.list(filters=filters)

for page in pages:
    for item in page:
        # Process each item
        process_item(item)

# Batch delete
dataset.items.delete(filters=filters)
```

### 3. Concurrent Operations

```python
import concurrent.futures

def process_batch(items):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_item, item) for item in items]
        concurrent.futures.wait(futures)
```

## Data Validation 🔍

### 1. Item Validation

```python
# Check item existence
try:
    item = dataset.items.get(filepath='/path/to/item.jpg')
except dl.exceptions.NotFound:
    print("Item not found!")

# Validate item metadata
def validate_item(item):
    required_fields = ['status', 'quality']
    metadata = item.metadata.get('user', {})
    return all(field in metadata for field in required_fields)
```

### 2. Batch Validation

```python
# Validate multiple items
def validate_items(dataset):
    invalid_items = []
    for item in dataset.items.list().all():
        if not validate_item(item):
            invalid_items.append(item.id)
    return invalid_items
```

### 3. Data Integrity Checks

```python
# Check for corrupted images
def check_image_integrity(item):
    try:
        buffer = item.download(save_locally=False)
        Image.open(buffer)
        return True
    except Exception as e:
        print(f"Corrupted image {item.name}: {e}")
        return False
```

## Best Practices 👑

### 1. File Organization
- Use consistent folder structures
- Implement clear naming conventions
- Keep related files together
- Document organization schema

### 32. Error Handling
```python
def safe_upload(path):
    try:
        item = dataset.items.upload(local_path=path, raise_on_error=True)
        return True, item
    except Exception as e:
        return False, str(e)
```

## Pro Tips 💡

1. **Efficient Data Organization**
   ```python
   # Create organized folder structure
   folders = ['train', 'val', 'test']
   for folder in folders:
       dataset.directory_tree.create(directory=f'/{folder}')
   ```

2. **Bulk Operations with Progress**
   ```python
   from tqdm import tqdm
   
   def upload_with_progress(files):
       for file in tqdm(files, desc="Uploading"):
           dataset.items.upload(local_path=file)
   ```

## Troubleshooting Guide 🔧

### Common Issues:

1. **Upload Failures**
   ```python
   # Retry mechanism
   def upload_with_retry(path, max_retries=3):
       for attempt in range(max_retries):
           try:
               return dataset.items.upload(local_path=path, raise_on_error=True)
           except Exception as e:
               if attempt == max_retries - 1:
                   raise e
               time.sleep(2 ** attempt)  # Exponential backoff
   ```

2. **Download Issues**
   ```python
   # Handle download errors
   try:
       item.download(local_path='path/to/save')
   except dl.exceptions.ItemNotFound:
       print("Item not found!")
   except dl.exceptions.ConnectionError:
       print("Connection error - retrying...")
   ```

Ready to start annotating your data? Let's move on to the annotation chapter! 🎯 