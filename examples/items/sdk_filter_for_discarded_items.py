def filter_by_status():
    """
    Function to filter items ber task by status, works for all status approved, completed, discard
    """
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    # Get project and dataset
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    task_id = 'task_id'
    # Create filters instance
    filters = dl.Filters()
    # Filter all approved items ber task, values can be any status - "completed", "done", "discard"
    item_status = "approved"
    filters.add(
        field='metadata.system.refs',
        values={
            "id": task_id,
            "type": "task",
            "metadata":
                {
                    "status":
                        {
                            '$' + dl.FiltersOperations.EQUAL: item_status
                        }
                }
        },
        operator=dl.FiltersOperations.MATCH
    )
    # AND filter items by their annotation - only items with 'box' annotations
    # Meaning you will get approved items with 'box' annotations
    filters.add_join(field='type', values='box')
    # optional - return results sorted by descending creation date
    filters.sort_by(field=dl.FILTERS_KNOWN_FIELDS_CREATED_AT, value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
    # Get filtered items list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of filtered items in dataset: {}'.format(pages.items_count))
    # Iterate through the items - Go over all item and print the properties
    for page in pages:
        for item in page:
            item.print()
