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


def section6():
    print(ontology.metadata['attributes'])
    keys = [att['key'] for att in ontology.metadata['attributes']]


def section7():
    print(ontology.labels_flat_dict)


def section8():
    list(ontology.labels_flat_dict.keys())
