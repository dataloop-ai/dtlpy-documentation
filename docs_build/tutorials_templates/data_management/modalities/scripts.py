import dtlpy as dl

class Scripts:
    def __init__(self):
        # section1
        self.project_name1 = None
        self.dataset_name1 = None
        # section2
        self.dataset2 = None
        self.first_item_id2 = None
        self.second_item_id2 = None
        self.modality_name2 = None
        # section3
        # NOT RUNNABLE
        # section4
        self.dataset4 = None
        # section5
        self.main5 = None

    def section1(self):
        import dtlpy as dl
        if dl.token_expired():
            dl.login()

        project_name = 'project_name'
        dataset_name = 'dataset_name'

        # DTLPY-STOP
        project_name = self.project_name1
        dataset_name = self.dataset_name1
        # DTLPY-START

        project = dl.projects.get(project_name=project_name)
        dataset = project.datasets.get(dataset_name=dataset_name)

    def section2(self):
        first_item_id = 'your-item-id'
        second_item_id = 'your-item-id'
        modality_name = 'your-modality-name'

        # DTLPY-STOP
        dataset = self.dataset2
        first_item_id = self.first_item_id2
        second_item_id = self.second_item_id2
        modality_name = self.modality_name2
        # DTLPY-START

        # Get the first item (main)
        item1 = dataset.items.get(item_id=first_item_id)
        # Get the second item
        item2 = dataset.items.get(item_id=second_item_id)
        # Create modality
        item1.modalities.create(name=modality_name,
                                modality_type=dl.ModalityTypeEnum.OVERLAY,
                                ref=item2.id)
        # Update item to apply changes to platform
        item1.update()

    def section3(self):
        {
            "https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9": [
                "https://images.unsplash.com/photo-1543852786-1cf6624b9987",
                "https://images.unsplash.com/photo-1561948955-570b270e7c36"
            ],
            "/home/items/primary/dogs/dog1.png": [
                "/home/items/modalities/dogs/dog1-mod1.png",
                "/home/items/modalities/dogs/dog1-mod2.png"
            ]
        }

    def section4(self):
        import os
        import dtlpy as dl
        import json
        from concurrent.futures import ThreadPoolExecutor

        # DTLPY-STOP
        dataset = self.dataset4
        # DTLPY-START

        def upload_single(dataset, source, modalities):
            # Upload main item. If it's not a local image - create a URL Link
            if not os.path.isfile(source):
                source = dl.UrlLink(ref=source)
            main_item: dl.Item = dataset.items.upload(local_path=source)

            # Upload the modalities. If it's not a local image - create a URL Link
            modalities = [modality if os.path.isfile(modality) else dl.UrlLink(ref=modality) for modality in modalities]
            modalities_items = dataset.items.upload(local_path=modalities, remote_path='/modalities')
            # create the modalities references
            for modality_item in modalities_items:
                main_item.modalities.create(modality_type=dl.ModalityTypeEnum.OVERLAY,
                                            ref=modality_item.id,
                                            name='{}:{}'.format(modality_item.name, modality_item.id))
            main_item.update(system_metadata=True)

        def main():
            with open('/home/project/images/modalities.json', 'r') as f:
                modalities_layout = json.load(f)
            # Run the following script to upload the modalities
            with ThreadPoolExecutor(max_workers=32) as executor:
                for source, modalities in modalities_layout.items():
                    executor.submit(upload_single,
                                    dataset=dataset,
                                    source=source,
                                    modalities=modalities)
            executor.shutdown()

        if __name__ == "__main__":
            main()

        # DTLPY STOP
        self.main5 = main

    def section5(self):
        # DTLPY-STOP
        main = self.main5
        # DTLPY-START

        main()
