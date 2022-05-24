import datetime

import dtlpy as dl


def filter_by_status(project_name: str,
                     dataset_name: str,
                     task_id: str,
                     status: list,
                     email: str,
                     greater_than: str,
                     less_than: str):
    """
    Function to filter items per task by status, works for all statuses (e.g., approved, completed, discard)
    We show how to create a filter object by creator, status or timestamp.

    :param project_name: dl.Project name
    :param dataset_name: dl.Dataset name
    :param task_id: dl.Task id of the task to filter by
    :param status: filter option (list)- filter by the status of the item: 'completed', 'approved', 'discarded', or any custom status created by the task creator (e.g., 'expert review').
    :param email: filter option - email of person who created the status
    :param greater_than: filter option - ISO format time to filter by. operators: dl.FiltersOperations.GREATER_THAN
    :param less_than: filter option - ISO format time to filter by. operators: dl.FiltersOperations.LESS_THAN
    :return:
    """

    # Get project and dataset
    project = dl.projects.get(project_name=project_name)
    dataset = project.datasets.get(dataset_name=dataset_name)
    # Create filters instance
    filters = dl.Filters()
    # Add filter options for tasks and assignments
    filters.add(
        field='metadata.system.refs',
        values={
            "id": task_id,  # Task id key can be omitted (and will return all tasks), or can be a list of tasks
            "type": "task", # Type can be "task" or "assignment"
            "metadata":
                {
                    "status": {'${}'.format(dl.FiltersOperations.IN): status},
                    # Status can also be used with dl.FiltersOperations.EXISTS to get any status or if there is no status at all
                    # "status": {'${}'.format(dl.FiltersOperations.EXISTS): True},
                    "creator": email,
                    "timestamp": {'${}'.format(dl.FiltersOperations.GREATER_THAN): greater_than,
                                  '${}'.format(dl.FiltersOperations.LESS_THAN): less_than}
                }
        },
        operator=dl.FiltersOperations.MATCH
    )
    # Optional: You can also filter by annotation type and sort the results
    # AND filter items by their annotations - for example, only items with 'box' annotations
    # As a result, you will get approved items with 'box' annotations
    filters.add_join(field='type', values='box')
    # Return results sorted by descending creation date
    filters.sort_by(field='createdAt', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)

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
    status = ["completed", "approved"]
    email = "pinky@looneytunes.ai"
    greater_than = datetime.datetime(year=2022, month=1, day=1).isoformat()
    less_than = datetime.datetime(year=2022, month=2, day=28).isoformat()

    filter_by_status(project_name=project_name,
                     dataset_name=dataset_name,
                     task_id=task_id,
                     status=status,
                     email=email,
                     greater_than=greater_than,
                     less_than=less_than)
