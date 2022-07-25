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
item = dataset.items.get(item_id='my-item-id')
item.update_status(status=dl.ItemStatus.COMPLETED)
item.update_status(status=dl.ItemStatus.APPROVED)
item.update_status(status=dl.ItemStatus.DISCARDED)
```
### 2. Set status on multiple items  

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
### 3. Clear status from an item (no-status)  
Clearing a status from an item will make it available again for work in the respective task, and the worker (annotator)  
will see the item in the assignment (either QA or annotations).  

```python
# Clear status for completed/approved/discarded
item.update_status(dl.ITEM_STATUS_COMPLETED, clear=True)
```
### 4. Manage task statuses  
The statuses in a task can be managed, add new custom statuses and remove existing ones.  
  
  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
Changing the statuses in the task doesn't change the status on any items that already received a status.  

```python
...
```
