import dtlpy as dl


def func1():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()


def func2():
    annotation_definition=dl.Note(top=10,left=10, bottom=100, right=100,label='my-label')
    annotation_definition.assignee = "user@dataloop.ai"
    annotation_definition.add_message("this is a message 1")
    annotation_definition.add_message("this is a message 2")

def func3():
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')

def func4():
    item = dataset.items.get(filepath='/your-image-file-path.jpg')

def func5():
    builder = item.annotations.builder()

def func6():
    annotation_definition=dl.Note(top=10,left=10, bottom=100, right=100,label='my-label')
    annotation_definition.assignee = "user@dataloop.ai" 
    annotation_definition.add_message("this is a message 1")
    annotation_definition.add_message("this is a message 2")
    builder.add(annotation_definition=annotation_definition)

def func7():
    item.annotations.upload(builder)