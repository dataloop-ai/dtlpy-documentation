def main():
    import dtlpy as dl
    # Get project
    project = dl.projects.get(project_name='project_name')

    # Get item
    item = dl.items.get(item_id='item_id')

    # get annotation
    annotation = dl.annotations.get(annotation_id='annotation_id')

    # Create item score
    # Can only accept 1 value -> example [90]
    # Refs are the context of score (vector)
    # Item refs input options: 1-dataset 2-task 3-assignment 4-annotator 5-relative

    itemScore = dl.features.create(
        [90],
        project_id=project.id,
        entity_id=item.id,
        feature_set_id='item_score_set_id',
        refs={'dataset': 'datasetId', 'task': 'taskId'}
    )

    # Create annotation score
    # Can only accept 1 value -> example [90]
    # Refs are the context of score (vector)
    # annotation refs input options: 1-dataset 2-task 3-assignment 4-item 5-annotator 6-relative

    annotationScore = dl.features.create(
        [90],
        project_id=project.id,
        entity_id=annotation.id,
        feature_set_id='annotation_score_set_id',
        refs={'dataset': 'datasetId', 'task': 'taskId', 'item': 'itemId'}
    )


