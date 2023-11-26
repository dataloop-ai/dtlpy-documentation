import dtlpy as dl


class Scripts:
    def __init__(self):
        # section1
        self.project = None
        self.dataset_id = None
        self.clone_name = None
        # section2
        self.dataset = None
        self.dataset_clone = None
        self.merge_name = None
        self.dataset_merge = None

    def section1(self):
        dataset_id = 'my-dataset-id'
        clone_name = 'clone-name'

        # DTLPY-STOP
        project = self.project
        dataset_id = self.dataset_id
        clone_name = self.clone_name
        # DTLPY-START

        dataset = project.datasets.get(dataset_id=dataset_id)
        dataset_clone = dataset.clone(clone_name=clone_name,
                                      filters=dl.Filters(field='dir', values='/only-this-folder'),
                                      with_items_annotations=True,
                                      with_metadata=True)

        # DTLPY-STOP
        self.dataset_clone = dataset_clone

    def section2(self):
        dataset_ids = ["dataset-1-id", "dataset-2-id"]
        project_ids = ["dataset-1-project-id", "dataset-2-project-id"]
        merge_name = 'my_dataset-merge'

        # DTLPY-STOP
        project = self.project
        dataset = self.dataset
        clone_dataset = self.dataset_clone

        dataset_ids = [dataset.id, clone_dataset.id]
        project_ids = [project.id, project.id]

        merge_name = self.merge_name
        # DTLPY-START

        dataset_merge = dl.datasets.merge(merge_name=merge_name,
                                          project_ids=project_ids,
                                          dataset_ids=dataset_ids,
                                          with_items_annotations=True,
                                          with_metadata=False)

        # DTLPY-STOP
        self.dataset_merge = dataset_merge
