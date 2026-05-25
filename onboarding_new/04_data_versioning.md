# Data Versioning: Managing Your Dataset Evolution 📚

Learn how to track, manage, and restore different versions of your datasets in Dataloop - your key to maintaining data lineage and reproducibility.

## Getting Started with Versioning 🌟

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
dataset_name = "onboarding-dataset-7"  # Name of your Dataloop dataset
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

### 1. Check Your Dataset

```python
dataset_id = dataset.id
dataset.items.list().print()
```

### 2. Dataset Cloning

```python
# Clone an entire dataset
dataset_cloned_name = 'dataset_v2'
dataset.clone(clone_name=dataset_cloned_name,
              filters=None,
              with_items_annotations=True,
              with_metadata=True,
              with_task_annotations_status=True)

#TODO set your filter dir value
flter_dir = '/folder/new_1' 
# Clone with filters
filters = dl.Filters()
filters.add(field='dir', values=flter_dir)
dataset.clone(clone_name='filtered_dataset',
              filters=filters,
              with_items_annotations=True)
```

## Dataset Management 📊

### 1. Listing Datasets

```python
# List all datasets in project
project.datasets.list()
```

```python
#explore your new datasets in DL Dashabord 

cloned_dataset = project.datasets.get(dataset_name=dataset_cloned_name)
filtered_dataset = project.datasets.get(dataset_name="filtered_dataset")

cloned_dataset.open_in_web()
filtered_dataset.open_in_web()
```

```python
project_id = project.id
cloned_ds_id = cloned_dataset.id

print(project_id)
print(cloned_ds_id)
```

### 2. Merging Datasets

```python
#TODO set the following dataset and project IDs
# Merge two datasets
# dataset_ids = ["dataset-1-id", "dataset-2-id"]
# project_ids = ["project-1-id", "project-2-id"]


dataset_ids = ["6a1296ae94a902e4e9340552", "6a129af3fe11fc28fc2a9e70"]
project_ids = ["f0625840-f0e4-42e1-afdc-786c545a8f1b", "f0625840-f0e4-42e1-afdc-786c545a8f1b"]
dataset_merge = dl.datasets.merge(
    merge_name="my_merged_dataset",
    project_ids=project_ids,
    dataset_ids=dataset_ids,
    with_items_annotations=True,
    with_metadata=False,
    with_task_annotations_status=False
)
```

## Best Practices 👑

### 1. Dataset Organization
- Use clear naming conventions for cloned datasets
- Document the purpose of each dataset version
- Keep track of dataset lineage
- Validate merged datasets before using them

### 2. Version Management
- Clone datasets before making major changes
- Use filters to create specific subset versions
- Maintain documentation of version differences
- Test merged datasets thoroughly

### 3. Error Prevention

```python
# Validate dataset before operations
try:
    dataset = project.datasets.get(dataset_id='dataset_id')
    # Proceed with operations
except dl.exceptions.NotFound:
    print("Dataset not found!")
```

## Pro Tips 💡

1. **Clone with Purpose**
   - Always specify meaningful clone names
   - Include relevant metadata and annotations
   - Document the reason for cloning

2. **Merge with Care**
   - Ensure datasets have compatible recipes
   - Verify project and dataset IDs
   - Test merged dataset integrity

3. **Version Control**
   - Keep track of dataset versions
   - Document changes between versions
   - Maintain clear version naming conventions

Ready to explore pipelines and automation? Let's move on to the next chapter! 🚀
