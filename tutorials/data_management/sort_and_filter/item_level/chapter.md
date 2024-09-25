To access the filters entity click <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.filters" target="_blank">here</a>.  
## The Dataloop Query Language - DQL  
Using The <a href="https://docs.dataloop.ai/docs/api-dql" target="_blank">Dataloop Query Language</a>, you may navigate through massive amounts of data.  
  
You can *filter*, *sort*, and *update* your metadata with it.  
  
### Filters  
Using filters, you can filter items and get a generator of the filtered items. The filters entity is used to build such filters.  
  
#### Filters - Field & Value  
Filter your items or annotations using the parameters in the JSON code that represent its data within our system.  
Access your item/annotation JSON using `to_json()`.  
##### Field  
Field refers to the attributes you filter by.  
  
For example, "dir" would be used if you wish to filter items by their folder/directory.  
  
##### Value  
Value refers to the input by which you want to filter.  
For example, `/new_folder` can be the directory/folder name where the items you wish to filter are located.  
#### Sort - Field & Value  
##### Field  
Field refers to the field you sort your items/annotations list by.  
For example, if you sort by filename, you will get the item list sorted in alphabetical order by filename.  
See the full list of the available fields <a href="https://docs.dataloop.ai/docs/api-dql" target="_blank">here</a>.  
##### Value  
Value refers to the list order direction. Either ascending or descending.  
  
### Filter Items  
Filter items by the item's JSON fields.  
In this example, you will get all annotated items in a dataset sorted by the filename.  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
See all of the items iterator options on the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/pagination/chapter.md#iterator-of-items" target="_blank">Iterator of Items</a> page.</div>  
  

