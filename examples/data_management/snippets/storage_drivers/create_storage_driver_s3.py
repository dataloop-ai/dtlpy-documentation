import dtlpy as dl

project = dl.projects.get('project_name')
driver = project.drivers.create(name='driver_name',
                                driver_type=dl.ExternalStorage.S3,
                                integration_id='integration_id',
                                bucket_name='bucket_name',
                                allow_external_delete=True,
                                region='eu-west-1',
                                storage_class='',
                                path='')
