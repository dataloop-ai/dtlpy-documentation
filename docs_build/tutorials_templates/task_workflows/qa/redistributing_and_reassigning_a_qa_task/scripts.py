import dtlpy as dl


def func1():
    QAtask = dl.tasks.get(task_id='<my-task-id>')


def func2():
    project = dl.projects.get(project_name='<project_name>')
    QAtask = project.tasks.get(task_name='<my-qa-task-name>')


def func3():
    dataset = project.datasets.get(dataset_name='<dataset_name>')
    QAtask = project.tasks.get(task_name='<my-qa-task-name>')


def func4():
    tasks = project.tasks.list()


def func5():
    tasks = dataset.tasks.list()


def func6():
    qa_task_items = QAtask.get_items()


def func7():
    assignment = dl.assignments.get(assignment_id='<my-assignment-id>')


def func8():
    project = dl.projects.get(project_name='<project_name>')
    assignment = project.assignments.get(assignment_name='<my-assignment-name>')


def func9():
    dataset = project.datasets.get(dataset_name='<dataset_name>')
    assignment = dataset.assignments.get(assignment_name='<my-assignment-name>')


def func10():
    task = project.tasks.get(task_name='<my-task-name>')
    assignment = task.assignments.get(assignment_name='<my-assignment-name>')


def func11():
    assignments = project.assignments.list()


def func12():
    assignments = dataset.assignments.list()


def func13():
    assignments = task.assignments.list()


def func14():
    assignment_items = assignment.get_items()


def func15():
    import dtlpy as dl
    import datetime
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name>')
    QAtask = dl.tasks.get(task_id='<my-task-id>')
    assignment = task.assignments.get(assignment_name='<my-assignment-name>')


def func16():
    # load is the workload percentage for each annotator
    assignment.redistribute(dl.Workload([dl.WorkloadUnit(assignee_id='<annotator1@dataloop.ai>', load=50),
                                         dl.WorkloadUnit(assignee_id='<annotator2@dataloop.ai>', load=50)]))


def func17():
    assignment.reassign(assignee_ids['<annotator1@dataloop.ai>'])


def func18():
    QAtask.delete()


def func19():
    assignment.delete()
