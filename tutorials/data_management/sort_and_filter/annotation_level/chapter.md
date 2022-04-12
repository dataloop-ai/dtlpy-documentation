To access the filters entity click <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.filters" target="_blank">here</a>.  
## The Dataloop Query Language - DQL  
Using The <a href="https://dataloop.ai/docs/api-dql" target="_blank">Dataloop Query Language</a>, you may navigate through massive amounts of data.  
  
You can *filter*, *sort*, and *update* your metadata with it.  
  
### Filters  
Using filters, you can filter items and get a generator of the filtered items. The filters entity is used to build such filters.  
  
#### Filters - Field & Value  
Filter your items or annotations using the parameters in the JSON code that represent its data within our system.  
Access your item/annotation JSON using <code>to_json()</code>.  
##### Field  
Field refers to the attributes you filter by.  
  
For example, "dir" would be used if you wish to filter items by their folder/directory.  
  
##### Value  
Value refers to the input by which you want to filter.  
For example, "/new_folder" can be the directory/folder name where the items you wish to filter are located.  
#### Sort - Field & Value  
##### Field  
Field refers to the field you sort your items/annotations list by.  
For example, if you sort by filename, you will get the item list sorted in alphabetical order by filename.  
See the full list of the available fields <a href="https://dataloop.ai/docs/api-dql" target="_blank">here</a>.  
##### Value  
Value refers to the list order direction. Either ascending or descending.  
  
### Filter Annotations  
Filter annotations by the annotations' JSON fields.  
In this example, you will get all of the note annotations in the dataset sorted by the label.  
  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
  
See all of the items iterator options on the <a href="https://dataloop.ai/docs/sdk-item-iterator" target="_blank">Iterator of Items</a> page.</div>  
  

```python
import dtlpy as dl
# Get project and dataset
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
# Create filters instance with annotation resource
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
# Filter example - only note annotations
filters.add(field='type', values='note')
# optional - return results sorted by descending label 
filters.sort_by(field='label', value=dl.FiltersOrderByDirection.DESCENDING)
pages = dataset.annotations.list(filters=filters)
# Count the annotations
print('Number of filtered annotations in dataset: {}'.format(pages.items_count))
# Iterate through the annotations - Go over all annotations and print the properties
for page in pages:
    for annotation in page:
        annotation.print()
```
  
### Filter Annotations by the Annotations' Item  
<code>add_join</code> - filter Annotations by the annotations' items' JSON fields. For example, filter only box annotations from image items.  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
See all of the items iterator options on the <a href="https://dataloop.ai/docs/sdk-item-iterator" target="_blank">Iterator of Items</a> page.</div>  
  

```python
# Create filters instance
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
# Filter all box annotations
filters.add(field='type', values='box')
# AND filter annotations by their items - only items that are of mimetype image
# Meaning you will get 'box' annotations of all image items
filters.add_join(field='metadata.system.mimetype', values="image*")
# optional - return results sorted by descending creation date
filters.sort_by(field='createdAt', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
# Get filtered annotations list in a page object
pages = dataset.annotations.list(filters=filters)
# Count the annotations
print('Number of filtered annotations in dataset: {}'.format(pages.items_count))
```
### Filters Method - "Or" and "And"  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Filters Operators</b><br>  
For more advanced filters operators visit the <a href="https://dataloop.ai/docs/sdk-advanced-filter#filter-operators" target="_blank">Advanced SDK Filters</a> page.</div>  
  
#### And  
If you wish to filter annotations with the "and" logical operator, you can do so by specifying which filters will be checked with "and".  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>  
AND is the default value and can be used without specifying the method.</b></div>  
In this example, you will get a list of annotations in the dataset of the type <b>box</b> and label <b>car</b>.  
  

```python
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
# set annotation resource
filters.add(field='type', values='box', method=dl.FiltersMethod.AND)
filters.add(field='label', values='car',
            method=dl.FiltersMethod.AND)  # optional - return results sorted by ascending creation date
filters.sort_by(field='createdAt')
# Get filtered annotations list
pages = dataset.annotations.list(filters=filters)
# Count the annotations
print('Number of filtered annotations in dataset: {}'.format(pages.items_count))
```
#### Or  
If you wish to filter annotations with the "or" logical operator, you can do so by specifying which filters will be checked with "or".  
In this example, you will get a list of the dataset's annotations that are either a 'box' or a 'point' type.  
  

