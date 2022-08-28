In this chapter we will create an ontology and populate it with labels  
  
## Preparing - Entities setup  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
# Get recipe from list
recipe = dataset.recipes.list()[0]
# Or get specific recipe:
recipe = dataset.recipes.get(recipe_id='id')
# Get ontology from list or create it using the "Create Ontology" script
ontology = recipe.ontologies.list()[0]
# Or get specific ontology:
ontology = recipe.ontologies.get(ontology_id='id')
# Print entities:
recipe.print()
ontology.print()
```
## Create an Ontology  
  

```python
project = dl.projects.get(project_name='project_name')
ontology = project.ontologies.create(title="your_created_ontology_title",
                                     labels=[dl.Label(tag="Chameleon", color=(255, 0, 0))])
```
## Labels  
  
Ontology uses the ‘Labels’  entity, which is a python list object, and as such you can use python list methods such as sort(). Be sure to use ontology.update() after each python list action.  
  

```python
ontology.add_labels(label_list=['Shark', 'Whale', 'Animal.Donkey'], update_ontology=True)
```
Labels can be added with branched hierarchy to facilitate sub-labels at up-to 5 levels.  
Labels hierarchy is created by adding ‘.’ between parent and child labels.  
In the above example, this script will get the Donkey Label:  

```python
child_label = ontology.labels[-1].children[0]
print(child_label.tag, child_label.rgb)
```
## Attributes  
An attribute describes a label, without having to add more labels. For example “Car” is a label, but its color is an attribute. You can add multiple attributes to the ontology, and map it to labels. For example create the “color” attribute once, but have multiple labels use it.  
Attributes can be multiple-selection (e.g checkbox), single selection (radio button), value over slider, a yes/no question and free-text.  
An attribute can be set as a mandatory one, so annotators have to answer it before they can complete the item.  
  
## Add attributes to the ontology  
The following example adds 1 attribute of every type, all as a mandatory attribute:  
* Multiple-choice attribute  
* Single-choice attributes  
* Slider attribute  
* Yes/no question attribute  
* Free text attribute  

```python
# Create CHECKBOX att
ontology.update_attributes(key='1', title='CHECKBOX', attribute_type=dl.AttributesTypes.CHECKBOX,
                           values=['1', '2', '3'], scope=['ontology name'])
# Create RADIO_BUTTON att
ontology.update_attributes(key='2', title='RADIO_BUTTON', attribute_type=dl.AttributesTypes.RADIO_BUTTON,
                           values=['1', '2', '3'], scope=['*'])
# Create SLIDER att
ontology.update_attributes(key='3', title='SLIDER', attribute_type=dl.AttributesTypes.SLIDER,
                           attribute_range=dl.AttributesRange(0, 1, 0.1), scope=['*'])
# Create YES_NO att
ontology.update_attributes(key='4', title='YES_NO', attribute_type=dl.AttributesTypes.YES_NO, scope=['*'])
# Create FREE_TEXT att
ontology.update_attributes(key='5', title='FREE_TEXT', attribute_type=dl.AttributesTypes.FREE_TEXT, scope=['*'])
```
## Read Ontology Attributes  
Read & print the all the ontology attributes:  
  

```python
print(ontology.metadata['attributes'])
keys = [att['key'] for att in ontology.metadata['attributes']]
```
## Getting all labels is (including children):  
  

```python
print(ontology.labels_flat_dict)
```
