

## Querying and Filtering

The Dataloop's Python SDK allows you to filter item data, which is extremely helpful when analysing your dataset. You can filter items by defining the parameters of the filter in Filter Queries. For example, you can create a Filter Query that filters item data based on a specific field name or an item's annotation label.

A Filter Query can have multiple parameters. For example, you can include a parameter that filters for all items that include Point Marker Annotation samples labeled as 'Ear', or any other criteria you want.

### Creating Filters
_**Reminder**_: To use any dataloop code, you need to be logged in to Dataloop and to ```import dtlpy```!
The first steps in working with filters is to create a filter variable:
```python
my_filter = dl.Filters()
```
You can now add filter parameters to the filter variable you just created. For example, you can extract all of the data samples that have point marker annotations:
```python
my_filter.add_join(field='type', values='point')
```
You now created a filter and defined the filtering parameters too look for any samples that have any Point Marker Annotations in it. You can now use this filter variable to actually look for any Point Makered samples in the dataset we defined earlier:
```python
pages = dataset.items.list(filters=my_filter)
for item in pages.all():
    item.print()
```
After executing these lines of code, the filter we created will be applied to the whole dataset. If you have multiple samples that have point markers in it, each of them will be displayed along with details for each sample extracted, as shown below:

```python
Iterate Entity: 100%|████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.66it/s]
+----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------+
|    | annotated   | filename   | name      | type   | id                       | hidden   | dir   |   annotationsCount | dataset                                                           | createdAt                | datasetId                | creator             |
|----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------|
|  0 | True        | /test1.jpg | test1.jpg | file   | 63cebe0f6f60196b004423d9 | False    | /     |                  3 | https://gate.dataloop.ai/api/v1/datasets/63cebc185bc9dbe3ed851dbe | 2023-01-23T17:04:15.000Z | 63cebc185bc9dbe3ed851dbe | emailaccount@gmail.com |
+----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------+
```

### Using filters to replace data
Existing item data can be replaced using filters. You can, for example, create and apply a Filter Query that returns a subset of item data that includes a specific Classification, such as 'Person,' and replace it with another value, such as 'Adult,' across the entire subset.

The first step is to create a new Filter Query with a Filter Parameter that looks for all items with the label 'Person,' which we previously created and assigned to a sample.

We can use the replacement filter to replace information about samples from our dataset, but we must first create it and assign some filtering parameters to it, similarly to the example above:
```python
person_filter = dl.Filters(resource=dl.FILTERS_RESOURCE_ITEM)
person_filter.add_join(field='label', values='Person')
```
We can now create a new label called 'Adult' and add it to the filter we just created, which will be used to replace all of the 'Person' samples in the dataset:
```python
dataset.add_label(label_name='Adult')
pages = dataset.items.list(filters=person_filter)
```
Now you can delete the existing label (Person) and replace it with the new label we just created (Adult), using the following code:
```python
import dtlpy as dl

person_ann_filter = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
person_ann_filter.add(field='label', values='Person')

for item in pages.all():
    item.annotations.delete(filters=person_ann_filter)
    annotations = item.annotations.builder()
    annotations.add(annotation_definition=dl.Classification(label='Adult'))
    item.annotations.upload(annotations)
```
After this code exectues, all samples that are labeled 'Person' will have that label removed and replaced with 'Adult'.

## Metadata

Metadata is a dictionary attribute that is used with items, annotations, and other Dataloop system entities such as [Recipes](https://dataloop.ai/blog/data-recipes/). Using the Python SDK, you can add any metadata values to any data sample. This user metadata can be used for data filtering, sorting, and other purposes.

You will first learn how to add a new metadata field to the "test1" dataset sample we added earlier. This metadata item is called "datetime", and will assign the current date and time to the sample you select.

To do that, we must first import the "datetime" module, which shouldn't require any installation, as it is already part of Python's standard library:
```python
import datetime
```
Now you need to find out the "item_id" of the sample that you want to add metadata to. You can use the following line of code to print all of the data samples inside of your dataset:
```python
dataset.items.get_all_items()
```
You should get something like this, in which you can find the 'id' of the sample you want to use. If you didn't add any other sample than the one we used in the tutorial, you will have only a single sample, called "test1":
```python
Iterate Entity: 100%|████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.15it/s]
[Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/63cebc185bc9dbe3ed851dbe', created_at='2023-01-23T17:04:15.000Z', dataset_id='63cebc185bc9dbe3ed851dbe', filename='/test1.jpg', name='test1.jpg', type='file', id='63cebe0f6f60196b004423d9', spec=None, creator='myfuncont@gmail.com', _description=None, annotations_count=3)]
```
Next, you need to create a new instance of "test1" datasample:

```python
item_1 = dataset.items.get(item_id='632dadf7b28a0c0da317dfc8')
```
An instance of item test1 named item_1 should be created. The current date can now be assigned to a new field in the item’s metadata named Date&Time and the item can be updated.

You can now asign the current date to a new metadata field for that variable:
```python
now = datetime.datetime.now().isoformat()
# modify metadata for the item
item_1.metadata['user'] = dict()
# add it to the item's metadata
item_1.metadata['user']['dateTime'] = now
# update the item
item_1 = item_1.update()
```
The date should now be assigned to a new metadata field for that variable, and the sample from your databes should be updated.

Now, you will learn to use the filters from the previous chapter, to create a metadata field for a whole subset of items. Since you most likely have only one item, labeled "Adult" after the label change we did earlier, that's the criteria we will use:
```python
filters = dl.Filters()
filters.add_join(field='label', values='Adult')
now = datetime.datetime.now().isoformat()
dataset.items.update(filters=filters, update_values={'user': {'dateTime': now}})
```
If all works well, you should have updated all of the items labeled "Adult" with the current date-time as a parameter. You should also get a long list of details of the dataset and the items modified, after running the command above. You can the save the datetime you just added and use it for various operations you may need to do in the future, such as querying and filtering, or to track changes done to the dataset.

Now you know how to use metadata, queries and filters. In the next chapter, you will learn about how to create tasks.
