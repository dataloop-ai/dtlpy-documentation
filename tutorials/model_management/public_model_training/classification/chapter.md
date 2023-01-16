# Training a classification model with ResNet  
In this tutorial we will download a public model from the AI library to inference and train on custom data locally.  
Here we will use a ResNet50 model.  
  
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
from dtlpy.ml import train_utils
```
## Create the Package and pretrained Model in your project  
  
First, we create the Model entity for our project. You can view the public models in the public Dataloop Github.  
You can view all publicly available models by using a Filter. Here we will use a ResNet50 model pretrained on the ImageNET dataset.  

```python
filters = dl.Filters(resource=dl.FiltersResource.MODEL, use_defaults=False)
filters.add(field='scope', values='public')
dl.models.list(filters=filters).print()
# get the public model
model = dl.models.get(model_name='pretrained-resnet50')
```
### Run a pretrained model  
We will then "build" a model adapter to get the package code locally and create an instance of the ModelAdapter class. Then we will load the pretrained model and weights into the model adapter.  

```python
package = dl.packages.get(package_id=model.package_id)
adapter = package.build(module_name='model-adapter')
adapter.load_from_model(model_entity=model)
```
### Predict on an item  
Now we can get an item and inference on it with the predict method and upload the annotations. If you would like to see the item and predictions, you can view it locally or you can open the item on the platform and edit it directly there.  

```python
item = dl.items.get(item_id='611e174e4c09acc3c5bb81d3')
annotations = adapter.predict_items([item], with_upload=True)
image = np.asarray(Image.open(item.download()))
plt.imshow(item.annotations.show(image,
                                 thickness=5))
print('Classification: {}'.format(annotations[0][0].label))
item.open_in_web()
```
## Train on new dataset  
Here we will use a public dataset of sheep faces. We create a project and a dataset and upload the data with 4 labels of sheep.  
NOTE: You might need to change the location of the items, which currently points to the root of the documentation repository. If you downloaded the dtlpy documentation repo locally, this should work as is.  

```python
project = dl.projects.create('Sheep Face - Model Mgmt')
dataset = project.datasets.create('Sheep Face')
dataset.to_df()
_ = dataset.items.upload(local_path='../../../../assets/sample_datasets/SheepFace/items/*',
                         local_annotations_path='../../../../assets/sample_datasets/SheepFace/json')
dataset.add_labels(label_list=['Merino', 'Poll Dorset', 'Suffolk', 'White Suffolk'])
```
Now we'll run the "prepare_dataset" method. This will clone and freeze the dataset so that we'll be able to reproduce the training with the same copy of the data. The cloned dataset will be split into subsets, either filtered using DQL or as percentages. In this example, we'll use an 80/20 train validation split.  
  

```python
pages = dataset.items.list()
num_items = pages.items_count
train_proportion = 0.8
val_proportion = 0.2
train_partitions = [0] * round(train_proportion * num_items)
val_partitions = [1] * round(val_proportion * num_items)
partitions = train_partitions + val_partitions
random.shuffle(partitions)
dataset.items.make_dir(directory='/train')
dataset.items.make_dir(directory='/val')
item_count = 0
for item in pages.all():
    if partitions[item_count] == 0:
        item.move(new_path='/train')
    elif partitions[item_count] == 1:
        item.move(new_path='/val')
    item_count += 1
subsets = {'train': dl.Filters(field='dir', values='/train'),
           'validation': dl.Filters(field='dir', values='/val')}
dataset.metadata['system']['subsets'] = {
    'train': json.dumps(dl.Filters(field='dir', values='/train').prepare()),
    'validation': json.dumps(dl.Filters(field='dir', values='/validation').prepare()),
}
dataset.update()
cloned_dataset = train_utils.prepare_dataset(dataset=dataset,
                                             filters=None,
                                             subsets=subsets)
# if you want to lock the dataset for future reproducibility, use:
# cloned_dataset.set_readonly()
```
After partitioning and cloning the data, we will clone the pretrained model to have a starting point for the fine-tuning. We create an artifact where we can save the model weights. We will also indicate the model's configuration will determine some runtime configurations, such as number of epochs. In this tutorial we will train for only 2 epochs.  

```python
artifact = dl.LocalArtifact(filepath='<dummy filepath>',
                            package_name=package.name,
                            model_name='sheep-soft-augmentations')
new_model = model.clone(model_name='sheep-soft-augmentations',
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
```
We'll load the new, untrained model into the adapter and prepare the local dataset to be used for training.  

```python
adapter.load_from_model(model=new_model)
root_path, data_path, output_path = adapter.prepare_training()
```
## Start the training  
The package, model, and data are now prepared. We are ready to train!  

```python
print("Training {!r} with model {!r} on data {!r}".format(package.name, new_model.id, data_path))
adapter.train(data_path=data_path,
              output_path=output_path)
```
## Save the Model  
We will save the locally-trained model and upload the trained weights to the Artifact Item. This ensures that everything is on the Dataloop platform and allows other developers to use our trained model.  

```python
adapter.save_to_model(local_path=output_path,
                      replace=True)
```
We can also list all Artifacts associated with this Package, and add more files that are needed to load or run the model.  

```python
adapter.model.artifacts.list_content()
```
## Predict on our newly trained model  
With everything in place, we will load our model and view an item's prediction.  

```python
item = dl.items.get(item_id='62b327f0da0d04bc7201e48a')
annotations = adapter.predict_items([item], with_upload=True)
image = Image.open(item.download())
plt.imshow(item.annotations.show(image,
                                 thickness=5))
print('Classification: {}'.format(annotations[0][0].label))
```
