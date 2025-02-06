# Storage Drivers  
  
  
### External Storage Driver  
  
Only after you created an integration, you can set up a storage driver, which adds a specific bucket (and optionally with a specific  
path/folder) as a storage resource.  
  
### Create Drivers in the Platform (browser)  

```python
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
Once the integration and drivers are ready, you can create a Dataloop Dataset and sync all the data:  

```python
# create a dataset from a driver name, you can also create by the driver ID
import dtlpy as dl
project: dl.Project
dataset = project.datasets.create(dataset_name=dataset_name,
                                  driver=driver)
dataset.sync()
```
