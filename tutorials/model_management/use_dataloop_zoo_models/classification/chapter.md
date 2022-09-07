# Training a classification model with ResNet  
In this tutorial we will use a publicly available model from the AI library to inference and train on custom data.  
Here we will use the resnet model.  
  
Start by installing the following packages if you don't have them installed already (the Torch Model Adapter will use them later):  
  
torch  
torchvision  
imgaug  
scikit-image<0.18  
  

```python
# !pip install torch torchvision imgaug "scikit-image<0.18"
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import dtlpy as dl
from dtlpy.ml import train_utils
```
## Create the Package and Pretrained Model in Your Project  
First, we create the entities for our project. The package codebase is available in the public Dataloop Github.  

```python
package = dl.packages.get(package_name='resnet')
model = package.models.get(model_name='pretrained-resnet50')
package.models.list().to_df()
```
### Run a pretrained model  
We will "build" to model adapter to get the package code locally and create an instance of the ModelAdapter class.  
Then we will load the pretrained model into the model adapter.  

```python
adapter = package.build()
adapter.load_from_model(model=model)
```
### Predict on an item  
Now you can get an item and inference on it with predict with upload.  
If you would like to see the item and predictions, you can open the item on the platform and edit there.  

```python
item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
annotations = adapter.predict_items([item], with_upload=True)
image = np.asarray(Image.open(item.download()))
plt.imshow(item.annotations.show(image,
                                 thickness=5))
print('Classification: {}'.format(annotations[0][0].label))
```
## Train on new dataset  
Here we will use a public dataset of sheep faces. We create a project and a dataset and upload the data with 4 labels of sheep.  
NOTE: You might need to change the location of the items (should point to the root of the documentation repository)  

```python
project = dl.projects.create('Sheep Face - Model Mgmt')
dataset = project.datasets.create('Sheep Face')
dataset.to_df()
_ = dataset.items.upload(local_path='../../../../assets/sample_datasets/SheepFace/items/*',
                         local_annotations_path='../../../../assets/sample_datasets/SheepFace/json')
dataset.add_labels(label_list=['Merino', 'Poll Dorset', 'Suffolk', 'White Suffolk'])
```
Now we'll run the "prepare_dataset" method. This will clone and freeze the dataset so that we'll be able to reproduce the training with and keep the snapshot of the data.  
The cloned dataset will be split into subsets, either filtered using DQL or as percentages. In this example, we'll use an 80/20 train validation split.  
After partitioning the data, we will clone the pretrained model to have a starting point for the fine-tuning.  
The model's configuration will determine some runtime configurations, such as number of epochs. In this tutorial we will train for only 2 epochs.  

```python
partitions = {dl.DatasetSubsetType.TRAIN: 0.8,
              dl.DatasetSubsetType.VALIDATION: 0.2}
cloned_dataset = train_utils.prepare_dataset(dataset,
                                             filters=None,
                                             partitions=partitions)
model_name = 'sheep-soft-augmentations'
# create an Item Artifact to save the model to your project
artifact = project.artifacts.create(artifact_type=dl.ArtifactType.ITEM,
                                    package_name=package.name,
                                    model_name=model_name)
new_model = model.clone(model_name=model_name,
                        dataset_id=cloned_dataset.id,
                        project_id=project.id,
                        artifact=artifact,
                        labels=list(dataset.instance_map.keys()),
                        configuration={'batch_size': 16,
                                       'start_epoch': 0,
                                       'num_epochs': 2,
                                       'input_size': 256,
                                       'id_to_label_map': {(v - 1): k for k, v in
                                                           dataset.instance_map.items()}
                                       })
new_model = package.models.get(model_name=model_name)
```
We'll load the new, un-trained model into the adapter and prepare the training local dataset.  

```python
adapter.load_from_model(model=new_model)
root_path, data_path, output_path = adapter.prepare_training()
```
## Start the Training  
The package, model, and data are now prepared. We are ready to train!  

```python
print("Training {!r} with model {!r} on data {!r}".format(package.name, new_model.id, data_path))
adapter.train(data_path=data_path,
              output_path=output_path)
```
## Save the Model  
We will save the locally-trained model and upload the trained weights to the Item Artifact.  
This will ensure that everything is in the Dataloop platform and everyone can use our trained model.  

```python
adapter.save_to_model(local_path=output_path,
                      replace=True)
```
We can also list all our artifacts associated with this package, and add more files that are needed to load or run the model.  

```python
adapter.model.artifacts.list_content()
```
## Predict on our newly trained model  
With everything in place, we will load our model and view the item's prediction.  

```python
item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
annotations = adapter.predict_items([item], with_upload=True)
image = Image.open(item.download())
plt.imshow(item.annotations.show(np.asarray(image),
                                 thickness=5))
print('Classification: {}'.format(annotations[0][0].label))
```
