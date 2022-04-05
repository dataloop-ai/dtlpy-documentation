## Create a Task  
To reach the tasks and assignments repositories go to <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.tasks" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.assignments" target="_blank">assignments</a>.  
  
  
To reach the tasks and assignments entities go to <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.task" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.assignment" target="_blank">assignments</a>.  
### Creating a Task with Assignments  
There are a couple of ways to create a task with assignments.  
#### 1. By Folder Directory  
This example will create a task for items that match a filter. The items will be divided equally between annotator's assignments:  
```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')    
filters = dl.Filters(field='<dir>', values='</my/folder/directory>') #filter by directory 
task = dataset.tasks.create(
task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'], #The items will be divided equally between assignments
        filters=filters  # filter by folder directory or use other filters
)
```
#### 2. By Filters  
This example will create a task for items that match a filter. The items will be divided equally between the annotator's assignments:  
  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
These examples are for creating a task from items without annotations.<br>  
You can also create tasks based on different filters, learn all about filters <a href="https://dataloop.ai/docs/sdk-sort-filter" target="_blank">here</a>.</div>  
```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')  
#filter items without annotations  
filters = dl.Filters(field='<annotated>', values=False) 
task = dataset.tasks.create(
task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'], #The items will be divided equally between assignments
        filters=filters  # filter items without annotations or use other filters
)
```
#### 3. List of Items  
Create a task from a list of items. The items will be divided equally between annotator's assignments:  
```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')    
items = dataset.items.list()
items_list = [item for item in items.all()]
task = dataset.tasks.create(
task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'], #The items will be divided equally between assignments
        items=items_list
)
```
#### 4. Full Dataset  
Create a task from all of the items in the dataset. The items will be divided equally between annotator's assignments:  
```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')    
task = dataset.tasks.create(
task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'] #The items will be divided equally between assignments
)
```
### Add items to an existing task  
Adding items to an existing task will create new assignments (for new assignee/s).  
  
#### 1. By Filters  
```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')    
filters = dl.Filters(field='<metadata.system.refs>', values=[]) #filter on unassigned items
task.add_items(
filters=filters,  # filter by folder directory or use other filters
assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'] )
```
#### 2. Single Item  
```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')    
item = dataset.items.get(item_id='<my-item-id>')
task.add_items(
    items=[item],
assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'])
```
#### 3. List of Items  
```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')    
items = dataset.items.list()
items_list = [item for item in items.all()]
task.add_items(
    items=items_list,
assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>']
)
```
