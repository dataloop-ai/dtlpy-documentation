import dtlpy as dl


def func1():
    import dtlpy as dl
    import datetime
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name>')  
    #Get the annotation task, you can also get a task by name or from a list
    task = project.tasks.get(task_id='<my-task-id>')


def func2():
    # Add filter for completed items
    filters = dl.Filters()
    filters.add(field='<metadata.system.annotationStatus>', values='<completed>')
    #create a QA task - fill in the due date and assignees.
    QAtask = dataset.tasks.create_qa_task(task=task,
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
        assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
            filters=filters  # this filter is for "completed items" 
    )


def func3():
    import dtlpy as dl
    import datetime
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name>')


def func4():
    filters = dl.Filters(field='<metadata.system.annotationStatus>', values='<completed>')
    filters.add(field='<dir>', values='</my/folder/directory>')


def func5():
    QAtask = dataset.tasks.create(
        task_type='<qa>',
        due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
        assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
        filters=filters  # filter by folder directory or use other filters
    )