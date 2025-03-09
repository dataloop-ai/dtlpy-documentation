# Understanding Feature Vectors in Dataloop 🧬

Welcome to your guide to working with feature vectors in Dataloop! Whether you're working with image embeddings, text representations, or custom features, we've got you covered. Let's dive into the world of vector representations!

## What Are Feature Vectors? 🤔

[Feature vectors](https://en.wikipedia.org/wiki/Feature_(machine_learning)) are like DNA sequences for your data - they capture the essential characteristics of items or annotations in numerical form. Think of them as a unique fingerprint that helps machines understand and compare your data.

### Key Concepts 🎯

* **Representation**: Feature vectors can describe anything - images, text, or even customer profiles
* **Flexibility**: Vectors can be any length, depending on what you need
* **Versatility**: They can come from raw data or AI models

### Real-World Examples 🌟

1. **Image Embeddings** 🖼️
   ```
   ResNet model → Image → [0.2, 0.8, ..., 0.5] (1024 dimensions)
   ```

2. **Text Embeddings** 📝
   ```
   BERT model → Text → [0.1, 0.3, ..., 0.7] (768 dimensions)
   ```

3. **Customer Profile** 👤
   ```
   Customer Data → [Age, Income, Years, Purchases, Value]
   Example: [35, 75000, 5, 20, 150]
   ```

## Working with Feature Sets 📦

### What is a Feature Set?

Think of a Feature Set as a container for your feature vectors. It holds:
- The vectors themselves
- Metadata about the features
- Information about size and type
- Connection to models (optional)

### Creating Your First Feature Set ✨

Let's start with the basics:

```python
import dtlpy as dl

# Get your project
project = dl.projects.get(project_id='your-project-id')

# Create a feature set
feature_set = project.feature_sets.create(
    name='text-embeddings-set',
    size=1024,                           # Vector dimension
    set_type='embeddings',
    entity_type=dl.FeatureEntityType.ITEM
)
```

### Connecting to Models 🤖

Want to link your feature set directly to a model? Here's how:

```python
feature_set = project.feature_sets.create(
    name='text-embedding-3',
    set_type='embeddings',
    entity_type=dl.FeatureEntityType.ITEM,
    model_id=project.models.get('my-embedder'),
    size=1536
)
```

## Adding Features to Your Set 🎨

### Using HuggingFace Models

Here's how to generate and add embeddings using HuggingFace:

```python
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
import torch
import dtlpy as dl
import tqdm

# Setup the embedding model
model_name = "BAAI/bge-large-en"
model_kwargs = {'device': 'cuda' if torch.cuda.is_available() else 'cpu'}
encode_kwargs = {'normalize_embeddings': True}
embeddings = HuggingFaceBgeEmbeddings(
    cache_folder='.cache',
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# Process your dataset
dataset = dl.datasets.get(dataset_id='your-dataset-id')
items = dataset.items.list()
pbar = tqdm.tqdm(total=items.items_count)

for item in items.all():
    # Get text from item
    text = item.download(save_locally=False).read().decode('utf8')
    # Generate embedding
    vector = embeddings.embed_documents([text])[0]
    # Add to feature set
    feature = feature_set.features.create(
        value=vector,
        entity=item
    )
    pbar.update()
```

## Managing Feature Sets 🛠️

### Basic Operations

```python
import dtlpy as dl

# Get a feature set
feature_set = dl.feature_sets.get(feature_set_name='my-embeddings')

# Delete a feature set
feature_set.delete()

# Get features for an item
item = dl.items.get(item_id='your-item-id')
item_features = list(item.features.list().all())
print(f'This item has {len(item_features)} feature vectors')
```


## Exporting Feature Sets 📤

Use the `export` method to export a feature set to a local file.

```python
dataset = dl.datasets.get(dataset_id='my-dataset-id')
dataset.export(local_path='./my-dataset',
               feature_vector_filters=None,
               include_feature_vectors=True)
```


## Finding Similar Items 🔍

### K-Nearest Neighbors Search

Want to find similar items? Here's how to query by vector similarity:

```python
# Your query vector
vector = [3, 1, 4, 1, 5, ..., 9]
k = 100  # Number of neighbors to find

# Setup the query
custom_filter = {
    'filter': {'$and': [{'hidden': False}, {'type': 'file'}]},
    'page': 0,
    'pageSize': k,
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
                    'input': vector,
                    '$euclidSort': {'eu_dist': 'ascending'}
                }
            },
            'featureSetId': feature_set.id
        },
    }
}

# Execute the search
filters = dl.Filters(
    custom_filter=custom_filter,
    resource=dl.FiltersResource.ITEM
)

results = dataset.items.list(filters=filters)

for i_item, item in enumerate(res.items):
    print(f"Similar item found: {item.name}")
    # get the feature vector value for the item
    vector_filter = dl.Filters(resource=dl.FiltersResource.FEATURE, field='entityId', values=item.id)
    vector = list(feature_set.features.list(filters=vector_filter).all())
    print(vector[0].value)
    if i_item == 10:
        break
```

### Distance-Based Search 📏

Need items within a specific distance? Use a distance threshold:

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
                    'input': "string || number[], // feature vector ID || actual vectors value",
                    '$euclidFilter': {
                        "optional - $eq || $lte || otherSupportedOperators": "number - other vector's value to calculate distance between them"
                    },
                    '$euclidSort': {'eu_dist': 'ascending'}
                }
            },
            'featureSetId': feature_set.id
        },
    }
}
```

## Best Practices 💡

1. **Vector Size**: Choose appropriate dimensions for your use case
2. **Normalization**: Consider normalizing vectors for better comparison
3. **Batch Processing**: Use batching for large datasets
4. **Model Selection**: Choose the right embedding model for your data type
5. **Index Management**: Consider the trade-off between search speed and accuracy

## Need More Help? 🤔

Check out our [comprehensive documentation](https://docs.dataloop.ai/docs/welcome) for more details on working with feature vectors.

Happy vectorizing! 🚀


