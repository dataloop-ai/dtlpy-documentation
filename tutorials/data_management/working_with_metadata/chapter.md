# Working with Metadata: Your Data's Personal Diary 📝

Let's start by getting our project and dataset ready for some metadata magic:

```python
import dtlpy as dl
# Get project and dataset
project = dl.projects.get(project_name="your-project-name")
dataset = project.datasets.get(dataset_name="your-dataset-name")
```

## What's Metadata? Think of it as Your Data's Personality! 🎭

Metadata is like a sticky note system for your data - you can attach any information you want to both items and annotations. It's super powerful for organizing, filtering, and finding your data later. Think of it as giving your data its own social media profile! 

> ⚠️ **Heads Up**: When adding new metadata to an item, it might overwrite existing metadata - kind of like updating your status!

### The Metadata Type Family 👨‍👩‍👧‍👦

Metadata can be stored in different formats, just like how you can express yourself in different ways. Here's the family:

1. 📝 **Strings** 
```python
item.metadata['user'] = {'message': 'Hello, World!'}
annotation.metadata['user'] = {'mood': 'Happy'}
```

1. 🔢 **Numbers**
```python
item.metadata['user'] = {'lucky_number': 42}
annotation.metadata['user'] = {'confidence_score': 0.95}
```

1. ✅ **Booleans**
```python
item.metadata['user'] = {'is_verified': True}
annotation.metadata['user'] = {'needs_review': False}
```

1. 👻 **Null**
```python
item.metadata['user'] = {'secret': None}
```

### Adding Metadata to Items 🏷️

Here's how to give your items some personality:

```python
# Get your item (either by uploading or fetching)
local_path = r'C:/home/project/images/item.mimetype'
item = dataset.items.upload(local_path=local_path)
# or get existing item
# item = dataset.items.get(item_id='your-item-id')

# Add some metadata flair
if 'user' not in item.metadata:
    item.metadata['user'] = dict()
item.metadata['user']['mood'] = 'fantastic'

# Save the changes
item = item.update()
```

### Annotating Your Annotations 🎯

Your annotations can have metadata too:

```python
annotation = dl.annotations.get(annotation_id='your-annotation-id')
annotation.metadata['user'] = {'confidence': 'high', 'reviewed': True}
annotation = annotation.update()
```

### Finding Items with Metadata Magic ✨

Want to find all your 'fantastic' items? Here's how:

```python
# Create your search spell
filters = dl.Filters(resource = dl.FiltersResource.ITEM)
filters.add(field='metadata.user.mood', values='fantastic')

# Find your treasures
pages = dataset.items.list(filters=filters)
for page in pages:
    for item in page:
        print(f"Found a fantastic item: {item.name}")
```

## Pro Tips 💡

1. Keep your metadata organized - think of it as a well-maintained filing system
2. Use consistent keys and values to make filtering easier
3. Don't go overboard - metadata should help you find things, not become a data dump
4. Remember to update your items after changing metadata

Now go forth and make your data more organized and discoverable! 🚀
