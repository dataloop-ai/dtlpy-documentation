# Managing Model Annotations: Your AI's Signature 🎨

Ever wondered how to keep track of which annotations came from which model? Let's explore how to add, find, and manage your model's predictions like a pro!

## Adding Your Model's Signature ✍️

Think of model metadata as your AI's signature on its work. Here's how to make your model sign its predictions:

```python
# Get predictions from your model
detections = model.predict(image)

# Create a new annotation collection
collection = item.annotations.builder()

# Add each detection with the model's signature
for detection in detections:
    # Unpack detection results
    x1, y1, x2, y2, label_ind, confidence = detection
    
    # Create the annotation with model's signature
    collection.add(
        # Define the bounding box
        annotation_definition=dl.Box(
            left=x1,
            top=y1,
            right=x2,
            bottom=y2,
            label=model_entity.id_to_label_map[label_ind]
        ),
        # Add model's signature
        model_info={
            'name': model_entity.name,
            'model_id': model_entity.id,
            'confidence': float(confidence)
        }
    )

# Upload the signed annotations
item.annotations.upload(collection)
```

> 💡 **Pro Tip**: The model info gets stored in `annotation.metadata.user.model` - perfect for filtering later!

## Finding Your Model's Work 🔍

### Visual Studio Magic ✨

Want to see all predictions from a specific model? Group annotations by creator in the studio:

![Model Filtering in Studio](../../../../assets/images/model_management/model_studio_filter.png)

### Power Search with SDK 🚀

Find all annotations from your model programmatically:

```python
# Setup
import dtlpy as dl
dl.setenv('prod')

# Get your dataset and model
dataset = dl.datasets.get(dataset_id='your-dataset-id')
model = dl.models.get(model_id='your-model-id')

# Create a filter for your model's annotations
filters = dl.Filters(resource=dl.FILTERS_RESOURCE_ANNOTATION)
filters.add(field='metadata.user.model.name', values=model.name)

# Count your model's annotations
pages = dataset.annotations.list(filters=filters)
print(f'🎯 Found {pages.items_count} annotations from {model.name}!')
```

## Cleaning Up: Delete with Care ⚠️

Need to remove your model's predictions? Here's how:

```python
# Setup your filter
filters = dl.Filters(resource=dl.FILTERS_RESOURCE_ANNOTATION)
filters.add(field='metadata.user.model.name', values=model.name)

# Double check what you're about to delete
pages = dataset.annotations.list(filters=filters)
print(f'⚠️ About to delete {pages.items_count} annotations from {model.name}')

# Get user confirmation
user_input = input("Type 'DELETE' to confirm: ")
if user_input == 'DELETE':
    # Delete the annotations
    dataset.annotations.delete(filters=filters)
    print('✨ Cleanup complete!')
else:
    print('🛑 Operation cancelled')
```

> ⚠️ **Warning**: Deletion is permanent! Always double-check your filters before deleting annotations.

## Best Practices 👑

1. **Organization** 📋
   - Always add model info to annotations
   - Use consistent naming conventions
   - Keep track of model versions

2. **Filtering** 🎯
   - Use specific filters to avoid mistakes
   - Verify filter results before actions
   - Combine filters for precise selection

3. **Safety** 🛡️
   - Backup important annotations
   - Double-check deletion filters
   - Use test runs on small subsets

Happy annotating! 🎨
