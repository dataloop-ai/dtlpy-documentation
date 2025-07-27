# Managing Item Status in Dataloop 🏷️

Welcome to your guide to managing item status in Dataloop! Whether you're tracking annotation progress, managing QA workflows, or organizing your data, understanding item status is key. Let's dive in!

## Understanding Item Status 🎓

Think of item status as traffic lights for your data workflow:
- 🟢 **COMPLETE**: Item is finished (for annotation tasks)
- ✅ **APPROVE**: Item passed review (for QA tasks)
- ⛔ **DISCARD**: Item should be excluded
- ⚪ **NO STATUS**: Item is available for work

### Default Status Types

1. **Annotation Tasks**:
   - `COMPLETE`: Work is finished
   - `DISCARD`: Item should be excluded

2. **QA Tasks**:
   - `APPROVE`: Item passed review
   - `DISCARD`: Item should be excluded

## Working with Item Status 🛠️

### Setting Status for Single Items

```python
import dtlpy as dl

# Get your project and resources
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
task = dataset.tasks.get(task_name='task_name')
assignment = dataset.assignments.get(assignment_name='assignment_name')
item = dataset.items.get(item_id='item-id')

# Set status in different contexts
item.update_status(status=dl.ItemStatus.COMPLETED, task_id=task.id)  # For task
item.update_status(status=dl.ItemStatus.APPROVED, assignment_id=assignment.id)  # For assignment
item.update_status(status=dl.ItemStatus.DISCARDED)  # For single-task items
```

### Batch Status Updates 🔄

#### Method 1: Using Dataset Filters (Recommended for Single-Task Items)

```python
# Update status for annotated items
filters = dl.Filters(field='annotated', values=True)

# Option 1: Using item list
items = dataset.items.list(filters=filters)
dataset.items.update_status(
    status=dl.ItemStatus.APPROVED,
    items=items
)

# Option 2: Using filters directly
dataset.items.update_status(
    status=dl.ItemStatus.DISCARDED,
    filters=filters
)

# Option 3: Using item IDs
item_ids = ['id1', 'id2', 'id3']
dataset.items.update_status(
    status=dl.ItemStatus.COMPLETED,
    item_ids=item_ids
)
```

#### Method 2: Using Task Entity (Recommended for Multi-Task Items)

```python
# Option 1: Using filters
filters = dl.Filters(field='annotated', values=True)
item_ids = [item.id for item in dataset.items.list(filters=filters).all()]

# Option 2: Using specific IDs
item_ids = ['id1', 'id2', 'id3']

# Update status through task
task = dataset.tasks.get(task_id='your_actual_task_id')

# Set status to APPROVED
task.set_status(
    status=dl.ItemStatus.APPROVED,
    operation='create',
    item_ids=item_ids
)
```

### Clearing Item Status ♻️

Need to make items available for work again? Here's how to clear their status:

```python
# Clear status in different contexts
item.update_status(dl.ITEM_STATUS_DISCARDED, task_id=task.id, clear=True)  # For task
item.update_status(dl.ITEM_STATUS_APPROVED, assignment_id=assignment.id, clear=True)  # For assignment
item.update_status(dl.ITEM_STATUS_COMPLETED, clear=True)  # For single-task items
```

### Custom Status Actions 🎨

Want to create tasks with custom status options? Here's how:

```python
# Create task with custom status actions
task = dataset.tasks.create(
    task_name='custom_status_task',
    assignee_ids=['annotator1@dataloop.ai'],
    available_actions=[
        dl.ItemAction(
            action='needs_review',
            display_name='Needs Review'
        ),
        dl.ItemAction(
            action='skip_item',
            display_name='Skip for Now'
        )
    ]
)
```

## Best Practices 💡

1. 🎯 **Choose the Right Method**:
   - Use dataset methods for items in multiple tasks
   - Use task methods for single-task items

2. 🔄 **Batch Operations**:
   - Use filters for bulk updates when possible
   - Group similar status updates together

3. 📝 **Status Management**:
   - Clear status when work needs to be redone
   - Use custom statuses for specific workflow needs
   - Document your status workflow

4. ⚠️ **Important Notes**:
   - Changing task statuses doesn't affect already-status-assigned items
   - Always verify status updates with filters or item counts
   - Consider using custom statuses for complex workflows

## Need More Help? 🤔

- Check out our [Item Status Documentation](https://docs.dataloop.ai/docs/tasks#section-4-statuses)
- Visit our [Task Management Guide](https://docs.dataloop.ai/docs/tasks)

Happy status managing! 🚀
