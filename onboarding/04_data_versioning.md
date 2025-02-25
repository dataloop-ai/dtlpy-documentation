# Data Versioning: Managing Your Dataset Evolution 📚

Learn how to track, manage, and restore different versions of your datasets in Dataloop - your key to maintaining data lineage and reproducibility.

## Getting Started with Versioning 🌟

### 1. Getting Your Dataset

```python
# Get your dataset
dataset = project.datasets.get(dataset_id='<dataset_id>')
```

### 2. Dataset Cloning

```python
# Clone an entire dataset
dataset.clone(clone_name='dataset_v2',
              filters=None,
              with_items_annotations=True,
              with_metadata=True,
              with_task_annotations_status=True)

# Clone with filters
filters = dl.Filters()
filters.add(field='dir', values='/specific/folder')
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

### 2. Merging Datasets

```python
# Merge two datasets
dataset_ids = ["dataset-1-id", "dataset-2-id"]
project_ids = ["project-1-id", "project-2-id"]
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