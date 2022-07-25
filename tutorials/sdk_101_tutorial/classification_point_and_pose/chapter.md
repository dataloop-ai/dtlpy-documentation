# Classification  
  
Classify a single item  
  

```python
# Get item from the platform
item = dataset.items.get(filepath='/your-image-file-path.jpg')
# Create a builder instance
builder = item.annotations.builder()
# Classify
builder.add(annotation_definition=dl.Classification(label=label))
# Upload classification to the item
item.annotations.upload(builder)
```
# Classify Multiple Items  
  
Classifying multiple items requires using an Items entity with a filter.  

```python
# mutiple items classification using filter
...
```
# Create a Point Annotation  

```python
# Get item from the platform
item = dataset.items.get(filepath='/your-image-file-path.jpg')
# Create a builder instance
builder = item.annotations.builder()
# Create point annotation with label and attribute
builder.add(annotation_definition=dl.Point(x=100,
                                           y=100,
                                           label='my-label',
                                           attributes={'color': 'red'}))
# Upload point to the item
item.annotations.upload(builder)
```
# Pose Annotation  

```python
# Pose annotation is based on pose template. Create the pose template from the platform UI and use it in the script by its ID
template_id = recipe.get_annotation_template_id(template_name="my_template_name")
# Get item
item = dataset.items.get(filepath='/your-image-file-path.jpg')
# Define the Pose parent annotation and upload it to the item
parent_annotation = item.annotations.upload(
    dl.Annotation.new(annotation_definition=dl.Pose(label='my_parent_label',
                                                    template_id=template_id,
                                                    # instance_id is optional
                                                    instance_id=None)))[0]
# Add child points
builder = item.annotations.builder()
builder.add(annotation_definition=dl.Point(x=x,
                                           y=y,
                                           label='my_point_label'),
            parent_id=parent_annotation.id)
builder.upload()
```
