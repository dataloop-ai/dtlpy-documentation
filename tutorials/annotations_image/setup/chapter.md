# Setup  
  
This tutorial guides you through the process using the Dataloop SDK to create and upload annotations into items.  
The tutorial includes chapters with different tools, and the last chapter includes various more advanced scripts  
- [Classification Point & Pose](../classification_point_and_pose/chapter.md)  
- [Bounding Box & Cuboid](../bounding_box_and_cuboid/chapter.md)  
- [Polygon & Polyline](../polygon_and_polyline/chapter.md)  
- [Ellipse & Item-Description](../ellipse_and_item_description/chapter.md)  
- [Advanced Tutorials](../advance_tutorials/chapter.md)  
    - [Copy Annotations Between Items](../advance_tutorials/chapter.md#copy-annotations-between-items)  
    - [Show Images & Annotations](../advance_tutorials/chapter.md#show-images--annotations)  
    - [Show Annotations from JSON file](../advance_tutorials/chapter.md#show-annotations-from-json-file-dataloop-format)  
    - [Count the Total Number of Annotations in a Dataset](../advance_tutorials/chapter.md#count-total-number-of-annotations)  
    - [Parenting Annotations](../advance_tutorials/chapter.md#parenting-annotations)  
    - [Change Annotation's Label to a New Label](../advance_tutorials/chapter.md#change-annotations-label)  
  
  
  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
```
## Initiation  
Using the annotation definitions classes you can create, edit, view and upload platform annotations. Each annotation init receives the coordinates for the specific type, label, and optional attributes.  
  
## Optional Plotting  
Before updating items with annotations, you can optionally plot the annotation you created and review it before uploading it. This applies to all annotations described in the following section.  
  

```python
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(builder.show())
for annotation in builder:
    plt.figure()
    plt.imshow(annotation.show())
    plt.title(annotation.label)
```
