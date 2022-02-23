def func1():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()


def func2():
    # Create a new project
    project = dl.projects.create(project_name='project-sdk-tutorial')


def func3():
    # Use an existing project
    project = dl.projects.get(project_name='project_name')


def func4():
    dataset = project.datasets.create(dataset_name='dataset-sdk-tutorial')
    item = dataset.items.upload(
        local_path=['https://raw.githubusercontent.com/dataloop-ai/tiny_coco/master/images/train2017/000000184321.jpg'],
        remote_path='/folder_name')
    # Remote path is optional, images will go to the main directory by default
