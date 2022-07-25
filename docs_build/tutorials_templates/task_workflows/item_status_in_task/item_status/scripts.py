import dtlpy as dl


def func1():
    import dtlpy as dl
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    item = dataset.items.get(item_id='my-item-id')
    item.update_status(status=dl.ItemStatus.COMPLETED)
    item.update_status(status=dl.ItemStatus.APPROVED)
    item.update_status(status=dl.ItemStatus.DISCARDED)


def func2():
    filters = dl.Filters(field='annotated', values=True)
    items = dataset.items.list(filters=filters)
    dataset.items.update_status(status=dl.ItemStatus.APPROVED, items=items)
    # With filters
    filters = dl.Filters(field='annotated', values=True)
    dataset.items.update_status(status=dl.ItemStatus.DISCARDED, filters=filters)
    # With list of item ids
    item_ids = ['id1', 'id2', 'id3']
    dataset.items.update_status(status=dl.ItemStatus.COMPLETED, item_ids=item_ids)


def func3():
    # Clear status for completed/approved/discarded
    item.update_status(dl.ITEM_STATUS_COMPLETED, clear=True)


def func4():
    ...
