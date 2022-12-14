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
        dataset_name = 'my-dataset-name'

        # DTLPY-STOP
        project = self.project1
        dataset_name = self.dataset_name1
        # DTLPY-START

        dataset = project.datasets.create(dataset_name=dataset_name)

        # DTLPY-STOP
        self.dataset1 = dataset

    def section2(self):
        project_name = 'my-project-name'
        driver = 'my_driver_name'
        dataset_name = 'my_dataset_name'

        # DTLPY-STOP
        project_name = self.project_name2
        driver = self.driver2
        dataset_name = self.dataset_name2
        # DTLPY-START

        project = dl.projects.get(project_name=project_name)
        # Get your drivers list
        project.drivers.list().print()
        # Create a dataset from a driver name. You can also create by the driver ID.
        dataset = project.datasets.create(driver=driver, dataset_name=dataset_name)

        # DTLPY-STOP
        self.dataset2 = dataset

    def section3(self):
        dataset_id = 'my-dataset-id'

        # DTLPY-STOP
        project = self.project3
        dataset_id = self.dataset_id3
        # DTLPY-START

        datasets = project.datasets.list()
        dataset = project.datasets.get(dataset_id=dataset_id)

        # DTLPY-STOP
        self.dataset3 = dataset

    def section4(self):
        directory = '/directory/name'

        # DTLPY-STOP
        dataset = self.dataset4
        # DTLPY-START

        dataset.items.make_dir(directory=directory)

    def section5(self):
        source_folder = '/source_folder'
        destination_folder = '/destination_folder'
        source_project_name = 'source_project_name'
        source_dataset_name = 'source_dataset_name'
        destination_project_name = 'destination_project_name'
        destination_dataset_name = 'destination_dataset_name'

        # DTLPY-STOP
        source_project_name = self.source_project_name5
        source_dataset_name = self.source_dataset_name5
        source_folder = self.source_folder5
        destination_project_name = self.destination_project_name5
        destination_dataset_name = self.destination_dataset_name5
        destination_folder = self.destination_folder5
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
