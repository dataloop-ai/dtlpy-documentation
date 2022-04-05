import dtlpy as dl


def func1():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name>')


def func2():
    # Mark single item as completed
    item = dataset.items.get(item_id='<my-item-id>')
    item.update_status(status=dl.ItemStatus.COMPLETED)
    # In the same way you can update to another status
    item.update_status(status=dl.ItemStatus.APPROVED)
    item.update_status(status=dl.ItemStatus.DISCARDED)

def func3():
    # Clear status for completed/approved/discarded
    item.update_status(dl.ITEM_STATUS_COMPLETED, clear=True)

def func4():
    # With items list
    filters = dl.Filters(field='<annotated>', values=True)
    items = dataset.items.list(filters=filters)
    dataset.items.update_status(status=dl.ItemStatus.APPROVED, items=items)
    # With filters
    filters = dl.Filters(field='<annotated>', values=True)
    dataset.items.update_status(status=dl.ItemStatus.DISCARDED, filters=filters)
    # With list of item ids
    item_ids = ['<id1>', '<id2>', '<id3>']
    dataset.items.update_status(status=dl.ItemStatus.COMPLETED, item_ids=item_ids)


def func5():
    task = dataset.tasks.get(task_name='<my-task-name>')
    dataset.items.update_status(status=dl.ItemStatus.COMPLETED, items=task.get_items())
