# Managing Datasets and Versioning in Dataloop 🗄️

Welcome to your guide to managing datasets in Dataloop! Whether you're organizing your data, connecting to cloud storage, or managing versions, we've got you covered. Let's dive in!

## Understanding Datasets 📚

Think of datasets as smart buckets in Dataloop that can hold any type of data item. The cool part? Your data can live anywhere - either on Dataloop's storage or your favorite cloud provider. There's no limit to how many datasets you can have in a project, making it perfect for versioning and experimentation.

## Creating and Managing Datasets 🛠️

### Creating Your First Dataset ✨

Let's start with the basics - creating a dataset:

```python
dataset_name = 'My Amazing Dataset'
dataset = project.datasets.create(dataset_name=dataset_name)
```

### Creating a Cloud-Connected Dataset ☁️

If you didn't connect your cloud storage to Dataloop yet, you can do it by following the instructions in one of the following tutorials:

- [Amazon Web Services (S3)](/tutorials/data_management/external_storage_drivers/aws_s3/chapter.md)
- [Microsoft Azure Blob Storage](/tutorials/data_management/external_storage_drivers/azure_blob/chapter.md)
- [Google Cloud Storage](/tutorials/data_management/external_storage_drivers/gcs/chapter.md)

Already have your data in the cloud? No problem! If you've set up your cloud integration and driver, you can create a dataset that connects directly to your cloud storage:

```python
project_name = 'my-project-name'
driver = 'my_driver_name'
dataset_name = 'my_dataset_name'

# Get your project
project = dl.projects.get(project_name=project_name)

# See available drivers
project.drivers.list().print()

# Create dataset with cloud driver
dataset = project.datasets.create(
    driver=driver,
    dataset_name=dataset_name
)
```

### Creating a Dataset with Elastic Metadata (Storage Analytics)

For a dataset on external storage (NFS, PowerScale or S3), you can store the items' metadata in Elasticsearch so it can be queried and analyzed there.

```python
# The platform manages the Elasticsearch metadata driver
dataset = project.datasets.create_storage_analytics(
    dataset_name='my-nfs-dataset',
    driver_id='storage-driver-id'
)

# Use your own Elasticsearch database driver instead
dataset = project.datasets.create_storage_analytics(
    dataset_name='my-nfs-dataset',
    driver_id='storage-driver-id',
    metadata_driver_id='elastic-driver-id'
)
```

`create_storage_analytics()` is a shortcut for `datasets.create()` with `metadata_driver_id`. If you leave `metadata_driver_id` out, it uses `dl.MetadataDriver.SYSTEM`, the platform's internal Elasticsearch:

```python
dataset = project.datasets.create(
    dataset_name='my-nfs-dataset',
    driver_id='storage-driver-id',
    metadata_driver_id=dl.MetadataDriver.SYSTEM
)
print(dataset.metadata_driver_id)  # 'system'
```

| Input | Explanation |
|---|---|
| `driver_id` | The storage driver of the dataset. A storage driver is required when you set `metadata_driver_id`. |
| `metadata_driver_id` | The ID of an Elasticsearch database driver, or `dl.MetadataDriver.SYSTEM`. |

`dataset.metadata_driver_id` is set by the platform and is read-only. This is different from a database-backed dataset, where the rows themselves live in the database - see [Database-Backed Datasets](/tutorials/data_management/external_storage_drivers/database_backed_datasets/chapter.md).

### Finding Your Datasets 🔍

Need to find specific datasets? Use our powerful DQL (Dataloop Query Language) to filter and search:

```python
# Set up filters
filters = dl.Filters(resource=dl.FiltersResource.DATASET)
filters.add(field='name', values='my dataset')

# List matching datasets
datasets = project.datasets.list(filters=filters)
datasets.print()
```

### Organizing with Directories 📂

Keep your files organized by creating directories based on any context you need - upload time, batch, source, etc:

```python
directory = '/directory/name'
dataset.items.make_dir(directory=directory)
```

### Deep Copying Between Datasets 📋

Need to copy data between datasets? Here's how to do it while preserving your folder structure and annotations:

```python
# Source and destination details
src_folder = '/source_folder'
dst_folder = '/destination_folder'
src_project_name = 'source_project_name'
src_dataset_name = 'source_dataset_name'
dst_project_name = 'destination_project_name'
dst_dataset_name = 'destination_dataset_name'

# Copy settings
copy_annotations = True
flat_copy = False  # Keep folder structure (False) or copy all files to root (True)

# Get source dataset
project = dl.projects.get(project_name=src_project_name)
dataset_from = project.datasets.get(dataset_name=src_dataset_name)

# Set up filters for source folder
filters = dl.Filters()
filters.add(field='filename', values=src_folder.rstrip('/') + '/**')

# Get all items to copy
pages = dataset_from.items.list(filters=filters)

# Get destination dataset
project = dl.projects.get(project_name=dst_project_name)
dataset_to = project.datasets.get(dataset_name=dst_dataset_name)

# Copy files and annotations
for page in pages:
    for item in page:
        # Download without saving to disk
        buffer = item.download(save_locally=False)
        
        # Set filename based on copy type
        if flat_copy:
            buffer.name = item.name
        else:
            buffer.name = item.filename[len(src_folder) + 1:]
            
        # Upload to destination
        print(f"Adding {buffer.name} to {dst_folder}")
        new_item = dataset_to.items.upload(
            local_path=buffer,
            remote_path=dst_folder
        )
        
        if not isinstance(new_item, dl.Item):
            print(f'Failed to upload {buffer.name} to {dst_folder}')
            continue
            
        print(f"Successfully uploaded {new_item.filename}")
        
        # Copy annotations if requested
        if copy_annotations:
            new_item.annotations.upload(item.annotations.list())
```

