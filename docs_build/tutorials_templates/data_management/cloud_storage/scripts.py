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


def section6():
    import os
    import urllib.parse

    # Set dataloop path to tmp (to read/write from the lambda)
    os.environ["DATALOOP_PATH"] = "/tmp"
    import dtlpy as dl

    DATASET_ID = ''
    DTLPY_USERNAME = ''
    DTLPY_PASSWORD = ''

    def lambda_handler(event, context):
        dl.login_m2m(email=DTLPY_USERNAME, password=DTLPY_PASSWORD)
        dataset = dl.datasets.get(dataset_id=DATASET_ID,
                                  fetch=False  # to avoid GET the dataset each time
                                  )

        for record in event['Records']:
            # Get the bucket name
            bucket = record['s3']['bucket']['name']

            # Get the file name
            filename = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')

            if 'ObjectRemoved' in record['eventName']:
                # On delete event - delete the item from Dataloop
                try:
                    dtlpy_filename = '/' + filename
                    filters = dl.Filters(field='filename', values=dtlpy_filename)
                    dataset.items.delete(filters=filters)
                except Exception as e:
                    raise e

            elif 'ObjectCreated' in record['eventName']:
                # On create event - add a new item to the Dataset
                try:
                    # upload the file
                    path = 'external://' + filename
                    # dataset.items.upload(local_path=path, overwrite=True) # if overwrite is required
                    dataset.items.upload(local_path=path)
                except Exception as e:
                    raise e
