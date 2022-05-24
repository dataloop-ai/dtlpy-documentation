class Scripts:
    def __init__(self):
        self.project = None
        self.item = None

    def func1(self):
        import dtlpy as dl
        if dl.token_expired():
            dl.login()

    def func2(self, dl):
        # Create a new project
        project = dl.projects.create(project_name='project-sdk-tutorial')

        # DTLPY-STOP
        self.project = project

    def func3(self, dl):
        # Use an existing project
        project = dl.projects.get(project_name='project-sdk-tutorial')

        # DTLPY-STOP
        self.project = project

    def func4(self, project):
        dataset = project.datasets.create(dataset_name='dataset-sdk-tutorial')
        item = dataset.items.upload(
            local_path=[
                'https://raw.githubusercontent.com/dataloop-ai/tiny_coco/master/images/train2017/000000184321.jpg'],
            remote_path='/folder_name')
        # Remote path is optional, images will go to the main directory by default

        # DTLPY-STOP
        self.item = item
