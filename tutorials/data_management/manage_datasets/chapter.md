# Manage Datasets  
  
Datasets are buckets in the dataloop system that hold a collection of data items of any type, regardless of their  
storage location (on Dataloop storage or external cloud storage).  
  
## Create Dataset  
  
You can create datasets within a project. There are no limits to the number of dataset a project can have, which  
correlates with data versioning where datasets can be cloned and merged.  

```python
dataset_name = 'my-dataset-name'
dataset = project.datasets.create(dataset_name=dataset_name)
```
## Create Dataset With Cloud Storage Driver  
  
If you’ve created an integration and driver to your cloud storage, you can create a dataset connected to that driver. A  
single integration (for example: S3) can have multiple drivers (per bucket or even per folder), so you need to specify  
that.  
  

```python
project_name = 'my-project-name'
driver = 'my_driver_name'
dataset_name = 'my_dataset_name'
project = dl.projects.get(project_name=project_name)
# Get your drivers list
project.drivers.list().print()
# Create a dataset from a driver name. You can also create by the driver ID.
dataset = project.datasets.create(driver=driver, dataset_name=dataset_name)
```
  
## Retrieve Datasets  
  
You can query over datasets with a DQL, filter over fields to get a project's datasets:  
  

```python
dataset_id = 'my-dataset-id'
filters = dl.Filters(resource=dl.FiltersResource.DATASET)
filters.add(field='name', values='my dataset')
datasets = project.datasets.list(filters=filters)
datasets.print()
```
  
## Create Directory  
  
A dataset can have multiple directories, allowing you to manage files by context, such as upload time, working batch,  
source, etc.  

```python
directory = '/directory/name'
dataset.items.make_dir(directory=directory)
```
## Deep Copy a Folder to Another Dataset  
  
You can create a clone of a folder into a new dataset, but if you want to actually move between datasets a folder with  
files that are stored in the Dataloop system, you’ll need to download the files and upload again to the destination dataset.  
  

```python
source_folder = '/source_folder'
destination_folder = '/destination_folder'
source_project_name = 'source_project_name'
source_dataset_name = 'source_dataset_name'
destination_project_name = 'destination_project_name'
destination_dataset_name = 'destination_dataset_name'
copy_annotations = True
flat_copy = False  # if true, it copies all dir files and sub dir files to the destination folder without sub directories
# Get source project dataset
project = dl.projects.get(project_name=source_project_name)
dataset_from = project.datasets.get(dataset_name=source_dataset_name)
source_folder = source_folder.rstrip('/')
# Filter to get all files of a specific folder
filters = dl.Filters()
filters.add(field='filename', values=source_folder + '/**')  # Get all items in folder (recursive)
pages = dataset_from.items.list(filters=filters)
# Get destination project and dataset
project = dl.projects.get(project_name=destination_project_name)
dataset_to = project.datasets.get(dataset_name=destination_dataset_name)
# Go over all projects and copy file from src to dst
for page in pages:
    for item in page:
        # Download item (without save to disk)
        buffer = item.download(save_locally=False)
        # Give the item's name to the buffer
        if flat_copy:
            buffer.name = item.name
        else:
            buffer.name = item.filename[len(source_folder) + 1:]
        # Upload item
        print("Going to add {} to {} dir".format(buffer.name, destination_folder))
        new_item = dataset_to.items.upload(local_path=buffer, remote_path=destination_folder)
        if not isinstance(new_item, dl.Item):
            print('The file {} could not be upload to {}'.format(buffer.name, destination_folder))
            continue
        print("{} has been uploaded".format(new_item.filename))
        if copy_annotations:
            new_item.annotations.upload(item.annotations.list())
```

## Collections

Use Collections to efficiently tag, group, and organize your data. Streamline labeling tasks, manage large datasets effectively, and structure your data for optimized model training, ensuring better control and usability.

