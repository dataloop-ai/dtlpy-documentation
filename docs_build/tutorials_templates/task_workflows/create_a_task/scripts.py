import dtlpy as dl


def func1():
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


def func2():
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


def func3():
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


def func4():
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
