# Chapter 6 - Data Versioning

Data Versioning is critical for data-centric AI and analytics applications to be effective. When files are added, removed, or modified in a Dataset, version control keeps track of the changes. This way, users can see how the data was changed, what changed, and who made the changes. This is important for a variety of reasons; from providing important insights for analytics and data-driven decision making, to enabling you to revert changes made to the dataset that reduced the performance of the AI model you trained.

Dataloop provides data [versioning tools](https://docs.dataloop.ai/docs/clone-merge-dataset?highlight=clone) to manage your data that you can use for:

1. Golden training dataset management;
2. [Reproducibility](https://en.wikipedia.org/wiki/Reproducibility);
3. Experimentation;
4. Task and Assignment management.

To get started with Data Versioning, you must first `get` the Dataset you want to version.

We already did this in the Dataset creation chapter.  As a reminder, this is how you `get` a Dataset you previously created:

```python
dataset = project.datasets.get(dataset_id='<dataset_id>')
```

After you've confirmed that you've chosen the correct Dataset, you can make a `clone` of it. Cloning a Dataset results in the creation of a new Dataset that contains the same data sample files as the original, including item Metadata, and the Dataset [Recipe and Ontology](https://docs.dataloop.ai/docs/ontology). The files in the cloned Dataset are actually a reference to the original file's binary rather than a new copy of the original, ensuring that your cloud data is safe and secure. When cloning a Dataset, you can specify the destination Dataset, remote file path, and other parameters.

```python
dataset.clone(clone_name='dataset_v2',
              filters=None,
              with_items_annotations=True,
              with_metadata=True,
              with_task_annotations_status=True)
```

As you may have noticed in the Python code, you can also use filters to clone a subset of the Dataset as defined by the Filter. For example, in a Dataset containing both cats and dogs, you could Filter by dogs to create a new Dataset containing only files that contain pictures of dogs.

Now you have a Clone of your initial Dataset, called `dataset_v2`.

### Merge 2 Datasets

If you have multiple Datasets that you want to merge, Dataloop provides this option as well. This can be useful when you have multiple annotation teams working on subsets of a big Dataset. After everyone has finished their Annotation and QA tasks (which you learned how to create previously), you might want to merge all of the annotated subsets together to end up with a complete master Dataset. You will now learn how to do just that.

To see all of the datasets you have inside of your current Project and details like the id of each Dataset, run the line of code below:

```python
project.datasets.list()
```

After running this, you should see all of the Datasets you have created. If you executed only the code in this onboarding tutorial, you should have only 2 Datasets, namely "My-First-Dataset", and "dataset_v2" which is a clone of "My-First-Dataset".

```python
[Dataset(id='63d94b3837906e27029899c2', url='https://gate.dataloop.ai/api/v1/datasets/63d94b3837906e27029899c2', name='Binaries', creator='email@dataloop.ai', items_count=1, expiration_options=None, index_driver='v1', created_at='2023-01-31T17:09:12.776Z'),
 Dataset(id='63da62d973b62f22086f1d8f', url='https://gate.dataloop.ai/api/v1/datasets/63da62d973b62f22086f1d8f', name='My-First-Dataset', creator='email@dataloop.ai', items_count=1, expiration_options=None, index_driver='v1', created_at='2023-02-01T13:02:17.250Z'),
 Dataset(id='63da63cab9421abb1ddd5a94', url='https://gate.dataloop.ai/api/v1/datasets/63da63cab9421abb1ddd5a94', name='dataset_v2', creator='email@dataloop.ai', items_count=1, expiration_options=None, index_driver='v1', created_at='2023-02-01T13:06:18.801Z'),
 Dataset(id='63da644a4d9815630ac3d50f', url='https://gate.dataloop.ai/api/v1/datasets/63da644a4d9815630ac3d50f', name='First_second_merged_dataset', creator='email@dataloop.ai', items_count=1, expiration_options=None, index_driver='v1', created_at='2023-02-01T13:08:26.592Z')]
```

The success of Dataset merging depends on how similar or different the Datasets are:

1. Cloned Datasets - Items, Annotations, and Metadata will be merged; this means that you will see Annotations from different Datasets on the same Item.
2. Different Datasets (not clones) with similar Recipes - Items will be summed up, which will cause duplication of similar Items.
3. Datasets with different Recipes - Datasets with different default Recipes **cannot be merged**. You must first "match" the Recipes of 2 Datasets, before attempting to merge them.

To merge Datasets, you will need both the Project ID and the Dataset ID. You should already have the Dataset ID which was shown for each Dataset when we ran the above code and listed all Datasets.

To find the Project ID, for all Projects, you can run the following code:

```python
dl.projects.list()
```

Remember that for two Datasets to be merged, they need to have the same [Recipes](https://docs.dataloop.ai/docs/ontology). To make things easy, we will just use the Dataset we just cloned named "dataset_v2" and merge it with the "My-First-Dataset".  Since they both have the same Recipe and Ontology we won't get any errors. Remember that a cloned Dataset will have the same Recipe and Ontology as the base Dataset.

After gathering all of the IDs you need, you can now proceed to merge "My-First-Dataset" with "dataset_v2" into a new Dataset. You can do that using the code below:

```python
dataset_ids = ["<dataset-1-id>", "<dataset-2-id>"]
project_ids = ["<dataset-1-project-id>", "<dataset-2-project-id>"]
dataset_merge = dl.datasets.merge(merge_name="my_merged_dataset",
                                  project_ids=<project_ids>,
                                  dataset_ids=<dataset_ids>,
                                  with_items_annotations=True,
                                  with_metadata=False,
                                  with_task_annotations_status=False)
```

All you have to do in this code is to replace the `dataset_ids` and the `project_ids` variables with the IDs of the Datasets you want to merge and the ID of the Project each Dataset is part of. In our case, the Project IDs will be the same for both Datasets, since we previously created them as part of the same Project.

After executing this, you should have successfully merged the two Datasets into a new one, called "my_merged_dataset".

In the next chapter, you will learn about Dataloop's Function-as-a-Service (FaaS), a Compute Service that can automatically run your code based on time patterns or in response to trigger events.
