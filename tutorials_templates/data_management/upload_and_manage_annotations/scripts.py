def section1():
    item = dl.items.get(item_id="")
    annotation = item.annotations.get(annotation_id="")
    annotation.metadata["user"] = True
    annotation.update()




def section2():
    import dtlpy as dl
    dataset = project.datasets.get(dataset_name='dataset_name')
    converter = dl.Converter()
    converter.upload_local_dataset(
        from_format=dl.AnnotationFormat.COCO,
        dataset=dataset,
        local_items_path=r'C:/path/to/items', # Please make sure the names of the items are the same as written in the COCO JSON file
        local_annotations_path=r'C:/path/to/annotations/file/coco.json'
    )


def section3():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    # Local path to the items folder
    # If you wish to upload items with your directory tree use : r'C:/home/project/images_folder' 
    local_items_path = r'C:/home/project/images_folder/*' 
    # Local path to the corresponding annotations - make sure the file names fit
    local_annotations_path = r'C:/home/project/annotations_folder'
    dataset.items.upload(local_path=local_items_path,
                            local_annotations_path=local_annotations_path)

def section4():
    import dtlpy as dl
    import pandas as pd
    project = dl.projects.get(project_name='my_project')
    dataset = project.datasets.get(dataset_id='my_dataset')
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
                        object_visible=row['visible'], # Support hidden annotations on the visible row
                        object_id=row['annotation id'], # Numbering system that separates different annotations
                        frame_num=row['frame'])
    # Upload all created annotations
    item.annotations.upload(annotations=builder)

def section5():
    # Use the show function for all annotation types
    box = dl.Box()
    # Must provide all inputs
    box.show(image='', thickness='', with_text='', height='', width='', annotation_format='', color='')

def section6():
    # Must input an image or height and width
    annotation.show(image='', height='', width='', annotation_format='dl.ViewAnnotationOptions.*', thickness='', with_text='')

def section7():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    dataset.download(local_path=r'C:/home/project/images', # The default value is ".dataloop" folder
                    annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON) 

def section8():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    dataset.download(local_path=r'C:/home/project/images', # The default value is ".dataloop" folder
                    annotation_options=[dl.VIEW_ANNOTATION_OPTIONS_MASK, dl.VIEW_ANNOTATION_OPTIONS_JSON, dl.ViewAnnotationOptions.INSTANCE])

def section9():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    # Filter items from "folder_name" directory
    item_filters = dl.Filters(resource='items',field='dir', values='/dog_name')
    # Filter items with dog annotations
    annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
    dataset.download( # The default value is ".dataloop" folder
                    local_path=r'C:/home/project/images',
                    filters = item_filters, 
                    annotation_filters=annotation_filters,
                    annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)

def section10():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    item = dataset.items.get(item_id="item_id") #Get item from dataset to be able to view the dataset colors on Mask
    # Filter items with dog annotations
    annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
    item.download( # the default value is ".dataloop" folder
                    local_path=r'C:/home/project/images',
                    annotation_filters=annotation_filters,
                    annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)

def section11():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')
    # Filter items from "folder_name" directory
    item_filters = dl.Filters(resource='items',field='dir', values='/dog_name')
    # Filter items with dog annotations
    annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
    converter = dl.Converter()
    converter.convert_dataset(dataset=dataset, to_format='coco',
                            local_path=r'C:/home/coco_annotations', 
                    filters = item_filters, 
                            annotation_filters=annotation_filters)
