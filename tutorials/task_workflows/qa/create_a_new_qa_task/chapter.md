## Create a QA Task  
To reach the tasks and assignments repositories go to <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.tasks" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.assignments" target="_blank">assignments</a>.  
  
  
To reach the tasks and assignments entities go to <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.task" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.assignment" target="_blank">assignments</a>.  
  
In Dataloop there are two ways to create a QA task:  
1. You can create a QA task from the annotation task. This will collect all completed Items and create a QA Task.  
2. You can create a standalone QA task.  
### QA task from the annotation task  
#### prep  

```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')
# Get the annotation task, you can also get a task by name or from a list
task = project.tasks.get(task_id='<my-task-id>')
```
#### 2. Create a QA Task  
This action will collect all completed Items and create a QA Task under the annotation task.  
  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
Adding filters is <b>optional</b>. Learn all about filters <a href="https://dataloop.ai/docs/sdk-sort-filter" target="_blank">here</a>.</div>  

```python
# Add filter for completed items
filters = dl.Filters()
filters.add(field='<metadata.system.annotationStatus>', values='<completed>')
# create a QA task - fill in the due date and assignees.
QAtask = dataset.tasks.create_qa_task(task=task,
                                      due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
                                      assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
                                      filters=filters  # this filter is for "completed items"
                                      )
```
### A standalone QA task  
#### prep  

```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')
```
#### 2. Add filter by directory  
  
<div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
Adding filters is <b>optional</b>. Learn all about filters <a href="https://dataloop.ai/docs/sdk-sort-filter" target="_blank">here</a>.</div>  

```python
filters = dl.Filters(field='<metadata.system.annotationStatus>', values='<completed>')
filters.add(field='<dir>', values='</my/folder/directory>')
```
### Create a QA Task  
This action will collect all items on the folder and create a QA Task from them.  

```python
QAtask = dataset.tasks.create(
    task_type='<qa>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    filters=filters  # filter by folder directory or use other filters
)
```
