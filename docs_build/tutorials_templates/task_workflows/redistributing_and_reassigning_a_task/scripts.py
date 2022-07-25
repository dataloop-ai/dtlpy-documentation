def func1():
    import dtlpy as dl

    # Get task by ID
    task = dl.tasks.get(task_id='<my-task-id>')

    # Get task by name - in a project
    project = dl.projects.get(project_name='<project_name>')
    task = project.tasks.get(task_name='<my-task-name>')

    # Get task by name - in a Dataset
    dataset = project.datasets.get(dataset_name='<dataset_name>')
    task = project.tasks.get(task_name='<my-task-name>')

    # Get all tasks (list) in a project
    tasks = project.tasks.list()

    # Get all tasks (list( in a dataset
    tasks = dataset.tasks.list()


def func2():
    # Get assignment by assignment ID
    assignment = dl.assignments.get(assignment_id='<my-assignment-id>')

    # Get assignment by name – in a project
    project = dl.projects.get(project_name='<project_name>')
    assignment = project.assignments.get(assignment_name='<my-assignment-name>')

    # Get assignment by name – in a dataset
    dataset = project.datasets.get(dataset_name='<dataset_name>')
    assignment = dataset.assignments.get(assignment_name='<my-assignment-name>')

    # Get assignment by name – in a task
    task = project.tasks.get(task_name='<my-task-name>')
    assignment = task.assignments.get(assignment_name='<my-assignment-name>')

    # Get assignments list - in a project
    assignments = project.assignments.list()

    # Get assignments list - in a dataset
    assignments = dataset.assignments.list()

    # Get assignments list - in a task
    assignments = task.assignments.list()


def func3():
    assignment_items = assignment.get_items()


def func4():
    import dtlpy as dl
    import datetime
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name>')
    task = dl.tasks.get(task_id='<my-task-id>')
    assignment = task.assignments.get(assignment_name='<my-assignment-name>')


def func5():
    # load is the workload percentage for each annotator
    assignment.redistribute(dl.Workload([dl.WorkloadUnit(assignee_id='<annotator1@dataloop.ai>', load=50),
                                         dl.WorkloadUnit(assignee_id='<annotator2@dataloop.ai>', load=50)]))


def func6():
    assignment.reassign(assignee_ids['<annotator1@dataloop.ai>'])


def func7():
    task.delete()


def func8():
    assignment.delete()
