def func1():
    import datetime
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from PIL import Image
    import numpy as np
    import os
    import dtlpy as dl
    from dtlpy.ml import train_utils


def func2():
    model = dl.models.get(model_name='ResNet')
    snapshot = model.snapshots.get('pretrained-resnet18')
    model.snapshots.list().to_df()


def func3():
    project = dl.projects.get('Sheeps Face Proj')
    dataset = project.datasets.create('Sheep Face')
    dataset.to_df()
    _ = dataset.items.upload(local_path='../../assets/sample_datasets/SheepFace/items/*',
                             local_annotations_path='../../assets/sample_datasets/SheepFace/json')
    dataset.add_labels(label_list=['Marino', 'Poll Dorset', 'Suffolk', 'White Suffolk'])


def func4():
    adapter = model.build()
    adapter.load_from_snapshot(snapshot=snapshot)


def func5():
    item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
    annotations = adapter.predict_items([item], with_upload=True)

    image = Image.open(item.download())
    plt.imshow(item.annotations.show(np.asarray(image),
                                     thickness=5))
    print('Classification: {}'.format(annotations[0][0].label))


def func6():
    dataset = project.datasets.get(dataset_name='Sheep Face')

    partitions = {dl.SnapshotPartitionType.TRAIN: 0.8,
                  dl.SnapshotPartitionType.VALIDATION: 0.2}

    cloned_dataset = train_utils.prepare_dataset(dataset,
                                                 filters=None,
                                                 partitions=partitions)
    cloned_dataset.add_labels(label_list=list(dataset.instance_map.keys()))

    snapshot_name = 'sheep-soft-augmentations'
    # create an Item Bucket to save snapshot in your project
    bucket = project.buckets.create(bucket_type=dl.BucketType.ITEM,
                                    model_name=model.name,
                                    snapshot_name=snapshot_name)
    new_snapshot = snapshot.clone(snapshot_name=snapshot_name,
                                  dataset_id=cloned_dataset.id,
                                  bucket=bucket,
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
