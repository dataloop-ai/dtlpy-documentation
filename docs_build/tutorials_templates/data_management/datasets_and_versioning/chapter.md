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
dataset.assign_collection(collection_name='my_collection', filters=filters)
```

Or everything in a directory:

```python
filters = dl.Filters()
filters.add(field='dir', values='/my_directory')
dataset.assign_collection(collection_name='my_collection', filters=filters)
```

Same for unassigning:

```python
filters = dl.Filters()
filters.add(field='id', values=['<item_id>'], operator=dl.FiltersOperations.IN)
dataset.unassign_collection(collection_name='my_collection', filters=filters)
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
