# Tasks and Assignments in Dataloop 📋

Welcome to your guide to managing tasks and assignments in Dataloop! Whether you're setting up annotation projects, managing QA workflows, or organizing your team's workload, we've got you covered. Let's dive in!

## Understanding Tasks and Assignments 🎓

Think of tasks as your project's to-do lists and assignments as individual work packages. Here's what you need to know:

- **Tasks** 📦 contain the overall work to be done
- **Assignments** 📝 distribute the work among team members
- **Items** 🖼️ are the actual data pieces to be worked on

## Creating Tasks 🛠️

### Basic Task Creation

Let's start with a simple annotation task:

```python
import dtlpy as dl
import datetime

if dl.token_expired():
    dl.login()

# Get your project and dataset
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')

# Create a basic task
task = dataset.tasks.create(
    task_name='my_annotation_task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai']
)
```

### Creating Tasks with Filters 🎯

Want to create a task for specific items? Use filters:

```python
# Filter by directory
filters = dl.Filters(field='dir', values='/my/folder/path')

# OR filter by annotation status
filters = dl.Filters(field='annotated', values=False)

# Create task with filters
task = dataset.tasks.create(
    task_name='filtered_task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    filters=filters
)
```

### Creating QA Tasks 🔍

Need to review annotations? Create a QA task:

```python
# Create QA task from an annotation task
qa_task = dataset.tasks.create_qa_task(
    task=task,
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['reviewer1@dataloop.ai', 'reviewer2@dataloop.ai']
)
```

## Smart Task Distribution 🎯

### Pulling Tasks (Dynamic Distribution) 🔄

Perfect for flexible teams and continuous work:

```python
pulling_task = dataset.tasks.create(
    task_name='dynamic_task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    batch_size=10,  # Items per batch (min: 3, max: 100)
    max_batch_workload=15,  # Max items per assignment
    allowed_assignees=['annotator1@dataloop.ai', 'annotator2@dataloop.ai']
)
```

### Consensus Tasks (Multiple Reviews) 👥

Need multiple annotators per item? Try consensus tasks:

```python
consensus_task = dataset.tasks.create(
    task_name='consensus_task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    consensus_percentage=100,  # Percentage of items for consensus
    consensus_assignees=2  # Number of annotators per item
)
```

## Managing Existing Tasks 🔧

### Adding Items to Tasks

```python
# Add items using filters
filters = dl.Filters(field='metadata.system.refs', values=[])  # Unassigned items
task.add_items(
    filters=filters,
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai']
)

# Add specific items
item = dl.items.get(item_id='item-id')
task.add_items(
    items=[item],
    assignee_ids=['annotator1@dataloop.ai']
)
```

### Finding Tasks and Assignments 🔍

```python
# Get task by ID
task = dl.tasks.get(task_id='task-id')

# Get task by name in project
task = project.tasks.get(task_name='task-name')

# List all tasks in dataset
tasks = dataset.tasks.list()

# Get assignment
assignment = dl.assignments.get(assignment_id='assignment-id')

# List assignments in task
assignments = task.assignments.list()
```

### Redistributing Work 🔄

Need to change who's working on what? Here's how:

```python
# Redistribute work between annotators
assignment.redistribute(
    dl.Workload([
        dl.WorkloadUnit(assignee_id='annotator1@dataloop.ai', load=50),
        dl.WorkloadUnit(assignee_id='annotator2@dataloop.ai', load=50)
    ])
)

# Reassign to new annotator
assignment.reassign(['new.annotator@dataloop.ai'])
```

## Pipeline Integration 🔗

Want to include tasks in your pipeline? Here's how:

```python
# Create a pipeline
pipeline = project.pipelines.create(name='my-pipeline')

# Add a task node
task_node = dl.TaskNode(
    name='Pipeline Task',
    recipe_id='recipe-id',
    recipe_title='recipe-title',
    task_owner='owner@dataloop.ai',
    workload=[dl.WorkloadUnit(assignee_id='annotator@dataloop.ai', load=100)],
    position=(2, 1),
    project_id=project.id,
    dataset_id=dataset.id
)

# Add node to pipeline
pipeline.nodes.add(node=task_node)
pipeline.update()
```

## Cleanup Operations 🧹

### Deleting Tasks and Assignments

```python
# Delete a task (this also deletes its assignments)
task.delete()

# Delete a specific assignment
assignment.delete()
```

## Best Practices 💡

1. 📊 Use filters to create focused tasks
2. 🔄 Consider pulling tasks for flexible teams
3. 👥 Use consensus tasks for critical annotations
4. 📅 Set realistic due dates
5. 🎯 Keep batch sizes manageable (10-20 items)

## Need More Help? 🤔

- Check out our [Task Management Documentation](https://docs.dataloop.ai/docs/labeling-overview)
- Visit our [Assignment Guide](https://docs.dataloop.ai/docs/assignments)
- Explore [Pipeline Integration](https://docs.dataloop.ai/docs/workflow-nodes)

Happy task managing! 🚀
