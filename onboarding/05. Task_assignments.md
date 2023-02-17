# Chapter 5 - Tasks

In the Dataloop platform, tasks are created to initiate Annotation or Quality Assurance (QA) workflows. It requires defining the data items to be included, the task assignees, and various options such as work-load, custom-status, and more. The tasks can be of 2 types, which were mentioned above - Annotation tasks or QA tasks. You will now find out how to create and assign people to both types of tasks.

The below example walks you through how to create a Task using the Python SDK.  Your first step is to name the Task then you set a due date for when the Task should be completed.  Add one or more Annotators (Assignees below) to work the Task.  If you don't want to assign all the objects in the Dataset to the Task, add a Filter. Simply run the following code with the desired parameters and your first Task will get created complete with a due date, assignee(s), and a filter:

```python
task = dataset.tasks.create(
    task_name='test_task1',
    due_date=datetime.datetime(day=11, month=3, year=2025).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    # The items will be divided equally between assignees
    filters=filters  # (optional) filter by folder directory or use other filters
)
```

To create a QA Task, the process is quite similar. See the code below:

```python
qa_task = dataset.tasks.create_qa_task(
    task=task,
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    filters=filters  # this filter is for "completed items"
)
```

If you simply want to create a Task out of an entire Dataset, you can simply remove the `filters` parameter, and a Task will be created and use the entire Dataset you identified:

```python
task = dataset.tasks.create(
    task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>']
    # The items will be divided equally between assignments
)
```

Now you know the basics of tasks. In the next chapter, you will learn how you can use data versioning tools to manage your data.
