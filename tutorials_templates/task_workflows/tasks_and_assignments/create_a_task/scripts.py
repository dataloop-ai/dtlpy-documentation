import dtlpy as dl


def func1():
    import dtlpy as dl
    import datetime
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name>')    
    filters = dl.Filters(field='<dir>', values='</my/folder/directory>') #filter by directory 
    task = dataset.tasks.create(
    task_name='<task_name>',
        due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
        assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'], #The items will be divided equally between assignments
            filters=filters  # filter by folder directory or use other filters
    )


def func2():
    import dtlpy as dl
    import datetime
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name>')  
    #filter items without annotations  
    filters = dl.Filters(field='<annotated>', values=False) 
    task = dataset.tasks.create(
    task_name='<task_name>',
        due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
        assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'], #The items will be divided equally between assignments
            filters=filters  # filter items without annotations or use other filters
    )


def func3():
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
        assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'], #The items will be divided equally between assignments
            items=items_list
    )


def func4():
    import dtlpy as dl
    import datetime
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name>')    
    task = dataset.tasks.create(
    task_name='<task_name>',
        due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
        assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'] #The items will be divided equally between assignments
    )


def func5():
    import dtlpy as dl
    import datetime
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name>')    
    filters = dl.Filters(field='<metadata.system.refs>', values=[]) #filter on unassigned items
    task.add_items(
    filters=filters,  # filter by folder directory or use other filters
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'] )

def func6():
    import dtlpy as dl
    import datetime
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name>')    
    item = dataset.items.get(item_id='<my-item-id>')
    task.add_items(
        items=[item],
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'])

def func7():
    import dtlpy as dl
    import datetime
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name>')    
    items = dataset.items.list()
    items_list = [item for item in items.all()]
    task.add_items(
        items=items_list,
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>']
    )