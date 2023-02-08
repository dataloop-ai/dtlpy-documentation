## Querying and Filtering

The Dataloop's Python SDK allows you to filter item data, which is extremely helpful when analysing your dataset. You can filter items by defining the parameters of the filter in Filter Queries. For example, you can create a Filter Query that filters item data based on a specific field name or an item's annotation label.

A Filter Query can have multiple parameters. For example, you can include a parameter that filters for all items that include Point Marker Annotation samples labeled as 'Ear', or any other criteria you want.

_**Reminder**_: To use any of the code, you need to be logged in to Dataloop and to ```import dtlpy```!

### Creating Filters
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

Now you know how to use queries and filters. Next, you will learn about metadata and how to create tasks, in the next chapter.
