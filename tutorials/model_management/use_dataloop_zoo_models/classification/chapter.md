# Training a classification model with ResNet  
In this tutorial we will use the Resnet Model Adapter to inference and train on custom data.  
If you don't have the following packages, you'll need to install. The Torch Model Adapter will use them later:  
torch  
torchvision  
imgaug  
scikit-image<0.18  
  

```python
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import dtlpy as dl
from dtlpy.ml import train_utils
```
## Get Global Model and Pretrained Snapshot  
We start by getting tne model and an ImageNet pretrained model  

```python
model = dl.models.get(model_name='ResNet')
snapshot = model.snapshots.get('pretrained-resnet18')
model.snapshots.list().to_df()
```
### Run Pretrained Model  
We will "build" to model adapter to get the model code locally and the create an instance of the ModelAdapter class.  
After that, we load the pretrained snapshot into the model adapter.  

```python
adapter = model.build()
adapter.load_from_snapshot(snapshot=snapshot)
```
Get an item and predict with upload.  
You can also open the item in the platform to view and edit annotations easily.  

```python
item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
annotations = adapter.predict_items([item], with_upload=True)
image = np.asarray(Image.open(item.download()))
plt.imshow(item.annotations.show(image,
                                 thickness=5))
print('Classification: {}'.format(annotations[0][0].label))
```
## Train on new dataset  
We will use a public sheep face dataset. We create a project and a dataset and upload the data with 4 labels of sheep.  
NOTE: You might need to change the location of the items (should point to the root of the documentation repository)  

```python
project = dl.projects.create('Sheep Face - Model Mgmt')
dataset = project.datasets.create('Sheep Face')
dataset.to_df()
_ = dataset.items.upload(local_path='../../../../assets/sample_datasets/SheepFace/items/*',
                         local_annotations_path='../../../../assets/sample_datasets/SheepFace/json')
dataset.add_labels(label_list=['Marino', 'Poll Dorset', 'Suffolk', 'White Suffolk'])
```
Now we'll run the "prepare_dataset" method. This will clone and freeze the dataset (so that we'll be able to reproduce the training and keep a snapshot of the data).  
The cloned dataset will be split into subsets (using DQL or percentage). In this examples, we'll use a 80/20 train validation split.  
After that we clone the pretrained snapshot to have a starting point for the fine-tuning.  
The snapshot's configuration will determine some runtime configurations, for instance, we will train for only 2 epochs.  

```python
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
                                             'input_size': 256,
                                             'id_to_label_map': {(v - 1): k for k, v in
                                                                 dataset.instance_map.items()}
                                             })
new_snapshot = model.snapshots.get(snapshot_name=snapshot_name)
```
We'll load the new un-trained snapshot to the adapter and prepare the training local dataset  

```python
adapter.load_from_snapshot(snapshot=new_snapshot)
root_path, data_path, output_path = adapter.prepare_training()
```
## Start The Train  
Now We have the model, the snapshot, and the data ready. We are ready to train.  

```python
print("Training {!r} with snapshot {!r} on data {!r}".format(model.name, new_snapshot.id, data_path))
adapter.train(data_path=data_path,
              output_path=output_path)
```
## Save the Snapshot  
We will save the locally-trained snapshot and upload the trained weights to the Item Bucket.  
This will ensure we have everything in the Dataloop platform and everyone can use our trained snapshot.  

```python
adapter.save_to_snapshot(local_path=output_path,
                         replace=True)
```
We can also list our bucket's content, and add more files that are needed for loading/running the snapshot  

```python
adapter.snapshot.bucket.list_content()
```
## Predict On Our New Trained Snapshot  
We will load our snapshot and visualize some items' predictions  

```python
item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
annotations = adapter.predict_items([item], with_upload=True)
image = Image.open(item.download())
plt.imshow(item.annotations.show(np.asarray(image),
                                 thickness=5))
print('Classification: {}'.format(annotations[0][0].label))
```