To learn more about setting up collection, please visit our [Dataloop documentation](https://docs.dataloop.ai/docs/data-browser#collections)

### Manage Collections in a Dataset

Leverage the Dataloop SDK to create, update, delete, and manage collections at both the dataset and item levels.

**Dataset Level Methods**

These methods operate on collections within a dataset, allow you to perform collection-level operations within a dataset, such as creating, updating, deleting, and retrieving collections.

1. Create a new collection in the dataset. The dataset can have a maximum of 10 collections. The collection name must be unique within the dataset.

	```
	dataset.collections.create(name: str)
	```

2. Rename an existing collection. The new collection name must be unique.

	```
	dataset.collections.update(collection_id: str, new_name: str): 
	```

3. Delete an existing collection. When deleted, the collection is automatically removed from all items assigned to it.

	```
	dataset.collections.delete(collection_id: str): 
	```

4. Clone an existing collection. The total number of collections in the dataset cannot exceed 10.

	```
	dataset.collections.clone(collection_id: str): 
	```

5. Retrieve a list of all collections within the dataset.

	```
	dataset.collections.list()
	```

6. List all item IDs in the dataset that are not assigned to any collections.

	```
	dataset.collections.list_unassigned_items(): 
	```


**Item Level Methods**

These methods work at the individual item level for managing collections. These methods allow direct manipulation of collections at the item level, including assigning, unassigning, and retrieving collection details.

1. Assign an item to a specific collection. If the specified collection does not exist, it is created (subject to validation rules like maximum collections and unique names).
	
	```
	item.assign_collection(item_id: str, collection_name: str)
	```

2. Remove an item from a specific collection.

	```
	item.unassign_collection(item_id: str, collection_id: str)
	```

3. Retrieve all collections that an item is currently assigned to.

	```
	item.list_collections(item_id: str)
	```

**Code Examples**: Using Collection Management Methods in the SDK

Below are practical examples demonstrating how to use the SDK for collection management.

1. List all collections in a dataset

	```
	dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').collections.list_all_collections()
	```

2. Create a new collection:
	
	```
	dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').collections.create(collection='my_collection')
	```

3. Clone a collection:

	```
	dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').collections.clone(collection_name='my_collection_copy')
	```

4. Delete a collection

	```
	dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').collections.delete(collection_name='my_collection_copy')
	```

5. Rename a collection

	```
	dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').collections.update(collection_name='my_collection')
	```

6. List unassigned items

	```
	dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').collections.list_unassigned_items()
	```

7. Assign an item to a collection

	```
	dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').items.get(item_id='678fa1490d9f072defec6c5e').assign_collection(collections=['my_collection'])
	```

8. Unassign an item from a collection

	```
	dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').items.get(item_id='678fa1490d9f072defec6c5e').unassign_collection(collections=['my_collection'])
	```

## ML Subsets

The ML Subsets View in Dataloop's Data Browser is a dedicated feature designed to enhance machine learning workflows by organizing and managing your dataset effectively. It allows you to classify and filter dataset items based on their ML Subset assignments, such as train, validation, and test, which are commonly used in the ML lifecycle for model development and evaluation.

To learn more about setting up ML Subsets, please visit our [Dataloop documentation](https://docs.dataloop.ai/docs/data-browser#ml-subsets)

### Manage ML Subsets in a Dataset

This SDK code demonstrates how to filter dataset items, split them into ML subsets, assign specific items to a subset, remove an item from a subset, and retrieve items missing an ML subset in Dataloop.

**1. Filtering Items of Type ‘File’ and Splitting into ML Subsets**

```
filters = dl.Filters(field='type', values='file')
dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').split_ml_subsets(
    items_query=filters,
    percentages={'train': 60, 'validation': 20, 'test': 20}
)

```

* Creates a filter (filters) to select only items of type ‘file’ in the dataset.
* Uses split_ml_subsets() to distribute these items into Train (60%), Validation (20%), and Test (20%) subsets.
* Ensures balanced dataset partitioning for ML training.

**2. Assigning a Specific Item to the ‘Train’ Subset**

```
filters = dl.Filters()
filters.add(field='id', values=['678fa1490d9f072defec6c5e'], operator=dl.FiltersOperations.IN)
dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').assign_subset_to_items(subset='train', items_query=filters)
```

* Creates an empty filter (filters) and adds a condition to select an item by its ID ('678fa1490d9f072defec6c5e').
* Uses assign_subset_to_items() to assign the selected item to the ‘train’ subset.

3. Removing an Item from Its ML Subset

```
filters = dl.Filters()
filters.add(field='id', values=['678fa1490d9f072defec6c5e'], operator=dl.FiltersOperations.IN)
dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').remove_subset_from_items(items_query=filters)
```

* Filters an item by its ID ('678fa1490d9f072defec6c5e').
* Uses remove_subset_from_items() to remove the item from any assigned ML subset.
* The item will no longer belong to Train, Validation, or Test subsets.

4.  Retrieving Items Without an Assigned ML Subset

```
dl.datasets.get(dataset_id='6785013bd25c9851e76313fd').get_items_missing_ml_subset()
```

* Fetches all dataset items that are not assigned to any ML subset.
* Useful for validating dataset completeness before training an ML model.
