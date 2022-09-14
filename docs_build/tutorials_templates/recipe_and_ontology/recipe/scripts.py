def section1():
    # Get recipe from a list
    recipe = dataset.recipes.list()[0]
    # Get recipe by ID - ID can be retrieved from the page URL when opening the recipe in the platform
    recipe = dataset.recipes.get(recipe_id='your-recipe-id')

    # Delete recipe - applies only for deleted datasets
    dataset.recipes.get(recipe_id='your-recipe-id').delete()


def section2():
    dataset = project.datasets.get(dataset_name="myDataSet")
    recipe = dataset.recipes.get(recipe_id="recipe_id")
    recipe2 = recipe.clone(shallow=False)


def section3():
    # as objects
    labels = dataset.labels
    # as instance map
    labels = dataset.instance_map


def section4():
    # Add multiple labels
    dataset.add_labels(label_list=['person', 'animal', 'object'])
    # Add single label with specific color and attributes
    dataset.add_label(label_name='person', color=(34, 6, 231))
    # Add single label with a thumbnail/icon
    dataset.add_label(label_name='person', icon_path='/home/project/images/icon.jpg')


def section5():
    # Create Labels list using Label object
    labels = [
        dl.Label(tag='Donkey', color=(255, 100, 0)),
        dl.Label(tag='Mammoth', color=(34, 56, 7)),
        dl.Label(tag='Bird', color=(100, 14, 150))
    ]
    # Add Labels to Dataset
    dataset.add_labels(label_list=labels)
    # or you can also create a recipe from the label list
    recipe = dataset.recipes.create(recipe_name='My-Recipe-name', labels=labels)


def section6():
    label = dl.Label(tag='Fish',
                     color=(34, 6, 231),
                     children=[dl.Label(tag='Shark',
                                        color=(34, 6, 231)),
                               dl.Label(tag='Salmon',
                                        color=(34, 6, 231))]
                     )
    dataset.add_labels(label_list=label)
    # or you can also create a recipe from the label list
    recipe = dataset.recipes.create(recipe_name='My-Recipe-name', labels=labels)


def section7():
    # Option A
    # add father label
    labels = dataset.add_label(label_name="animal", color=(123, 134, 64))
    # add child label
    labels = dataset.add_label(label_name="animal.Dog", color=(45, 34, 164))
    # add grandchild label
    labels = dataset.add_label(label_name="animal.Dog.poodle")

    # Option B: only if you dont have attributes
    # parent and grandparent (animal and dog) will be generated automatically
    labels = dataset.add_label(label_name="animal.Dog.poodle")

    # Option C: with the Big Dict
    nested_labels = [
        {'label_name': 'animal.Dog',
         'color': '#220605',
         'children': [{'label_name': 'poodle',
                       'color': '#298345'},
                      {'label_name': 'labrador',
                       'color': '#298651'}]},
        {'label_name': 'animal.cat',
         'color': '#287605',
         'children': [{'label_name': 'Persian',
                       'color': '#298345'},
                      {'label_name': 'Balinese',
                       'color': '#298651'}]}
    ]
    # Add Labels to the dataset:
    labels = dataset.add_labels(label_list=nested_labels)


def section8():
    dataset.delete_labels(label_names=['Cat', 'Dog'])


def section9():
    # update existing label , if not exist fails
    dataset.update_label(label_name='Cat', color="#000080")
    # update label, if not exist add it
    dataset.update_label(label_name='Cat', color="#fcba03", upsert=True)
