# Manage Datasets

Datasets are buckets in the dataloop system that holds a collection of data items of any type, regardless of their
storage location (on Dataloop storage or external cloud storage).

## Create Dataset

You can create datasets within a project. There are no limits as for the number of dataset a project can have, which
correlates with data versioning where datasets can be cloned and merged.
```
```
## Create Dataset With Cloud Storage Driver

If you’ve created an integration and driver to your cloud storage, you can create a dataset connected to that driver. A
single integration (for example: S3) can have multiple drivers (per bucket, or even per folder), so you need to specify
that.

```
project = dl.projects.get(project_name='my-project-name')
# Get your drivers list
project.drivers.list().print()
# create a dataset from a driver name, you can also create by the driver ID
```

## Retrieve Datasets

You can read all datasets that exist in a project, and then access the datasets by their ID (or name).

```
datasets = project.datasets.list()
```

## Create Directory

A dataset can have multiple directories, allowing you to manage files by context, such as upload time, working batch,
source etc.
```
```
## Hard-copy a Folder to Another Dataset

You can create a clone of folder into a new dataset, but if you want to actually move between datasets a folder with
files that are stored in the Dataloop system, you’ll need to download them and upload again to the destination dataset.

```
copy_annotations = True
flat_copy = False  # if true it copy all dir files and sub dir files to the destination folder without sub directories
source_folder = '/source_folder'
destination_folder = '/destination_folder'
source_project_name = 'source_project_name'
source_dataset_name = 'source_dataset_name'
destination_project_name = 'destination_project_name'
destination_dataset_name = 'destination_dataset_name'
# Get source project dataset
project = dl.projects.get(project_name=source_project_name)
dataset_from = project.datasets.get(dataset_name=source_dataset_name)
source_folder = source_folder.rstrip('/')
# filter to get all files of a specific folder
filters = dl.Filters()
filters.add(field='filename', values=source_folder + '/**')  # get all items in folder (recursive)
pages = dataset_from.items.list(filters=filters)
# Get destination project and dataset
project = dl.projects.get(project_name=destination_project_name)
dataset_to = project.datasets.get(dataset_name=destination_dataset_name)
# go over all projects and copy file from src to dst
for page in pages:
    for item in page:
        # download item (without save to disk)
        buffer = item.download(save_locally=False)
        # give the items name to the buffer
        if flat_copy:
            buffer.name = item.name
        else:
            buffer.name = item.filename[len(source_folder) + 1:]
        # upload item
        print("Going to add {} to {} dir".format(buffer.name, destination_folder))
        new_item = dataset_to.items.upload(local_path=buffer, remote_path=destination_folder)
        if not isinstance(new_item, dl.Item):
            print('The file {} could not be upload to {}'.format(buffer.name, destination_folder))
            continue
        print("{} has been uploaded".format(new_item.filename))
        if copy_annotations:
```
