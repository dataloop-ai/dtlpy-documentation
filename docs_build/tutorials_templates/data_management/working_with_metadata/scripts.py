import dtlpy as dl


class Scripts:
    def __init__(self):
        # section1
        self.project_name1 = None
        self.dataset_name1 = None
        # section2
        self.item2 = None
        self.annotation2 = None
        # section3
        self.item3 = None
        self.annotation3 = None
        # section4
        self.item4 = None
        self.annotation4 = None
        # section5
        self.item5 = None
        self.annotation5 = None
        # section6
        self.item6 = None
        self.annotation6 = None
        # section7
        self.item7 = None
        self.annotation7 = None
        # section8
        self.dataset8 = None
        self.local_path8 = None
        self.item_id8 = None
        # section9
        self.annotation_id9 = None
        # section10
        self.project_name10 = None
        self.dataset_name10 = None
        # section11
        self.dataset11 = None
        self.local_path11 = None
        self.item_id11 = None
        # section12
        # NO VARIABLES REQUIRED
        # section13
        self.filters13 = None
        # section14
        self.dataset14 = None
        self.filters14 = None
        # section15
        self.dataset15 = None
        self.local_path15 = None
        self.item_id15 = None

    def section1(self):
        import dtlpy as dl

        project_name = 'project_name'
        dataset_name = 'dataset_name'

        # DTLPY-STOP
        project_name = self.project_name1
        dataset_name = self.dataset_name1
        # DTLPY-START

        # Get project and dataset
        project = dl.projects.get(project_name=project_name)
        dataset = project.datasets.get(dataset_name=dataset_name)

    def section2(self):
        # DTLPY-STOP
        item = self.item2
        annotation = self.annotation2
        # DTLPY-START

        item.metadata['user'] = {}
        item.metadata['user']['MyKey'] = 'MyValue'
        annotation.metadata['user']['MyKey'] = 'MyValue'
        item = item.update()
        annotation = annotation.update()

    def section3(self):
        # DTLPY-STOP
        item = self.item3
        annotation = self.annotation3
        # DTLPY-START

        item.metadata['user']['MyKey'] = 3
        annotation.metadata['user']['MyKey'] = 3
        item = item.update()
        annotation = annotation.update()

    def section4(self):
        # DTLPY-STOP
        item = self.item4
        annotation = self.annotation4
        # DTLPY-START

        item.metadata['user']['MyKey'] = True
        annotation.metadata['user']['MyKey'] = True
        item = item.update()
        annotation = annotation.update()

    def section5(self):
        # DTLPY-STOP
        item = self.item5
        annotation = self.annotation5
        # DTLPY-START

        item.metadata['user']['MyKey'] = None
        annotation.metadata['user']['MyKey'] = None
        item = item.update()
        annotation = annotation.update()

    def section6(self):
        # DTLPY-STOP
        item = self.item6
        annotation = self.annotation6
        # DTLPY-START

        # add metadata of a list (can contain elements of different types).
        item.metadata['user']['MyKey'] = ["A", 2, False]
        annotation.metadata['user']['MyKey'] = ["A", 2, False]
        item = item.update()
        annotation = annotation.update()

    def section7(self):
        # DTLPY-STOP
        item = self.item7
        annotation = self.annotation7
        # DTLPY-START

        item.metadata['user']['MyKey'].append(3)
        item = item.update()
        annotation.metadata['user']['MyKey'].append(3)
        annotation = annotation.update()

    def section8(self):
        local_path = r'C:/home/project/images/item.mimetype'
        item_id = 'write-your-id-number'

        # DTLPY-STOP
        dataset = self.dataset8
        local_path = self.local_path8
        item_id = self.item_id8
        # DTLPY-START

        # upload and claim item
        item = dataset.items.upload(local_path=local_path)
        # or get item
        item = dataset.items.get(item_id=item_id)
        # modify metadata
        item.metadata['user'] = dict()
        item.metadata['user']['MyKey'] = 'MyValue'
        # update and reclaim item
        item = item.update()

    def section9(self):
        annotation_id = 'my-annotation-id'

        # DTLPY-STOP
        annotation_id = self.annotation_id9
        # DTLPY-START

        # Get annotation
        annotation = dl.annotations.get(annotation_id=annotation_id)
        # modify metadata
        annotation.metadata['user'] = dict()
        annotation.metadata['user']['red'] = True
        # update and reclaim annotation
        annotation = annotation.update()

    def section10(self):
        project_name = 'project_name'
        dataset_name = 'dataset_name'

        # DTLPY-STOP
        project_name = self.project_name10
        dataset_name = self.dataset_name10
        # DTLPY-START

        project = dl.projects.get(project_name=project_name)
        dataset = project.datasets.get(dataset_name=dataset_name)

    def section11(self):
        local_path = r'C:/home/project/images/item.mimetype'
        item_id = 'write-your-id-number'

        # DTLPY-STOP
        dataset = self.dataset11
        local_path = self.local_path11
        item_id = self.item_id11
        # DTLPY-START

        # upload and claim item
        item = dataset.items.upload(local_path=local_path)
        # or get item
        item = dataset.items.get(item_id=item_id)
        # modify metadata
        item.metadata['user'] = dict()
        item.metadata['user']['MyKey'] = 'MyValue'
        # update and reclaim item
        item = item.update()

    def section12(self):
        filters = dl.Filters()
        # set resource - optional - default is item
        filters.resource = dl.FiltersResource.ITEM

        # DTLPY-STOP
        self.filters13 = filters

    def section13(self):
        # DTLPY-STOP
        filters = self.filters13
        # DTLPY-START

        filters.add(field='metadata.user.Key', values='Value')

        # DTLPY-STOP
        self.filters14 = filters

    def section14(self):
        # DTLPY-STOP
        dataset = self.dataset14
        filters = self.filters14
        # DTLPY-START

        pages = dataset.items.list(filters=filters)
        # Go over all item and print the properties
        for page in pages:
            for item in page:
                item.print()

    def section15(self):
        local_path = r'C:/home/project/images/item.mimetype'
        item_id = 'write-your-id-number'

        # DTLPY-STOP
        dataset = self.dataset15
        local_path = self.local_path15
        item_id = self.item_id15
        # DTLPY-START

        # upload and claim item
        item = dataset.items.upload(local_path=local_path)
        # or get item
        item = dataset.items.get(item_id=item_id)
        # modify metadata
        if 'user' not in item.metadata:
            item.metadata['user'] = dict()
        item.metadata['user']['MyKey'] = 'MyValue'
        # update and reclaim item
        item = item.update()
