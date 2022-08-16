# Cloud Storage  
## External Storage Dataset  
  
If you already have your data managed and organized on a cloud storage service, such as GCS/S3/Azure, you may want to  
utilize that with Dataloop, and not upload the binaries and create duplicates.  
  
### Cloud Storage Integration  
  
Access & Permissions - Creating an integration with GCS/S2/Azure cloud requires adding a key/secret with the following  
permissions:  
  
List (Mandatory) - allowing Dataloop to list all of the items in the storage.  
Get (Mandatory) - get the items and perform pre-process functionalities like thumbnails, item info etc.  
Put / Write (Mandatory) - lets you upload your items  
directly to the external storage from the Dataloop platform.  
Delete - lets you delete your items directly from the external storage using the Dataloop platform.  
  
### Create Integration With GCS  
  
### Creating an integration GCS requires having JSON file with GCS configuration.  

```python
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
```
### Create Integration With S3  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
organization = dl.organizations.get(organization_name='my-org')
organization.integrations.create(name='S3integration', integrations_type=dl.ExternalStorage.S3,
                                 options={'key': "my_key", 'secret': "my_secret"})
```
### Create Integration With Azure  

```python
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
```
### Storage Driver  
  
Once you have an integration, you can set up a driver, which adds a specific bucket (and optionally with a specific  
path/folder) as a storage resource.  
  
### Create Drivers in the Platform (browser)  

```python
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
```
Once the integration and drivers are ready, you can create a Dataloop Datsaset and sync all the data:  

```python
# create a dataset from a driver name, you can also create by the driver ID
import dtlpy as dl
project: dl.Project
dataset = project.datasets.create(dataset_name=dataset_name,
                                  driver=driver)
dataset.sync()
```
## Create an AWS Lambda to Continuously Sync a Bucket with Dataloop's Dataset  
  
If you want to catch events from the AWS bucket and update the Dataloop Dataset you need to set up a Lambda.  
The Lambda will catch the AWS bucket events and will reflect them into the Dataloop Platform.  
  
We have prepared an environment zip file with our SDK for python3.8 so you don't need to create anything else to use dtlpy in the lambda.  
  
NOTE: For any other custom use (e.g other python version or more packages) try creating your own layer (We used [this](https://www.geeksforgeeks.org/how-to-install-python-packages-for-aws-lambda-layers) tutorial and the python:3.8 docker image).  
  
### Create the Lambda  
1. Create a new Lambda  
2. The default timeout is 3[s] so we'll need to change to 1[m]:  
    Configuration → General configuration → Edit → Timeout  
3. Copy the following code:  

```python
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
```
### Add a Layer to the Lambda  
We have created an AWS Layer with the Dataloop SDK ready. Click [here](https://storage.googleapis.com/dtlpy/aws-python3.8-lambda-layer/layer.zip) to download the zip file.  
Because the layer's size is larger than 50MB you cannot use it directly (AWS restrictions), but need to upload it to a bucket first.  
Once uploaded, create a new layer for the dtlpy env:  
1. Go to the layers screen and "click Add Layer".  
![add_layer](../../../../assets/aws-lambda-screenshots/create_layer.png)  
2. Choose a name (dtlpy-env).  
3. Use the link to the bucket layer.zip.  
4. Select the env (x86_64, python3.8).  
5. Click "Create" and the bottom on the page.  
  
Go back to your lambda and add the layer:  
1. Select the "Add Layer".  
![add_layer](../../../../assets/aws-lambda-screenshots/add_layer.png)  
2. Choose "Custom layer" and select the Layer you've added and the version.  
3. click "Add" at the bottom.  
  
### Create the Bucket Events  
Go to the bucket you are using, and create the event:  
1. Go to Properties → Event notifications → Create event notification  
1. Choose a name for the Event  
1. For Event types choose: All object create events, All object delete events  
1. Destination - Lambda function → Choose from your Lambda functions → choose the function you build → SAVE  
  
Deploy and you're good to go!  
