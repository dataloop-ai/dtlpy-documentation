def section1():
    import dtlpy as dl
    item = dl.items.get(item_id="")
    annotation = item.annotations.get(annotation_id="")
    annotation.metadata["user"] = True
    annotation.update()


def section2():
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    dataset.items.upload(local_path=r'<items path>',
                         local_annotations_path=r'<annotation json file path>',
                         item_metadata=dl.ExportMetadata.FROM_JSON,
                         overwrite=True)


def section2a():
    import dtlpy as dl
    item = dl.items.get(item_id="")

    # Get the entities to add to the context
    assignment = dl.assignments.get(assignment_id="")

    task = dl.tasks.get(task_id="")
    # OR
    task = assignment.task

    recipe = dl.recipes.get(recipe_id="")
    # OR
    recipe = dl.recipes.get(recipe_id=task.recipe_id)

    # Context dictionary
    context = {'taskId': task.id,
               'assignmentId': assignment.id,
               'recipeId': recipe.id}

    # Create the annotation
    collection = item.annotations.builder()
    collection.add(annotation_definition=dl.Classification(label='Komodo Dragon'),
                   metadata={'system': context})
    item.annotations.upload(annotations=collection)

    # Or Update existing one
    annotation = item.annotations.get(annotation_id="")
    annotation.metadata["system"].update(context)
    annotation.update(system_metadata=True)


def section3():
    import dtlpy as dl
    from dtlpyconverters.uploaders import ConvertersUploader

    converter = ConvertersUploader()
    loop = converter._get_event_loop()

    # Use the converter of choice
    coco_dataset = dl.datasets.get(dataset_id="dataset_id")
    loop.run_until_complete(converter.coco_to_dataloop(dataset=coco_dataset,
                                                       input_items_path=r"C:/path/to/coco/items",
                                                       input_annotations_path=r"C:/path/to/coco/items/annotations",
                                                       # Please make sure the filenames of the items are the same as written in the COCO json file
                                                       coco_json_filename="annotations.json",
                                                       annotation_options=[dl.AnnotationType.BOX,
                                                                           dl.AnnotationType.SEGMENTATION],
                                                       upload_items=True,
                                                       to_polygon=True))

    yolo_dataset = dl.datasets.get(dataset_id="dataset_id")
    loop.run_until_complete(converter.yolo_to_dataloop(dataset=yolo_dataset,
                                                       input_items_path=r"C:/path/to/yolo/items",
                                                       # Please make sure the filenames of the items are the same as the YOLO txt filenames
                                                       input_annotations_path=r"C:/path/to/yolo/items/annotations",
                                                       upload_items=True,
                                                       add_labels_to_recipe=True,
                                                       labels_txt_filepath=r"C:/path/to/yolo/items/labels/labels.txt"))

    voc_dataset = dl.datasets.get(dataset_id='dataset_id')
    loop.run_until_complete(converter.voc_to_dataloop(dataset=voc_dataset,
                                                      input_items_path=r"C:/path/to/voc/items",
                                                      # Please make sure the filenames of the items are the same as the VOC xml filenames
                                                      input_annotations_path=r"C:/path/to/voc/items/annotations",
                                                      upload_items=True,
                                                      add_labels_to_recipe=True))


def section4():
    # Local path to the items folder
    # If you wish to upload items with your directory tree use : r'C:/home/project/images_folder'
    local_items_path = r'C:/home/project/images_folder/*'
    # Local path to the corresponding annotations - make sure the file names fit
    local_annotations_path = r'C:/home/project/annotations_folder'
    dataset.items.upload(local_path=local_items_path,
                         local_annotations_path=local_annotations_path)


def section5():
    import pandas as pd
    # Read CSV file
    df = pd.read_csv(r'C:/file.csv')
    # Get item
    item = dataset.items.get(item_id='my_item_id')
    builder = item.annotations.builder()
    # Read line by line from the csv file
    for i_row, row in df.iterrows():
        # Create box annotation from csv rows and add it to a builder
        builder.add(annotation_definition=dl.Box(top=row['top'],
                                                 left=row['left'],
                                                 bottom=row['bottom'],
                                                 right=row['right'],
                                                 label=row['label']),
                    object_visible=row['visible'],  # Support hidden annotations on the visible row
                    object_id=row['annotation id'],  # Numbering system that separates different annotations
                    frame_num=row['frame'])
    # Upload all created annotations
    item.annotations.upload(annotations=builder)


def section5a():
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    # local path to item
    local_item_path = r'/Users/local/path/to/item.png'
    # local path to vtt
    local_vtt_path = r'/Users/local/path/to/subtitles.vtt'
    # upload item
    item = dataset.items.upload(local_path=local_item_path)

    # upload VTT file - wait until the item finishs uploading
    builder = item.annotations.builder()
    builder.from_vtt_file(filepath=local_vtt_path)
    item.annotations.upload(builder)


