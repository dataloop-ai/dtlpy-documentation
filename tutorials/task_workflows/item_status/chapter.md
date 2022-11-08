## Item Status  
To flag for finishing work on an item in a task, the worker assigns a status to the item.  
The Dataloop system has default statuses, as well as the option to add custom statuses  
Default statuses for annotation tasks: COMPLETE and DISCARD  
Default statuses for QA tasks: APPROVE and DISCARD  
  
### 1. Set status on an item in task  

```python
import dtlpy as dl
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
task = dataset.tasks.get(task_name='task_name')
assignment = dataset.assignments.get(assignment_name='assignment_name')
item = dataset.items.get(item_id='my-item-id')
item.update_status(status=dl.ItemStatus.COMPLETED, task_id=task.id)
item.update_status(status=dl.ItemStatus.APPROVED, assignment_id=assignment.id)
item.update_status(status=dl.ItemStatus.DISCARDED)  # this will work if the item is included in only one task
```
### 2. Set status on multiple items  
#### 1. using dataset and filter (this way recommended of the items is not in the same task and items that include in only one task)  

```python
filters = dl.Filters(field='annotated', values=True)
items = dataset.items.list(filters=filters)
dataset.items.update_status(status=dl.ItemStatus.APPROVED, items=items)
# With filters
filters = dl.Filters(field='annotated', values=True)
dataset.items.update_status(status=dl.ItemStatus.DISCARDED, filters=filters)
# With list of item ids
item_ids = ['id1', 'id2', 'id3']
dataset.items.update_status(status=dl.ItemStatus.COMPLETED, item_ids=item_ids)
```
#### 2. use task entity (this way recommended for items in the same task)  

```python
# With filter
filters = dl.Filters(field='annotated', values=True)
item_ids = [item.id for item in dataset.items.list(filters=filters).all()]
# With list of item ids
item_ids = ['id1', 'id2', 'id3']
task.set_status(status=dl.ItemStatus.APPROVED, operation='create', items=item_ids)
```
### 3. Clear status from an item (no-status)  
Clearing a status from an item will make it available again for work in the respective task, and the worker (annotator)  
will see the item in the assignment (either QA or annotations).  

```python
# Clear status for completed/approved/discarded
item.update_status(dl.ITEM_STATUS_DISCARDED, task_id=task.id, clear=True)
item.update_status(dl.ITEM_STATUS_APPROVED, assignment_id=assignment.id, clear=True)
item.update_status(dl.ITEM_STATUS_COMPLETED, clear=True)  # this will work if the item is included in only one task
```
### 4. Add task statuses  

```python
# Create annotation task with new statue
task = dl.tasks.create(
    task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    # The items will be divided equally between assignments
    filters=filters,  # filter by folder directory or use other filters,
    available_actions=[dl.ItemAction(action='action_name', display_name='display_name')]  # Task statuses
)
```
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
Changing the statuses in the task doesn't change the status on any items that already received a status.  
