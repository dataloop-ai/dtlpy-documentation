import dtlpy as dl


def func1():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')


def func2():
    # Mark a single annotation with an open issue
    item = dataset.items.get(item_id='my-item-id')
    annotation = item.annotations.get(annotation_id='your-annotation-id-number')
    annotation.update_status(dl.AnnotationStatus.ISSUE)
    # In the same way you can update to another status
    annotation.update_status(dl.AnnotationStatus.APPROVED)
    annotation.update_status(dl.AnnotationStatus.REVIEW)
    annotation.update_status(dl.AnnotationStatus.CLEAR) # Have the annotation without status

def func3():
    # Get Task
    task = project.tasks.get(task_id='my_task_id')
    #Add filters for items in the task who have annotations with issues
    filters = dl.Filters()
    filters.add_join(field='metadata.system.status', values='issue')
    items = task.get_items(filters=filters)
    #Go over all of the items
    for page in items:
        for item in page:
            #Add filter for annotations with issues
            filters = dl.Filters()
            filters.resource = dl.FiltersResource.ANNOTATION
            filters.add(field='metadata.system.status', values='issue')
            annotations = item.annotations.list(filters=filters)
            #For every annotation that has issue in the item update the status to "for review"
            for annotation in annotations:           annotation.update_status(dl.AnnotationStatus.REVIEW)