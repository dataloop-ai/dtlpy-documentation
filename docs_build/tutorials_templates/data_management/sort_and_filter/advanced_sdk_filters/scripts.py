def section1():
    import dtlpy as dl
    # Get project and dataset
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    # Create filters instance
    filters = dl.Filters()
    # Filter only items from a specific folder directory
    filters.add(field='dir', values='/DatasetFolderName', operator=dl.FILTERS_OPERATIONS_EQUAL)
    # optional - return results sorted by ascending file name 
    filters.sort_by(field='filename')
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section2():
    filters = dl.Filters()
    # Filter ONLY a cat label
    filters.add_join(field='label', values='cat', operator=dl.FILTERS_OPERATIONS_NOT_EQUAL)
    # optional - return results sorted by ascending file name 
    filters.sort_by(field='filename')
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in the dataset: {}'.format(pages.items_count))


def section3():
    filters = dl.Filters()
    # Filter images with a bigger height size
    filters.add(field='metadata.system.height', values=height_number_in_pixels,
                operator=dl.FILTERS_OPERATIONS_GREATER_THAN)
    # optional - return results sorted by ascending file name 
    filters.sort_by(field='filename')
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section4():
    filters = dl.Filters()
    # Filter images with a bigger height size
    filters.add(field='metadata.system.width', values=width_number_in_pixels, operator=dl.FILTERS_OPERATIONS_LESS_THAN)
    # optional - return results sorted by ascending file name 
    filters.sort_by(field='filename')
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section5():
    filters = dl.Filters()
    # Filter items with dog OR cat labels
    filters.add_join(field='label', values=['dog', 'cat'], operator=dl.FILTERS_OPERATIONS_IN)
    # optional - return results sorted by ascending file name 
    filters.sort_by(field='filename')
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section6():
    filters = dl.Filters(use_defaults=False)


def section7():
    filters = dl.Filters()
    filters.add(field='type', values='dir')
    # or
    filters.pop(field='type')


def section8():
    filters = dl.Filters()
    # For example, if you added the following filter:
    filters.add(field='to-delete-field', values='value')
    # Use this command to delete the filter
    filters.pop(field='to-delete-field')
    # or for items by their annotations
    filters.pop_join(field='to-delete-annotation-field')


def section9():
    import datetime
    # To filter absolute date (between 2-3, May 2024) use datetime directly
    earlier_timestamp = datetime.datetime(year=2024, month=5, day=2, hour=0, minute=0, second=0).isoformat()
    later_timestamp = datetime.datetime(year=2024, month=5, day=3, hour=0, minute=0, second=0).isoformat()

    # To filter relative time filtering, you'll need use utc time.
    # The following example will give only items uploaded in the last hour
    earlier_timestamp = (datetime.datetime.utcnow() - datetime.timedelta(hours=1)).isoformat()
    later_timestamp = datetime.datetime.utcnow().isoformat()

    # now we can construct the filter and send the request
    filters = dl.Filters()
    filters.add(field='createdAt', values=earlier_timestamp, operator=dl.FiltersOperations.GREATER_THAN)
    filters.add(field='createdAt', values=later_timestamp, operator=dl.FiltersOperations.LESS_THAN)
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of items in dataset: {}'.format(pages.items_count))


def section10():
    # Get all items
    all_items = set([item.id for item in dataset.items.list().all()])

    # Get all items WITH the label cat
    filters = dl.Filters()
    filters.add_join(field='label', values='cat')
    cat_items = set([item.id for item in dataset.items.list(filters=filters).all()])

    # Get the difference between the sets. This will give you a list of the items with no cat
    no_cat_items = all_items.difference(cat_items)

    print('Number of filtered items in dataset: {}'.format(len(no_cat_items)))
    # Iterate through the ID's  - Go over all ID's and print the matching item
    for item_id in no_cat_items:
        print(dataset.items.get(item_id=item_id))

def section11():
    filters = dl.Filters()
    filters.add(field='metadata.user', values=True, operator=dl.FILTERS_OPERATIONS_EXISTS)
    dataset.items.list(filters=filters)