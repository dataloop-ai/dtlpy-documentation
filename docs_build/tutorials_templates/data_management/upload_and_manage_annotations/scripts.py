import dtlpy as dl

class Scripts:
    def __init__(self):
        # section1
        self.item_id1 = None
        self.annotation_id1 = None
        self.annotation1 = None
        # section2
        self.project_name2 = None
        self.dataset_name2 = None
        self.local_items_path2 = None
        self.local_annotations_path2 = None
        # section3
        self.dataset3 = None
        self.local_items_path3 = None
        self.local_annotations_path3 = None
        # section4
        self.dataset4 = None
        self.local_items_path4 = None
        self.local_annotations_path4 = None
        # section5
        self.csv_file_path5 = None
        self.dataset5 = None
        self.item_id5 = None

    def section1(self):
        # DTLPY-STOP
        item_id = getattr(self, 'item_id1', 'item_id')
        annotation_id = getattr(self, 'annotation_id1', 'annotation_id')
        # DTLPY-START

        import dtlpy as dl
        item = dl.items.get(item_id=item_id)
        annotation = item.annotations.get(annotation_id=annotation_id)
        annotation.metadata["user"] = True
        annotation.update()

        # DTLPY-STOP
        self.annotation1 = annotation

    def section2(self):
        # DTLPY-STOP
        project_name = getattr(self, 'project_name2', 'project')
        dataset_name = getattr(self, 'dataset_name2', 'dataset')
        local_items_path = getattr(self, 'local_items_path2', r'<items path>')
        local_annotations_path = getattr(self, 'local_annotations_path2', r'<annotation json file path>')
        # DTLPY-START

        import dtlpy as dl
        project = dl.projects.get(project_name=project_name)
        dataset = project.datasets.get(dataset_name=dataset_name)
        dataset.items.upload(local_path=local_items_path,
                             local_annotations_path=local_annotations_path,
                             item_metadata=dl.ExportMetadata.FROM_JSON,
                             overwrite=True)

    def section3(self):
        # DTLPY-STOP
        dataset = getattr(self, 'dataset3', 'dataset')
        local_items_path = getattr(self, 'local_items_path3', r'C:/path/to/items')
        local_annotations_path = getattr(self, 'local_annotations_path3', r'C:/path/to/annotations/file/coco.json')
        # DTLPY-START

        import dtlpy as dl
        converter = dl.Converter()
        converter.upload_local_dataset(
            from_format=dl.AnnotationFormat.COCO,
            dataset=dataset,
            local_items_path=local_items_path,
            # Please make sure the names of the items are the same as written in the COCO JSON file
            local_annotations_path=local_annotations_path
        )

    def section4(self):
        # DTLPY-STOP
        dataset = getattr(self, 'dataset4', 'dataset')
        local_items_path = getattr(self, 'local_items_path4', r'C:/home/project/images_folder/*')
        local_annotations_path = getattr(self, 'local_annotations_path4', r'C:/home/project/annotations_folder')
        # DTLPY-START

        dataset.items.upload(
            # Local path to the items folder
            # If you wish to upload items with your directory tree use : r'C:/home/project/images_folder'
            local_path=local_items_path,
            # Local path to the corresponding annotations - make sure the file names fit
            local_annotations_path=local_annotations_path
        )

    def section5(self):
        # DTLPY-STOP
        csv_file_path = getattr(self, 'csv_file_path5', r'C:/file.csv')
        dataset = getattr(self, 'dataset5', 'dataset')
        item_id = getattr(self, 'item_id5', 'my_item_id')
        # DTLPY-START

        import dtlpy as dl
        import pandas as pd
        # Read CSV file
        df = pd.read_csv(csv_file_path)
        # Get item
        item = dataset.items.get(item_id=item_id)
        builder = item.annotations.builder()
        # Read line by line from the csv file
        for i_row, row in df.iterrows():
            # Create box annotation from csv rows and add it to a builder
            builder.add(annotation_definition=dl.Box(top=row['top'],
                                                     left=row['left'],
                                                     bottom=row['bottom'],
                                                     right=row['right'],
                                                     label=row['label']),
                        object_visible=row['visible'],   # Support hidden annotations on the visible row
                        object_id=row['annotation id'],  # Numbering system that separates different annotations
                        frame_num=row['frame'])
        # Upload all created annotations
        item.annotations.upload(annotations=builder)


    def section5a(self):
        import dtlpy as dl
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


    def section5b(self):
        project = dl.projects.get(project_name='project_name')
        dataset = project.datasets.get(dataset_name='dataset_name')
        item = dataset.items.get(filepath='/my_item.mp4')
        # Using annotation builder
        builder = item.annotations.builder()
        builder.add(annotation_definition=dl.Subtitle(label='<label>', text='<text>'),
                    start_time='<start>',
                    end_time='<end>')



    def section6(self):
        dl.use_attributes_2(True)
        annotation.attributes.update({"ID of the attribute": "value of the attribute"})
        annotation = annotation.update(True)


    def section7(self):
        dl.use_attributes_2(True)
        annotation.attributes.update({"<attribute-id>": number_on_range})
        annotation = annotation.update(system_metadata=True)


    def section8(self):
        dl.use_attributes_2(True)
        annotation.attributes.update({"<attribute-id>": ["selection", "selection"]})
        annotation = annotation.update(system_metadata=True)


    def section9(self):
        dl.use_attributes_2(True)
        annotation.attributes.update({"<attribute-id>": "selection"})
        annotation = annotation.update(system_metadata=True)


    def section10(self):


        dl.use_attributes_2(True)
        annotation.attributes.update({"<attribute-id>": True / False})
        annotation = annotation.update(system_metadata=True)


    def section11(self):
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


    def section12(self):
        # Must input an image or height and width
        annotation.show(image='',
                        height='', width='',
                        annotation_format='dl.ViewAnnotationOptions.*',
                        thickness='',
                        with_text='')


    def section13(self):
        dataset.download(local_path=r'C:/home/project/images',  # The default value is ".dataloop" folder
                         annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)


    def section14(self):
        dataset.download(local_path=r'C:/home/project/images',  # The default value is ".dataloop" folder
                         annotation_options=[dl.VIEW_ANNOTATION_OPTIONS_MASK,
                                             dl.VIEW_ANNOTATION_OPTIONS_JSON,
                                             dl.ViewAnnotationOptions.INSTANCE])


    def section15(self):
        # Filter items from "folder_name" directory
        item_filters = dl.Filters(resource='items', field='dir', values='/dog_name')
        # Filter items with dog annotations
        annotation_filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION, field='label', values='dog')
        dataset.download(local_path=r'C:/home/project/images',  # The default value is ".dataloop" folder
                         filters=item_filters,
                         annotation_filters=annotation_filters,
                         annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)


    def section16(self):
        item = dataset.items.get(item_id="item_id")  # Get item from dataset to be able to view the dataset colors on Mask
        # Filter items with dog annotations
        annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
        item.download(local_path=r'C:/home/project/images',  # the default value is ".dataloop" folder
                      annotation_filters=annotation_filters,
                      annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)


    def section17(self):
        # Filter items from "folder_name" directory
        item_filters = dl.Filters(resource='items', field='dir', values='/dog_name')
        # Filter items with dog annotations
        annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
        converter = dl.Converter()
        converter.convert_dataset(dataset=dataset,
                                  # Use the converter of choice
                                  # to_format='yolo',
                                  # to_format='voc',
                                  to_format='coco',
                                  local_path=r'C:/home/coco_annotations',
                                  filters=item_filters,
                                  annotation_filters=annotation_filters)


    def section18(self):
        # Param export_version will be set to ExportVersion.V1 by default.
        dataset.download(local_path='/path',
                         annotation_options='json',
                         export_version=dl.ExportVersion.V2)


    def section19(self):
        from PIL import Image
        item = dl.items.get(item_id='my-item-id')
        array = item.download(save_locally=False, to_array=True)
        # Check out the downloaded Ndarray with these commands - optional
        image = Image.fromarray(array)
        image.save(r'C:/home/project/images.jpg')
