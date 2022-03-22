import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import datetime
import os
import sys

# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'distillator-obsolete/dtlpy'))

import dtlpy as dl
from dtlpy.ml import train_utils

dl.setenv('prod')
from pytorch_adapters import resnet_adapter as res

project = dl.projects.get('distillator')
model = dl.models.get(model_name='ResNet')


# res.snapshot_creation(project.name, model=model, resnet_ver='50')
snapshot = model.snapshots.get('pretrained-resnet50')

# model.snapshots.list().to_df()

dataset = project.datasets.get(None, '61680bfa82e9a80fc61262e9') # gtsrb
# dataset.to_df()



adapter = model.build(local_path='/home/shira/workspace/pytorch_adapters', from_local=True)
adapter.load_from_snapshot(snapshot=snapshot) # local_path=snapshot.bucket.local_path

#### inference
# item = dl.items.get(item_id='6205097d8ea6ad0abe7b90ba') #dog
# annotations = adapter.predict_items([item], with_upload=False)
# image = Image.open(item.download())
# plt.imshow(item.annotations.show(np.asarray(image),
#                                  thickness=5))
# print('Classification: {}'.format(annotations[0][0].label))

# item.open_in_web()


#train on new dataset

partitions = {dl.SnapshotPartitionType.TRAIN: 0.8,
              dl.SnapshotPartitionType.VALIDATION: 0.1,
              dl.SnapshotPartitionType.TEST: 0.1}

cloned_dataset = train_utils.prepare_dataset(dataset,
                                             filters=None,
                                             partitions=partitions)


# new_snapshot = snapshot.clone(snapshot_name='test01-resnet',
#                               dataset_id=cloned_dataset.id)

# OR
new_snapshot = model.snapshots.get(snapshot_name='test01-resnet')

# and add new configuration for the snapshot
new_snapshot.configuration.update({'batch_size': 16,
                                  'start_epoch': 0,
                                  'num_epochs': 1,
                                  'input_size': 256})
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
