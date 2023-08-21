# Dataloop Dataset Generator  
The DatasetGenerator is a helper class for the dl.Dataset object.  
  
The generator will to list, get, batch and visualize images and annotations easily.  
  
Here are some use-cases and some usage options for the DatasetGenerator:  

```python
from dtlpy.utilities import DatasetGenerator
import dtlpy as dl
dataset = dl.datasets.get(dataset_id='611b86e647fe2f865323007a')
datagen = DatasetGenerator(data_path='train',
                           dataset_entity=dataset,
                           annotation_type=dl.AnnotationType.BOX)
```
## Object detection examples  
We can visualize a specific item using its index:  

```python
datagen.visualize(idx=10)
```
Or visualize five random items from the dataset (if `idx` input is None) :  

```python
for i in range(5):
    datagen.visualize()
```
To add augmentations, we use [imgaug](https://github.com/aleju/imgaug):  

```python
from imgaug import augmenters as iaa
import numpy as np
augmentation = iaa.Sequential([
    iaa.Resize({"height": 256, "width": 256}),
    # iaa.Superpixels(p_replace=(0, 0.5), n_segments=(10, 50)),
    iaa.flip.Fliplr(p=0.5),
    iaa.flip.Flipud(p=0.5),
    iaa.GaussianBlur(sigma=(0.0, 0.8)),
])
tfs = [
    augmentation,
    np.copy,
    # transforms.ToTensor()
]
datagen = DatasetGenerator(data_path='train',
                           dataset_entity=dataset,
                           annotation_type=dl.AnnotationType.BOX,
                           transforms=tfs)
datagen.visualize()
datagen.visualize(10)
```
All of the `DataGenerator` options (from the function docstring):  
  
:param dataset_entity: dl.Dataset entity  
:param annotation_type: dl.AnnotationType - type of annotation to load from the annotated dataset  
:param filters: dl.Filters - filtering entity to filter the dataset items  
:param data_path: Path to Dataloop annotations (root to "item" and "json").  
:param overwrite:  
:param label_to_id_map: dict - {label_string: id} dictionary  
:param transforms: Optional transform to be applied on a sample. list or torchvision.Transform  
:param num_workers:  
:param shuffle: Whether to shuffle the data (default: True) If set to False, sorts the data in alphanumeric order.  
:param seed: Optional random seed for shuffling and transformations.  
:param to_categorical: convert label id to categorical format  
:param class_balancing: if True - performing random over-sample with class ids as the target to balance training data  
:param return_originals: bool - If True, return ALSO images and annotations before transformations (for debug)  
:param ignore_empty: bool - If True, generator will NOT collect items without annotations  
  
  
The output of a single element is a dictionary holding all the relevant information.  
the keys for the DataGen above are: ['image_filepath', 'item_id', 'box', 'class', 'labels', 'annotation_filepath', 'image', 'annotations', 'orig_image', 'orig_annotations']  

```python
print(list(datagen[0].keys()))
```
We'll add the flag to return the origin items to understand better how the augmentations look like.  
Let's set the flag and we can plot:  

```python
import matplotlib.pyplot as plt
datagen = DatasetGenerator(data_path='train',
                           dataset_entity=dataset,
                           annotation_type=dl.AnnotationType.BOX,
                           return_originals=True,
                           shuffle=False,
                           transforms=tfs)
fig, ax = plt.subplots(2, 2)
for i in range(2):
    item_element = datagen[np.random.randint(len(datagen))]
    ax[i, 0].imshow(item_element['image'])
    ax[i, 0].set_title('After Augmentations')
    ax[i, 1].imshow(item_element['orig_image'])
    ax[i, 1].set_title('Before Augmentations')
```
## Segmentation examples  
First we'll load a semantic dataset and view some images and the output structure  
  

```python
dataset = dl.datasets.get(dataset_id='6197985a104eb81cb728e4ac')
datagen = DatasetGenerator(data_path='semantic',
                           dataset_entity=dataset,
                           transforms=tfs,
                           return_originals=True,
                           annotation_type=dl.AnnotationType.SEGMENTATION)
for i in range(5):
    datagen.visualize()
```
Visualize original vs augmented image and annotations mask:  

```python
fig, ax = plt.subplots(2, 4)
for i in range(2):
    item_element = datagen[np.random.randint(len(datagen))]
    ax[i, 0].imshow(item_element['orig_image'])
    ax[i, 0].set_title('Original Image')
    ax[i, 1].imshow(item_element['orig_annotations'])
    ax[i, 1].set_title('Original Annotations')
    ax[i, 2].imshow(item_element['image'])
    ax[i, 2].set_title('Augmented Image')
    ax[i, 3].imshow(item_element['annotations'])
    ax[i, 3].set_title('Augmented Annotations')
```
Converting to 3d one-hot encoding to visualize the binary mask per label. We will plot only 8 labels (there might be more on the item):  

```python
item_element = datagen[np.random.randint(len(datagen))]
annotations = item_element['annotations']
unique_labels = np.unique(annotations)
one_hot_annotations = np.arange(len(datagen.id_to_label_map)) == annotations[..., None]
print('unique label indices in the item: {}'.format(unique_labels))
print('unique labels in the item: {}'.format([datagen.id_to_label_map[i] for i in unique_labels]))
plt.figure()
plt.imshow(item_element['image'])
fig = plt.figure()
for i_label_ind, label_ind in enumerate(unique_labels[:8]):
    ax = fig.add_subplot(2, 4, i_label_ind + 1)
    ax.imshow(one_hot_annotations[:, :, label_ind])
    ax.set_title(datagen.id_to_label_map[label_ind])
```
## Setting a label map  
One of the inputs to the DatasetGenerator is 'label_to_id_map'. This variable can be used to change the label mapping for the annotations  
and allow using the dataset ontology in a greater variety of cases.  
For example, you can map multiple labels so a single id or add a default value for all the unlabeled pixels in segmentation annotations.  
This is what the annotation looks like without any mapping:  

```python
# project = dl.projects.get(project_name='Semantic')
# dataset = project.datasets.get(dataset_name='Hamster')
# dataset.items.upload(local_path='assets/images/hamster.jpg',
#                      local_annotations_path='assets/images/hamster.json')
dataset = dl.datasets.get(dataset_id='621ddc855c2a3d151451ec58')
datagen = DatasetGenerator(data_path='semantic',
                           dataset_entity=dataset,
                           return_originals=True,
                           overwrite=True,
                           annotation_type=dl.AnnotationType.SEGMENTATION)
datagen.visualize()
data_item = datagen[0]
plt.imshow(data_item['annotations'])
print('BG value: {}'.format(data_item['annotations'][0, 0]))
```
Now, we'll map both the 'eye' label and the background to 2 and the 'fur' to 1:  

```python
dataset = dl.datasets.get(dataset_id='6197985a104eb81cb728e4ac')
label_to_id_map = {'cat': 1,
                   'dog': 1,
                   '$default': 0}
dataloader = DatasetGenerator(data_path='semantic',
                              dataset_entity=dataset,
                              transforms=tfs,
                              return_originals=True,
                              label_to_id_map=label_to_id_map,
                              annotation_type=dl.AnnotationType.SEGMENTATION)
for i in range(5):
    dataloader.visualize()
```
## Batch size and batch_size and collate_fn  
If batch_size is not None, the returned structure will be a list with batch_size data items.  
Setting a collate function will convert the returned structure to a tensor of any kind.  
The default collate will convert everything to ndarrays. We also have tensorflow and torch collate to convert to the corresponding tensors.  

```python
dataset = dl.datasets.get(dataset_id='611b86e647fe2f865323007a')
datagen = DatasetGenerator(data_path='train',
                           dataset_entity=dataset,
                           batch_size=10,
                           annotation_type=dl.AnnotationType.BOX)
batch = datagen[0]
print('type: {}, len: {}'.format(type(batch), len(batch)))
print('single element in the list: {}'.format(batch[0]['image']))
# with collate
from dtlpy.utilities.dataset_generators import collate_default
datagen = DatasetGenerator(data_path='train',
                           dataset_entity=dataset,
                           collate_fn=collate_default,
                           batch_size=10,
                           annotation_type=dl.AnnotationType.BOX)
batch = datagen[0]
print('type: {}, len: {}, shape: {}'.format(type(batch['images']), len(batch['images']), batch['images'].shape))
```
