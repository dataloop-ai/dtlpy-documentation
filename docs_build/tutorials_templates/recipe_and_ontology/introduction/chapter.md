# Recipes and Ontologies: Your Data's Secret Sauce 🧪

Welcome to the world of recipes and ontologies in Dataloop! Think of recipes as your master cookbook 📖 and ontologies as your ingredient lists 📝. Let's dive in and learn how to create the perfect data labeling recipe!

## Understanding the Basics 🎓

### What's a Recipe? 🍳

A recipe in Dataloop is like your cooking instructions - it tells annotators exactly how to label your data. It includes:
- 🔗 Link to an ontology (your ingredients)
- 🛠️ Labeling tools (box, polygon, etc.)
- 📄 Optional PDF instructions
- ✨ And more goodies!

### What's an Ontology? 🌳

An ontology is your structured knowledge base that contains:
- 🏷️ Labels (like "Dog", "Cat", "Car")
- 📊 Attributes (properties like "Color", "Size")
- 🔄 Relationships between labels and attributes

## Working with Recipes 🧑‍🍳

### Basic Recipe Operations

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()

# Get your project and dataset
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')

# Get a recipe from the list
recipe = dataset.recipes.list()[0]

# Get a specific recipe by ID
recipe = dataset.recipes.get(recipe_id='your-recipe-id')

# Delete a recipe (only works on deleted datasets)
dataset.recipes.get(recipe_id='your-recipe-id').delete()
```

### Cloning Recipes 🐑

Need a recipe that's similar to an existing one? Clone it! It's like copying your grandma's recipe and adding your own twist.

```python
# Clone with options:
# shallow=True: Links to existing ontology
# shallow=False: Creates new copies of all linked ontologies
recipe2 = recipe.clone(shallow=False)
```

### Switching Dataset Recipes 🔄

Want to try a different recipe on your dataset? Here's how:

```python
dataset = project.datasets.get(dataset_name="myDataSet")
recipe = dataset.switch_recipe(recipe_id="recipe_id")
```

## Creating Your Ontology 📚

### Starting Fresh

```python
# Create a new ontology with a starter label
ontology = project.ontologies.create(
    title="my_awesome_ontology",
    labels=[dl.Label(tag="Chameleon", color=(255, 0, 0))]
)
```

### Connecting Ontology to an Existing Recipe

```python
recipe.ontology_ids = [ontology.id]
recipe.update()
```

### Getting Ontology related Recipes

```python
filters = dl.Filters(resource=dl.FiltersResource.RECIPE)
filters.add(field="ontologies", values=[ontology.id])  # Don't use dl.FiltersResource.ONTOLGY
recipes = ontology.project.recipes.list(filters=filters)
```

### Adding Labels 🏷️

You've got multiple ways to add labels - pick your favorite!

#### Method 1: Quick Add
```python
# Add multiple labels at once
dataset.add_labels(label_list=['person', 'animal', 'object'])

# Add a single label with style
dataset.add_label(
    label_name='person',
    color=(34, 6, 231),
    icon_path='/home/project/images/icon.jpg'
)
```

#### Method 2: Using Label Objects
```python
# Create fancy labels with colors
labels = [
    dl.Label(tag='Donkey', color=(255, 100, 0)),
    dl.Label(tag='Mammoth', color=(34, 56, 7)),
    dl.Label(tag='Bird', color=(100, 14, 150))
]
dataset.add_labels(label_list=labels)
```

### Creating Label Hierarchies 🌲

Want to organize your labels like a family tree? Here's how:

```python
# Create a parent label with children
label = dl.Label(
    tag='Fish',
    color=(34, 6, 231),
    children=[
        dl.Label(tag='Shark', color=(34, 6, 231)),
        dl.Label(tag='Salmon', color=(34, 6, 231))
    ]
)
dataset.add_labels(label_list=label)
```

### The Big Nested Labels Adventure 🗺️

Want to create complex hierarchies? Try this super-powered approach:

```python
nested_labels = [
    {
        'label_name': 'animal.Dog',
        'color': '#220605',
        'children': [
            {'label_name': 'poodle', 'color': '#298345'},
            {'label_name': 'labrador', 'color': '#298651'}
        ]
    },
    {
        'label_name': 'animal.cat',
        'color': '#287605',
        'children': [
            {'label_name': 'Persian', 'color': '#298345'},
            {'label_name': 'Balinese', 'color': '#298651'}
        ]
    }
]
labels = dataset.add_labels(label_list=nested_labels)
```

## Working with Attributes 🎨

Attributes are like special powers for your labels. They help describe additional properties without creating new labels.

### Types of Attributes

1. ✅ **Checkbox** (Multiple Choice)
```python
ontology.update_attributes(
    key='color',
    title='Choose a color',
    attribute_type=dl.AttributesTypes.CHECKBOX,
    values=['red', 'blue', 'green'],
    scope=['<label1>', '<label2>']
)
```

2. 🔘 **Radio Button** (Single Choice)
```python
ontology.update_attributes(
    key='occluded',
    title='Level of occlusion',
    attribute_type=dl.AttributesTypes.RADIO_BUTTON,
    values=['no', 'mid', 'high'],
    scope=['*']
)
```

3. 🎚️ **Slider**
```python
ontology.update_attributes(
    key='height',
    title='Person height[cm]',
    attribute_type=dl.AttributesTypes.SLIDER,
    attribute_range=dl.AttributesRange(0, 200, 10),
    scope=['*']
)
```

4. ❓ **Yes/No Question**
```python
ontology.update_attributes(
    key='female',
    title='Is mosquito female?',
    attribute_type=dl.AttributesTypes.YES_NO,
    scope=['*']
)
```

5. ✍️ **Free Text**
```python
ontology.update_attributes(
    key='age',
    title='How old is the person',
    attribute_type=dl.AttributesTypes.FREE_TEXT,
    scope=['*']
)
```

## Handy Tips and Tricks 💡

1. **View All Labels**
```python
# Get all labels (including children)
print(ontology.labels_flat_dict)
```

2. **Check Attributes**
```python
# See all attributes
print(ontology.metadata['attributes'])
# Get attribute keys
keys = [att['key'] for att in ontology.metadata['attributes']]
```

3. **Update Labels**
```python
# Update existing label
dataset.update_label(label_name='Cat', color="#000080")
# Update or create if not exists
dataset.update_label(label_name='Cat', color="#fcba03", upsert=True)
```

4. **Delete Labels**
```python
dataset.delete_labels(label_names=['Cat', 'Dog'])
```

## Best Practices 🌟

1. 📝 Plan your ontology structure before creating it
2. 🎨 Use consistent color schemes for related labels
3. 📊 Keep your attribute choices clear and concise
4. 🌳 Don't go too deep with label hierarchies (max 5 levels)
5. 🔄 Test your recipe with a small dataset first

## Need More Help? 🤔

- Check out our [Recipe Documentation](https://docs.dataloop.ai/docs/ontology-overview#recipe)
- Visit our [Ontology Guide](https://docs.dataloop.ai/docs/ontology-overview#ontology)

Happy labeling! 🚀
