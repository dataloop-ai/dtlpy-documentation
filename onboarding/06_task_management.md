# Task Management: Orchestrating Your Annotation Workflow 🎯

Learn how to efficiently create, manage, and track annotation tasks in Dataloop - your key to organizing team workflows and ensuring quality annotations.

## Creating Tasks 📝

### 1. Basic Task Creation

```python
import dtlpy as dl

# Create a simple task
task = dataset.tasks.create(
    task_name='Annotate Cars',
    assignee_ids=['annotator@company.com'],
    due_date=dl.utils.datetime_to_timestamp(datetime(2024, 12, 31))
)

# Create task with specific items
task = dataset.tasks.create(
    task_name='Urgent Review',
    assignee_ids=['annotator1@company.com', 'annotator2@company.com'],
    item_ids=['item1_id', 'item2_id'],
    due_date=dl.utils.datetime_to_timestamp(datetime(2024, 12, 31))
)
```

### 2. Advanced Task Configuration

```python
# Create task with filters
filters = dl.Filters()
filters.add(field='dir', values='/folder/to/annotate')
filters.add(field='metadata.user.status', values='to-annotate')

task = dataset.tasks.create(
    task_name='Batch Annotation',
    assignee_ids=['team@company.com'],
    filters=filters,
    project_id=project.id,
    task_type='annotation',
    task_owner='owner@company.com',
    workload=[
        dl.WorkloadUnit(
            assignee_id='annotator1@company.com',
            load=50  # percentage
        ),
        dl.WorkloadUnit(
            assignee_id='annotator2@company.com',
            load=50
        )
    ]
)
```

## Managing Tasks 📋

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