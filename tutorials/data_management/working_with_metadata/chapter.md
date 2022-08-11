# Working with Metadata  

```python
import dtlpy as dl
# Get project and dataset
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
```
## User Metadata  
As a powerful tool to manage data based on your categories and information, you can add any keys and values to both the item’s and annotations’ user-metadata sections using the Dataloop SDK. Then, you can use your user-metadata for data filtering, sorting, etc.  
  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
When adding  metadata to the same item, the new metadata overwrites existing metadata. To avoid overwriting existing metadata, use the <a href="https://dataloop.ai/docs/sdk-add-item-metadata#list" target="_blank">"list"</a> data type and add to the list the new metadata.</div>  
  
### Metadata Data Types  
Metadata is a dictionary attribute used with items, annotations, and other entities of the Dataloop system (task, recipe, and more). As such, it can be used with string, number, boolean, list or null types.  
### String  

```python
item.metadata['user']['MyKey'] = 'MyValue'
annotation.metadata['user']['MyKey'] = 'MyValue'
```
### Number  

```python
item.metadata['user']['MyKey'] = 3
annotation.metadata['user']['MyKey'] = 3
```
### Boolean  

```python
item.metadata['user']['MyKey'] = True
annotation.metadata['user']['MyKey'] = True
```
### Null – add metadata with no information  

```python
item.metadata['user']['MyKey'] = None
annotation.metadata['user']['MyKey'] = None
```
### List  

```python
# add metadata of a list (can contain elements of different types).
item.metadata['user']['MyKey'] = ["A", 2, False]
annotation.metadata['user']['MyKey'] = ["A", 2, False]
```
### Add new metadata to a list without losing existing data  

```python
item.metadata['user']['MyKey'].append(3)
item = item.update()
annotation.metadata['user']['MyKey'].append(3)
annotation = annotation.update()
```
### Add metadata to an item's user metadata  

```python
# upload and claim item
item = dataset.items.upload(local_path=r'C:/home/project/images/item.mimetype')
# or get item
item = dataset.items.get(item_id='write-your-id-number')
# modify metadata
item.metadata['user'] = dict()
item.metadata['user']['MyKey'] = 'MyValue'
# update and reclaim item
item = item.update()
```
  
### Modify an existing user metadata field  

```python
# upload and claim item
item = dataset.items.upload(local_path=r'C:/home/project/images/item.mimetype')
# or get item
item = dataset.items.get(item_id='write-your-id-number')
# modify metadata
if 'user' not in item.metadata:
    item.metadata['user'] = dict()
item.metadata['user']['MyKey'] = 'MyValue'
# update and reclaim item
item = item.update()
```
### Add metadata to annotations' user metadata  

```python
# Get annotation
annotation = dl.annotations.get(annotation_id='my-annotation-id')
# modify metadata
annotation.metadata['user'] = dict()
item.metadata['user']['red'] = True
# update and reclaim annotation
annotation = annotation.update()
```
### Filter items by user metadata  
#### 1. Get your dataset  

```python
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
```
#### 2. Add metadata to an item  
You can also <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/item_level/chapter.md" target="_blank">add metadata to filtered items</a>  

```python
# upload and claim item
item = dataset.items.upload(local_path=r'C:/home/project/images/item.mimetype')
# or get item
item = dataset.items.get(item_id='write-your-id-number')
# modify metadata
item.metadata['user'] = dict()
item.metadata['user']['MyKey'] = 'MyValue'
# update and reclaim item
item = item.update()
```
#### 3. Create a filter  

```python
filters = dl.Filters()
# set resource - optional - default is item
filters.resource = dl.FiltersResource.ITEM
```
#### 4. Filter by your written key  

```python
filters.add(field='metadata.user.Key', values='Value')
```
#### 5. Get filtered items  

```python
pages = dataset.items.list(filters=filters)
# Go over all item and print the properties
for page in pages:
    for item in page:
        item.print()
```
