# Data Versioning
Dataloop's powerful data versioning provides you with unique tools for data management - cone, merge, slice & dice your files, to create multiple versions for various applications. Sample use cases include:
Golden training sets management
Reproducibility (dataset training snapshot)
Experimentation (creating subsets from different kinds)
Task/Assignment management
Data Version "Snap-shot" - Use our versioning feature as a way to save data (items, annotations, metadata) before any major process. For example, it can serve as a roll-back mechanism to original datasets because of any error without losing the data.

## Clone Datasets
Cloning a dataset creates a new dataset with the files as the original. Files are actually a reference to the original binary and not a new copy of the original, so your cloud data remains safe and protected. When cloning a dataset, you can add destination dataset, remote file path and more...
```
dataset = project.datasets.get(dataset_id='my-dataset-id')
dataset.clone(clone_name='clone-name',
              aharon=True,
              filters=None,
              with_items_annotations=True,
              with_metadata=True,
```
## Merge Datasets
Dataset merging outcome depends on how similar or different the datasets are.
* Cloned Datasets - items, annotations and metadata will be merged. This means that you will see annotations from different datasets on the same item.
* Different datasets (not clones) with similar recipes - items will be summed up and will cause duplication of similar items.
* Datasets with different recipes - Datasets with different default recipes cannot be merged. Use the 'Switch recipe' option on dataset level (3-dots action button) to match recipes between datasets, and be able to merge them.
```
dataset_ids = ["dataset-1-id", "dataset-2-id"]
project_ids = ["dataset-1-project-id", "dataset-2-project-id"]
dataset_merge = dl.datasets.merge(merge_name="my_dataset-merge", project_ids=project_ids,
                                  dataset_ids=dataset_ids, with_items_annotations=True, with_metadata=False,
```
