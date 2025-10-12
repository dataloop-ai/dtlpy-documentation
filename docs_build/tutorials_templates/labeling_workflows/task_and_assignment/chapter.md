# Tasks and Assignments in Dataloop 📋

Welcome to your guide to managing tasks and assignments in Dataloop! Whether you're setting up annotation projects, managing QA workflows, or organizing your team's workload, we've got you covered. Let's dive in!

## Understanding Tasks and Assignments 🎓

Think of tasks as your project's to-do lists and assignments as individual work packages. Here's what you need to know:

- **Tasks** 📦 contain the overall work to be done
- **Assignments** 📝 distribute the work among team members
- **Items** 🖼️ are the actual data pieces to be worked on

## Creating Tasks 🛠️

The SDK provides specialized methods to create different task types. These methods allow you to clearly define task objectives (labeling, QA, consensus, honeypot, qualification).

**Important**: The following new helper methods do not replace or remove the existing basic task creation method `(task = dataset.tasks.create(...)`. You can still create tasks the original way.

#### Prerequisites

Use this snippet once to authenticate and select your project/dataset.

```python
import dtlpy as dl
import datetime

if dl.token_expired():
    dl.login()

project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
```

### Creating Labeling Tasks

Labeling tasks are the most common type of annotation tasks. They can be created either as distribution tasks (direct assignment) or pulling tasks (dynamic batch allocation).

```python
# Create a distribution task (assign immediately)
dataset.tasks.create_labeling(
    name='my_distribution_task',
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai']
)

# Create a pulling task (dynamic distribution via batches)
dataset.tasks.create_labeling(
    name='my_pulling_task',
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    batch_size=5,           # items per batch
    max_batch_workload=7    # max items per assignment
)
```

### Creating Tasks with Filters

Filters allow you to restrict a task to specific items based on metadata or annotation status.

```python
# Filter by directory
filters = dl.Filters(field='dir', values='/my/folder/path')

# OR filter by annotation status
filters = dl.Filters(field='annotated', values=False)

# Create task with filters
dataset.tasks.create_labeling(
    name='filtered_task',
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    filters=filters
)
```

### Creating QA Tasks

QA (Quality Assurance) tasks are designed to review and validate work completed in an annotation task.

```python
# Create QA task from an annotation task
qa_task = dataset.tasks.create_qa_task(
    task=task_entity,    # reference an existing annotation task
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['reviewer1@dataloop.ai', 'reviewer2@dataloop.ai']
)
```

### Creating Consensus Tasks

Consensus tasks require multiple annotators to label the same items, enabling accuracy measurement and agreement scoring.

```python
# Create a consensus task
dataset.tasks.create_consensus_task(
    name='my_consensus_task',
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    consensus_percentage=66,  # percent of items to be reviewed in consensus
    consensus_assignees=2     # annotators per item
)
```

### Creating Honeypot Tasks

Honeypot tasks introduce pre-labeled “gold standard” items to measure annotator accuracy and reliability.

```python
# Create a honeypot task
dataset.tasks.create_honeypot_task(
    name='my_honeypot_task',
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    consensus_percentage=66,
    consensus_assignees=2
)
```

### Creating Qualification Tasks

Qualification tasks assess annotators’ capabilities before they are assigned to production labeling.

```python
# Create a qualification task
dataset.tasks.create_qualification_task(
    name='my_qualification_task',
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    consensus_percentage=66,
    consensus_assignees=2
)
```

## Managing Existing Tasks 🔧

This section explains how to work with tasks that have already been created. Using the Dataloop SDK, you can add or reassign items, look up specific tasks or assignments, and maintain ongoing annotation workflows efficiently.

### Adding Items to Tasks

Use this method to expand an existing task with new data. You can add items either by applying filters (for example, all unassigned items) or by directly passing a list of item IDs. You can also specify which annotators should receive the new assignments.

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

The SDK allows you to search and retrieve tasks or assignments in different ways. You can get a task by its ID, find it by name within a project, list all tasks in a dataset, or access assignment details by ID. This makes it easy to track progress, manage workloads, and monitor task completion.

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

Use cleanup operations to remove tasks or assignments that are no longer required. This helps keep your projects organized and ensures that only active, relevant tasks remain accessible.

### Deleting Tasks and Assignments

You can delete an entire task—including all of its associated assignments—or remove specific assignments individually:

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
- Visit our [Assignment Guide](https://docs.dataloop.ai/docs/assignments-overview)
- Explore [Pipeline Integration](https://docs.dataloop.ai/docs/labeling-nodes)

Happy task managing! 🚀
