def section1():
    annotations_definition = dl.Segmentation(geo=mask, label=label)


def section2():
    # Get item from the platform
    item = dataset.items.get(filepath='/your-image-file-path.jpg')
    # Create a builder instance
    builder = item.annotations.builder()
    # Create semantic segmentation mask with label and attribute
    mask = np.zeros(shape=(item.height, item.width), dtype=np.uint8)
    # mark some part in the middle
    mask[50:100, 200:250] = 1
    # Add annotations of type segmentation
    builder.add(annotation_definition=dl.Segmentation(geo=mask,
                                                      label='my-label'))
    # Optional: Plot all of the annotations you created before uploading them to the platform
    import matplotlib.pyplot as plt
    plt.figure()
    plt.imshow(builder.show())
    for annotation in builder:
        plt.figure()
        plt.imshow(annotation.show())
        plt.title(annotation.label)
    # Upload semantic segmentation to the item
    item.annotations.upload(builder)


def section3():
    filters = dl.Filters()
    # set resource
    filters.resource = 'items'
    # add filter - only files
    filters.add(field='type', values='file')
    # add annotation filters - only items with 'binary' annotations
    filters.add_join(field='type', values='binary')
    # get results
    pages = dataset.items.list(filters=filters)
    # run over all items in page
    for page in pages:
        for item in page:
            print('item=' + item.id)
            annotations = item.annotations.list()
            builder = item.annotations.builder()
            # run over all annotation in item
            for annotation in annotations:
                # print(annotation)
                if annotation.type == 'binary':
                    print("Found binary annotation - id:", annotation.id)
                    builder.add(dl.Polygon.from_segmentation(mask=annotation.annotation_definition.geo,
                                                             # binary mask of the annotation
                                                             label=annotation.label,
                                                             max_instances=None))
                    annotation.delete()
            item.annotations.upload(annotations=builder)


def section4():
    from PIL import Image
    filters = dl.Filters()
    # set resource
    filters.resource = 'items'
    # add filter - only files
    filters.add(field='type', values='file')

    # add annotation filters - only items with polygon annotations
    filters.add_join(field='type', values='segment')

    # get results
    pages = dataset.items.list(filters=filters)
    # run over all items in page
    for page in pages:
        for item in page:
            print('item=' + item.id)
            annotations = item.annotations.list()
            item = dataset.items.get(item_id=item.id)
            buffer = item.download(save_locally=False)
            img = Image.open(buffer)
            builder = item.annotations.builder()
            # run over all annotation in item
            for annotation in annotations:
                # print(annotation)
                if annotation.type == 'segment':
                    print("Found polygon annotation - id:", annotation.id)
                    builder.add(dl.Segmentation.from_polygon(geo=annotation.annotation_definition.geo,
                                                             # binary mask of the annotation
                                                             label=annotation.label,
                                                             shape=img.size[::-1]  # (h,w)
                                                             ))
                    annotation.delete()
            item.annotations.upload(annotations=builder)


def section5():
    from PIL import Image
    import numpy as np
    import dtlpy as dl
    # Get project and dataset
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    # image filepath
    image_filepath = r'C:/home/images/with_family.png'
    # annotations filepath - RGB with color for each label
    annotations_filepath = r'C:/home/masks/with_family.png'
    # upload item to root directory
    item = dataset.items.upload(local_path=image_filepath,
                                remote_path='/')
    # read mask from file
    mask = np.array(Image.open(annotations_filepath))
    # get unique color (labels)
    unique_colors = np.unique(mask.reshape(-1, mask.shape[2]), axis=0)
    # init dataloop annotations builder
    builder = item.annotations.builder()
    # for each label - create a dataloop mask annotation
    for i, color in enumerate(unique_colors):
        print(color)
        if i == 0:
            # ignore background
            continue
        # get mask of same color
        class_mask = np.all(color == mask, axis=2)
        # add annotation to builder
        builder.add(annotation_definition=dl.Segmentation(geo=class_mask,
                                                          label=str(i)))
        # upload all annotations
        item.annotations.upload(builder)


def section6():
    import dtlpy as dl
    import numpy as np
    # Get project, dataset and item
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    item = dataset.items.get(filepath='file_path')
    # Create a builder instance
    builder = item.annotations.builder()
    # Create a random mask
    mask = np.random.randint(2, size=(item.height, item.width))
    instance_map = ["background", "foreground"]
    # Add convert the instance mask to segmentation annotations
    builder.from_instance_mask(mask=mask, instance_map=instance_map)
    # Upload the annotations to the item
    item.annotations.upload(annotations=builder)


def section7():
    import dtlpy as dl
    import numpy as np
    # Get project, dataset and item
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    item = dataset.items.get(filepath='filepath')
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
        # Get segmentation annotation mask and reference
        if annotation.type == dl.AnnotationType.SEGMENTATION:
            mask = annotation.geo
            segmentation_ref = annotation
        # Convert the polygon to segmentation and get its mask
        else:
            mask = dl.Segmentation.from_polygon(geo=annotation.geo,
                                                label=annotation.label,
                                                shape=(item.height, item.width)).geo
            segmentation_ref = None
        # Merge the masks
        if annotation.label not in list(final_masks.keys()):
            final_masks[annotation.label] = {"mask": mask, "segmentation_ref": segmentation_ref}
        else:
            final_masks[annotation.label]["mask"] = np.logical_or(final_masks[annotation.label]["mask"], mask)
            if segmentation_ref is not None:
                final_masks[annotation.label]["segmentation_ref"] = segmentation_ref
    # Upload masks to the item
    builder = item.annotations.builder()
    for label, mask in final_masks.items():
        annotation = mask["segmentation_ref"]
        if annotation is None:
            builder.add(annotation_definition=dl.Segmentation(geo=mask["mask"], label=label))
        else:
            annotation.geo = mask["mask"]
            annotation.update()
    if len(builder) > 0:
        builder.upload()
        # Delete all the polygon annotations
        polygon_filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
        polygon_filters.add(field=dl.KnownFields.TYPE, values=dl.AnnotationType.POLYGON)
        item.annotations.delete(filters=polygon_filters)
