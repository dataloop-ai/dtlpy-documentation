def section1():
    import dtlpy as dl
    project = dl.projects.get('prject_name')
    driver = project.drivers.create(name='driver_name',
                                    driver_type=dl.ExternalStorage.S3,
                                    integration_id='integration_id',
                                    bucket_name='bucket_name',
                                    allow_external_delete=True,
                                    region='eu-west-1',
                                    storage_class="",
                                    path="")


def section2():
    # create a dataset from a driver name, you can also create by the driver ID
    import dtlpy as dl
    project: dl.Project
    dataset = project.datasets.create(dataset_name=dataset_name,
                                      driver=driver)
    dataset.sync()
