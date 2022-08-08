import dtlpy as dl


def func1():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    # Get the project
    project = dl.projects.get(project_name='project_name')
    # Get the dataset
    dataset = project.datasets.get(dataset_name='dataset_name')
    # Get items in pages (100 item per page)
    filters = dl.Filters()
    filters.add(field='filename', values='/your/file/path.mimetype')
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))
    # Go over all item and print the properties
    for page in pages:
        for item in page:
            item.print()


def func2():
    for page in reversed(pages):
        for item in page:
            item.print()


def func3():
    for page in pages.all():
        for item in page:
            item.print()


def func4():
    pages = dataset.annotations.list(filters=filters)
    # Iterate through the annotations - Go over all annotations and print the properties
    for page in pages:
        for annotation in page:
            print(annotation)
