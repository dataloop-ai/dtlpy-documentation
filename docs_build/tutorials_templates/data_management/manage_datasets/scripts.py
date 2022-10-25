import dtlpy as dl


def section1(project, dataset_name):
    """
    Required parameters:

    :param dl.Project project:
    :param str dataset_name: 'my-dataset-name'
    """

    dataset = project.datasets.create(dataset_name=dataset_name)


def section2(project_name, driver, dataset_name):
    """
    Required parameters:

    :param str project_name: 'my-project-name'
    :param str driver: 'my-dataset-name'
    :param str dataset_name: 'dataset_name'
    """

    project = dl.projects.get(project_name=project_name)
    # Get your drivers list
    project.drivers.list().print()
    # Create a dataset from a driver name. You can also create by the driver ID.
    dataset = project.datasets.create(driver=driver, dataset_name=dataset_name)


def section3(project, dataset_id):
    """
    Required parameters:

    :param dl.Project project:
    :param str dataset_id: 'my-dataset-id'
    """

    datasets = project.datasets.list()
    dataset = project.datasets.get(dataset_id=dataset_id)


def section4(dataset, directory):
    """
    Required parameters:

    :param dl.Dataset dataset:
    :param str directory: "/directory/name"
    """

    dataset.items.make_dir(directory=directory)


def section5(source_folder, destination_folder, source_project_name, source_dataset_name, destination_project_name, destination_dataset_name):
    """
    Required parameters:

    :param str source_folder: '/source_folder'
    :param str destination_folder: '/destination_folder'
    :param str source_project_name: 'source_project_name'
    :param str source_dataset_name: 'source_dataset_name'
    :param str destination_project_name: 'destination_project_name'
    :param str destination_dataset_name: 'destination_dataset_name'
    """

    copy_annotations = True
    flat_copy = False  # if true, it copies all dir files and sub dir files to the destination folder without sub directories
    # Get source project dataset
    project = dl.projects.get(project_name=source_project_name)
    dataset_from = project.datasets.get(dataset_name=source_dataset_name)
    source_folder = source_folder.rstrip('/')
    # Filter to get all files of a specific folder
    filters = dl.Filters()
    filters.add(field='filename', values=source_folder + '/**')  # Get all items in folder (recursive)
    pages = dataset_from.items.list(filters=filters)
    # Get destination project and dataset
    project = dl.projects.get(project_name=destination_project_name)
    dataset_to = project.datasets.get(dataset_name=destination_dataset_name)
    # Go over all projects and copy file from src to dst
    for page in pages:
        for item in page:
            # Download item (without save to disk)
            buffer = item.download(save_locally=False)
            # Give the item's name to the buffer
            if flat_copy:
                buffer.name = item.name
            else:
                buffer.name = item.filename[len(source_folder) + 1:]
            # Upload item
            print("Going to add {} to {} dir".format(buffer.name, destination_folder))
            new_item = dataset_to.items.upload(local_path=buffer, remote_path=destination_folder)
            if not isinstance(new_item, dl.Item):
                print('The file {} could not be upload to {}'.format(buffer.name, destination_folder))
                continue
            print("{} has been uploaded".format(new_item.filename))
            if copy_annotations:
                new_item.annotations.upload(item.annotations.list())
