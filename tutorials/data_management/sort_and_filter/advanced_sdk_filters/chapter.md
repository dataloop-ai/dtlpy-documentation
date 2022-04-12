To access the filters entity click <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.filters" target="_blank">here</a>.  
### Filter Operators  
To understand more about filter operators please click <a href="https://dataloop.ai/docs/dql-operators" target="_blank">here</a>.  
  
When adding a filter, several operators are available for use:  
  
#### Equal  
eq -> equal  
(or dl.FiltersOperation.EQUAL)  
  
For example, filter items from a specific folder directory.  

```python
import dtlpy as dl
# Get project and dataset
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
# Create filters instance
filters = dl.Filters()
# Filter only items from a specific folder directory
filters.add(field='dir', values='/DatasetFolderName', operator=dl.FILTERS_OPERATIONS_EQUAL)
# optional - return results sorted by ascending file name 
filters.sort_by(field='filename')
# Get filtered items list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
#### Not Equal  
ne -> not equal  
(or dl.FiltersOperation.NOT_EQUAL)  
  
In this example, you will get all items that do not have ONLY a 'cat' label.  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
This Operator is a better fit for filters of a single value because, for example, this filter will return items that have both 'cat' and 'dog' labels.  
View an example of a solution for the issue in the <a href="https://docs.dataloop.ai/docs/sdk-advanced-filter#full-examples" target="_blank">full example section</a> at the bottom of the page.</div>  

```python
filters = dl.Filters()
# Filter ONLY a cat label
filters.add_join(field='label', values='cat', operator=dl.FILTERS_OPERATIONS_NOT_EQUAL)
# optional - return results sorted by ascending file name 
filters.sort_by(field='filename')
# Get filtered items list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in the dataset: {}'.format(pages.items_count))
```
#### Greater Than  
gt -> greater than  
(or dl.FiltersOperation.GREATER_THAN)  
  
You will get items with a greater height (in pixels) than the given value in this example.  

```python
filters = dl.Filters()
# Filter images with a bigger height size
filters.add(field='metadata.system.height', values=height_number_in_pixels,
            operator=dl.FILTERS_OPERATIONS_GREATER_THAN)
# optional - return results sorted by ascending file name 
filters.sort_by(field='filename')
# Get filtered items list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
#### Less Than  
lt -> less than  
(or dl.FiltersOperation.LESS_THAN)  
  
You will get items with a width (in pixels) less than the given value in this example.  

```python
filters = dl.Filters()
# Filter images with a bigger height size
filters.add(field='metadata.system.width', values=width_number_in_pixels, operator=dl.FILTERS_OPERATIONS_LESS_THAN)
# optional - return results sorted by ascending file name 
filters.sort_by(field='filename')
# Get filtered items list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
#### In a List  
in -> is in a list (when using this expression, values should be a list).  
(or dl.FiltersOperation.IN)  
In this example, you will get items with dog OR cat labels.  

```python
filters = dl.Filters()
# Filter items with dog OR cat labels
filters.add_join(field='label', values=['dog', 'cat'], operator=dl.FILTERS_OPERATIONS_IN)
# optional - return results sorted by ascending file name 
filters.sort_by(field='filename')
# Get filtered items list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
#### Exist  
The filter param FILTERS_OPERATIONS_EXISTS checks if an attribute exists. The following example checks if there is an item with user metadata:  

```python
filters = dl.Filters()
filters.add(field='metadata.user', values=True, operator=dl.FILTERS_OPERATIONS_EXISTS)
dataset.items.list(filters=filters)
```
### SDK defaults  
Filters ignore SDK defaults like hidden items and directories or note annotations as issues.  
If you wish to change this behavior, you may do the following:  

```python
filters = dl.Filters(use_defaults=False)
```
#### Hidden Items and Directories  
If you wish to only show hidden items & directories in your filters use this code:  

```python
filters = dl.Filters()
filters.add(field='type', values='dir')
# or
filters.pop(field='type')
```
### Delete a Filter  

```python
filters = dl.Filters()
# For example, if you added the following filter:
filters.add(field='to-delete-field', values='value')
# Use this command to delete the filter
filters.pop(field='to-delete-field')
# or for items by their annotations
filters.pop_join(field='to-delete-annotation-field')
```
### Full Examples  
#### How to filter items that were created between specific dates?  
In this example, you will get all of the items that were created in 2018.  

```python
import datetime, time
filters = dl.Filters()
# -- time filters -- must be in ISO format and in UTC (offset from local time). converting using datetime package as follows:
earlier_timestamp = datetime.datetime(year=2018, month=1, day=1, hour=0, minute=0, second=0,
                                      tzinfo=datetime.timezone(
                                          datetime.timedelta(seconds=-time.timezone))).isoformat()
later_timestamp = datetime.datetime(year=2019, month=1, day=1, hour=0, minute=0, second=0,
                                    tzinfo=datetime.timezone(
                                        datetime.timedelta(seconds=-time.timezone))).isoformat()
filters.add(field='createdAt', values=earlier_timestamp, operator=dl.FiltersOperations.GREATER_THAN)
filters.add(field='createdAt', values=later_timestamp, operator=dl.FiltersOperations.LESS_THAN)
# change method to OR
filters.method = dl.FiltersMethod.OR
# Get filtered items list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
#### How to filter items that don't have a specific label?  
In this example, you will get all items that do not have a 'cat' label AT ALL.  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
This filter will NOT return items that have both 'cat' and 'dog' labels.</div>  

```python
# Get all items
all_items = set([item.id for item in dataset.items.list().all()])
# Get all items WITH the label cat
filters = dl.Filters()
filters.add_join(field='label', values='cat')
cat_items = set([item.id for item in dataset.items.list(filters=filters).all()])
# Get the difference between the sets. This will give you a list of the items with no cat
no_cat_items = all_items.difference(cat_items)
print('Number of filtered items in dataset: {}'.format(len(no_cat_items)))
# Iterate through the ID's  - Go over all ID's and print the matching item
for item_id in no_cat_items:
    print(dataset.items.get(item_id=item_id))
```
