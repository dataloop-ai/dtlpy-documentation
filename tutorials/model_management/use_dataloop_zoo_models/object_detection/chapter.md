# Training an Object Detection Model with YOLOv5  
In this tutorial we will download a public model from the AI library to inference and train on custom data locally.  
Here we will use a YOLOv5 model.  
  
Start by installing the following packages if you don't have them installed already. The model adapter will use them later.  
torch  
torchvision  
imgaug  
scikit-image<0.18  
  
Then, import the modules required for the scripts in this tutorial.  

```python
# !pip install torch torchvision imgaug "scikit-image<0.18"
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import dtlpy as dl
import json
from dtlpy.ml import train_utils
```
## Create a Project and a Dataset  
We will use a public fruits dataset. We create a project and a dataset and upload the data with 3 labels of fruit.  
NOTE: You might need to change the location of the items, which currently points to the root of the documentation repository. If you downloaded the dtlpy documentation repo locally, this should work as-is.  
  

```python
project = dl.projects.create('Fruit - Model Mgmt')
dataset = project.datasets.create('Fruit')
dataset.to_df()
_ = dataset.items.upload(local_path='../../../../assets/sample_datasets/FruitImage/items/*',
                         local_annotations_path='../../../../assets/sample_datasets/FruitImage/json')
dataset.add_labels(label_list=['orange', 'banana', 'apple'])
dataset.open_in_web()
```
Now we'll add the train and validation sets to the dataset metadata:  

```python
subsets = {'train': json.dumps(dl.Filters(field='dir', values='/train').prepare()),
           'validation': json.dumps(dl.Filters(field='dir', values='/validation').prepare())}
dataset.metadata['system']['subsets'] = subsets
dataset.update(True)
```
## Clone the Public Model Into Your Project  
We'll get and clone the public yolo pretrained model (you can view the public models in the public Dataloop Github).  
You can view all publicly available models by using a Filter. Here we will use a YOLOv5 model pretrained on the COCO dataset.  
  

```python
import dtlpy as dl
filters = dl.Filters(resource=dl.FiltersResource.MODEL, use_defaults=False)
filters.add(field='scope', values='public')
dl.models.list(filters=filters).to_df()
# get the public model
pretrained_model = dl.models.get(model_name='pretrained-yolo-v5-small')
model = pretrained_model.clone(model_name='fruits-model',
                               dataset=dataset,
                               project_id=project.id,
                               configuration={'batch_size': 16,
                                              'start_epoch': 0,
                                              'num_epochs': 2,
                                              'input_size': 256,
                                              'id_to_label_map': {(v - 1): k for k, v in
                                                                  dataset.instance_map.items()}
                                              })
```
## Train on Your Dataset  
We'll load the new, untrained model into the adapter and prepare the local dataset to be used for training.  

```python
adapter = dl.packages.build(package=model.package,
                            init_inputs={'model_entity': model},
                            module_name='model-adapter')
```
## Start the Training  
The package, model, and data are now prepared. We are ready to train!  

```python
print("Training {!r} on data {!r}".format(model.name, data_path))
adapter.train_model(model=model)
```
We can list all Artifacts associated with this Package, and add more files that are needed to load or run the model.  

```python
adapter.model.artifacts.list_content()
```
## Predict Your Newly Trained Model  
With everything in place, we will load our model and view an item's prediction.  

```python
item = dl.items.get(item_id='6110d4a41467ded7a8c2a23d')
annotations = adapter.predict_items([item], with_upload=True)
image = Image.open(item.download())
plt.imshow(item.annotations.show(image,
                                 thickness=5))
print('Classes found: {}'.format([ann.label for ann in annotations[0]]))
```
