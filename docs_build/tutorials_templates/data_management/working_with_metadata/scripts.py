def section1():
    import dtlpy as dl
    # Get project and dataset
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')


def section2():
    item.metadata['user']['MyKey'] = 'MyValue'
    annotation.metadata['user']['MyKey'] = 'MyValue'


def section3():
    item.metadata['user']['MyKey'] = 3
    annotation.metadata['user']['MyKey'] = 3


def section4():
    item.metadata['user']['MyKey'] = True
    annotation.metadata['user']['MyKey'] = True


def section5():
    item.metadata['user']['MyKey'] = None
    annotation.metadata['user']['MyKey'] = None


def section6():
    # add metadata of a list (can contain elements of different types).
    item.metadata['user']['MyKey'] = ["A", 2, False]
    annotation.metadata['user']['MyKey'] = ["A", 2, False]


def section7():
    item.metadata['user']['MyKey'].append(3)
    item = item.update()
    annotation.metadata['user']['MyKey'].append(3)
    annotation = annotation.update()


def section8():
    # upload and claim item
    item = dataset.items.upload(local_path=r'C:/home/project/images/item.mimetype')
    # or get item
    item = dataset.items.get(item_id='write-your-id-number')
    # modify metadata
    item.metadata['user'] = dict()
    item.metadata['user']['MyKey'] = 'MyValue'
    # update and reclaim item
    item = item.update()


def section9():
    # Get annotation
    annotation = dl.annotations.get(annotation_id='my-annotation-id')
    # modify metadata
    annotation.metadata['user'] = dict()
    item.metadata['user']['red'] = True
    # update and reclaim annotation
    annotation = annotation.update()


def section10():
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')


def section11():
    # upload and claim item
    item = dataset.items.upload(local_path=r'C:/home/project/images/item.mimetype')
    # or get item
    item = dataset.items.get(item_id='write-your-id-number')
    # modify metadata
    item.metadata['user'] = dict()
    item.metadata['user']['MyKey'] = 'MyValue'
    # update and reclaim item
    item = item.update()


def section12():
    filters = dl.Filters()
    # set resource - optional - default is item
    filters.resource = dl.FiltersResource.ITEM


def section13():
    filters.add(field='metadata.user.Key', values='Value')


def section14():
    pages = dataset.items.list(filters=filters)
    # Go over all item and print the properties
    for page in pages:
        for item in page:
            item.print()


def section15():
    # upload and claim item
    item = dataset.items.upload(local_path=r'C:/home/project/images/item.mimetype')
    # or get item
    item = dataset.items.get(item_id='write-your-id-number')
    # modify metadata
    if 'user' not in item.metadata:
        item.metadata['user'] = dict()
    item.metadata['user']['MyKey'] = 'MyValue'
    # update and reclaim item
    item = item.update()
