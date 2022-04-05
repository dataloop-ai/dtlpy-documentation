## Task Assignment  
To reach the tasks and assignments repositories go to <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.tasks" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.assignments" target="_blank">assignments</a>.  
  
  
To reach the tasks and assignments entities go to <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.task" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.assignment" target="_blank">assignments</a>.  
### Item Review  
The Annotation Studio is built for realtime review, task assignment and feedback.  
  
Each item can be classified in 3 ways:  
* **Discarded**: Items that are not relevant for labeling  
* **Complete** (or an alternate custom status created by the task creator): Items after an annotation process  
* **Approved** (or an alternate custom status created by the task creator): Completed items after a QA process  
#### Prep  
```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')
```
#### Single status update  
```python
# Mark single item as completed
item = dataset.items.get(item_id='<my-item-id>')
item.update_status(status=dl.ItemStatus.COMPLETED)
# In the same way you can update to another status
item.update_status(status=dl.ItemStatus.APPROVED)
item.update_status(status=dl.ItemStatus.DISCARDED)
```
#### Clear status  
```python
# Clear status for completed/approved/discarded
item.update_status(dl.ITEM_STATUS_COMPLETED, clear=True)
```
### Bulk status update  
```python
# With items list
filters = dl.Filters(field='<annotated>', values=True)
items = dataset.items.list(filters=filters)
dataset.items.update_status(status=dl.ItemStatus.APPROVED, items=items)
# With filters
filters = dl.Filters(field='<annotated>', values=True)
dataset.items.update_status(status=dl.ItemStatus.DISCARDED, filters=filters)
# With list of item ids
item_ids = ['<id1>', '<id2>', '<id3>']
dataset.items.update_status(status=dl.ItemStatus.COMPLETED, item_ids=item_ids)
```
####    Example  
To mark an entire task as completed use the following:  
```python
task = dataset.tasks.get(task_name='<my-task-name>')
dataset.items.update_status(status=dl.ItemStatus.COMPLETED, items=task.get_items())
```
