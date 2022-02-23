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


def func4():
    adapter = model.build()


def func5():
    adapter.load_from_snapshot(snapshot=snapshot)


def func6():
    item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
    annotations = adapter.predict_items([item], with_upload=True)

    image = Image.open(item.download())
    plt.imshow(item.annotations.show(np.asarray(image),
                                     thickness=5))
    print('Classification: {}'.format(annotations[0][0].label))


def func7():
    dataset = project.datasets.get(dataset_name='Sheep Face')

    partitions = {dl.SnapshotPartitionType.TRAIN: 0.8,
                  dl.SnapshotPartitionType.VALIDATION: 0.2}

    cloned_dataset = train_utils.prepare_dataset(dataset,
                                                 filters=None,
                                                 partitions=partitions)

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
                                                 'input_size': 256})

    new_snapshot = model.snapshots.get(snapshot_name=snapshot_name)


def func8():
    adapter.load_from_snapshot(snapshot=new_snapshot)

    root_path, data_path, output_path = adapter.prepare_training()


def func9():
    print("Training {!r} with snapshot {!r} on data {!r}".format(model.name, new_snapshot.id, data_path))

    adapter.train(data_path=data_path,
                  output_path=output_path)


def func10():
    adapter.save_to_snapshot(local_path=output_path,
                             replace=True)


def func11():
    adapter.snapshot.bucket.list_content()


def func12():
    from imgaug import augmenters as iaa
    from torchvision import transforms
    from dtlpy.ml.ml_dataset import get_torch_dataset
    augmentation = iaa.Sequential([
        iaa.Resize({"height": 256, "width": 256}),
        # iaa.Superpixels(p_replace=(0, 0.5), n_segments=(10, 50)),
        iaa.flip.Fliplr(p=0.5),
        iaa.flip.Flipud(p=0.5),
        #         iaa.GaussianBlur(sigma=(0.0, 0.8)),
    ])
    tfs = transforms.Compose([
        augmentation,
        np.copy,
        transforms.ToTensor()
    ])
    dataloader = get_torch_dataset()(data_path=os.path.join(data_path, 'train'),
                                     dataset_entity=cloned_dataset,
                                     annotation_type=dl.AnnotationType.CLASSIFICATION,
                                     transforms=tfs,
                                     with_orig=True)


def func13():
    adapter = model.build()
    trained_snapshot = model.snapshots.get(snapshot_name='sheep-soft-augmentations')
    adapter.load_from_snapshot(snapshot=trained_snapshot,
                               overwrite=True)


def func14():
    fig, ax = plt.subplots(1, 2)
    for i in range(2):
        image, target, orig_image, orig_targets = dataloader[np.random.randint(len(dataloader))]
        anno = adapter.predict([orig_image])
        ax[i].imshow(orig_image)
        ax[i].set_title('GT: {!r}\n Pred: {!r}:{:.2f}'.format(adapter.label_map[str(int(target))],
                                                              anno[0][0].label,
                                                              anno[0][0].metadata['user']['model']['confidence']))
