## Managing Tasks & Assignments  
### Get Task  

```python
import dtlpy as dl
# Get task by ID
task = dl.tasks.get(task_id='<my-task-id>')
# Get task by name - in a project
project = dl.projects.get(project_name='<project_name>')
task = project.tasks.get(task_name='<my-task-name>')
# Get task by name - in a Dataset
dataset = project.datasets.get(dataset_name='<dataset_name>')
task = project.tasks.get(task_name='<my-task-name>')
# Get all tasks (list) in a project
tasks = project.tasks.list()
# Get all tasks (list( in a dataset
tasks = dataset.tasks.list()
```
### Get Assignments  

```python
# Get assignment by assignment ID
assignment = dl.assignments.get(assignment_id='<my-assignment-id>')
# Get assignment by name – in a project
project = dl.projects.get(project_name='<project_name>')
assignment = project.assignments.get(assignment_name='<my-assignment-name>')
# Get assignment by name – in a dataset
dataset = project.datasets.get(dataset_name='<dataset_name>')
assignment = dataset.assignments.get(assignment_name='<my-assignment-name>')
# Get assignment by name – in a task
task = project.tasks.get(task_name='<my-task-name>')
assignment = task.assignments.get(assignment_name='<my-assignment-name>')
# Get assignments list - in a project
assignments = project.assignments.list()
# Get assignments list - in a dataset
assignments = dataset.assignments.list()
# Get assignments list - in a task
assignments = task.assignments.list()
```
#### Get Assignment Items  

```python
assignment_items = assignment.get_items()
```
## Redistribute and Reassign Assignments  

```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')
task = dl.tasks.get(task_id='<my-task-id>')
assignment = task.assignments.get(assignment_name='<my-assignment-name>')
```
### Redistribute  
Redistributing an assignment means to distribute the items among an combination of assignees.  
The process is identical to annotation and QA tasks.  

```python
# load is the workload percentage for each annotator
assignment.redistribute(dl.Workload([dl.WorkloadUnit(assignee_id='<annotator1@dataloop.ai>', load=50),
                                     dl.WorkloadUnit(assignee_id='<annotator2@dataloop.ai>', load=50)]))
```
#### Reassign  
Reassigning an assignment changes the assignee from its original one to another.  

```python
assignment.reassign(assignee_ids['<annotator1@dataloop.ai>'])
```
#### Delete Task and Assignments  
##### Delete Task  
<div style="background-color: lightyellow; color: black; width: 85%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>  
When a task is deleted, all its assignments will be deleted as well.</div>  

```python
task.delete()
```
##### Delete Assignment  

```python
assignment.delete()
```
