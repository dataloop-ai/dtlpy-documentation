import dtlpy as dl


class Scripts:
    def __init__(self):
        # section1
        self.project1 = None
        self.dataset_name1 = None
        self.dataset1 = None
        # section2
        self.project_name2 = None
        self.driver2 = None
        self.dataset_name2 = None
        self.dataset2 = None
        # section3
        self.project3 = None
        self.dataset_id3 = None
        self.dataset3 = None
        # section4
        self.dataset4 = None
        # section5
        self.source_project_name5 = None
        self.source_dataset_name5 = None
        self.source_folder5 = None
        self.destination_project_name5 = None
        self.destination_dataset_name5 = None
        self.destination_folder5 = None

    def section1(self):
        # DTLPY-STOP
        project = getattr(self, 'project1', 'project')
        dataset_name = getattr(self, 'dataset_name1', 'my-dataset-name')
        # DTLPY-START

        dataset = project.datasets.create(dataset_name=dataset_name)

        # DTLPY-STOP
        self.dataset1 = dataset

    def section2(self):
        # DTLPY-STOP
        project_name = getattr(self, 'project_name2', 'my-project-name')
        driver = getattr(self, 'driver2', 'my_driver_name')
        dataset_name = getattr(self, 'dataset_name2', 'my_dataset_name')
        # DTLPY-START

        project = dl.projects.get(project_name=project_name)
        # Get your drivers list
        project.drivers.list().print()
        # Create a dataset from a driver name. You can also create by the driver ID.
        dataset = project.datasets.create(driver=driver, dataset_name=dataset_name)

        # DTLPY-STOP
        self.dataset2 = dataset

    def section3(self):
        # DTLPY-STOP
        project = getattr(self, 'project3', 'project')
        dataset_id = getattr(self, 'dataset_id3', 'my-dataset-id')
        # DTLPY-START

        datasets = project.datasets.list()
        dataset = project.datasets.get(dataset_id=dataset_id)

        # DTLPY-STOP
        self.dataset3 = dataset

    def section4(self):
        # DTLPY-STOP
        dataset = getattr(self, 'dataset4', 'dataset')
        # DTLPY-START

        dataset.items.make_dir(directory='/directory/name')

    def section5(self):
        # DTLPY-STOP
        source_project_name = getattr(self, 'source_project_name5', 'source_project_name')
        source_dataset_name = getattr(self, 'source_dataset_name5', 'source_dataset_name')
        source_folder = getattr(self, 'source_folder5', '/source_folder')
        destination_project_name = getattr(self, 'destination_project_name5', 'destination_project_name')
        destination_dataset_name = getattr(self, 'destination_dataset_name5', 'destination_dataset_name')
        destination_folder = getattr(self, 'destination_folder5', '/destination_folder')
        # DTLPY-START

        copy_annotations = True
        flat_copy = False  # if true, it copies all dir files and sub dir files to the destination folder without sub directories
        # Get source project dataset
        project = dl.projects.get(project_name=source_project_name)
        dataset_from = project.datasets.get(dataset_name=source_dataset_name)
        source_folder = source_folder.rstrip('/')
        # Filter to get all files of a specific folder
        filters = dl.Filters()
        filters.add(field='filename', values=source_folder + '/**')  # Get all items in folder (recursive)
        pages = dataset_from.items.list(filters=filters)
        # Get destination project and dataset
        project = dl.projects.get(project_name=destination_project_name)
        dataset_to = project.datasets.get(dataset_name=destination_dataset_name)
        # Go over all projects and copy file from src to dst
        for page in pages:
            for item in page:
                # Download item (without save to disk)
                buffer = item.download(save_locally=False)
                # Give the item's name to the buffer
                if flat_copy:
                    buffer.name = item.name
                else:
                    buffer.name = item.filename[len(source_folder) + 1:]
                # Upload item
                print("Going to add {} to {} dir".format(buffer.name, destination_folder))
                new_item = dataset_to.items.upload(local_path=buffer, remote_path=destination_folder)
                if not isinstance(new_item, dl.Item):
                    print('The file {} could not be upload to {}'.format(buffer.name, destination_folder))
                    continue
                print("{} has been uploaded".format(new_item.filename))
                if copy_annotations:
                    new_item.annotations.upload(item.annotations.list())
