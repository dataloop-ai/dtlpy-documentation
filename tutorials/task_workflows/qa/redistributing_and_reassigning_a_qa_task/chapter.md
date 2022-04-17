## Redistributing and Reassigning a QA Task  
To reach the tasks and assignments repositories go to <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.tasks" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.assignments" target="_blank">assignments</a>.  
  
  
To reach the tasks and assignments entities go to <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.task" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.assignment" target="_blank">assignments</a>.  
  
### Get QA Task and Assignments  
#### Get Task  
##### Get by ID  

```python
QAtask = dl.tasks.get(task_id='<my-task-id>')
```
##### Get by name – in a <b>project</b>  

```python
project = dl.projects.get(project_name='<project_name>')
QAtask = project.tasks.get(task_name='<my-qa-task-name>')
```
##### Get by name – in a <b>dataset</b>  

```python
dataset = project.datasets.get(dataset_name='<dataset_name>')
QAtask = project.tasks.get(task_name='<my-qa-task-name>')
```
##### Get list – in a <b>project</b>  

```python
tasks = project.tasks.list()
```
##### Get list – in a <b>dataset</b>  

```python
tasks = dataset.tasks.list()
```
##### Get Task Items  

```python
qa_task_items = QAtask.get_items()
```
#### Get Assignments  
##### Get by ID  

```python
assignment = dl.assignments.get(assignment_id='<my-assignment-id>')
```
##### Get by name – in a <b>project</b>  

```python
project = dl.projects.get(project_name='<project_name>')
assignment = project.assignments.get(assignment_name='<my-assignment-name>')
```
##### Get by name – in a <b>dataset</b>  

```python
dataset = project.datasets.get(dataset_name='<dataset_name>')
assignment = dataset.assignments.get(assignment_name='<my-assignment-name>')
```
##### Get by name – in a <b>task</b>  

```python
task = project.tasks.get(task_name='<my-task-name>')
assignment = task.assignments.get(assignment_name='<my-assignment-name>')
```
##### Get list – in a <b>project</b>  

```python
assignments = project.assignments.list()
```
##### Get list – in a <b>dataset</b>  

```python
assignments = dataset.assignments.list()
```
##### Get list – in a <b>task</b>  

```python
assignments = task.assignments.list()
```
#### Get Assignment Items  

```python
assignment_items = assignment.get_items()
```
### Redistribute and Reassign the QA Assignment  
##### prep  

```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')
QAtask = dl.tasks.get(task_id='<my-task-id>')
assignment = task.assignments.get(assignment_name='<my-assignment-name>')
```
#### Redistribute  

```python
# load is the workload percentage for each annotator
assignment.redistribute(dl.Workload([dl.WorkloadUnit(assignee_id='<annotator1@dataloop.ai>', load=50), dl.WorkloadUnit(assignee_id='<annotator2@dataloop.ai>', load=50)]))
```
#### Reassign  

```python
assignment.reassign(
ignee_ids['<annotator1@dataloop.ai>']
```
### Delete Task and Assignments  
#### Delete Task  
<div style="background-color: lightyellow; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
In case you delete a task it will delete all its assignments as well.</div>  

```python
QAtask.delete()
```
#### Delete Assignment  

```python
assignment.delete()
```