```python
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
# filters with or
filters.add(field='type', values='/box', method=dl.FiltersMethod.OR)
filters.add(field='type', values='/point',
            method=dl.FiltersMethod.OR)  # optional - return results sorted by descending updated date
filters.sort_by(field='createdAt', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
# Get filtered annotations list
pages = dataset.annotations.list(filters=filters)
# Count the annotations
print('Number of filtered annotations in dataset: {}'.format(pages.items_count))
```
### Delete Filtered Items  
In this example, you will delete annotations that were created on 30/8/2020 at 8:17 AM.  
  

```python
filters = dl.Filters()
# set annotation resource
filters.resource = dl.FiltersResource.ANNOTATION
# Example - created on 30/8/2020 at 8:17 AM
filters.add(field='createdAt', values="2020-08-30T08:17:08.000Z")
dataset.annotations.delete(filters=filters)
```
### Annotation Filtering Fields  
#### More Filter Options  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;">  
Use a dot to access parameters within curly brackets.  
For example use field='metadata.system.status' to filter by the annotation's status.</div>  
  

```python
{
    "id": "5f576f660bb2fb455d79ffdf",
    "datasetId": "5e368bee106a76a61cf05282",
    "type": "segment",
    "label": "Planet",
    "attributes": [],
    "coordinates": [
        [
            {
                "x": 856.25,
                "y": 1031.2499999999995
            },
            {
                "x": 1081.25,
                "y": 1631.2499999999995
            },
            {
                "x": 485.41666666666663,
                "y": 1735.4166666666665
            },
            {
                "x": 497.91666666666663,
                "y": 1172.9166666666665
            }
        ]
    ],
    "metadata": {
        "system": {
            "status": null,
            "startTime": 0,
            "endTime": 1,
            "frame": 0,
            "endFrame": 1,
            "snapshots_": [
                {
                    "fixed": true,
                    "type": "transition",
                    "frame": 0,
                    "objectVisible": true,
                    "data": [
                        [
                            {
                                "x": 856.25,
                                "y": 1031.2499999999995
                            },
                            {
                                "x": 1081.25,
                                "y": 1631.2499999999995
                            },
                            {
                                "x": 485.41666666666663,
                                "y": 1735.4166666666665
                            },
                            {
                                "x": 497.91666666666663,
                                "y": 1172.9166666666665
                            }
                        ]
                    ],
                    "label": "Planet",
                    "attributes": []
                }
            ],
            "automated": false,
            "isOpen": false,
            "system": false
        },
        "user": {}
    },
    "creator": "user@dataloop.ai",
    "createdAt": "2020-09-08T11:47:50.576Z",
    "updatedBy": "user@dataloop.ai",
    "updatedAt": "2020-09-08T11:47:50.576Z",
    "itemId": "5f572f4423a69b8c83408f12",
    "url": "https://gate.dataloop.ai/api/v1/annotations/5f576f660bb2fb455d79ffdf",
    "item": "https://gate.dataloop.ai/api/v1/items/5f572f4423a69b8c83408f12",
    "dataset": "https://gate.dataloop.ai/api/v1/datasets/5e368bee106a76a61cf05282",
    "hash": "11fdc816804faf0f7266b40d1cb67aff38e5c10d"
}
```
### Full Examples  
#### How to filter annotations by their label?  
  

```python
filters = dl.Filters()
# set resource
filters.resource = dl.FiltersResource.ANNOTATION
filters.add(field='label', values='your_label_value')
pages = dataset.annotations.list(filters=filters)
# Count the annotations
print('Number of filtered annotations in dataset: {}'.format(pages.items_count))
```
### Advanced Filtering Operators  
Explore advanced filtering options on <a href="https://dataloop.ai/docs/sdk-advanced-filter" target="_blank">this page</a>.  
  
