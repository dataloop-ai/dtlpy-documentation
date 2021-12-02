import dtlpy as dl

dataset_id = ''
annotations_path = r''

# make sure they have the same hierarchy
dataset = dl.datasets.get(dataset_id=dataset_id)
# clean: bool - if True it remove the old annotations
# remote_root_path: str - the remote root path to match remote and local items
dataset.upload_annotations(local_path=annotations_path, clean=False, remote_root_path='/')
