## Data versioning
Data versioning is critical for big data and data-centric AI & analytics applications to be effective. When files are added, removed, or modified in a dataset, version control keeps track of the changes so that users can see how the data was changed, what changed, and who made the changes. This is important for a variety of reasons, from providing important insights for analytics and data-driven decision making, to enabling you to revert changes made to the dataset that reduced the performance of the AI model you trained.

Dataloop provides data [versioning tools](https://dataloop.ai/docs/clone-merge-dataset?highlight=clone) to manage your data that you can use for:
1. Golden training sets management;
2. [Reproducibility](https://en.wikipedia.org/wiki/Reproducibility);
3. Rxperimentation;
4. Task and assignment management.

To get started with data versioning, you must first "get" the dataset you want to version.

We already done this in the dataset chapter. But as a reminder, this is how you "get" a dataset you previously created:

```python
dataset = project.datasets.get(dataset_id='dataset_id')
```
After you've confirmed that you've chosen the correct dataset, you can make a "clone" of it. Cloning a dataset results in the creation of a new dataset that contains the same files as the original. Files are actually a reference to the original binary rather than a new copy of the original, ensuring that your cloud data is safe and secure. When cloning a dataset, you can specify the destination dataset, remote file path, and so on.

```python
dataset.clone(clone_name='dataset_v2',
              filters=None,
              with_items_annotations=True,
              with_metadata=True,
              with_task_annotations_status=True)
```
As you may have noticed, you can also use filters to clone a dataset with only specific sub-categories of the main dataset. For example, in a dataset containing both cats and dogs, you could filter by dogs to create a new dataset containing only dog pictures.

Now you have a clone of your initial dataset, called "dataset_v2".

## Merge 2 datasets

If you have multiple datasets that you want to merge, Dataloop provides this option as well. This can be useful when you have multiple annotation teams, working on subsets of a big dataset you want to put together. After everyone has finished their tasks (which you leaned how to create previously), you now want to merge all of the anotated datasets together, to finish your job. You will now learn how to do that.

To see all of the datasets you have inside of your project, you can run the following line of code:
```python
project.datasets.list()
```
After runing this, you should see all of the datasets you have created. If you executed only the code in this onboarding tutorial, you should have 2 datasets, namely "My-First-Dataset", and "dataset_v2" clone of "My-First-Dataset. Remember that you can find out the id of each dataset, and other details, after runing the line of code from above.

The success of dataset merging depends on how similar or different the datasets are:
1. Cloned Datasets - items, annotations, and metadata will be merged; this means that you will see annotations from different datasets on the same item.
2. Different datasets (not clones) with similar recipes - items will be summed up, which will cause duplication of similar items.
3. Datasets with different recipes - Datasets with different default recipes cannot be merged. You must first "match" the recipes of 2 datasets, before attempting to merge them.

To merge datasets, you will need both the project's id and the dataset's id. You should already have the dataset's id, which was shown, for each dataset, when we listed all datasets, above.

To find the project id, for all projects, you can run the following code:
```python
dl.projects.list()
```
Remember that for 2 datasets to be merged, they need to have the same [Recipes](https://dataloop.ai/docs/ontology). To make things easy, we will just used the dataset we just cloned named "dataset_v2" and merge it with the "My-First-Dataset". We do this since they both have the same Recipe and Ontology, so we won't get any errors. Remember that a cloned dataset will have the same recipe and ontology as the base dataset.

After gathering all of the ids you need, you can now proceed to merge "My-First-Dataset" with "dataset_v2" and create a bigger dataset. You can do that using the code below:
```python
dataset_ids = ["dataset-1-id", "dataset-2-id"]
project_ids = ["dataset-1-project-id", "dataset-2-project-id"]
dataset_merge = dl.datasets.merge(merge_name="my_merged_dataset",
                                  project_ids=project_ids,
                                  dataset_ids=dataset_ids,
                                  with_items_annotations=True,
                                  with_metadata=False,
                                  with_task_annotations_status=False)
```
All you have to do in this code is to replace the "dataset_ids" and the "project_ids" variables with the id of the datasets you want to merge and the id of the project each dataset is part of. In our case, the project ID's will be the same for both datasets, since we previously created them as part of the same project.

After executing this, you should have successfully merged the 2 datasets into a bigger one, called "my_merged_dataset".

In the next chapter, you will learn about Dataloop's Function-as-a-Service (FAAS), a compute service that automatically runs your code based on time patterns or in response to trigger events.
