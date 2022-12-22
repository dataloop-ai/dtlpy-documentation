# Data Versioning  
Dataloop's powerful data versioning provides you with unique tools for data management - clone, merge, slice & dice your files, to create multiple versions for various applications. Sample use cases include:  
Golden training sets management  
Reproducibility (dataset training snapshot)  
Experimentation (creating subsets from different kinds)  
Task/Assignment management  
Data Version "Snapshot" - Use our versioning feature as a way to save data (items, annotations, metadata) before any major process. For example, a snapshot can serve as a roll-back mechanism to original datasets in case of any error without losing the data.  
  
## Clone Datasets  
Cloning a dataset creates a new dataset with the same files as the original. Files are actually a reference to the original binary and not a new copy of the original, so your cloud data remains safe and protected. When cloning a dataset, you can add a destination dataset, remote file path, and more...  

```python
dataset_id = 'my-dataset-id'
clone_name = 'clone-name'
dataset = project.datasets.get(dataset_id=dataset_id)
dataset_clone = dataset.clone(clone_name=clone_name,
                              filters=None,
                              with_items_annotations=True,
                              with_metadata=True,
                              with_task_annotations_status=True)
```
## Merge Datasets  
Dataset merging outcome depends on how similar or different the datasets are.  
* Cloned Datasets - items, annotations, and metadata will be merged. This means that you will see annotations from different datasets on the same item.  
* Different datasets (not clones) with similar recipes - items will be summed up, which will cause duplication of similar items.  
* Datasets with different recipes - Datasets with different default recipes cannot be merged. Use the 'Switch recipe' option on dataset level (3-dots action button) to match recipes between datasets and be able to merge them.  

```python
dataset_ids = ["dataset-1-id", "dataset-2-id"]
project_ids = ["dataset-1-project-id", "dataset-2-project-id"]
merge_name = 'my_dataset-merge'
dataset_merge = dl.datasets.merge(merge_name=merge_name,
                                  project_ids=project_ids,
                                  dataset_ids=dataset_ids,
                                  with_items_annotations=True,
                                  with_metadata=False,
                                  with_task_annotations_status=False)
```
