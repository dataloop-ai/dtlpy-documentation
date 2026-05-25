# Data Management Fundamentals 💾

Master the essentials of managing your data in Dataloop - from uploading files to organizing your datasets efficiently.

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
```

## Configuration Setup

```python
#TODO Please review the configuration and set your configuration setup

# ============================================================================
# Configuration
project_name = "onboarding-project-1"  # Name of your Dataloop project
# ============================================================================
# Project and Dataset Names
dataset_name = "onboarding-dataset-10"  # Name of your Dataloop dataset

# Local File Paths
# Note: The 'r' prefix creates a raw string, which treats backslashes as literal characters.
# This prevents Python from interpreting backslashes as escape sequences (e.g., \n, \t, \U).
# Essential for Windows paths to avoid SyntaxError and incorrect path handling.
# TODO  - set you  local file and folder images paths 
local_jpg_path_1 = r"C:\Users\Yigal_Pinhasi\OneDrive - Dell Technologies\Pictures\dogs\dog1.jpg"  # Path to first single image file
local_jpg_path_2 = r"C:\Users\Yigal_Pinhasi\OneDrive - Dell Technologies\Pictures\dogs\dog2.jpg"  # Path to second single image file
local_folder_path = r"C:\Users\Yigal_Pinhasi\OneDrive - Dell Technologies\Pictures\dogs2"  # Path to local folder for batch upload
local_folder_download_path = r"C:\Users\Yigal_Pinhasi\OneDrive - Dell Technologies\Pictures\dogs3"  # Path to local folder for downloading items

# Remote Paths (virtual folder structure in Dataloop)
remote_item_path = "/folder/new_1"  # Remote path for single item uploads
remote_batch_path = "/my-folder/news"  # Remote path for batch folder uploads
remote_bulk_path = "/my-folder/bulk"  # Remote path for bulk operations
```

```python
# ============================================================================
# Project and Dataset Setup
# ============================================================================
# Create your project and dataset (or get if they already exist)

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

## Uploading Items 📤

### 1. Single Item Upload

```python
#delete all dataset items
for item in dataset.items.list().all():
    item.delete()
```

```python
import dtlpy as dl

# Upload a single file
item = dataset.items.upload(
    local_path=local_jpg_path_1,
    remote_path=remote_item_path,  # Optional
    item_metadata={
        'photographer': 'John Doe',
        'location': 'New York'
    }
)

item.metadata['user'] = {
    'name': 'Lucky luke',
    'location': 'Israel'
}

item.update()

item_id = item.id

item.print()
print(item.metadata)
```

```python
# Open the item in the Dataloop web dashboard to view metadata
item.open_in_web()
```

### 2. Batch Upload

```python
dataset.items.list().print()


# Upload entire directory
dataset.items.upload(
    local_path=local_folder_path,
    remote_path=remote_batch_path,
    # local_annotations_path='/path/to/annotations'  # Optional
)

dataset.items.list().print()


```

```python
# Upload multiple specific files
items = dataset.items.upload(
    local_path=[local_jpg_path_1, local_jpg_path_2],
    remote_path=remote_item_path
)

dataset.items.list().print()
```

```python
# List items in the dataset
dataset.items.list().print()

dataset.open_in_web()
```

## File Organization Strategies 📂

### 1. Directory Structure

```python
item.print()
# Move items
item.move(
    new_path='/new/path/item.jpg'
)

item.print()

# List directory contents
pages = dataset.items.list(filters=dl.Filters(field='dir', values=remote_item_path))
pages.print()
```

### 2. Item Management

```python
# Set your filter directory value
dataset.items.list().print()

# Get the directory path from the 'dir' column in the output above
# This is the virtual folder path where items are stored in Dataloop
filter_dir = remote_item_path
```

```python
# Get item by ID or filename
item = dataset.items.get(item_id=item_id)
# Delete items
dataset.items.delete(filters=dl.Filters(field='dir', values=filter_dir))
dataset.items.list().print()
```

### 3. Metadata Organization

```python
item = dataset.items.get(item_id=item_id)
item.print()

# Add metadata to item
item.metadata['user'] = {
    'status': 'reviewed',
    'quality': 'high',
    'tags': ['validated', 'ready']
}
item = item.update()

```

```python
dataset.items.list().print()

#TODO Set the directory filter value (use the 'dir' column from the items list)
filter_items_dir = '/dataset/folder/dogs2'

# Batch metadata update
filters = dl.Filters(field='dir', values=filter_items_dir)
dataset.items.update(
    filters=filters,
    update_values ={'user.status': 'reviewed_in_batch'}
    # system_update_values={'user.status': 'reviewed_in_batch'},
    # system_metadata=True
)

#YGP-TODO cant see data updatedd
for item in dataset.items.list().all():
    print(item.metadata)

```

## Batch Operations ⚡

### 1. Bulk Upload and Download

```python
# Bulk upload
dataset.items.upload(
    local_path=local_folder_path,
    remote_path='/dataset/folder'
)

dataset.items.list().print()

# Bulk download
dataset.items.download(
    local_path=local_folder_download_path,
    filters=dl.Filters(field='dir', values=filter_items_dir)
)
```

### 2. Batch Processing

```python
#TODO  - set the filter_item_dir with coreesponng value from the items list
filter_item_dir = '/my-folder/news/dogs2'
# Process multiple items
filters = dl.Filters(field='dir', values=filter_item_dir)
pages = dataset.items.list(filters=filters)

def process_item(item):
    """Process a single item"""
    print(f'Processing: {item.name}')
    # Add your processing logic here
    # e.g., download, transform, analyze
    return item

for page in pages:
    for item in page:
        # Process each item
        process_item(item)

print(f"filtter_items_dir: {filter_items_dir}")
dataset.items.list().print()
# Batch delete
dataset.items.delete(filters=filters)
dataset.items.list().print()
```

### 3. Concurrent Operations

```python
import concurrent.futures

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

#YGP-TODO- doesnt work - need to futher investigate
for folder in folders:
    dataset.folders.create(folder_name=folder)
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
