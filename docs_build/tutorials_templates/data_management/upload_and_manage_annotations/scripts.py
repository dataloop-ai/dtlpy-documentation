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
        # section5a
        self.project_name5a = None
        self.dataset_name5a = None
        self.local_item_path5a = None
        self.local_vtt_path5a = None
        # section5b
        self.project_name5b = None
        self.dataset_name5b = None
        self.filepath5b = None
        self.label5b = None
        self.text5b = None
        self.start_time5b = None
        self.end_time5b = None
        # section6
        self.annotation6 = None
        # section7
        self.annotation7 = None
        self.attribute_id7 = None
        self.number_on_range7 = None
        # section8
        self.annotation8 = None
        self.attribute_id8 = None
        # section9
        self.annotation9 = None
        self.attribute_id9 = None
        # section10
        self.annotation10 = None
        self.attribute_id10 = None
        self.true_or_false10 = None
        # section11
        self.image11 = None
        self.thickness11 = None
        self.with_text11 = None
        self.height11 = None
        self.width11 = None
        self.annotation_format11 = None
        self.color11 = None
        # section12
        self.annotation12 = None
        self.image12 = None
        self.height12 = None
        self.width12 = None
        self.thickness12 = None
        self.with_text12 = None
        # section13
        self.dataset13 = None
        self.local_path13 = None
        # section14
        self.dataset14 = None
        self.local_path14 = None
        # section15
        self.dataset15 = None
        self.local_path15 = None
        # section16
        self.dataset16 = None
        self.local_path16 = None
        # section17
        self.dataset17 = None
        self.local_path17 = None
        # section18
        self.dataset18 = None
        self.local_path18 = None
        # section19
        self.item_id19 = None
        self.save_path19 = None

    def section1(self):
        item_id = 'item_id'
        annotation_id = 'annotation_id'

        # DTLPY-STOP
        item_id = self.item_id1
        annotation_id = self.annotation_id1
        # DTLPY-START

        import dtlpy as dl
        item = dl.items.get(item_id=item_id)
        annotation = item.annotations.get(annotation_id=annotation_id)
        annotation.metadata["user"] = True
        annotation.update()

        # DTLPY-STOP
        self.annotation1 = annotation

    def section2(self):
        project_name = 'project_name'
        dataset_name = 'dataset_name'
        local_items_path = r'<items path>'
        local_annotations_path = r'<annotation json file path>'

        # DTLPY-STOP
        project_name = self.project_name2
        dataset_name = self.dataset_name2
        local_items_path = self.local_items_path2
        local_annotations_path = self.local_annotations_path2
        # DTLPY-START

        import dtlpy as dl
        project = dl.projects.get(project_name=project_name)
        dataset = project.datasets.get(dataset_name=dataset_name)
        dataset.items.upload(local_path=local_items_path,
                             local_annotations_path=local_annotations_path,
                             item_metadata=dl.ExportMetadata.FROM_JSON,
                             overwrite=True)

    def section3(self):
        dataset = 'dataset'
        local_items_path = r'C:/path/to/items'
        local_annotations_path = r'C:/path/to/annotations/file/coco.json'

        # DTLPY-STOP
        dataset = self.dataset3
        local_items_path = self.local_items_path3
        local_annotations_path = self.local_annotations_path3
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
        dataset = 'dataset'
        # Local path to the items folder
        # If you wish to upload items with your directory tree use : r'C:/home/project/images_folder'
        local_items_path = r'C:/home/project/images_folder/*'
        # Local path to the corresponding annotations - make sure the file names fit
        local_annotations_path = r'C:/home/project/annotations_folder'

        # DTLPY-STOP
        dataset = self.dataset4
        local_items_path = self.local_items_path4
        local_annotations_path = self.local_annotations_path4
        # DTLPY-START

        dataset.items.upload(
            local_path=local_items_path,
            local_annotations_path=local_annotations_path
        )

    def section5(self):
        csv_file_path = r'C:/file.csv'
        dataset = 'dataset'
        item_id = 'my_item_id'

        # DTLPY-STOP
        csv_file_path = self.csv_file_path5
        dataset = self.dataset5
        item_id = self.item_id5
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
        project_name = 'project_name'
        dataset_name = 'dataset_name'
        local_item_path = r'/Users/local/path/to/item.png'
        local_vtt_path = r'/Users/local/path/to/subtitles.vtt'

        # DTLPY-STOP
        project_name = self.project_name5a
        dataset_name = self.dataset_name5a
        local_item_path = self.local_item_path5a
        local_vtt_path = self.local_vtt_path5a
        # DTLPY-START

        import dtlpy as dl
        project = dl.projects.get(project_name=project_name)
        dataset = project.datasets.get(dataset_name=dataset_name)

        # upload item
        item = dataset.items.upload(local_path=local_item_path)  # local path to item

        # upload VTT file - wait until the item finishes uploading
        builder = item.annotations.builder()
        builder.from_vtt_file(filepath=local_vtt_path)  # local path to vtt
        item.annotations.upload(builder)

    def section5b(self):
        project_name = 'project_name'
        dataset_name = 'dataset_name'
        filepath = '/my_item.mp4'
        label = '<label>'
        text = '<text>'
        start_time = '<start>'
        end_time = '<end>'

        # DTLPY-STOP
        project_name = self.project_name5b
        dataset_name = self.dataset_name5b
        filepath = self.filepath5b
        label = self.label5b
        text = self.text5b
        start_time = self.start_time5b
        end_time = self.end_time5b
        # DTLPY-START

        project = dl.projects.get(project_name=project_name)
        dataset = project.datasets.get(dataset_name=dataset_name)
        item = dataset.items.get(filepath=filepath)
        # Using annotation builder
        builder = item.annotations.builder()
        builder.add(annotation_definition=dl.Subtitle(label=label, text=text),
                    start_time=start_time,
                    end_time=end_time)

    def section6(self):
        annotation = 'annotation'
        # DTLPY-STOP
        annotation = self.annotation6
        # DTLPY-START

        dl.use_attributes_2(True)
        annotation.attributes.update({"ID of the attribute": "value of the attribute"})
        annotation = annotation.update(True)

    def section7(self):
        annotation = 'annotation'
        attribute_id = '<attribute-id>'
        number_on_range = 0.5

        # DTLPY-STOP
        annotation = self.annotation7
        attribute_id = self.attribute_id7
        number_on_range = self.number_on_range7
        # DTLPY-START

        dl.use_attributes_2(True)
        annotation.attributes.update({attribute_id: number_on_range})
        annotation = annotation.update(system_metadata=True)

    def section8(self):
        annotation = 'annotation'
        attribute_id = '<attribute-id>'

        # DTLPY-STOP
        annotation = self.annotation8
        attribute_id = self.attribute_id8
        # DTLPY-START

        dl.use_attributes_2(True)
        annotation.attributes.update({attribute_id: ["selection", "selection"]})
        annotation = annotation.update(system_metadata=True)

    def section9(self):
        annotation = 'annotation'
        attribute_id = '<attribute-id>'

        # DTLPY-STOP
        annotation = self.annotation9
        attribute_id = self.attribute_id9
        # DTLPY-START

        dl.use_attributes_2(True)
        annotation.attributes.update({attribute_id: "selection"})
        annotation = annotation.update(system_metadata=True)

    def section10(self):
        annotation = 'annotation'
        attribute_id = '<attribute-id>'
        true_or_false = True / False

        # DTLPY-STOP
        annotation = self.annotation10
        attribute_id = self.attribute_id10
        true_or_false = self.true_or_false10
        # DTLPY-START

        dl.use_attributes_2(True)
        annotation.attributes.update({attribute_id: true_or_false})
        annotation = annotation.update(system_metadata=True)

    def section11(self):
        image = 'image'
        thickness = 'thickness'
        with_text = 'with_text'
        height = 'height'
        width = 'width'
        annotation_format = 'annotation_format'
        color = 'color'

        # DTLPY-STOP
        image = self.image11
        thickness = self.thickness11
        with_text = self.with_text11
        height = self.height11
        width = self.width11
        annotation_format = self.annotation_format11
        color = self.color11
        # DTLPY-START

        # Use the show function for all annotation types
        box = dl.Box()
        # Must provide all inputs
        box.show(image=image,
                 thickness=thickness,
                 with_text=with_text,
                 height=height,
                 width=width,
                 annotation_format=annotation_format,
                 color=color)

    def section12(self):
        annotation = 'annotation'
        image = 'image'
        height = 'height'
        width = 'width'
        thickness = 'thickness'
        with_text = 'with_text'

        # DTLPY-STOP
        annotation = self.annotation12
        image = self.image12
        height = self.height12
        width = self.width12
        thickness = self.thickness12
        with_text = self.with_text12
        # DTLPY-START

        # Must input an image or height and width
        annotation.show(image=image,
                        height=height, width=width,
                        annotation_format='dl.ViewAnnotationOptions.*',
                        thickness=thickness,
                        with_text=with_text)

    def section13(self):
        dataset = 'dataset'
        local_path = r'C:/home/project/images'

        # DTLPY-STOP
        dataset = self.dataset13
        local_path = self.local_path13
        # DTLPY-START

        dataset.download(local_path=local_path,  # The default value is ".dataloop" folder
                         annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)

    def section14(self):
        dataset = 'dataset'
        local_path = r'C:/home/project/images'

        # DTLPY-STOP
        dataset = self.dataset14
        local_path = self.local_path14
        # DTLPY-START

        dataset.download(local_path=local_path,  # The default value is ".dataloop" folder
                         annotation_options=[dl.VIEW_ANNOTATION_OPTIONS_MASK,
                                             dl.VIEW_ANNOTATION_OPTIONS_JSON,
                                             dl.ViewAnnotationOptions.INSTANCE])

    def section15(self):
        dataset = 'dataset'
        local_path = r'C:/home/project/images'

        # DTLPY-STOP
        dataset = self.dataset15
        local_path = self.local_path15
        # DTLPY-START

        # Filter items from "folder_name" directory
        item_filters = dl.Filters(resource='items', field='dir', values='/dog_name')
        # Filter items with dog annotations
        annotation_filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION, field='label', values='dog')
        dataset.download(local_path=local_path,  # The default value is ".dataloop" folder
                         filters=item_filters,
                         annotation_filters=annotation_filters,
                         annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)

    def section16(self):
        dataset = 'dataset'
        local_path = r'C:/home/project/images'

        # DTLPY-STOP
        dataset = self.dataset16
        local_path = self.local_path16
        # DTLPY-START

        item = dataset.items.get(item_id="item_id")  # Get item from dataset to be able to view the dataset colors on Mask
        # Filter items with dog annotations
        annotation_filters = dl.Filters(resource='annotations', field='label', values='dog')
        item.download(local_path=local_path,  # the default value is ".dataloop" folder
                      annotation_filters=annotation_filters,
                      annotation_options=dl.VIEW_ANNOTATION_OPTIONS_JSON)

    def section17(self):
        dataset = 'dataset'
        local_path = r'C:/home/coco_annotations'

        # DTLPY-STOP
        dataset = self.dataset17
        local_path = self.local_path17
        # DTLPY-START

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
                                  local_path=local_path,
                                  filters=item_filters,
                                  annotation_filter=annotation_filters)

    def section18(self):
        dataset = 'dataset'
        local_path = '/path'

        # DTLPY-STOP
        dataset = self.dataset18
        local_path = self.local_path18
        # DTLPY-START

        # Param export_version will be set to ExportVersion.V1 by default.
        dataset.download(local_path=local_path,
                         annotation_options='json',
                         export_version=dl.ExportVersion.V2)

    def section19(self):
        item_id = 'my-item-id'
        save_path = r'C:/home/project/images.jpg'

        # DTLPY-STOP
        item_id = self.item_id19
        save_path = self.save_path19
        # DTLPY-START

        from PIL import Image
        item = dl.items.get(item_id=item_id)
        array = item.download(save_locally=False, to_array=True)
        # Check out the downloaded Ndarray with these commands - optional
        image = Image.fromarray(array)
        image.save(save_path)
