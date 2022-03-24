from re import A
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import datetime
import os
import sys

sys.path.insert(0, '/home/shira/workspace/distillator-obsolete/dtlpy')  # HACK: local hack, remove
sys.path.insert(1, '/home/shira/workspace')

from dtlpy.ml import train_utils
import dtlpy as dl
from keras_adapters import inception_adapter


def get_globals():
    model = dl.models.get(model_name='InceptionV3')
    snapshot = model.snapshots.get('pretrained-inception')
    model.snapshots.list().to_df()
    return model, snapshot


def create_sample_dataset(project):
    try:
        dataset = project.datasets.get(dataset_name='Sheep Face')
    except dl.exceptions.NotFound:
        dataset = project.datasets.create('Sheep Face')
        _ = dataset.items.upload(local_path='../../assets/sample_datasets/SheepFace/items/*',
                            local_annotations_path='../../dtlpy-documentation/assets/sample_datasets/SheepFace/json')
    dataset.to_df()

    return dataset


def create_model_and_snapshot():
    inception_adapter.model_and_snapshot_creation(args.project)


def pretrained_inference(item_id, model, snapshot):
    adapter = model.build()
    adapter.load_from_snapshot(snapshot=snapshot)

    item = dl.items.get(item_id=item_id)
    annotations = adapter.predict_items([item], with_upload=False)
    image = Image.open(item.download())
    plt.imshow(item.annotations.show(np.asarray(image),
                                     thickness=5))
    print('Classification: {}'.format(annotations[0][0].label))
    item.open_in_web()


def train_on_new_dataset(model, snapshot, dataset):
    partitions = {dl.SnapshotPartitionType.TRAIN: 0.8,
                  dl.SnapshotPartitionType.VALIDATION: 0.1,
                  dl.SnapshotPartitionType.TEST: 0.1}

    snapshot_name = f'trained-{dataset.name}'
    try:
        new_snapshot = model.snapshots.get(snapshot_name=snapshot_name)
    except dl.exceptions.NotFound:
        cloned_dataset = train_utils.prepare_dataset(dataset,
                                                filters=None,
                                                partitions=partitions)
        new_snapshot = snapshot.clone(snapshot_name=snapshot_name,
                                      dataset_id=cloned_dataset.id)

    new_snapshot.configuration.update({'batch_size': 16,
                                    'start_epoch': 0,
                                    'num_epochs': 1,
                                    'input_size': (299, 299)})

    adapter = model.build()
    adapter.load_from_snapshot(snapshot=new_snapshot,
                               configuration=new_snapshot.configuration)

    root_path, data_path, output_path = adapter.prepare_training(root_path=os.path.join('tmp', new_snapshot.id))

    print("Training {!r} with snapshot {!r} on data {!r}".format(model.name, new_snapshot.id, data_path))
    adapter.train(data_path=data_path,
                  output_path=output_path)

    adapter.snapshot.bucket.list_content()

    adapter.save_to_snapshot(local_path=output_path,
                             replace=True,
                             weights_filename='model.hdf5')

    adapter.snapshot.bucket.list_content()


def main(args, **kwargs):
    project = dl.projects.get(args.project)
    model, snapshot = get_globals()
    if args.mode == 'train':
        if not args.dataset:
            dataset = create_sample_dataset(project)
        else:
            dataset = project.datasets.get(None, args.dataset)
        dataset.to_df()
        train_on_new_dataset(model=model,
                            snapshot=snapshot,
                            dataset=dataset)
    elif args.mode == 'inference':
        pretrained_inference(item_id=args.item,
                            model=model,
                            snapshot=snapshot)


if __name__ == '__main__':
    import argparse
    dl.setenv('prod')
    parser = argparse.ArgumentParser(description='local runner for model management testing')

    parser.add_argument('--env', '-e', default='prod', help='dtlpy env')
    parser.add_argument('--project', '-p', default='distillator', help='dtlpy project name',) #required=True)
    parser.add_argument('--dataset', '-d', default='', help='dtlpy dataset id')
    parser.add_argument('--item', '-i', default='6205097d8ea6ad0abe7b90ba', help='dtlpy single item id')
    parser.add_argument('--mode', '-m', default='inference', help='inference or training')

    args = parser.parse_args()

    main(args)
    print('Done!')
