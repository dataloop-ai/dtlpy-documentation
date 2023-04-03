
### External Storage Driver

Once you have an integration, you can set up a driver, which adds a specific bucket (and optionally with a specific
path/folder) as a storage resource.

### Create Drivers in the Platform (browser)

```python
# param name: the driver name
# param driver_type: ExternalStorage.GCS
# param integration_id: the integration id
# param bucket_name: the external bucket name
# param project_id:
# param allow_external_delete:
# param path: Optional. By default, path is the root folder. Path is case sensitive.
# return: driver object
import dtlpy as dl
project = dl.projects.get('prject_name')
driver = project.drivers.create(name='driver_name',
                                driver_type=dl.ExternalStorage.GCS,
                                integration_id='integration_id',
                                bucket_name='bucket_name',
                                allow_external_delete=True,
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
