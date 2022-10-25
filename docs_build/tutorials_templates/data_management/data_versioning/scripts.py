import dtlpy as dl


def section1(project, dataset_id, clone_name):
    """
    Required parameters:

    :param dl.Project project:
    :param str dataset_id: 'my-dataset-id'
    :param set clone_name: 'clone-name'
    """
    dataset = project.datasets.get(dataset_id=dataset_id)
    dataset.clone(clone_name=clone_name,
                  filters=None,
                  with_items_annotations=True,
                  with_metadata=True,
                  with_task_annotations_status=True)


def section2(dataset_ids, project_ids, merge_name):
    """
    Required parameters:

    :param dataset_ids = ["dataset-1-id", "dataset-2-id"]
    :param project_ids: ["dataset-1-project-id", "dataset-2-project-id"]
    :param merge_name: "my_dataset-merge"
    """
    dataset_merge = dl.datasets.merge(merge_name=merge_name,
                                      project_ids=project_ids,
                                      dataset_ids=dataset_ids,
                                      with_items_annotations=True,
                                      with_metadata=False,
                                      with_task_annotations_status=False)
