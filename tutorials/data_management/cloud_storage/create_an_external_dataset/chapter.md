## Connect Cloud Storage  
  
  
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
