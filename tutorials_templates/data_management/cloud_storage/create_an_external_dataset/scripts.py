def section1():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    organization = dl.organizations.get(organization_name=org_name)
    with open(r"C:\gcsfile.json", 'r') as f:
        gcs_json = json.load(f)
    gcs_to_string = json.dumps(gcs_json)
    organization.integrations.create(name='gcsintegration',
                                     integrations_type=dl.ExternalStorage.GCS,
                                     options={'key': '',
                                              'secret': '',
                                              'content': gcs_to_string})


def section2():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    organization = dl.organizations.get(organization_name='my-org')
    organization.integrations.create(name='S3integration', integrations_type=dl.ExternalStorage.S3,
                                     options={'key': "my_key", 'secret': "my_secret"})


def section3():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    organization = dl.organizations.get(organization_name='my-org')
    organization.integrations.create(name='azureintegration',
                                     integrations_type=dl.ExternalStorage.AZUREBLOB,
                                     options={'key': 'my_key',
                                              'secret': 'my_secret',
                                              'clientId': 'my_clientId',
                                              'tenantId': 'my_tenantId'})


def section4():
    # param name: the driver name
    # param driver_type: ExternalStorage.S3, ExternalStorage.GCS , ExternalStorage.AZUREBLOB
    # param integration_id: the integration id
    # param bucket_name: the external bucket name
    # param project_id:
    # param allow_external_delete:
    # param region: relevant only for s3 - the bucket region
    # param storage_class: relevant only for s3
    # param path: Optional. By default, path is the root folder. Path is case sensitive.
    # return: driver object
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


def section5():
    # create a dataset from a driver name, you can also create by the driver ID
    import dtlpy as dl
    project: dl.Project
    dataset = project.datasets.create(dataset_name=dataset_name,
                                      driver=driver)

    dataset.sync()
