import dtlpy as dl


def section1():
    dataset = project.datasets.get(dataset_id='my-dataset-id')
    dataset.clone(clone_name='clone-name',
                  filters=None,
                  with_items_annotations=True,
                  with_metadata=True,
                  with_task_annotations_status=True)


def section2():
    dataset_ids = ["dataset-1-id", "dataset-2-id"]
    project_ids = ["dataset-1-project-id", "dataset-2-project-id"]
    dataset_merge = dl.datasets.merge(merge_name="my_dataset-merge",
                                      project_ids=project_ids,
                                      dataset_ids=dataset_ids,
                                      with_items_annotations=True,
                                      with_metadata=False,
                                      with_task_annotations_status=False)
