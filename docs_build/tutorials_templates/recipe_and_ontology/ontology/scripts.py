def section1():
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


def section2():
    project = dl.projects.get(project_name='project_name')
    ontology = project.ontologies.create(title="your_created_ontology_title",
                                         labels=[dl.Label(tag="Chameleon", color=(255, 0, 0))])


def section3():
    ontology.add_labels(label_list=['Shark', 'Whale', 'Animal.Donkey'], update_ontology=True)


def section4():
    child_label = ontology.labels[-1].children[0]
    print(child_label.tag, child_label.rgb)


def section5():
    # checkbox attribute
    ontology.update_attributes(key='color',
                               title='Choose a color',
                               attribute_type=dl.AttributesTypes.CHECKBOX,
                               values=['red', 'blue', 'green'],
                               scope=['<label1>', '<label2>'])

    # radio button attribute
    ontology.update_attributes(key='occluded',
                               title='Level of occlusion',
                               attribute_type=dl.AttributesTypes.RADIO_BUTTON,
                               values=['no', 'mid', 'high'],
                               scope=['*'])

    # slider attribute
    ontology.update_attributes(key='height',
                               title='Persons height[cm]',
                               attribute_type=dl.AttributesTypes.SLIDER,
                               attribute_range=dl.AttributesRange(0, 200, 10),
                               scope=['*'])

    # yes/no attribute
    ontology.update_attributes(key='female',
                               title='Is mosquito female?',
                               attribute_type=dl.AttributesTypes.YES_NO,
                               scope=['*'])

    # free text attribute
    ontology.update_attributes(key='age',
                               title='How old is the person',
                               attribute_type=dl.AttributesTypes.FREE_TEXT,
                               scope=['*'])


def section6():
    print(ontology.metadata['attributes'])
    keys = [att['key'] for att in ontology.metadata['attributes']]


def section7():
    print(ontology.labels_flat_dict)


def section8():
    list(ontology.labels_flat_dict.keys())
