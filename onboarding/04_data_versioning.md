# Data Versioning: Managing Your Dataset Evolution 📚

Learn how to track, manage, and restore different versions of your datasets in Dataloop - your key to maintaining data lineage and reproducibility.

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
>     print("Dataset is empty. Please upload some items before proceeding.")
>     print("You can upload items by running: dataset.items.upload(local_path='path/to/your/files')")
> else:
>     print(f"Dataset has {dataset.items.list().items_count} items")
> ```

## Getting Started with Versioning 🌟

This section will use all three dataset types.
 Please review them in the following link:
 [Dataset Types Overview](https://docs.dataloop.ai/docs/datasets-overview#dataset-types)

### 1. Check Your Dataset

> ```python
> # Check the dataset items
> dataset_id = dataset.id
> dataset.items.list().print()
>
> # Explore the dataset in the Dataloop platform
> dataset.open_in_web()
> ```

### 2. Dataset Cloning

> ```python
> # Clone an entire dataset
> # Set your clone dataset names
> dataset_cloned_name = 'dataset_v1'
> dataset_filter_cloned_name = 'dataset_v1_filtered'
>
> dataset_cloned = dataset.clone(clone_name=dataset_cloned_name,
>               filters=None,
>               with_items_annotations=True,
>               with_metadata=True,
>               with_task_annotations_status=True)
>
> # Create a filtered clone dataset
> # Set the filter_dir to filter files by directory from the items list
> # Set this to a directory that exists in your dataset (check the items list above)
> filter_dir = '/batch-upload'
> # Clone with filters
> filters = dl.Filters()
> filters.add(field='dir', values=filter_dir)
>
> dataset_filter_cloned = dataset_cloned.clone(clone_name=dataset_filter_cloned_name,
>               filters=filters,
>               with_items_annotations=True)
> 
> # Print the cloned datasets
> dataset_cloned.items.list().print()
> # Print the filtered cloned dataset
> dataset_filter_cloned.items.list().print()
> ```

## Dataset Management 📊

### 1. Listing Datasets

> ```python
> # List all datasets in project
> project.datasets.list().print()
> ```

### 2. Merging Datasets

> ```python
> # NOTE: Not all datasets can be merged. Merge conditions:
> # 1. Cloned datasets: merge works only if items originated from the same master item (same source).
> # 2. Non-cloned datasets with the same recipe: items are summed, similar items will be duplicated.
> # 3. Datasets with different recipes: CANNOT be merged — align recipes first using 'Switch recipe'.
>
> # Multiple cloned datasets can be merged into one, which enables multiple annotations to be merged onto the same item.
>
> # Merge two cloned datasets
> dataset_ids = [dataset_cloned.id, dataset_filter_cloned.id]
> project_ids = [project.id]
>
> merged_dataset_name = "my_merged_dataset"
>
> dl.datasets.merge(
>     merge_name=merged_dataset_name,
>     project_ids=project_ids,
>     dataset_ids=dataset_ids,
>     with_items_annotations=True,
>     with_metadata=False,
>     with_task_annotations_status=False
> )
> ```

> ```python
> # Print the datasets items
> merged_dataset = project.datasets.get(dataset_name=merged_dataset_name)
>
> dataset_cloned.items.list().print()
> dataset_filter_cloned.items.list().print()
> merged_dataset.items.list().print()
> ```

> ```python
> # Explore the dataset in the Dataloop platform
> merged_dataset.open_in_web()
> ```

Ready to explore metadata and filtering? Let's move on to the next chapter! 🚀
