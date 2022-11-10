import dtlpy as dl


class Scripts:
    def __init__(self):
        # section1
        self.project_name1 = None
        self.dataset_name1 = None
        self.local_path_item1 = None
        self.local_path_item2 = None
        self.local_path_item3 = None
        self.remote_path1 = None
        self.project1 = None
        self.dataset1 = None
        # section2
        self.project_name2 = None
        self.dataset_name2 = None
        self.local_path2 = None
        self.remote_path2 = None
        # section3
        self.project3 = None
        self.dataset_name3 = None
        self.file_name3 = None
        self.link3 = None
        self.item3 = None
        # section4
        self.item4 = None
        # section 5
        self.dataset_id5 = None
        self.first_local_path5 = None
        self.first_local_annotations_path5 = None
        self.second_local_path5 = None
        self.second_local_annotations_path5 = None
        self.items5 = None

    def section1(self):
        # DTLPY-STOP
        project_name = getattr(self, 'project_name1', 'project_name')
        dataset_name = getattr(self, 'dataset_name1', 'dataset_name')
        local_path_item1 = getattr(self, 'local_path_item1', r'C:/home/project/images/John Morris.jpg')
        local_path_item2 = getattr(self, 'local_path_item2', r'C:/home/project/images/John Benton.jpg')
        local_path_item3 = getattr(self, 'local_path_item3', r'C:/home/project/images/Liu Jinli.jpg')
        remote_path = getattr(self, 'remote_path1', '/folder_name')
        # DTLPY-START

        import dtlpy as dl
        if dl.token_expired():
            dl.login()
        project = dl.projects.get(project_name=project_name)
        dataset = project.datasets.get(dataset_name=dataset_name)
        dataset.items.upload(local_path=[local_path_item1, local_path_item2, local_path_item3],
                             remote_path=remote_path)  # Remote path is optional, images will go to the root directory by default

        # DTLPY-STOP
        self.project1 = project
        self.dataset1 = dataset

    def section2(self):
        # DTLPY-STOP
        project_name = getattr(self, 'project_name2', 'project_name')
        dataset_name = getattr(self, 'dataset_name2', 'dataset_name')
        local_path = getattr(self, 'local_path2', r'C:/home/project/images')
        remote_path = getattr(self, 'remote_path2', '/folder_name')
        # DTLPY-START

        import dtlpy as dl
        if dl.token_expired():
            dl.login()
        project = dl.projects.get(project_name=project_name)
        dataset = project.datasets.get(dataset_name=dataset_name)
        dataset.items.upload(local_path=local_path,
                             remote_path=remote_path)  # Remote path is optional, images will go to the root directory by default

    def section3(self):
        # DTLPY-STOP
        project = getattr(self, 'project3', 'project')
        dataset_name = getattr(self, 'dataset_name3', 'dataset_name')
        file_name = getattr(self, 'file_name3', 'file_name.jpg')
        # DTLPY-START

        dataset = project.datasets.get(dataset_name=dataset_name)
        url_path = 'http://ww.some_website/beautiful_flower.jpg'
        # Create link
        link = dl.UrlLink(ref=url_path, mimetype='image', name=file_name)
        # Upload link
        item = dataset.items.upload(local_path=link)

        # DTLPY-STOP
        self.link3 = link
        self.item3 = item

    def section4(self):
        # DTLPY - STOP
        item = getattr(self, 'item4', 'item')
        # DTLPY-START

        item.open_in_web()

    def section5(self):
        # DTLPY - STOP
        dataset_id = getattr(self, 'dataset_id5', 'id')
        ''' First item and info attached: '''
        local_path1 = getattr(self, 'first_local_path5', r"E:\TypesExamples\000000000064.jpg")
        local_annotations_path1 = getattr(self, 'first_local_annotations_path5', r"E:\TypesExamples\000000000776.json")
        ''' Second item and info attached: '''
        local_path2 = getattr(self, 'second_local_path5', r"E:\TypesExamples\000000000776.jpg")
        local_annotations_path2 = getattr(self, 'second_local_annotations_path5', r"E:\TypesExamples\000000000776.json")
        # DTLPY-START

        import pandas
        import dtlpy as dl
        dataset = dl.datasets.get(dataset_id=dataset_id)  # Get dataset
        to_upload = list()
        # First item and info attached:
        to_upload.append({'local_path': local_path1,  # Local path to image
                          'local_annotations_path': local_annotations_path1,  # Local path to annotation file
                          'remote_path': "/first",  # Remote directory of uploaded image
                          'remote_name': 'f.jpg',  # Remote name of image
                          'item_metadata': {'user': {'dummy': 'fir'}}})  # Metadata for the created item
        # Second item and info attached:
        to_upload.append({'local_path': local_path2,  # Local path to image
                          'local_annotations_path': local_annotations_path2,  # Local path to annotation file
                          'remote_path': "/second",  # Remote directory of uploaded image
                          'remote_name': 's.jpg',  # Remote name of image
                          'item_metadata': {'user': {'dummy': 'sec'}}})  # Metadata for the created item
        df = pandas.DataFrame(to_upload)  # Make data into DF table
        items = dataset.items.upload(local_path=df,
                                     overwrite=True)  # Upload DF to platform

        # DTLPY - STOP
        self.items5 = items
