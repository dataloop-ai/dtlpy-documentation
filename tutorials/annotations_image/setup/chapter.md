This tutorial guides you through the process using the Dataloop SDK to create and upload annotations into items.  
The tutorial includes chapters with different tools, and the last chapter includes various more advanced scripts  
- Classification & Pose  
- Bounding box & Cuboid  
- Polygon & Polyline  
- Ellipse & Item-Description  
- Advanced tutorials  
    - Copy Annotations Between Items  
    - Show Images & Annotations  
    - Show Annotations from JSON file  
    - Count the Total Number of Annotations in a Dataset  
    - Parenting Annotations  
    - Change Annotation's Label to a New Label  
    - Append Attribute to an Existing Label  
  
## Setup  
  

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
