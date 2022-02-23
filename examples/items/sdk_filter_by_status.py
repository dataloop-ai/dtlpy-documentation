import datetime

import dtlpy as dl


def filter_by_status(project_name:str,
                     dataset_name:str,
                     task_id:str,
                     status:str,
                     email:str,
                     timestamp:str):
    """
    Function to filter items per task by status, works for all statuses (e.g., approved, completed, discard)
    We show how to create a filter object by creator, status or timestamp.

    :param project_name: dl.Project name
    :param dataset_name: dl.Dataset name
    :param task_id: dl.Task id of the task to filter by
    :param status: filter option - filter by the status of the item: 'completed', 'approved', 'discarded', or any custom status created by the task creator (e.g., 'expert review').
    :param email: filter option - email of person who created the status
    :param timestamp: filter option - ISO format time to filter by. operators: dl.FiltersOperations.GREATER_THAN, dl.FiltersOperations.LESS_THAN
    :return:
    """

    # Get project and dataset
    project = dl.projects.get(project_name=project_name)
    dataset = project.datasets.get(dataset_name=dataset_name)
    # Create filters instance
    filters = dl.Filters()
    # Filter all approved items per task, values can be any status - "completed", "approved", "discard"
    filters.add(
        field='metadata.system.refs',
        values={
            "id": task_id,
            "type": "task",
            "metadata":
                {
                    "status": {'${}'.format(dl.FiltersOperations.EQUAL): status},
                    "creator": email,
                    "timestamp": {'${}'.format(dl.FiltersOperations.GREATER_THAN): timestamp}
                }
        },
        operator=dl.FiltersOperations.MATCH
    )
    # Optional: You can also filter by annotation type and sort the results
    # AND filter items by their annotations - for example, only items with 'box' annotations
    # As a result, you will get approved items with 'box' annotations
    filters.add_join(field='type', values='box')
    # Return results sorted by descending creation date
    filters.sort_by(field=dl.FILTERS_KNOWN_FIELDS_CREATED_AT, value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)

    # Get filtered item list in a page object
    pages = dataset.items.list(filters=filters)
    # Count the items
    print('Number of filtered items in dataset: {}'.format(pages.items_count))
    # Iterate through the items - go over all items and print the properties
    for page in pages:
        for item in page:
            item.print()

    return pages


if __name__ == "__main__":
    project_name = "My Project"
    dataset_name = "My Dataset"
    task_id = "Task Id"
    status = "approved"
    email = "pinky@looneytunes.ai"
    timestamp = datetime.datetime(year=2022, month=1, day=1).isoformat()

    filter_by_status(project_name=project_name,
                     dataset_name=dataset_name,
                     task_id=task_id,
                     status=status,
                     email=email,
                     timestamp=timestamp)
