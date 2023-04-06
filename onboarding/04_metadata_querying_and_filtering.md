# Chapter 4 - Metadata, querying and filtering

### Querying and Filtering a Dataset

Dataloop's Python SDK allows you to filter Items based on their metadata which is extremely helpful when analyzing your Dataset. You can filter Items by defining the parameters of the Filter in Filter Queries. For example, you can create a Filter Query that filters Item data based on a specific field name or an Item's annotation label.

A Filter Query can have multiple parameters. For example, you can include a parameter that filters for all Items that include Point Marker Annotation samples labeled as 'Ear', or any other criteria available as part of the metadata for the collection of data samples in the Dataset.

#### Creating Filters

_**Reminder**_: To use any Dataloop Python SDK code, you need to `import dtlpy` and be logged in to Dataloop. 

The first steps in working with Filters is to create a Filter variable:

```python
my_filter = dl.Filters()
```

You can now add Filter Parameters to the Filter Variable you just created. For example, you can segregate all of the data samples that have point marker annotations:

```python
my_filter.add_join(field='type', values='point')
```

You now created a Filter and defined the filtering parameters to look for any samples that have Point Marker Annotations. You can now use this Filter Variable to look for any Point Marker samples in the Dataset we defined earlier in the Point Marker Example:

```python
pages = dataset.items.list(filters=my_filter)
for item in pages.all():
    item.print()
```

After executing these lines of code, the Filter we created will be applied to the entire Dataset. If you have multiple samples that have Point Markers associated with them, each of them will be displayed along with details for each sample, as shown below:

```python
Iterate Entity: 100%|████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.66it/s]
+----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------+
|    | annotated   | filename   | name      | type   | id                       | hidden   | dir   |   annotationsCount | dataset                                                           | createdAt                | datasetId                | creator             |
|----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------|
|  0 | True        | /test1.jpg | test1.jpg | file   | 63cebe0f6f60196b004423d9 | False    | /     |                  3 | https://gate.dataloop.ai/api/v1/datasets/63cebc185bc9dbe3ed851dbe | 2023-01-23T17:04:15.000Z | 63cebc185bc9dbe3ed851dbe | emailaccount@gmail.com |
+----+-------------+------------+-----------+--------+--------------------------+----------+-------+--------------------+-------------------------------------------------------------------+--------------------------+--------------------------+---------------------+
```

Here's an example of how to Filter on Tasks (Tasks are covered in a later chapter):

```
import dtlpy as dl

project = dl.projects.get(project_name='<replace with your project name>')

dataset = project.datasets.get(dataset_name='<replace with your dataset name')

filteredtasks = dataset.tasks.get_items(task_name='<replace with your task name>')
filteredtasks.print()
```

After you learn about Tasks, come back here and give this Filter for Tasks a try.

#### Using Filters to replace data

Existing Item data can be replaced using Filters. You can, for example, create and apply a Filter Query that returns a subset of Item data that includes a specific Classification, such as 'Person', and replace it with another value, such as 'Adult', across the entire subset.

The first step is to create a new Filter Query with a Filter Parameter that looks for all Items with the Label 'Person', which we previously created and assigned to a sample.

We can use the replacement Filter to replace information about samples from our Dataset, but we must first create it and assign some Filter Parameters to it, similar to the example above:

```python
person_filter = dl.Filters(resource=dl.FILTERS_RESOURCE_ITEM)
person_filter.add_join(field='label', values='Person')
```

We can now create a new Label called 'Adult' and add it to the Filter we just created, which will be used to replace all of the 'Person' samples in the Dataset:

```python
dataset.add_label(label_name='Adult')
pages = dataset.items.list(filters=person_filter)
```

Now you can delete the existing Label (Person) and replace it with the new Label we just created (Adult), using the following code:

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

After this code executes, all samples that are labeled 'Person' will have that Label removed and replaced with 'Adult'.

### Metadata

Metadata is a dictionary attribute that is used with Items, Annotations, and other Dataloop system entities such as [Recipes](https://dataloop.ai/blog/data-recipes/). Using the Python SDK, you can add any metadata values to any data sample. This user created metadata can be used for data filtering, sorting, and other purposes.

You will first learn how to add a new metadata field to the `test1.jpg` Dataset sample file we added earlier. This metadata item is called `datetime`, and will assign the current date and time to the sample you select.

To do this, we must first import the `datetime` module, which shouldn't require any installation as it is already part of Python's standard library:

```python
import datetime
```

Now you need to find out the `item_id` of the sample to which you want to add metadata. You can use the following line of code to print all of the data samples inside of your Dataset:

```python
dataset.items.get_all_items()
```

You should get something like this, in which you can find the `id` of the sample you want to use. If you didn't add any other samples other than the one we used in the tutorial, you will have only a single sample, called `test1.jpg`:

```python
Iterate Entity: 100%|████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.15it/s]
[Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/63cebc185bc9dbe3ed851dbe', created_at='2023-01-23T17:04:15.000Z', dataset_id='63cebc185bc9dbe3ed851dbe', filename='/test1.jpg', name='test1.jpg', type='file', id='63cebe0f6f60196b004423d9', spec=None, creator='myfuncont@gmail.com', _description=None, annotations_count=3)]
```

Next, `get` the `item_id` for `test1.jpg` in the data sample and assign it to a variable `item_1`:

```python
item_1 = dataset.items.get(item_id='632dadf7b28a0c0da317dfc8')
```

The current date and time can now be assigned to a new user defined field in the Item’s metadata named `dateTime` using the variable `item_1` you just created. Run the following code:

```python
now = datetime.datetime.now().isoformat()
# modify metadata for the item
item_1.metadata['user'] = dict()
# add it to the item's metadata
item_1.metadata['user']['dateTime'] = now
# update the item
item_1 = item_1.update()
```

The date and time should now be assigned to a new metadata field for that variable, and the sample from your Dataset should be updated.

Now, you will learn to use the filters from the previous chapter to create a metadata field for a whole subset of Items. Since you most likely have only one Item labeled "Adult" after the Label change we did earlier, this is the Filter criteria we will use:

```python
filters = dl.Filters()
filters.add_join(field='label', values='Adult')
now = datetime.datetime.now().isoformat()
dataset.items.update(filters=filters, update_values={'user': {'dateTime': now}})
```

If all works well, you should have updated all of the Items labeled 'Adult' with the current date and time and filtered them using the date and time as a Filter Parameter. You should also get a list of details for the Dataset and the Items modified after running the command above. You can the save the `dateTime` code you used and apply it to various operations you may need to do in the future, such as querying and filtering, or to track changes done to the Dataset.

If you want to see more examples of how you can work with Metadata, look at our [Metadata Python SDK Documentation](https://sdk-docs.dataloop.ai/en/latest/tutorials/data_management/working_with_metadata/chapter.html).

Now you know how to use Metadata, Queries and Filters. In the next chapter, you will learn about how to create Tasks.
