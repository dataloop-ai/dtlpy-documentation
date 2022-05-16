def func1():
    import matplotlib.pyplot as plt
    from PIL import Image
    import numpy as np
    import dtlpy as dl
    from dtlpy.ml import train_utils


def func2():
    import dtlpy as dl
    filters = dl.Filters(resource=dl.FiltersResource.MODEL)
    filters.add(field='name', values='yolo-v5')
    filters.add(field='scope', values='public')
    models = dl.models.list(filters=filters)
    models.to_df()
    model = models.items[0]
    snapshot = model.snapshots.get('pretrained-yolo-v5-small')
    model.snapshots.list().to_df()


def func3():
    adapter = model.build()
    adapter.load_from_snapshot(snapshot=snapshot)


def func4():
    item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
    annotations = adapter.predict_items([item], with_upload=True)
    image = np.asarray(Image.open(item.download()))
    plt.imshow(item.annotations.show(image,
                                     thickness=5))
    print('Classes found: {}'.format([ann.label for ann in annotations[0]]))


def func5():
    project = dl.projects.create('Fruit - Model Mgmt')
    dataset = project.datasets.create('Fruit')
    dataset.to_df()
    _ = dataset.items.upload(local_path='../../../../assets/sample_datasets/FruitImage/items/*',
                             local_annotations_path='../../../../assets/sample_datasets/FruitImage/json')
    dataset.add_labels(label_list=['orange', 'banana', 'apple'])


def func6():
    partitions = {dl.SnapshotPartitionType.TRAIN: 0.8,
                  dl.SnapshotPartitionType.VALIDATION: 0.2}
    cloned_dataset = train_utils.prepare_dataset(dataset,
                                                 filters=None,
                                                 partitions=partitions)
    snapshot_name = 'fruits'
    # create an Item Bucket to save snapshot in your project
    bucket = project.buckets.create(bucket_type=dl.BucketType.ITEM,
                                    model_name=model.name,
                                    snapshot_name=snapshot_name)
    new_snapshot = snapshot.clone(snapshot_name=snapshot_name,
                                  dataset_id=cloned_dataset.id,
                                  project_id=project.id,
                                  bucket=bucket,
                                  labels=list(dataset.instance_map.keys()),
                                  configuration={'batch_size': 16,
                                                 'start_epoch': 0,
                                                 'num_epochs': 2,
                                                 'input_size': 256,
                                                 'id_to_label_map': {(v - 1): k for k, v in
                                                                     dataset.instance_map.items()}
                                                 })

    new_snapshot = model.snapshots.get(snapshot_name=snapshot_name)


def func7():
    adapter.load_from_snapshot(snapshot=new_snapshot)
    root_path, data_path, output_path = adapter.prepare_training()


def func8():
    print("Training {!r} with snapshot {!r} on data {!r}".format(model.name, new_snapshot.id, data_path))

    adapter.train(data_path=data_path,
                  output_path=output_path)


def func9():
    adapter.save_to_snapshot(local_path=output_path,
                             replace=True)


def func10():
    adapter.snapshot.bucket.list_content()


def func11():
    item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
    annotations = adapter.predict_items([item], with_upload=True)

    image = Image.open(item.download())
    plt.imshow(item.annotations.show(np.asarray(image),
                                     thickness=5))
    print('Classification: {}'.format(annotations[0][0].label))
