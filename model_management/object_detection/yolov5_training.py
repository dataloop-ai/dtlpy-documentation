import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import datetime
import os
import sys
import inspect

sys.path.insert(0, '/home/shira/workspace/distillator-obsolete/dtlpy') #HACK: local hack, remove
sys.path.insert(1, '/home/shira/workspace')


import dtlpy as dl
from dtlpy.ml import train_utils

dl.setenv('prod')
from yolov5 import model_adapter as yol

project = dl.projects.get('distillator')


# model = yol.model_creation(project_name=project.name)
model = dl.models.get('yolo-v5')


# snapshot = yol.snapshot_creation(project_name=project.name, model=model, yolo_ver='yolov5s', env='prod')
snapshot = model.snapshots.get('pretrained-yolov5s')

# model.snapshots.list().to_df()

dataset = project.datasets.get(None, '61680bfa82e9a80fc61262e9') # gtsrb
# dataset.to_df()



adapter = model.build()
adapter.load_from_snapshot(snapshot=snapshot) # local_path=snapshot.bucket.local_path


item = dl.items.get(item_id='6205097d8ea6ad0abe7b90ba') #dog
image = np.asarray(Image.open(item.download()))

# use the adapter to inference without uploading annotations
all_annotations = adapter.predict_items([item], with_upload=False, min_score=0.1)

item_annotations = all_annotations[0]  # predict items returns a list for each of the input items
print(item_annotations.print(to_return=True))
# print(item.annotations.list().print(to_return=True))
print(item_annotations.to_df())

# add the items to the image
annotated_image = item.annotations.show(image=image, thickness=5)
# plt.imshow(annotated_image)


#train on new dataset

# # split the dataset to 2 partitions - 80% train 20% validation - randomly
partitions = {dl.SnapshotPartitionType.TRAIN: 0.8,
              dl.SnapshotPartitionType.VALIDATION: 0.2}

# # use DQL to set the two directories and the train/val split
# partitions = {dl.SnapshotPartitionType.TRAIN: dl.Filters(field='dir', values='/train'),
#               dl.SnapshotPartitionType.VALIDATION: dl.Filters(field='dir', values='/test')}

cloned_dataset = train_utils.prepare_dataset(dataset,
                                             filters=None,
                                             partitions=partitions)


snapshot_name='test-yolov5'
try:
    new_snapshot = model.snapshots.get(snapshot_name=snapshot_name)
except Exception:
    bucket = project.buckets.create(bucket_type=dl.BucketType.ITEM, model_name=model.name, snapshot_name=snapshot_name)
    new_snapshot = snapshot.clone(snapshot_name=snapshot_name,
                                dataset_id=cloned_dataset.id,
                                bucket=bucket,
                                configuration={'batch_size': 2,
                                                'start_epoch': 0,
                                                'max_epoch': 5,
                                                'id_to_label_map': {(v-1):k for k, v in dataset.instance_map.items()}
                                                })


adapter.load_from_snapshot(snapshot=new_snapshot)
root_path, data_path, output_path = adapter.prepare_training()

print("Training {!r} with snapshot {!r} on data {!r}".format(model.name, new_snapshot.id, data_path))
adapter.train(data_path=data_path, output_path=output_path)

adapter.save_to_snapshot(local_path=output_path, replace=True)


# Predict New Snapshot on Local Item
adapter.load_from_snapshot(snapshot=new_snapshot)

item = dl.items.get(item_id='')
image = Image.open(item.download())

all_annotations = adapter.predict_items([item], with_upload=True)  # use with_upload = False
plt.imshow(item.annotations.show(np.asarray(image), thickness=5))