## Data Versioning: Your Time Machine 🕰️

Dataloop's powerful versioning system helps you manage your data like a pro. Here's what you can do:

- Create golden training sets 🏆
- Snapshot datasets for reproducibility 📸
- Experiment with different subsets 🧪
- Manage tasks and assignments 📋
- Roll back to previous versions if needed ⏮️

### Cloning Datasets 🐑

Want a copy of your dataset? Cloning creates a new dataset that references the original files (no duplicate storage needed):

```python
dataset_id = 'my-dataset-id'
clone_name = 'clone-name'

# Get original dataset
dataset = project.datasets.get(dataset_id=dataset_id)

# Create clone with specific settings
dataset_clone = dataset.clone(
    clone_name=clone_name,
    filters=dl.Filters(field='dir', values='/only-this-folder'),
    with_items_annotations=True,
    with_metadata=True,
    with_task_annotations_status=True,
    target_directory='/clone-folder'
)
```

### Merging Datasets 🤝

Need to combine datasets? Here's what happens when you merge:

* **Cloned Datasets**: Items, annotations, and metadata merge smoothly - you'll see all annotations on the same items
* **Different Datasets (non-clones)**: Similar items might appear multiple times
* **Different Recipes**: You'll need to match recipes before merging (use 'Switch recipe' in dataset options)

Here's how to merge datasets:

```python
dataset_ids = ["dataset-1-id", "dataset-2-id"]
project_ids = ["dataset-1-project-id", "dataset-2-project-id"]
merge_name = 'my_dataset-merge'

# Merge the datasets
dataset_merge = dl.datasets.merge(
    merge_name=merge_name,
    project_ids=project_ids,
    dataset_ids=dataset_ids,
    with_items_annotations=True,
    with_metadata=False
)
```

### Exporting Datasets

The following example using Dataloop's Python SDK demonstrates how to export datasets with advanced options. It includes generating a *summary file*, enabling *dataset locking during export* to maintain data consistency, and setting an *automatic unlock timeout* to handle potential export delays and reduce workflow interruptions.


```python
import dtlpy as dl

filters = dl.Filters()
# Filer for all annotated items
filters.add(field='annotated', values=True)
# Join by filtering a specific label on the annotations
filters.add_join(field='label', values='<name>')

# Get the project
project = dl.projects.get(project_id='<id>')

# Export dataset
project.datasets.export(dataset_id='<id>', 
                        export_type='zip',
                        export_summary=True,
                        filters=filters)

# Lock dataset during export
project.datasets.export(dataset_id='<id>', 
                        export_type='zip', 
                        dataset_lock=True,
                        filters=filters) 

# Set automatic-lock timeout for stuck exports
project.datasets.export(dataset_id='<id>', 
                        export_type='zip', 
                        lock_timeout_sec=1000, 
                        filters=filters)

```