def section5b():
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    item = dataset.items.get(filepath='/my_item.mp4')
    # Using annotation builder
    builder = item.annotations.builder()
    builder.add(annotation_definition=dl.Subtitle(label='<label>',
                                                  text='<text>'),
                start_time='<start>',
                end_time='<end>')


def section6():
    dl.use_attributes_2(True)
    annotation.attributes.update({"ID of the attribute": "value of the attribute"})
    annotation = annotation.update(True)


def section7():
    dl.use_attributes_2(True)
    annotation.attributes.update({"<attribute-id>": number_on_range})
    annotation = annotation.update(system_metadata=True)


def section8():
    dl.use_attributes_2(True)
    annotation.attributes.update({"<attribute-id>": ["selection", "selection"]})
    annotation = annotation.update(system_metadata=True)


def section9():
    dl.use_attributes_2(True)
    annotation.attributes.update({"<attribute-id>": "selection"})
    annotation = annotation.update(system_metadata=True)


def section10():
    dl.use_attributes_2(True)
    annotation.attributes.update({"<attribute-id>": True / False})
    annotation = annotation.update(system_metadata=True)


def section11():
    # Use the show function for all annotation types
    box = dl.Box()
    # Must provide all inputs
    box.show(image='',
             thickness='',
             with_text='',
             height='',
             width='',
             annotation_format='',
             color='')


def section12():
    # Must input an image or height and width
    annotation.show(image='',
                    height='', width='',
                    annotation_format='dl.ViewAnnotationOptions.*',
                    thickness='',
                    with_text='')


def section13():
    dataset.download(local_path=r'C:/home/project/images',  # The default value is ".dataloop" folder
                     annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)


def section14():
    dataset.download(local_path=r'C:/home/project/images',  # The default value is ".dataloop" folder
                     annotation_options=[dl.VIEW_ANNOTATION_OPTIONS_MASK,
                                         dl.VIEW_ANNOTATION_OPTIONS_JSON,
                                         dl.ViewAnnotationOptions.INSTANCE])


def section15():
    # Filter items from "folder_name" directory
    item_filters = dl.Filters(resource='items', field='dir', values='/dog_name')
    # Filter items with dog annotations
    annotation_filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION, field='label', values='dog')
    dataset.download(local_path=r'C:/home/project/images',  # The default value is ".dataloop" folder
                     filters=item_filters,
                     annotation_filters=annotation_filters,
                     annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)


def section16():
    item = dataset.items.get(item_id="item_id")  # Get item from dataset to be able to view the dataset colors on Mask
    # Filter items with dog annotations
    annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
    item.download(local_path=r'C:/home/project/images',  # the default value is ".dataloop" folder
                  annotation_filters=annotation_filters,
                  annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)


def section17():
    import dtlpy as dl
    from dtlpyconverters.services import DataloopConverters
    from dtlpyconverters import coco_converters, yolo_converters, voc_converters

    converter = DataloopConverters()
    loop = converter._get_event_loop()

    # DQL Query is optional
    filters = dl.Filters()
    query = filters.prepare()

    # Filter items from "folder_name" directory
    filters = dl.Filters(resource=dl.FiltersResource.ITEM, field=dl.FiltersKnownFields.DIR, values='/dog_name')
    # Filter items with dog annotations (add_join is used to filter by resource annotation)
    filters.add_join(field=dl.FiltersKnownFields.LABEL, values='dog')

    # Use the converter of choice
    coco_dataset = dl.datasets.get(dataset_id='')
    coco_converter = coco_converters.DataloopToCoco(input_annotations_path=r'C:/input/coco',
                                                    output_annotations_path=r'C:/output/coco',
                                                    download_annotations=True,
                                                    filters=filters,
                                                    dataset=coco_dataset)
    loop.run_until_complete(coco_converter.convert_dataset())

    yolo_dataset = dl.datasets.get(dataset_id='')
    yolo_converter = yolo_converters.DataloopToYolo(input_annotations_path=r'C:/input/yolo',
                                                    output_annotations_path=r'C:/output/yolo',
                                                    download_annotations=True,
                                                    filters=filters,
                                                    dataset=yolo_dataset)
    loop.run_until_complete(yolo_converter.convert_dataset())

    voc_dataset = dl.datasets.get(dataset_id='')
    voc_converter = voc_converters.DataloopToVoc(input_annotations_path=r'C:/input/voc',
                                                 output_annotations_path=r'C:/output/voc',
                                                 download_annotations=True,
                                                 filters=filters,
                                                 dataset=voc_dataset)
    loop.run_until_complete(voc_converter.convert_dataset())


def section18():
    # Param export_version will be set to ExportVersion.V1 by default.
    dataset.download(local_path='/path',
                     annotation_options='json',
                     export_version=dl.ExportVersion.V2)


def section19():
    from PIL import Image
    item = dl.items.get(item_id='my-item-id')
    array = item.download(save_locally=False, to_array=True)
    # Check out the downloaded Ndarray with these commands - optional
    image = Image.fromarray(array)
    image.save(r'C:/home/project/images.jpg')
