import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import datetime
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'distillator-obsolete/dtlpy')) #HACK: remove

import dtlpy as dl
from dtlpy.ml import train_utils

dl.setenv('prod')
from keras_adapters import inception_adapter


def get_globals():
    model = dl.models.get(model_name='InceptionV3')
    snapshot = model.snapshots.get('pretrained-inception')
    model.snapshots.list().to_df()
    return model, snapshot

def create_sample_dataset(project_name):
    project = dl.projects.get(project_name)
    dataset = project.datasets.create('Sheep Face')
    dataset.to_df()
    _ = dataset.items.upload(local_path='../../assets/sample_datasets/SheepFace/items/*',
                         local_annotations_path='../../assets/sample_datasets/SheepFace/json')

def create_model_and_snapshot(project_name):
    inception_adapter.model_and_snapshot_creation(project_name)

project = dl.projects.get('distillator')


dataset = project.datasets.get(None, '61680bfa82e9a80fc61262e9') # gtsrb
# dataset.to_df()



def pretrained_inference(item_id, model, snapshot):
    adapter = model.build()
    adapter.load_from_snapshot(snapshot=snapshot) # local_path=snapshot.bucket.local_path

    item = dl.items.get(item_id=item_id)
    annotations = adapter.predict_items([item], with_upload=False)
    image = Image.open(item.download())
    plt.imshow(item.annotations.show(np.asarray(image),
                                    thickness=5))
    print('Classification: {}'.format(annotations[0][0].label))
    item.open_in_web()


def train_on_new_dataset(model, snapshot):
    partitions = {dl.SnapshotPartitionType.TRAIN: 0.8,
                dl.SnapshotPartitionType.VALIDATION: 0.1,
                dl.SnapshotPartitionType.TEST: 0.1}

    cloned_dataset = train_utils.prepare_dataset(dataset,
                                                filters=None,
                                                partitions=partitions)

    try:
        new_snapshot = model.snapshots.get(snapshot_name='trained')
    except dl.exceptions.NotFound:
        new_snapshot = snapshot.clone(snapshot_name='trained',
                                    dataset_id=cloned_dataset.id,
                                    configuration=)

    new_snapshot.configuration.update({'batch_size': 16,
                                    'start_epoch': 0,
                                    'num_epochs': 1,
                                    'input_size': (299,299)})
    new_snapshot.update()



adapter = model.build()
adapter.load_from_snapshot(snapshot=new_snapshot,
                           configuration=new_snapshot.configuration)

root_path, data_path, output_path = adapter.prepare_training(root_path=os.path.join('tmp', new_snapshot.id))


# Start the Train
print("Training {!r} with snapshot {!r} on data {!r}".format(model.name, new_snapshot.id, data_path))
adapter.train(data_path=data_path,
              output_path=output_path)

adapter.snapshot.bucket.list_content()

adapter.save_to_snapshot(local_path=output_path,
                         replace=True,
                         weights_filename='model.hdf5')
#%%
adapter.snapshot.bucket.list_content()


def main(dataset: dl.Dataset, project: dl.Project):

    pass



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='local runner for model management testing',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--env', '-e', default='prod', help='dtlpy env')
    parser.add_argument('--project', '-p', default='distillator', help='dtlpy project name')
    parser.add_argument('--dataset', '-d', default='', help='dtlpy dataset id')
    parser.add_argument('--item', '-i', default='', help='dtlpy single item id')

    args = parser.parse_args()

    project = dl.projects.get(args.project)
    dataset = project.datasets.get(args.dataset)

    main(project=project, item_id='6205097d8ea6ad0abe7b90ba')