```python
import dtlpy as dl
# Get project and dataset
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
# Create filters instance
filters = dl.Filters()
# Filter only annotated items
filters.add(field='annotated', values=True)
# optional - return results sorted by ascending file name 
filters.sort_by(field="filename")
# Get filtered items list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
### Filter Items by the Items' Annotations  
<code>add_join</code> - filter items by the items' annotations JSON fields. For example, filter only items with 'box' annotations.  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
See all of the items iterator options on the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/pagination/chapter.md#iterator-of-items" target="_blank">Iterator of Items</a> page.</div>  
  

```python
filters = dl.Filters()
# Filter all approved items
filters.add(field='metadata.system.annotationStatus', values="approved")
# AND filter items by their annotation - only items with 'box' annotations
# Meaning you will get approved items with 'box' annotations
filters.add_join(field='type', values='box')
# optional - return results sorted by descending creation date 
filters.sort_by(field='createdAt', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
# Get filtered items list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
### Filters Method - "Or" and "And"  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Filters Operators</b><br>  
For more advanced filters operators visit the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.md" target="_blank">Advanced SDK Filters</a> page.</div>  
  
#### And  
If you wish to filter annotations with the "and" logical operator, you can do so by specifying which filters will be checked with "and".  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>  
AND is the default value and can be used without specifying the method.</b></div>  
In this example, you will get a list of annotated items with <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/working_with_metadata/chapter.md" target="_blank">user metadata</a> of the field "is_automated" and value True.  
  

```python
filters = dl.Filters()  # filters with and
filters.add(field='annotated', values=True, method=dl.FiltersMethod.AND)
filters.add(field='metadata.user.is_automated', values=True,
            method=dl.FiltersMethod.AND)  # optional - return results sorted by ascending file name
filters.sort_by(field='name')
# Get filtered items list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
#### Or  
If you wish to filter annotations with the "or" logical operator, you can do so by specifying which filters will be checked with "or".  
In this example, you will get a list of items that are either on "folder1" or "folder2" directories.  
  

```python
filters = dl.Filters()
# filters with or
filters.add(field='dir', values='/folderName1', method=dl.FiltersMethod.OR)
filters.add(field='dir', values='/folderName2',
            method=dl.FiltersMethod.OR)  # optional - return results sorted by descending directory name
filters.sort_by(field='dir', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
# Get filtered items list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
### Update User Metadata of Filtered Items  
<b>Update Filtered Items</b> - The `update_value` must be a dictionary.  
The dictionary will only update user metadata.  
Understand more about user metadata [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/working_with_metadata/chapter.md).  
In this example, you will update/add user metadata (with the field "BlackDogs" and value True), to items in a specific folder 'dogs' with an attribute 'black'.  
  

```python
filters = dl.Filters()
# For example -  filter only items in a specific folder - like 'dogs'
filters.add(field='dir', values='/dogs')
# For example - filter items by their annotation - only items with 'black' attribute
filters.add_join(field='attributes', values='black')
# to add filed BlackDogs to all filtered items and give value True
# this field will be added to user metadata
# create update order
update_values = {'BlackDogs': True}
# update
pages = dataset.items.update(filters=filters, update_values=update_values)
```
### Delete Filtered Items  
In this example, you will delete items that were created on 30/8/2020 at 8:17 AM.  
  

```python
filters = dl.Filters()
# For example -  filter only annotated items
filters.add(field='createdAt', values="2020-08-30T08:17:08.000Z")
dataset.items.delete(filters=filters)
```
### Item Filtering Fields  
#### More Filter Options  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;">  
Use a dot to access parameters within curly brackets.  
For example use field='metadata.system.originalname' to filter by the item's original name.</div>  
  

```python
{
    "id": "5f4b60848ced1d50c3df114a",
    "datasetId": "5f4b603d9825b9f191bbd3b3",
    "createdAt": "2020-08-30T08:17:08.000Z",
    "dir": "/new_folder",
    "filename": "/new_folder/optional.jpg",
    "type": "file",
    "hidden": false,
    "metadata": {
        "system": {
            "originalname": "file",
            "size": 3290035,
            "encoding": "7bit",
            "mimetype": "image/jpeg",
            "annotationStatus": [
                "completed"
            ],
            "refs": [
                {
                    "type": "task",
                    "id": "5f4b61f8f81ab6238c331bd2"
                },
                {
                    "type": "assignment",
                    "id": "5f4b61f8f81ab60508331bd3"
                }
            ],
            "executionLogs": {
                "image-metadata-extractor": {
                    "default_module": {
                        "run": {
                            "5f4b60841b892d82eaa2d95b": {
                                "progress": 100,
                                "status": "success"
                            }
                        }
                    }
                }
            },
            "exif": {},
            "height": 2734,
            "width": 4096,
            "statusLog": [
                {
                    "status": "completed",
                    "timestamp": "2020-08-30T14:54:17.014Z",
                    "creator": "user@dataloop.ai",
                    "action": "created"
                }
            ],
            "isBinary": true
        }
    },
    "name": "optional.jpg",
    "url": "https://gate.dataloop.ai/api/v1/items/5f4b60848ced1d50c3df114a",
    "dataset": "https://gate.dataloop.ai/api/v1/datasets/5f4b603d9825b9f191bbd3b3",
    "annotationsCount": 18,
    "annotated": "discarded",
    "stream": "https://gate.dataloop.ai/api/v1/items/5f4b60848ced1d50c3df114a/stream",
    "thumbnail": "https://gate.dataloop.ai/api/v1/items/5f4b60848ced1d50c3df114a/thumbnail",
    "annotations": "https://gate.dataloop.ai/api/v1/items/5f4b60848ced1d50c3df114a/annotations"
}
```
### Full Examples  
#### How to filter items by their annotations label?  
  

```python
filters = dl.Filters()
filters.add_join(field='label', values='your_label_value')
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of filtered items in dataset: {}'.format(pages.items_count))
```
#### How to filter items by completed and approved status?  

```python
filters = dl.Filters()
filters.add(field='metadata.system.annotationStatus', values=["completed", "approved"])
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
#### How to filter items by completed status (with items who are approved as well)?  

```python
filters = dl.Filters()
# set resource
filters.add(field='metadata.system.annotationStatus', values="completed")
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
#### How to filter items by only completed status?  

```python
filters = dl.Filters()
filters.add(field='metadata.system.annotationStatus', values=["completed"])
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
#### How to filter unassigned items?  

```python
filters = dl.Filters()
filters.add(field='metadata.system.refs', values=[])
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
#### How to filter items by a specific folder?  

```python
filters = dl.Filters()
filters.add(field='dir', values="/folderName")
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
#### Get all items named foo.bar  

```python
filters = dl.Filters()
filters.add(field='name', values='foo.bar.*')
# Get filtered item list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of filtered items in dataset: {}'.format(pages.items_count))
```
#### Sort files of size 0-5 MB by name, in ascending order  

```python
filters = dl.Filters()
filters.add(field='metadata.system.size', values='0', operator='gt')
filters.add(field='metadata.system.size', values='5242880', operator='lt')
filters.sort_by(field='filename', value=dl.FILTERS_ORDERBY_DIRECTION_ASCENDING)
# Get filtered item list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of filtered items in dataset: {}'.format(pages.items_count))
```
#### Sort with multiple fields: Sort Items by labels ascending and createdAt descending  

```python
filters = dl.Filters()
# set annotation resource
filters.resource = dl.FiltersResource.ANNOTATION
# return results sorted by descending label
filters.sort_by(field='label', value=dl.FILTERS_ORDERBY_DIRECTION_ASCENDING)
filters.sort_by(field='createdAt', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
# Get filtered item list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of filtered items in dataset: {}'.format(pages.items_count))
```
### Advanced Filtering Operators  
Explore advanced filtering options on <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.md/" target="_blank">this page</a>.  
  
### Response to DQL Query  
A typical response to a DQL query will look like the following:  

```python
{
    "totalItemsCount": number,
    "items": Array,
    "totalPagesCount": number,
    "hasNextPage": boolean,
}
# A possible result:
{
    "totalItemsCount": 2,
    "totalPagesCount": 1,
    "hasNextPage": false,
    "items": [
        {
            "id": "5d0783852dbc15306a59ef6c",
            "createdAt": "2019-06-18T23:29:15.775Z",
            "filename": "/5546670769_8df950c6b6.jpg",
            "type": "file"
                    // ...
        },
        {
            "id": "5d0783852dbc15306a59ef6d",
            "createdAt": "2019-06-19T23:29:15.775Z",
            "filename": "/5551018983_3ce908ac98.jpg",
            "type": "file"
                    // ...
        }
    ]
}
```
### Using Custom DQL Filter  
If you have a DQL JSON copied from the platform you can create an SDK Filter directly with it using the `custom_filter` attribute:  

```python
filters = dl.Filters(custom_filter={"$and": [{"hidden": False},
                                             {"type": "file"},
                                             {"annotated": True}]},
                     )
pages = dataset.items.list(filters=filters)
print('Number of filtered items in dataset: {}'.format(pages.items_count))
```
