# Data Versioning: Managing Your Dataset Evolution 📚

Learn how to track, manage, and restore different versions of your datasets in Dataloop - your key to maintaining data lineage and reproducibility.

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

# Initialize Dataloop with the API key
dl.login_api_key(api_key=api_key)
```

### Project and Dataset Setup

```python
# Set your project and dataset names
project_name = "onboarding-project"
dataset_name = "onboarding-dataset"

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
## Getting Started with Versioning 🌟

> This section will use all three dataset types.
> Please review them in the following link:
> [Dataset Types Overview](https://docs.dataloop.ai/docs/datasets-overview#dataset-types)

### 1. Check Your Dataset

```python
# Check the dataset items
dataset_id = dataset.id
dataset.items.list().print()
```

```python
# Explore the dataset in the Dataloop platform
dataset.open_in_web()
```

### 2. Dataset Cloning

```python
# Clone an entire dataset
# Set your clone datset names
dataset_cloned_name = 'dataset_v1'
dataset_filter_cloned_name = 'dataset_v1_filtered'

dataset_cloned = dataset.clone(clone_name=dataset_cloned_name,
              filters=None,
              with_items_annotations=True,
              with_metadata=True,
              with_task_annotations_status=True)

# Create a filtered clone dataset 
# Set the flter_dir to filter in files from  with coresponding dir value taken out of the items list
filter_dir = '/batch-upload/dogs2' 
# Clone with filters
filters = dl.Filters()
filters.add(field='dir', values=filter_dir)

dataset_filter_cloned = dataset_cloned.clone(clone_name=dataset_filter_cloned_name,
              filters=filters,
              with_items_annotations=True)
```

```python
dataset_cloned.items.list().print()
dataset_filter_cloned.items.list(filters=filters).print()
```

## Dataset Management 📊

### 1. Listing Datasets

```python
# List all datasets in project
project.datasets.list()
```

### 2. Merging Datasets

```python
# Multiple cloned datasets can be merged into one, which enables multiple annotations to be merged onto the same item.

# Merge two cloned datasets
dataset_ids = [dataset_cloned.id, dataset_filter_cloned.id]
project_ids = [project.id]

merged_dataset_name = "my_merged_dataset"

dl.datasets.merge(
    merge_name=merged_dataset_name,
    project_ids=project_ids,
    dataset_ids=dataset_ids,
    with_items_annotations=True,
    with_metadata=False,
    with_task_annotations_status=False
)
```

```python
# Print ore the datasets items
merged_dataset = project.datasets.get(dataset_name=merged_dataset_name)

dataset_cloned.items.list().print()
dataset_filter_cloned.items.list().print()
merged_dataset.items.list().print()
```

```python
# Explore the dataset in the Dataloop platform
merged_dataset.open_in_web()
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
