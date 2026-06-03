# Task Management: Orchestrating Your Annotation Workflow 🎯

Learn how to efficiently create, manage, and track annotation tasks in Dataloop - your key to organizing team workflows and ensuring quality annotations.
## Project Setup ⚙️

### Dataloop Login 🔐

> ```python
> import dtlpy as dl
> from dotenv import load_dotenv
> import os
>
> # Load environment variables from .env file
> load_dotenv(override=True)
>
> # Access your API key securely
> api_key = os.getenv('DTLPY_API_KEY')
>
> # Initialize Dataloop with the API key
> dl.login_api_key(api_key=api_key)
> ```

### Project and Dataset Setup

> ```python
> # Set your project and dataset names
> project_name = "onboarding-project"
> dataset_name = "onboarding-dataset"
>
> try:
>     # Try to get existing project
>     project = dl.projects.get(project_name=project_name)
>     print(f"Project '{project_name}' already exists")
> except Exception:
>     project = dl.projects.create(project_name=project_name)
>     # Create project if it doesn't exist
>     print(f"Created project '{project_name}'")
>
> try:
>     # Try to get existing dataset
>     dataset = project.datasets.get(dataset_name=dataset_name)
>     print(f"Dataset '{dataset_name}' already exists")
>
> except Exception:
>     # Create dataset if it doesn't exist
>     dataset = project.datasets.create(dataset_name=dataset_name)
>     print(f"Created dataset '{dataset_name}'")
> ```

## Creating Tasks

The SDK provides specialized methods to create different task types. These methods allow you to clearly define task objectives (labeling, QA, consensus, honeypot, and qualification).
**Important**: The following new helper methods do not replace or remove the existing basic task creation method `(task = dataset.tasks.create(...)`, and you can still create tasks using the original method.

### 1. Simple Labeling Task Creation

Labeling tasks are the foundation of annotation workflows. They can be configured as:

- Distribution tasks — work is assigned directly to specific annotators.
- Pulling tasks — annotators dynamically pull batches of items until the task is complete.
- Item-specific tasks — assign selected items to annotators for targeted review or urgent labeling.

> ```python
> # Task cleanup before we start
> for task in project.tasks.list():
>     task.delete()
> ```

> ```python
> dataset.items.list().print()
> ```

> ```python
> # set your four jpg items
> item_1 = dataset.items.get(item_id='item_id_1')
> item_2 = dataset.items.get(item_id='item_id_2')
> item_3 = dataset.items.get(item_id='item_id_3')
> item_4 = dataset.items.get(item_id='item_id_4')
> ```

> ```python
> import dtlpy as dl
> import datetime
>
> # Add annotators to your project e.g 'annotator1@dataloop.ai', 'annotator2@dataloop.ai'
> # Set your real email address in assignee_ids email 'my-email@dell.com'
> task_1 = dataset.tasks.create_labeling_task(
>     name='my_distribution_task',
>     assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai', 'my-email@dell.com'],
>     dataset=dataset
> )
>
> # Create a simple pulling task (dynamic distribution via batches)
> task_2 = dataset.tasks.create_labeling_task(
>     name='my_pulling_task',
>     assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai', 'my-email@dell.com'],
>     batch_size=5,           # items per batch
>     max_batch_workload=7    # max items per assignment
> )
>
> # Create task with specific items using filters
> # Note: Use filters to select specific items instead of item_ids
> # filters = dl.Filters(field='id', values=['item1_id', 'item2_id'])
> filters = dl.Filters(field='id', values=[item_1.id, item_2.id])
>
>
> task_3 = dataset.tasks.create_labeling_task(
>     name='Urgent Review',
>     assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai','my-email@dell.com'],
>     filters=filters,
>     due_date=datetime.datetime(2026, 12, 31).timestamp()
> )
> ```

> ```python
> # Explore your tasks in dataloop dashboard platform
> # ecplore each task assignmemts
> dataset.tasks.open_in_web()
>
> # Check your email and verify you received email notification on task creation/completed
> ```

### 2. Advanced Task Configuration

Advanced configurations extend beyond basic labeling to support specialized workflows and quality assurance mechanisms:

- [Tasks with Filters](https://developers.dataloop.ai/tutorials/labeling_workflows/task_and_assignment/chapter#creating-tasks-with-filters): Create tasks only for items that match defined criteria (e.g., directory, metadata, or annotation status).
- [QA Tasks](https://developers.dataloop.ai/tutorials/labeling_workflows/task_and_assignment/chapter#creating-qa-tasks): Assign reviewers to validate and ensure annotation quality.
- [Consensus Tasks](https://developers.dataloop.ai/tutorials/labeling_workflows/task_and_assignment/chapter#creating-consensus-tasks): Require multiple annotators to label the same item to measure agreement and accuracy.
- [Honeypot Tasks](https://developers.dataloop.ai/tutorials/labeling_workflows/task_and_assignment/chapter#creating-honeypot-tasks): Insert "gold standard" items to monitor annotator performance.
- [Qualification Tasks](https://developers.dataloop.ai/tutorials/labeling_workflows/task_and_assignment/chapter#creating-qualification-tasks): Test annotators with sample work before assigning them to production tasks.

This level of configuration is best suited for production environments, where maintaining annotation accuracy, consistency, and reliability is critical.

## Managing Tasks 📋

This section covers how to manage existing tasks in the Dataloop SDK. You can retrieve tasks by ID, update their properties, change their status, delete them when no longer needed, and manage the items assigned to each task.

### 1. Task Operations

> ```python
> dataset.tasks.list().print()
> ```

> ```python
> # Get task by ID
> task = dataset.tasks.get(task_id=task_1.id)
>
> # Update task
> task.name = 'Updated Task Name'
> task.update()
>
>
> # Change task status
> task.set_status(status='completed', operation='create', item_ids=[item_1.id, item_2.id])
>
> # Delete task
> task.delete()
> ```

> ```python
> dataset.tasks.list().print()
> ```

### 2. Item Management

> ```python
> # Get existing task
> task = dataset.tasks.get(task_id=task_2.id)
> # Add items to task
> task.add_items(
>     items=[item_3, item_4],
>     assignee_ids=['annotator@company.com']
> )
>
> # Remove items from task
> task.remove_items(items=[item_3, item_4])
> ```

> ```python
> #  Create a distribution task (not pulling task)
> task = dataset.tasks.create_labeling_task(
>     name='my_distribution_task',
>     assignee_ids=['annotator1@dataloop.ai'],
>     dataset=dataset
> )
>
> # Then reassignment will work
> assignment = task.assignments.list()[0]
> assignment.reassign('new_annotator@company.com')
> ```

> ```python
> # Check new reassignment in dashboard
> task.open_in_web()
> ```


Ready to explore model management? Let's move on to the next chapter! 🚀
