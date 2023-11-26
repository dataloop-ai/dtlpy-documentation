def section1():
    # Set the source item with the annotations we want to copy
    project = dl.projects.get(project_name='second-project_name')
    dataset = project.datasets.get(dataset_name='second-dataset_name')

    item = dataset.items.get(item_id='first-id-number')
    annotations = item.annotations.list()

    # Set the target item where we want to copy to. If located on a different Project or Dataset, set these accordingly
    item = dataset.items.get(item_id='second-id-number')
    item.annotations.upload(annotations=annotations)
    # Copy the annotation into multiple items, based on a filter entity. In this example, the filter is based on directory
    filters = dl.Filters()
    filters.add(field='filename', values='/fighting/**')  # take files from the directory only (recursive)
    filters.add(field='type', values='file')  # only files
    pages = dataset.items.list(filters=filters)
    for page in pages:
        for item in page:
            # upload annotations
            item.annotations.upload(annotations=annotations)


def section2():
    from PIL import Image
    # Get item
    item = dataset.items.get(item_id='write-your-id-number')
    # download item as a buffer
    buffer = item.download(save_locally=False)
    # open image
    image = Image.open(buffer)
    # download annotations
    annotations = item.annotations.show(width=image.size[0],
                                        height=image.size[1],
                                        thickness=3)
    annotations = Image.fromarray(annotations.astype(np.uint8))
    # show the annotations and the image separately
    annotations.show()
    image.show()
    # Show the annotations with the image
    image.paste(annotations, (0, 0), annotations)
    image.show()


def section3():
    from PIL import Image
    import json
    with open(r'C:/home/project/images/annotation.json', 'r') as f:
        data = json.load(f)
    for annotation in data['annotations']:
        annotations = dl.Annotation.from_json(annotation)
        mask = annotations.show(width=640,
                                height=480,
                                thickness=3,
                                color=(255, 0, 0))
        mask = Image.fromarray(mask.astype(np.uint8))
        mask.show()


def section4():
    # Create annotations filters instance
    filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
    filters.page_size = 0
    # Count the annotations
    annotations_count = dataset.annotations.list(filters=filters).items_count


def section5():
    builder = item.annotations.builder()
    builder.add(annotation_definition=dl.Box(top=10, left=10, bottom=100, right=100,
                                             label='my-parent-label'))
    # upload parent annotation
    annotations = item.annotations.upload(annotations=builder)
    # create the child annotation
    builder = item.annotations.builder()
    builder.add(annotation_definition=dl.Box(top=10, left=10, bottom=100, right=100,
                                             label='my-child-label'),
                parent_id=annotations[0].id)
    # upload annotations to item
    item.annotations.upload(annotations=builder)


def section6():
    # create and upload parent annotation
    builder = item.annotations.builder()
    builder.add(annotation_definition=dl.Box(top=10, left=10, bottom=100, right=100,
                                             label='my-parent-label'))
    parent_annotation = item.annotations.upload(annotations=builder)[0]
    # create and upload child annotation
    builder = item.annotations.builder()
    builder.add(annotation_definition=dl.Box(top=10, left=10, bottom=100, right=100,
                                             label='my-child-label'))
    child_annotation = item.annotations.upload(annotations=builder)[0]
    # set the child parent ID to the parent
    child_annotation.parent_id = parent_annotation.id
    # update the annotation
    child_annotation.update(system_metadata=True)


def section7():
    # Create a new label
    dataset.add_label(label_name='newLabel', color=(2, 43, 123))
    # Filter annotations with the "oldLabel" label.
    filters = dl.Filters()
    filters.resource = dl.FiltersResource.ANNOTATION
    filters.add(field='label', values='oldLabel')
    pages = dataset.annotations.list(filters=filters)
    # Change the Label of the Annotations - For every annotation we filtered out, Change it's Label to the "newLabel".

    for annotation in pages.all():
        annotation.label = 'newLabel'
        annotation.update()
