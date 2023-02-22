def main():
    import dtlpy as dl
    # Get project
    project = dl.projects.get(project_name='project_name')

    # Create item score set
    # DataType must be provided in order for the feature set to support scoring type , itemScore
    # Size must be 1

    itemScoreSet = dl.feature_sets.create(
        project_id=project.id,
        name='my_items_set',
        data_type=dl.FeatureDataType.ITEM_SCORE,
        entity_type=dl.FeatureEntityType.ITEM,
        set_type='score',
        size=1
    )

    # Create annotation score set
    # DataType Must be provided in order for the feature set to support scoring type , annotationScore
    # Size must be 1

    annotationScoreSet = dl.feature_sets.create(
        project_id='projectId',
        name='my_annotations_set',
        data_type=dl.FeatureDataType.ANNOTATION_SCORE,
        entity_type=dl.FeatureEntityType.ANNOTATION,
        set_type='score',
        size=1
    )






