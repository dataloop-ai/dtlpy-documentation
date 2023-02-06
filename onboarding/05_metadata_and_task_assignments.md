### Metadata
Metadata is a dictionary attribute that is used with items, annotations, and other Dataloop system entities such as [Recipes](https://dataloop.ai/blog/data-recipes/). Using the SDK, you can add any metadata values to any data sample. This user metadata can be used for data filtering, sorting, and other purposes.

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
If all works well, you should have updated all of the items labeled "Adult" with the current date-time as a parameter. You should also get a long list of details of the dataset and the items modified, after running the command above. You can the save the datetime you just added and use it for various operations you may need to do in the future, or to track changes done to the dataset.

### Tasks
In the Dataloop platform, tasks are created to initiate annotation or QA (Quality Assurance) work. It requires defining the data items to be included, the task assignees, and various options such as work-load, custom-statuse, and more. The tasks can be of 2 types, which was  mentioned above - annotation tasks or quality assurance tasks. You will now find out how to create and assign people to both types of tasks.

To create a task that uses a filter, first name it, then add a due date for when it should be completed, and then add one or more annotators to handle that task and a filter. To create an annotation task, simply run the following code with the desired parameters:
```python
task = dataset.tasks.create(
    task_name='test_task1',
    due_date=datetime.datetime(day=11, month=3, year=2025).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    # The items will be divided equally between assignees
    filters=filters  # filter by folder directory or use other filters
)
```
To create a quality assurance tasks, the process is quite similar. See the code below:
```python
qa_task = dataset.tasks.create_qa_task(task=task,
                                       due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
                                       assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
                                       filters=filters  # this filter is for "completed items"
                                       )
```
If you simply want to create a task out of an entier dataset, you can simply remove the "filters" parameter, and a task will be created out of the entire dataset you select:
```python
task = dataset.tasks.create(
    task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>']
    # The items will be divided equally between assignments
)
```

Now you know the basics of metadata and tasks. In the next chapter, you will learn  how you can use data versioning tools to manage your data.
