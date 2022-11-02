class Scripts:
    def __init__(self):
        # section1
        self.project_name1 = None
        self.dataset_name1 = None
        self.local_path1 = None
        self.remote_path1 = None
        self.project1 = None
        self.dataset1 = None
        # section2
        self.project_name2 = None
        self.dataset_name2 = None
        self.local_path2 = None
        self.remote_path2 = None


    def section1(self):
        # DTLPY-STOP
        project_name = getattr(self, 'project_name1', 'project_name')
        dataset_name = getattr(self, 'dataset_name1', 'dataset_name')
        local_path = getattr(self, 'local_path1', [[r'C:/home/project/images/John Morris.jpg',
                                                    r'C:/home/project/images/John Benton.jpg',
                                                    r'C:/home/project/images/Liu Jinli.jpg']])
        remote_path = getattr(self, 'remote_path1', '/folder_name')
        # DTLPY-START

        import dtlpy as dl
        if dl.token_expired():
            dl.login()
        project = dl.projects.get(project_name=project_name)
        dataset = project.datasets.get(dataset_name=dataset_name)
        dataset.items.upload(local_path=local_path,
                             remote_path=remote_path)  # Remote path is optional, images will go to the root directory by default

        # DTLPY-STOP
        self.project1 = project
        self.dataset1 = dataset

    def section2(self):
        # DTLPY-STOP
        project_name = getattr(self, 'project_name', 'project_name')
        dataset_name = getattr(self, 'dataset', 'dataset_name')
        local_path = getattr(self, 'local_path', [[r'C:/home/project/images/John Morris.jpg',
                                                   r'C:/home/project/images/John Benton.jpg',
                                                   r'C:/home/project/images/Liu Jinli.jpg']])
        remote_path = getattr(self, 'remote_path', '/folder_name')
        # DTLPY-START
        import dtlpy as dl
        if dl.token_expired():
            dl.login()
        project = dl.projects.get(project_name='project_name')
        dataset = project.datasets.get(dataset_name='dataset_name')
        dataset.items.upload(local_path=r'C:/home/project/images',
                             remote_path='/folder_name')  # Remote path is optional, images will go to the root directory by default

    def section3(self):
        dataset = project.datasets.get(dataset_name='dataset_name')
        url_path = 'http://ww.some_website/beautiful_flower.jpg'
        # Create link
        link = dl.UrlLink(ref=url_path, mimetype='image', name='file_name.jpg')
        # Upload link
        item = dataset.items.upload(local_path=link)

    def section4(self):
        item.open_in_web()

    def section5(self):
        import pandas
        import dtlpy as dl
        dataset = dl.datasets.get(dataset_id='id')  # Get dataset
        to_upload = list()
        # First item and info attached:
        to_upload.append({'local_path': r"E:\TypesExamples\000000000064.jpg",  # Local path to image
                          'local_annotations_path': r"E:\TypesExamples\000000000776.json",
                          # Local path to annotation file
                          'remote_path': "/first",  # Remote directory of uploaded image
                          'remote_name': 'f.jpg',  # Remote name of image
                          'item_metadata': {'user': {'dummy': 'fir'}}})  # Metadata for the created item
        # Second item and info attached:
        to_upload.append({'local_path': r"E:\TypesExamples\000000000776.jpg",  # Local path to image
                          'local_annotations_path': r"E:\TypesExamples\000000000776.json",
                          # Local path to annotation file
                          'remote_path': "/second",  # Remote directory of uploaded image
                          'remote_name': 's.jpg',  # Remote name of image
                          'item_metadata': {'user': {'dummy': 'sec'}}})  # Metadata for the created item
        df = pandas.DataFrame(to_upload)  # Make data into DF table
        items = dataset.items.upload(local_path=df,
                                     overwrite=True)  # Upload DF to platform
