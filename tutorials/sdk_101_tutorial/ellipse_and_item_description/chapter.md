## Create Ellipse Annotation  
  

```python
# Get item from the platform
item = dataset.items.get(filepath='/your-image-file-path.jpg')
# Create a builder instance
builder = item.annotations.builder()
# Create ellipse annotation with label - With params for an ellipse; x and y for the center, rx, and ry for the radius and rotation angle:
builder.add(annotations_definition=dl.Ellipse(x=x,
                                              y=y,
                                              rx=rx,
                                              ry=ry,
                                              angle=angle,
                                              label=label))
# Upload the ellipse to the item
item.annotations.upload(builder)
```
## Item Description  
  
Item description is added as a “system annotation”, and serves as a way to save information about the item, that can be seen by anyone accessing it.  
  

```python
# Get item from the platform
item = dataset.items.get(filepath='/your-image-file-path.jpg')
# Add description (update if already exists)- if text is empty it will remove the description from the item
item.set_description(text="this is item description")
```
