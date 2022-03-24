
from posixpath import dirname
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import datetime
import os
import sys
import inspect

sys.path.insert(0, '/home/shira/workspace/distillator-obsolete/dtlpy')  # HACK: local hack, remove
sys.path.insert(1, '/home/shira/workspace')

from yolov5 import model_adapter as yol
from dtlpy.ml import train_utils
import dtlpy as dl




def get_globals():
    model = dl.models.get(model_name='yolo-v5')
    snapshot = model.snapshots.get('pretrained-yolo-v5-small')
    model.snapshots.list().to_df()
    return model, snapshot


def create_sample_dataset(project):
    try:
        dataset = project.datasets.get(dataset_name='FruitImage')
    except dl.exceptions.NotFound:
        dataset = project.datasets.create('FruitImage')
        _ = dataset.items.upload(local_path='../../assets/sample_datasets/FruitImage/items/train/*',
                                 local_annotations_path='../../assets/sample_datasets/FruitImage/json/train',
                                 remote_path='train')
        _ = dataset.items.upload(local_path='../../assets/sample_datasets/FruitImage/items/test/*',
                                 local_annotations_path='../../assets/sample_datasets/FruitImage/json/test',
                                 remote_path='test')
        dataset.labels = ['apple', 'banana', 'orange', 'mixed']

    dataset.to_df()

    return dataset


def create_model_and_snapshot(project):
    model = yol.model_creation(project_name=project.name)
    snapshot = yol.snapshot_creation(model, yolo_size='small')

    return model, snapshot

def pretrained_inference(item_id, model, snapshot):
    ###
    project = dl.projects.get('distillator')
    dataset = project.datasets.get(dataset_name='FruitImage')
    snapshot.configuration['id_to_label_map'] = {}
    ###

    adapter = model.build()  # local_path='/home/shira/workspace/pytorch_adapters', from_local=True
    adapter.load_from_snapshot(snapshot=snapshot)  # local_path=snapshot.bucket.local_path
    item = dl.items.get(item_id=item_id)
    image = np.asarray(Image.open(item.download()))

    # use the adapter to inference without uploading annotations
    all_annotations = adapter.predict_items([item], with_upload=False, min_score=0.1)

    item_annotations = all_annotations[0]  # predict items returns a list for each of the input items
    print(item_annotations.to_df())

    # add the items to the image
    annotated_image = item.annotations.show(image=image, thickness=5)
    plt.imshow(annotated_image)


def train_on_new_dataset(model, project, snapshot, dataset):

    partitions = {dl.SnapshotPartitionType.TRAIN: dl.Filters(field='dir', values='/train'),
                  dl.SnapshotPartitionType.VALIDATION: dl.Filters(field='dir', values='/test')}

    snapshot_name = f'trained-{dataset.name}'
    try:
        new_snapshot = model.snapshots.get(snapshot_name=snapshot_name)
    except dl.exceptions.NotFound:
        cloned_dataset = train_utils.prepare_dataset(dataset,
                                                     filters=None,
                                                     partitions=partitions)
        bucket = project.buckets.create(bucket_type=dl.BucketType.ITEM, model_name=model.name, snapshot_name=snapshot_name)
        new_snapshot = snapshot.clone(snapshot_name=snapshot_name,
                                      dataset_id=cloned_dataset.id,
                                      bucket=bucket)

    new_snapshot.configuration.update({'batch_size': 16,
                                       'start_epoch': 0,
                                       'max_epoch': 5,
                                       })

    adapter = model.build()
    adapter.load_from_snapshot(snapshot=new_snapshot,
                               configuration=new_snapshot.configuration)

    root_path, data_path, output_path = adapter.prepare_training(root_path=os.path.join('tmp', new_snapshot.id))

    print("Training {!r} with snapshot {!r} on data {!r}".format(model.name, new_snapshot.id, data_path))
    adapter.train(data_path=data_path,
                  output_path=output_path)

    adapter.snapshot.bucket.list_content().to_df()

    adapter.save_to_snapshot(local_path=output_path,
                             replace=True)

    adapter.snapshot.bucket.list_content().to_df()


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
                             project=project,
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
    parser.add_argument('--project', '-p', default='distillator', help='dtlpy project name',)  # required=True) #TODO: remove comment
    parser.add_argument('--dataset', '-d', default='', help='dtlpy dataset id')
    parser.add_argument('--item', '-i', default='6205097d8ea6ad0abe7b90ba', help='dtlpy single item id')
    parser.add_argument('--mode', '-m', default='inference', help='inference or training')

    args = parser.parse_args()
    # args.mode = 'train'  # TODO: remove
    main(args)
    print('Done!')
