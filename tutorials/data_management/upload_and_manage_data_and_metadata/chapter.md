# Upload & Manage Data & Metadata

## Upload specific files

When you have specific files you want to upload, you can upload them all into a dataset using this script:
```
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
dataset.items.upload(local_path=[r'C:/home/project/images/John Morris.jpg',
                                 r'C:/home/project/images/John Benton.jpg',
                                 r'C:/home/project/images/Liu Jinli.jpg'],
```


## Upload all files in a folder


If you want to upload all files from a folder, you can do that by just specifying the folder name:

```
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
dataset.items.upload(local_path=r'C:/home/project/images',
```

## Upload items from URL link
You can provide Dataloop with the link to the item, and not necessarily the item itself.
```
dataset = project.datasets.get(dataset_name='dataset_name')
url_path = 'http://ww.some_website/beautiful_flower.jpg'
# Create link
link = dl.UrlLink(ref=url_path, mimetype='image', name='file_name.jpg')
# Upload link
```

You can open an item uploaded to Dataloop by opening it in a viewer.
```
show
```


### Additional upload options

Additional upload options include using buffer, pillow, openCV and NdArray - see our complete documentation for code examples.

## Upload Items and Annotations Metadata
You can upload items as a table using a pandas data frame that will let you upload items with info (annotations, metadata such as confidence, filename etc) attached to it.
```
import pandas
import dtlpy as dl
dataset = dl.datasets.get(dataset_id='id')  # Get dataset
to_upload = list()
# First item and info attached:
to_upload.append({'local_path': r"E:\TypesExamples\000000000064.jpg",  # item file path
                  'local_annotations_path': r"E:\TypesExamples\000000000776.json",  # annotations file path
                  'remote_path': "/first",  # dataset folder to upload the item to
                  'remote_name': 'f.jpg',  # dataset folder name
                  'item_metadata': {'user': {'dummy': 'fir'}}})  # added user metadata
# Second item and info attached:
to_upload.append({'local_path': r"E:\TypesExamples\000000000776.jpg",  # item file path
                  'local_annotations_path': r"E:\TypesExamples\000000000776.json",  # annotations file path
                  'remote_path': "/second",  # dataset folder to upload the item to
                  'remote_name': 's.jpg',  # dataset folder name
                  'item_metadata': {'user': {'dummy': 'sec'}}})  # added user metadata
df = pandas.DataFrame(to_upload)  # make data into table
items = dataset.items.upload(local_path=df,
```
