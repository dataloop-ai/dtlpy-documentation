import dtlpy as dl
import numpy as np


def polygon2segmentation(item: dl.Item):
    # Get item semantic segmentation and polygon annotations
    filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
    filters.add(field=dl.KnownFields.TYPE,
                values=[dl.AnnotationType.SEGMENTATION, dl.AnnotationType.POLYGON],
                operator=dl.FiltersOperations.IN)
    annotations = item.annotations.list(filters=filters)
    if isinstance(annotations, dl.entities.PagedEntities):
        annotations = annotations.all()
    # Merge all the annotations into masks
    final_masks = dict()
    for annotation in annotations:
        # Get the segmentation annotation mask
        if annotation.type == dl.AnnotationType.SEGMENTATION:
            mask = annotation.geo
        # Convert the polygon to segmentation annotation and get its mask
        else:
            mask = dl.Segmentation.from_polygon(geo=annotation.geo,
                                                label=annotation.label,
                                                shape=(item.height, item.width)).geo
        # Merge the masks
        if annotation.label not in list(final_masks.keys()):
            final_masks[annotation.label] = np.zeros(shape=(item.height, item.width))
        final_masks[annotation.label] = np.logical_or(final_masks[annotation.label], mask)

    # Create a builder instance and add the masks
    builder = item.annotations.builder()
    for label, mask in final_masks.items():
        builder.add(annotation_definition=dl.Segmentation(geo=mask, label=label))
    # Check if there are any annotations to upload
    if len(builder) > 0:
        # Delete previous annotations
        item.annotations.delete(filters=filters)
        # Upload masks to the item
        builder.upload()


if __name__ == '__main__':
    # Get project, dataset and item
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    item = dataset.items.get(filepath='filepath')
    polygon2segmentation(item=item)
