# Task Management: Orchestrating Your Annotation Workflow 🎯

Learn how to efficiently create, manage, and track annotation tasks in Dataloop - your key to organizing team workflows and ensuring quality annotations.

## Creating Tasks

The SDK provides specialized methods to create different task types. These methods allow you to clearly define task objectives (labeling, QA, consensus, honeypot, and qualification).
**Important**: The following new helper methods do not replace or remove the existing basic task creation method `(task = dataset.tasks.create(...)`, and you can still create tasks using the original method.


### 1. Simple Labeling Task Creation

Labeling tasks are the foundation of annotation workflows. They can be configured as:

- Distribution tasks — work is assigned directly to specific annotators.
- Pulling tasks — annotators dynamically pull batches of items until the task is complete.
- Item-specific tasks — assign selected items to annotators for targeted review or urgent labeling.

```python
import dtlpy as dl
import datetime

if dl.token_expired():
    dl.login()

project = dl.projects.get(project_name='project_name')          # select your project.
dataset = project.datasets.get(dataset_name='dataset_name')     # select your dataset.

# Create a simple distribution task 
dataset.tasks.create_labeling(
    name='my_distribution_task',
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai']
)

# Create a simple pulling task (dynamic distribution via batches)
dataset.tasks.create_labeling(
    name='my_pulling_task',
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    batch_size=5,           # items per batch
    max_batch_workload=7    # max items per assignment
)

# Create task with specific items
dataset.tasks.create_labeling(
    name='Urgent Review',
    assignee_ids=['annotator1@company.com', 'annotator2@company.com'],
    item_ids=['item1_id', 'item2_id'],
    due_date=dl.utils.datetime_to_timestamp(datetime(2024, 12, 31))
)
```

### 2. Advanced Task Configuration

Advanced configurations extend beyond basic labeling to support specialized workflows and quality assurance mechanisms:

- [Tasks with Filters](https://developers.dataloop.ai/tutorials/labeling_workflows/task_and_assignment/chapter#creating-tasks-with-filters): Create tasks only for items that match defined criteria (e.g., directory, metadata, or annotation status).
- [QA Tasks](https://developers.dataloop.ai/tutorials/labeling_workflows/task_and_assignment/chapter#creating-qa-tasks): Assign reviewers to validate and ensure annotation quality.
- [Consensus Tasks](https://developers.dataloop.ai/tutorials/labeling_workflows/task_and_assignment/chapter#creating-consensus-tasks): Require multiple annotators to label the same item to measure agreement and accuracy.
- [Honeypot Tasks](https://developers.dataloop.ai/tutorials/labeling_workflows/task_and_assignment/chapter#creating-honeypot-tasks): Insert “gold standard” items to monitor annotator performance.
- [Qualification Tasks](https://developers.dataloop.ai/tutorials/labeling_workflows/task_and_assignment/chapter#creating-qualification-tasks): Test annotators with sample work before assigning them to production tasks.

This level of configuration is best suited for production environments, where maintaining annotation accuracy, consistency, and reliability is critical.

## Managing Tasks 📋

This section covers how to manage existing tasks in the Dataloop SDK. You can retrieve tasks by ID, update their properties, change their status, delete them when no longer needed, and manage the items assigned to each task.

### 1. Task Operations

```python
# Get task by ID
task = dataset.tasks.get(task_id='task_id')

# Update task
task.name = 'Updated Task Name'
task.update()

# Change task status
task.set_status(status='completed')

# Delete task
task.delete()
```

### 2. Item Management

```python
# Add items to task
task.add_items(
    item_ids=['item3_id', 'item4_id'],
    assignee_ids=['annotator@company.com']
)

# Remove items from task
task.remove_items(item_ids=['item3_id'])

# Reassign items
task.reassign_items(
    item_ids=['item1_id'],
    assignee_id='new_annotator@company.com'
)
```

Ready to explore model management? Let's move on to the next chapter! 🚀 