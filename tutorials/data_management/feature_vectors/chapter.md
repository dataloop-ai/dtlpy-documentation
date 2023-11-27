# Feature Vectors

## General

[Feature Vectors](https://en.wikipedia.org/wiki/Feature_(machine_learning)) are numeric representations of an entity.
Entities can be an item, an annotation Features are described using vectors which can be of any length.
For example, image embedding using a pre-trained model can produce a feature vector of size of 1024 for resnet (for
example).

A Feature can exist for an item or annotation, representing feature relevant for the entity.

## Feature Set

Feature vectors can be grouped in a "feature set". A feature set contains the metadata for describing a set of feature
vectors, and includes general information about the features.
Feature sets can be the aforementioned "scores", or they can be products of a model. In the example of images, images
can be input into models, and models will output a feature vector for that image that is a numeric a representation of
the image.
Example

```json
{
    "id": "af1e7fcf-29c7-4b5b-8702-ec97792c891b",
    "type": "model",
    "entityType": "item",
    "project": "8b45d2f7-ebae-4f85-bbf6-35c40565c396",
    "creator": "or@dataloop.ai",
    "createdAt": "2021-06-28T17:27:11.012Z",
    "updatedAt": "2021-06-28T17:27:11.012Z",
    "updatedBy": "or@dataloop.ai",
    "name": "inceptionv3",
    "size": 2056,
    "url": "https://dev-gate.dataloop.ai/api/v1/features/sets/af1e7fcf-29c7-4b5b-8702-ec97792c891b"
}
```

## Feature Vector

A single feature vector is the vector itself - the new representation of the entity - with a pointer to the feature set
and the entity it was created from.

Example:

```json
{
    "id": "b5212bda-acdf-4cfd-86f7-76a19f19436c",
    "entityId": "60d36af50f8f90fa6f677ea1",
    "project": "8b45d2f7-ebae-4f85-bbf6-35c40565c396",
    "creator": "or@dataloop.ai",
    "createdAt": "2021-06-28T19:19:03.587Z",
    "value": [
        1,
        2,
        3,
        4
    ],
    "featureSetId": "af1e7fcf-29c7-4b5b-8702-ec97792c891b",
    "version": "1.0.0",
    "url": "https://dev-gate.dataloop.ai/api/v1/features/vectors/b5212bda-acdf-4cfd-86f7-76a19f19436c"
}
```

## Child Vectors

A sub-feature is a dimension reduction of featureVector
Sub-feature is simply a featureVector with additional fields:
parentId - the parent feature vector id from which it was reduced
FeatureSetID - can indicate different type, i.e. the reduction algo.

## Create, Get, Delete

First we need to create a feature set on a project.
Creating a set using the SDK:

```python
import dtlpy as dl

project = dl.projects.get(project_id='60c8561b374417847ff59fba')
feature_set = project.feature_sets.create(name='inceptionv3',
                                          set_type='model',
                                          entity_type='item',
                                          size=2056)
```

Now we can add feature vectors for items using InceptionV3

```python
import keras.applications.inception_v3
import keras.backend as K
import cv2

model = keras.applications.inception_v3.InceptionV3(include_top=True)
K.get_session()
layer_ind = -2

get_activations = K.function(model.layers[0].input, [model.layers[layer_ind].output])
dataset = dl.datasets.get()
items = dataset.items.list()
pbar = tqdm.tqdm(total=items.items_count)

for item in items.all():
    image = item.download(to_array=True)
    input_tensor = cv2.resize(preprocess_batch(image.astype(float)), (299, 299))
    feat = get_activations(input_tensor[None, ...])
    feature = feature_set.features.create(value=feat[0][0],
                                          entity_id=item.id,
                                          version='1.0.0')
    pbar.update()
```

After that, GEt and DELETE are easy, same as all other SDK enetities:

```python
import dtlpy as dl

feature_set = dl.feature_sets.get(feature_set_name='inceptionv3')
feature_set.delete()

```

Getting the feature vector value from of a single item

```python
item = dl.items.get(item_id='618126e38f1fa2b52ae96d05')
item.features.list().print()
```

## Querying

We can query over feature vectors distance

```python

custom_filter = {
    'filter': {'$and': [{'hidden': False}, {'type': 'file'}]},
    'page': 0,
    'pageSize': 1000,
    'resource': 'items',
    'join': {
        'on': {
            'resource': 'feature_vectors',
            'local': 'entityId',
            'forigen': 'id'
        },
        'filter': {
            'value': {
                '$euclid': {
                    'input': [5, 5],
                    '$euclidSort': {'eu_dist': 'ascending'}
                }
            },
            'featureSetId': feature_set.id
        },
    }
}
filters = dl.Filters(custom_filter=custom_filter,
                     resource=dl.FiltersResource.ITEM)

res = dataset.items.list(filters=filters)
print(res.items_count)

for i, f in enumerate(res.items):
    filt = dl.Filters(resource=dl.FiltersResource.FEATURE, field='entityId', values=f.id)
    p = list(feature_set.features.list(filters=filt).all())
    print(p[0].value)
    if i == 10:
        break

```
