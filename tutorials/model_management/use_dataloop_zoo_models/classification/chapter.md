# Training a classification model with ResNet  
```python
import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
import dtlpy as dl
from dtlpy.ml import train_utils
```
## Get Global Model and Pretrained Snapshot  
```python
model = dl.models.get(model_name='ResNet')
snapshot = model.snapshots.get('pretrained-resnet18')
model.snapshots.list().to_df()
```
## Upload Dataset  
```python
project = dl.projects.get('Sheeps Face Proj')
dataset = project.datasets.create('Sheep Face')
dataset.to_df()
_ = dataset.items.upload(local_path='../../assets/sample_datasets/SheepFace/items/*',
                         local_annotations_path='../../assets/sample_datasets/SheepFace/json')
```
## Run Pretrained Model  
```python
adapter = model.build()
```
Load the pretrained snapshot into the model adapter  
```python
adapter.load_from_snapshot(snapshot=snapshot)
```
Get an item and predict with upload  
```python
item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
annotations = adapter.predict_items([item], with_upload=True)
image = Image.open(item.download())
plt.imshow(item.annotations.show(np.asarray(image),
                                 thickness=5))
print('Classification: {}'.format(annotations[0][0].label))
```
You can alos open the item in the platform to view and edit annotations easily  
```python
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
```
## Train on new dataset  
Here we will train on the Sheep dataset.  
First we will clone and split the dataset to 2 partitions - train and validation.  
After that we will clone the pretrained snapshot  
  
```python
adapter.load_from_snapshot(snapshot=new_snapshot)
root_path, data_path, output_path = adapter.prepare_training()
```
# Train on new dataset  
Here we will train on the Sheep dataset.  
First we will clone and split the dataset to 2 partitions - train and validation.  
After that we will clone the pretrained snapshot  
```python
print("Training {!r} with snapshot {!r} on data {!r}".format(model.name, new_snapshot.id, data_path))
adapter.train(data_path=data_path,
              output_path=output_path)
```
# Start The Train  
Finally we are ready to train!  
```python
adapter.save_to_snapshot(local_path=output_path,
                         replace=True)
```
