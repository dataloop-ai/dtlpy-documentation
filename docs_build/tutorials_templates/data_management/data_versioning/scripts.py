import dtlpy as dl


class Scripts:
    def __init__(self):
        # section1
        self.project = None
        self.dataset = None
        self.clone_name = None
        # section2
        self.dataset_clone = None
        self.merge_name = None
        self.dataset_merge = None

    def section1(self):
        # DTLPY-STOP
        project = getattr(self, 'project', 'project-sdk-tutorial')
        dataset = getattr(self, 'dataset', 'dataset-sdk-tutorial')
        dataset_id = dataset.id
        clone_name = getattr(self, 'clone_name', 'clone-name')
        # DTLPY-START

        dataset = project.datasets.get(dataset_id=dataset_id)
        dataset_clone = dataset.clone(clone_name=clone_name,
                                      filters=None,
                                      with_items_annotations=True,
                                      with_metadata=True,
                                      with_task_annotations_status=True)

        # DTLPY-STOP
        self.dataset_clone = dataset_clone

    def section2(self):
        # DTLPY-STOP
        project = getattr(self, 'project', 'project-sdk-tutorial')
        dataset = getattr(self, 'dataset', 'dataset-sdk-tutorial')
        clone_dataset = getattr(self, 'dataset', 'dataset-sdk-tutorial')

        dataset_ids = [dataset.id, clone_dataset.id]
        project_ids = [project.id, project.id]

        merge_name = getattr(self, 'merge_name', 'my_dataset-merge')
        # DTLPY-START

        dataset_merge = dl.datasets.merge(merge_name=merge_name,
                                          project_ids=project_ids,
                                          dataset_ids=dataset_ids,
                                          with_items_annotations=True,
                                          with_metadata=False,
                                          with_task_annotations_status=False)

        # DTLPY-STOP
        self.dataset_merge = dataset_merge
