import dtlpy as dl


def func1():
    import dtlpy as dl
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    task = dataset.tasks.get(task_name='task_name')
    assignment = dataset.assignments.get(assignment_name='assignment_name')
    item = dataset.items.get(item_id='my-item-id')
    item.update_status(status=dl.ItemStatus.COMPLETED, task_id=task.id)
    item.update_status(status=dl.ItemStatus.APPROVED, assignment_id=assignment.id)
    item.update_status(status=dl.ItemStatus.DISCARDED)  # this will work if the item is included in only one task


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
    # With filter
    filters = dl.Filters(field='annotated', values=True)
    item_ids = [item.id for item in dataset.items.list(filters=filters).all()]
    # With list of item ids
    item_ids = ['id1', 'id2', 'id3']

    task.set_status(status=dl.ItemStatus.APPROVED, operation='create', items=item_ids)


def func4():
    # Clear status for completed/approved/discarded
    item.update_status(dl.ITEM_STATUS_DISCARDED, task_id=task.id, clear=True)
    item.update_status(dl.ITEM_STATUS_APPROVED, assignment_id=assignment.id, clear=True)
    item.update_status(dl.ITEM_STATUS_COMPLETED, clear=True)  # this will work if the item is included in only one task


def func5():
    # Create annotation task with new statue
    task = dl.tasks.create(
        task_name='<task_name>',
        due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
        assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
        # The items will be divided equally between assignments
        filters=filters,  # filter by folder directory or use other filters,
        available_actions=[dl.ItemAction(action='action_name', display_name='display_name')]  # Task statuses
    )
