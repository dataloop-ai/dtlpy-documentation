def section1():
    # Get item from the platform
    item = dataset.items.get(filepath='/your-image-file-path.jpg')

    # Create a builder instance
    builder = item.annotations.builder()

    # Create polygon annotation with label
    # with array of points: [[x1, y1], [x2, y2], ..., [xn, yn]]
    builder.add(annotation_definition=dl.Polygon(geo=[[100, 50],
                                                      [80, 120],
                                                      [110, 130]],
                                                 label='my-label'))

    # create Polyline annotation with label
    builder.add(annotation_definition=dl.Polyline(geo=[[100, 50],
                                                       [80, 120],
                                                       [110, 130]],
                                                  label='my-label'))

    # Upload polygon to the item
    item.annotations.upload(builder)


def section2():
    annotations = item.annotations.list()
    mask_annotation = annotations[0]
    builder = item.annotations.builder()
    builder.add(dl.Polygon.from_segmentation(mask_annotation.geo,
                                             max_instances=2,
                                             label=mask_annotation.label))
    item.annotations.upload(builder)


def section3():
    annotations = item.annotations.list()
    builder = item.annotations.builder()
    # run over all annotation in item
    for annotation in annotations:
        if annotation.type == dl.AnnotationType.SEGMENTATION:
            print("Found binary annotation - id:", annotation.id)
            builder.add(dl.Polygon.from_segmentation(mask=annotation.annotation_definition.geo,
                                                     # binary mask of the annotation
                                                     label=annotation.label,
                                                     max_instances=None))
            annotation.delete()
    item.annotations.upload(annotations=builder)


def section4():
    if annotation.type == dl.AnnotationType.POLYGON:
        print("Found polygon annotation - id:", annotation.id)
        builder.add(dl.Segmentation.from_polygon(geo=annotation.annotation_definition.geo,
                                                 # binary mask of the annotation
                                                 label=annotation.label,
                                                 shape=img.size[::-1]  # (h,w)
                                                 ))
    annotation.delete()
    item.annotations.upload(annotations=builder)