Check out our Dataloop documentation for details:
- [Export Datasets](https://docs.dataloop.ai/docs/manage-your-datasets#export-entire-datasets)
- [Lock Datasets During Export](https://docs.dataloop.ai/docs/datasets-overview#lock-datasets-during-export)
- [Download an Export Summary File](https://docs.dataloop.ai/docs/manage-your-datasets#download-an-export-summary-file)
- [Automatic lock timeout for stuck exports](https://docs.dataloop.ai/docs/datasets-overview#lock-datasets-during-export:~:text=Automatic%20lock%20timeout%20for%20stuck%20exports)

### Download Annotations

This script downloads annotations from a Dataloop dataset in JSON and mask formats, with options to include label text, control dataset locking, and set an automatic unlock timeout.

```python
dataset.download(local_path='local_path',
                 annotation_options=[dl.ViewAnnotationOptions.JSON, dl.ViewAnnotationOptions.MASK],
                 overwrite=False,
                 thickness=1,
                 with_text=False,
                 alpha=1,
                 dataset_lock=True,
                 lock_timeout_sec=300
                 )
```


## Collections: Your Data's Best Friend 🤝

Think of Collections as smart tags on steroids! They're your secret weapon for organizing data like a pro. Whether you're juggling labeling tasks, managing massive datasets, or getting your data ready for model training - Collections have got your back! 

Want to learn all the cool tricks? Check out our [Dataloop documentation](https://docs.dataloop.ai/docs/organize-your-data#collections) for the full scoop! 🎓

### Become a Collections Master 🎯

Ready to become a Collections wizard? The Dataloop SDK gives you superpowers to create, update, delete, and manage collections at both dataset and item levels. Let's break it down!

**Dataset Level Magic Tricks ✨**

These are your dataset-wide spells for managing collections. Think of them as your high-level organization tools:

1. Create a new collection (max 10 per dataset - choose wisely!)
```python
dataset.collections.create(name: str)
```

2. Give your collection a fancy new name (keep it unique!)
```python
dataset.collections.update(collection_id: str, new_name: str)
```

3. Make a collection disappear (poof! 🎩)
```python
dataset.collections.delete(collection_id: str)
```

4. Clone a collection (it's like ctrl+c, ctrl+v, but cooler)
```python
dataset.collections.clone(collection_id: str)
```

5. See all your collections in one place
```python
dataset.collections.list_all_collections()
```

6. Find the lone wolves (items not in any collection)
```python
dataset.collections.list_unassigned_items()
```

**Item Level Ninja Moves 🥷**

These methods are your precision tools - perfect for when you need that surgical accuracy:

1. Add an item to a collection (like adding a card to your favorite deck)
```python
item.assign_collection(item_id: str, collection_name: str)
```

2. Remove an item from a collection (no hard feelings!)
```python
item.unassign_collection(item_id: str, collection_id: str)
```

3. Check which collections an item belongs to
```python
item.list_collections(item_id: str)
```

** Bulk Operations 🤖**

Assign and unassign items to collections in bulk, using dl.Filters:

```python
filters = dl.Filters()
filters.add(field='id', values=['<item_id>'], operator=dl.FiltersOperations.IN)
dataset.collections.assign(collections=['my_collection'], filters=filters)
```

Or everything in a directory:

```python
filters = dl.Filters()
filters.add(field='dir', values='/my_directory')
dataset.collections.assign(collections=['my_collection'], filters=filters)
```

Same for unassigning:

```python
filters = dl.Filters()
filters.add(field='id', values=['<item_id>'], operator=dl.FiltersOperations.IN)
dataset.collections.unassign(collections=['my_collection'], filters=filters)
```

**Show Time! 🎬 Real-World Examples**

Let's see these powers in action:

```python
import dtlpy as dl

project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_id='<dataset_id>')

# Get a VIP list of all collections
dataset.collections.list_all_collections()

# Create a shiny new collection
dataset.collections.create(collection='my_awesome_collection')

# Clone it (because good things deserve doubles!)
dataset.collections.clone(collection_name='my_awesome_collection_2')

# Oops, changed our mind - let's delete one
dataset.collections.delete(collection_name='my_awesome_collection_2')

# Give it a cooler name
dataset.collections.update(collection_name='my_super_awesome_collection')

# Find the items playing hide and seek
dataset.collections.list_unassigned_items()

# Add an item to our cool collection
dataset.items.get(item_id='<item_id>').assign_collection(collections=['my_super_awesome_collection'])

# Let an item go free
dataset.items.get(item_id='<item_id>').unassign_collection(collections=['my_super_awesome_collection'])
```

## ML Subsets: Your Dataset's Secret Sauce 🌟

Welcome to ML Subsets - your dataset's personal organizer for machine learning! It's like having a smart assistant that helps you split your data into perfect training, validation, and test portions. No more manual sorting - we've got you covered! 

Want to become an ML Subsets guru? Check out our [detailed guide](https://docs.dataloop.ai/docs/organize-your-data#ml-subsets)! 📚

### ML Subsets: The Fun Way! 🎮

Let's see how to slice and dice your dataset with style:

**1. The Perfect Split (60-20-20 Style) 🎯**
```python
import dtlpy as dl

project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_id='<dataset_id>')

filters = dl.Filters(field='type', values='file')
dataset.split_ml_subsets(
    items_query=filters,
    percentages={'train': 60, 'validation': 20, 'test': 20}
)
```
* Like a chef perfectly portioning ingredients! 👨‍🍳
* Your files get VIP treatment in train (60%), validation (20%), and test (20%) clubs
* Perfectly balanced, as all things should be! 

**2. Send an Item to Training Camp 🏋️‍♂️**
```python
filters = dl.Filters()
filters.add(field='id', values=['<item_id>'], operator=dl.FiltersOperations.IN)
dataset.assign_subset_to_items(subset='train', items_query=filters)
```
* Hand-pick items for special training
* Like choosing your star player for the big game!

**3. Give an Item a Break 🏖️**
```python
filters = dl.Filters()
filters.add(field='id', values=['<item_id>'], operator=dl.FiltersOperations.IN)
dataset.remove_subset_from_items(items_query=filters)
```
* Sometimes items need a vacation from their subset
* No hard feelings - they can always come back later!

**4. Find the Free Agents 🔍**
```python
dataset.get_items_missing_ml_subset()
```
* Spot items that haven't joined a team yet
* Perfect for making sure no data is left behind!

## Need More Help? 🤔

Check out our [comprehensive documentation](https://docs.dataloop.ai/docs/welcome) for more details on dataset management and versioning.

Happy data managing! 🚀
