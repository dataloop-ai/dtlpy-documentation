# Creating Tasks  
Tasks are created in the Dataloop platform to initiate annotation or QA work.  
It requires defining the data items to be included, the assignees working on the task, and various options such as work-load, custom-statuses and more.  
  
## Create A Task (Annotation task or QA task) Using Filter  
The following example demonstrates creating a task from an items filter.  
The script includes 2 example, for filtering an entire folder/directory, and for filtering by item annotation status.  
  

```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')
# Create a task with all items in a specific folder
filters = dl.Filters(field='<dir>', values='</my/folder/directory>')
# filter items without annotations
filters = dl.Filters(field='<annotated>', values=False)
# Create annotation task with filters
task = dataset.tasks.create(
    task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    # The items will be divided equally between assignments
    filters=filters  # filter by folder directory or use other filters
)
# Create QA task with filters
qa_task = dataset.tasks.create_qa_task(task=task,
                                       due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
                                       assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
                                       filters=filters  # this filter is for "completed items"
                                       )
```
## List of Items  
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
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    # The items will be divided equally between assignments
    items=items_list
)
```
## Entire Dataset  
Create a task from all items in a dataset. The items will be divided equally between annotator's assignments:  

```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')
# Create annotation task
task = dataset.tasks.create(
    task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>']
    # The items will be divided equally between assignments
)
```
# Create a Pulling Task  
In this task, items are queued in a hidden assignment, and distributed to assignees in small batches, according to their progress.  
Changes to the team are very easy to do, as no assignee has a large number of items in their assignment.  

```python
task = dataset.tasks.create(
    task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    # batch_size: Pulling batch size (items), use with pulling allocation method. Restrictions - Min 3, max 100
    batch_size=10,
    # max_batch_workload: Max items in assignment, use with pulling allocation method. Restrictions - Min batchSize + 2, max batchSize * 2
    max_batch_workload=15,
    # allowed_assignees - list the task assignees (contributors) that should be working on the task. Provide a list of users' emails
    allowed_assignees=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>']
)
```
# Add items to an existing task  
Adding items to an existing task will create new assignments (for new assignee/s).  
  
## By Filters  

```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')
filters = dl.Filters(field='<metadata.system.refs>', values=[])  # filter on unassigned items
# Create annotation task
task.add_items(
    filters=filters,  # filter by folder directory or use other filters
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'])
```
## Single or a List of Items  

```python
item = dl.items.get(item_id='<item-id>')
task.add_items(items=[item],
               assignee_ids=['<annotator1@dataloop.ai>'])
```
## Creating Consensus Tasks  

```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')
# Create annotation task
task = dataset.tasks.create(
    task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    consensus_percentage=100,  # the consensus percentage ber task
    consensus_assignees=2,  # the consensus assignees number of the task
)
```
## Creating Pipeline Tasks Node  
this example will create a task node in a pipeline.  
all options are the same as creating a task, with the addition of the pipeline node options.  

```python
import dtlpy as dl
import datetime
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name>')
pipeline = project.pipelines.create(name='pipeline-faas-example-dataset')
# Create annotation task
task_node = dl.TaskNode(
    name='My Task',
    recipe_id='<recipe_id>',
    recipe_title='<recipe_title>',
    task_owner='owner',
    workload=[dl.WorkloadUnit(assignee_id='assignee_id', load=100)],
    position=(2, 1),
    project_id=project.id,
    dataset_id=dataset.id,
)
pipeline.nodes.add(node=task_node)
pipeline.update()
```
