def func1():
    # !pip install torch torchvision imgaug "scikit-image<0.18"
    import matplotlib.pyplot as plt
    from PIL import Image
    import numpy as np
    import dtlpy as dl
    from dtlpy.ml import train_utils


def func2():
    package = dl.packages.get(package_name='resnet')
    model = package.models.get(model_name='pretrained-resnet50')
    package.models.list().to_df()


def func3():
    adapter = package.build()
    adapter.load_from_model(model=model)


def func4():
    item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
    annotations = adapter.predict_items([item], with_upload=True)

    image = np.asarray(Image.open(item.download()))
    plt.imshow(item.annotations.show(image,
                                     thickness=5))
    print('Classification: {}'.format(annotations[0][0].label))


def func5():
    project = dl.projects.create('Sheep Face - Model Mgmt')
    dataset = project.datasets.create('Sheep Face')
    dataset.to_df()
    _ = dataset.items.upload(local_path='../../../../assets/sample_datasets/SheepFace/items/*',
                             local_annotations_path='../../../../assets/sample_datasets/SheepFace/json')
    dataset.add_labels(label_list=['Merino', 'Poll Dorset', 'Suffolk', 'White Suffolk'])


def func6():
    partitions = {dl.DatasetSubsetType.TRAIN: 0.8,
                  dl.DatasetSubsetType.VALIDATION: 0.2}
    cloned_dataset = train_utils.prepare_dataset(dataset,
                                                 filters=None,
                                                 partitions=partitions)
    model_name = 'sheep-soft-augmentations'
    # create an Item Artifact to save the model to your project
    artifact = project.artifacts.create(artifact_type=dl.ArtifactType.ITEM,
                                        package_name=package.name,
                                        model_name=model_name)
    new_model = model.clone(model_name=model_name,
                            dataset_id=cloned_dataset.id,
                            project_id=project.id,
                            artifact=artifact,
                            labels=list(dataset.instance_map.keys()),
                            configuration={'batch_size': 16,
                                           'start_epoch': 0,
                                           'num_epochs': 2,
                                           'input_size': 256,
                                           'id_to_label_map': {(v - 1): k for k, v in
                                                               dataset.instance_map.items()}
                                           })
    new_model = package.models.get(model_name=model_name)


def func7():
    adapter.load_from_model(model=new_model)
    root_path, data_path, output_path = adapter.prepare_training()


def func8():
    print("Training {!r} with model {!r} on data {!r}".format(package.name, new_model.id, data_path))

    adapter.train(data_path=data_path,
                  output_path=output_path)


def func9():
    adapter.save_to_model(local_path=output_path,
                          replace=True)


def func10():
    adapter.model.artifacts.list_content()


def func11():
    item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
    annotations = adapter.predict_items([item], with_upload=True)
    image = Image.open(item.download())
    plt.imshow(item.annotations.show(np.asarray(image),
                                     thickness=5))
    print('Classification: {}'.format(annotations[0][0].label))
