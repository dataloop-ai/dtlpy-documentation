
## Tasks
In the Dataloop platform, tasks are created to initiate annotation or QA (Quality Assurance) work. It requires defining the data items to be included, the task assignees, and various options such as work-load, custom-status, and more. The tasks can be of 2 types, which were mentioned above - annotation tasks or quality assurance tasks. You will now find out how to create and assign people to both types of tasks.

To create a task that uses a filter, first name it, then add a due date for when it should be completed, and then add one or more annotators to handle that task and a filter. To create an annotation task, simply run the following code with the desired parameters:
```python
task = dataset.tasks.create(
    task_name='test_task1',
    due_date=datetime.datetime(day=11, month=3, year=2025).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    # The items will be divided equally between assignees
    filters=filters  # (optional) filter by folder directory or use other filters
)
```
To create a quality assurance tasks, the process is quite similar. See the code below:
```python
qa_task = dataset.tasks.create_qa_task(task=task,
                                       due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
                                       assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
                                       filters=filters  # this filter is for "completed items"
                                       )
```
If you simply want to create a task out of an entire dataset, you can simply remove the "filters" parameter, and a task will be created out of the entire dataset you select:
```python
task = dataset.tasks.create(
    task_name='<task_name>',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>']
    # The items will be divided equally between assignments
)
```

Now you know the basics of tasks. In the next chapter, you will learn  how you can use data versioning tools to manage your data.
