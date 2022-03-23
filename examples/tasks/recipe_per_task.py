import dtlpy as dl


# Before using recipe-per-task feature, please make sure it is enabled by the Dataloop team on your project

def create_multiple_tasks():
    project_name = "Multiple Recipes"
    dataset_name = "Single Dataset"

    project = dl.projects.create(project_name=project_name)

    # Create a dataset to use with multiple recipes (you can also use an exisitng dataset)
    dataset = project.datasets.create(dataset_name=dataset_name)

    # Create the label sets
    labels_set_1 = [dl.Label(tag='liu kang'),
                    dl.Label(tag='subzero'),
                    dl.Label(tag='scorpion'),
                    dl.Label(tag='raiden')]
    labels_set_2 = [dl.Label(tag='pepperoni'),
                    dl.Label(tag='cheddar'),
                    dl.Label(tag='olives')]
    labels_set_3 = [dl.Label(tag='bulbasaur'),
                    dl.Label(tag='pikachu'),
                    dl.Label(tag='togepi')]

    # Add all labels to the main ontology of the Dataset
    dataset.add_labels(label_list=labels_set_1)
    dataset.add_labels(label_list=labels_set_2)
    dataset.add_labels(label_list=labels_set_3)

    # Create any number of recipes (3 in this example) and add the labels to them
    task_1_recipe = project.recipes.create(project_ids=[project.id],
                                           recipe_name='mortal-combat',
                                           labels=labels_set_1)
    task_2_recipe = project.recipes.create(project_ids=[project.id],
                                           recipe_name='pizza',
                                           labels=labels_set_2)
    task_3_recipe = project.recipes.create(project_ids=[project.id],
                                           recipe_name='pokemon',
                                           labels=labels_set_3)

    # Edit the recipes from Dataloop UI to manage labeling tools, recipe settings etc.

    # Print all recipes in the project
    project.recipes.list().print()

    # Create 3 tasks with different recipes. Tasks can be opened with specific filters, and not necessarily the entire dataset
    task_1 = dataset.tasks.create(task_name='mortal-combat',
                                  assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
                                  recipe_id=task_1_recipe.id,
                                  metadata={'system': {'explicitRecipe': True}})
    task_2 = dataset.tasks.create(task_name='pizza',
                                  assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
                                  recipe_id=task_2_recipe.id,
                                  metadata={'system': {'explicitRecipe': True}})
    task_3 = dataset.tasks.create(task_name='pokemon',
                                  assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
                                  recipe_id=task_3_recipe.id,
                                  metadata={'system': {'explicitRecipe': True}})
    print('TasK name: {!r} with recipe id: {} on dataset name: {}'.format(task_1.name,
                                                                          task_1.recipe_id,
                                                                          task_1.dataset.name))
    print('TasK name: {!r} with recipe id: {} on dataset name: {}'.format(task_2.name,
                                                                          task_2.recipe_id,
                                                                          task_2.dataset.name))
    print('TasK name: {!r} with recipe id: {} on dataset name: {}'.format(task_3.name,
                                                                          task_3.recipe_id,
                                                                          task_3.dataset.name))
