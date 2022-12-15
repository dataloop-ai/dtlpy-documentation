import dtlpy as dl


class Scripts:
    def __init__(self):
        # section1
        self.project_name1 = None
        self.dataset_name1 = None
        # section2

        # section3

        # section4

        # section5

        # section6

        # section7

        # section8

        # section9

        # section10

        # section11

        # section12

        # section13

        # section14

        # section15


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

        item.metadata['user']['MyKey'] = 'MyValue'
        annotation.metadata['user']['MyKey'] = 'MyValue'

    def section3(self):
        # DTLPY-STOP
        item = self.item3
        annotation = self.annotation3
        # DTLPY-START

        item.metadata['user']['MyKey'] = 3
        annotation.metadata['user']['MyKey'] = 3

    def section4(self):
        # DTLPY-STOP
        item = self.item3
        annotation = self.annotation3
        # DTLPY-START

        item.metadata['user']['MyKey'] = True
        annotation.metadata['user']['MyKey'] = True

    def section5(self):
        # DTLPY-STOP
        item = self.item5
        annotation = self.annotation5
        # DTLPY-START

        item.metadata['user']['MyKey'] = None
        annotation.metadata['user']['MyKey'] = None

    def section6(self):
        # DTLPY-STOP
        item = self.item6
        annotation = self.annotation6
        # DTLPY-START

        # add metadata of a list (can contain elements of different types).
        item.metadata['user']['MyKey'] = ["A", 2, False]
        annotation.metadata['user']['MyKey'] = ["A", 2, False]

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
        annotation_id = self.annotation_id8
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
        self.filters12 = filters

    def section13(self):
        # DTLPY-STOP
        filters = self.filters13
        # DTLPY-START

        filters.add(field='metadata.user.Key', values='Value')

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
