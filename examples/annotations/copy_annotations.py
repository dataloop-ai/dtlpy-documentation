def example():
    """
    Copy annotations between items
    :return:
    """
    import dtlpy as dl

    # FROM get the annotations from item
    project = dl.projects.get(project_name=from_project)
    dataset = project.datasets.get(dataset_name=from_dataset)
    item = dataset.items.get(filepath=from_item_filepath)

    # get annotations
    annotations = item.annotations.list()

    # TO post annotations to other item
    project = dl.projects.get(project_name=to_project)
    dataset = project.datasets.get(dataset_name=to_dataset)
    item = dataset.items.get(filepath=to_item_filepath)

    # post
    item.annotations.upload(annotations=annotations)


def preparation():
    ...


if __name__ == "__main__":
    # 1. preparation
    project = dl.create()
    # 2. run
    main()
    # 3. verify - in the tests folder
    # 4.cleanup
