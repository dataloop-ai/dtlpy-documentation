# Upload & Manage Data & Metadata  
  
## Upload Specific Files  
  
When you have specific files you want to upload, you can upload them all into a dataset using this script:  

```python
project_name = 'project_name'
dataset_name = 'dataset_name'
local_path = [r'C:/home/project/images/John Morris.jpg',
              r'C:/home/project/images/John Benton.jpg',
              r'C:/home/project/images/Liu Jinli.jpg']
remote_path = '/folder_name'
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name=project_name)
dataset = project.datasets.get(dataset_name=dataset_name)
dataset.items.upload(local_path=local_path,
                     remote_path=remote_path)  # Remote path is optional, images will go to the root directory by default
```
  
  
## Upload All Files in a Folder  
  
  
If you want to upload all files from a folder, you can do that by just specifying the folder name:  
  

```python
project_name = 'project_name'
dataset_name = 'dataset_name'
local_path = r'C:/home/project/images'
remote_path = '/folder_name'
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name=project_name)
dataset = project.datasets.get(dataset_name=dataset_name)
dataset.items.upload(local_path=local_path,
                     remote_path=remote_path)  # Remote path is optional, images will go to the root directory by default
```
  
## Upload Items From URL Links  
You can provide Dataloop with the link to the item, and not necessarily the item itself.  

```python
dataset_name = 'dataset_name'
file_name = 'file_name.jpg'
dataset = project.datasets.get(dataset_name=dataset_name)
url_path = 'http://ww.some_website/beautiful_flower.jpg'
# Create link
link = dl.UrlLink(ref=url_path, mimetype='image', name=file_name)
# Upload link
item = dataset.items.upload(local_path=link)
```
  
You can open an item uploaded to Dataloop by opening it in a viewer.  

```python
item.open_in_web()
```
## Upload Items with Metadata  
You can upload items as a table using a Pandas DataFrame that will let you upload items with info (annotations, metadata such as confidence, filename, etc.) attached to it.  
  

```python
dataset_id = 'id'
# First item:
local_path1 = r"E:\TypesExamples\000000000064.jpg"
local_annotations_path1 = r"E:\TypesExamples\000000000776.json"
remote_path1 = '/first'
remote_name1 = 'f.jpg'
item_metadata1 = {'user': {'dummy': 'fir'}}
# Second item:
local_path2 = r"E:\TypesExamples\000000000776.jpg"
local_annotations_path2 = r"E:\TypesExamples\000000000776.json"
remote_path2 = "/second"
remote_name2 = 's.jpg'
item_metadata2 = {'user': {'dummy': 'sec'}}
import pandas
import dtlpy as dl
dataset = dl.datasets.get(dataset_id=dataset_id)  # Get dataset
to_upload = list()
# First item and info attached:
to_upload.append({'local_path': local_path1,  # Local path to image
                  'local_annotations_path': local_annotations_path1,  # Local path to annotation file
                  'remote_path': remote_path1,  # Remote directory of uploaded image
                  'remote_name': remote_name1,  # Remote name of image
                  'item_metadata': item_metadata1})  # Metadata for the created item
# Second item and info attached:
to_upload.append({'local_path': local_path2,  # Local path to image
                  'local_annotations_path': local_annotations_path2,  # Local path to annotation file
                  'remote_path': remote_path2,  # Remote directory of uploaded image
                  'remote_name': remote_name2,  # Remote name of image
                  'item_metadata': item_metadata2})  # Metadata for the created item
df = pandas.DataFrame(to_upload)  # Make data into DF table
items = dataset.items.upload(local_path=df,
                             overwrite=True)  # Upload DF to platform
```
