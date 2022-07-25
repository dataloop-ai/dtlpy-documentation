## Create Box Annotation  
  

```python
# Get item from the platform
item = dataset.items.get(filepath='/your-image-file-path.jpg')
# Create a builder instance
builder = item.annotations.builder()
# Create box annotation with label
builder.add(annotation_definition=dl.Box(top=10,
                                         left=10,
                                         bottom=100,
                                         right=100,
                                         label='my-label'))
# Upload box to the item
item.annotations.upload(builder)
```
## Create a Rotated Bounding Box Annotation  
A rotated box is created by setting its top-left and bottom-right coordinates, and providing its rotation angle.  
  
  

```python
# Get item from the platform
item = dataset.items.get(filepath='/your-image-file-path.jpg')
# Create a builder instance
builder = item.annotations.builder()
# Create box annotation with label
builder.add(annotation_definition=dl.Box(top=10,
                                         left=10,
                                         bottom=100,
                                         right=100,
                                         angle=80,
                                         label='my-label'))
# Upload box to the item
item.annotations.upload(builder)
```
## Convert Semantic Segmentation to Bounding Box  
  
Convert all semantic segmentation annotations in an item into box annotation  
  

```python
annotations = item.annotations.list()
builder = item.annotations.builder()
# run over all annotation in item
for annotation in annotations:
    if annotation.type == dl.AnnotationType.SEGMENTATION:
        print("Found binary annotation - id:", annotation.id)
        builder.add(annotation_definition=annotation.annotation_definition.to_box())
item.annotations.upload(annotations=builder)
```
## Create Cuboid (3D Box) Annotation  
  
Create cuboid annotation in one of two ways :  
  

```python
# A.Bring front and back rectangles and the angel of the cuboid
builder.add(annotation_definition=dl.Cube.from_boxes_and_angle(label="label",
                                                               front_top=100,
                                                               front_left=100,
                                                               front_right=300,
                                                               front_bottom=300,
                                                               back_top=200,
                                                               back_left=200,
                                                               back_right=400,
                                                               back_bottom=400,
                                                               angle=0
                                                               ))
# B.Bring all 8 points of the Cuboid
builder.add(annotation_definition=dl.Cube(label="label",
                                          # front top left point coordinates
                                          front_tl=[200, 200],
                                          # front top right point coordinates
                                          front_tr=[500, 250],
                                          # front bottom right point coordinates
                                          front_br=[500, 550],
                                          # front bottom left point coordinates
                                          front_bl=[200, 500],
                                          # back top left point coordinates
                                          back_tl=[300, 300],
                                          # back top right point coordinates
                                          back_tr=[600, 350],
                                          # back bottom right point coordinates
                                          back_br=[600, 650],
                                          # back bottom left point coordinates
                                          back_bl=[300, 600]
                                          ))
item.annotations.upload(builder)
```
