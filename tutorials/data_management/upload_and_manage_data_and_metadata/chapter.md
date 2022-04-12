# Upload & Manage Data & Metadata  
  
## Upload specific files  
  
When you have specific files you want to upload, you can upload them all into a dataset using this script:  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
dataset.items.upload(local_path=[r'C:/home/project/images/John Morris.jpg',
                                 r'C:/home/project/images/John Benton.jpg',
                                 r'C:/home/project/images/Liu Jinli.jpg'],
                     remote_path='/folder_name')  # Remote path is optional, images will go to the main directory by default
```
  
  
## Upload all files in a folder  
  
  
If you want to upload all files from a folder, you can do that by just specifying the folder name:  
  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
dataset.items.upload(local_path=r'C:/home/project/images',
                     remote_path='/folder_name')  # Remote path is optional, images will go to the main directory by default
```
  
## Upload items from URL link  
You can provide Dataloop with the link to the item, and not necessarily the item itself.  

```python
dataset = project.datasets.get(dataset_name='dataset_name')
url_path = 'http://ww.some_website/beautiful_flower.jpg'
# Create link
link = dl.UrlLink(ref=url_path, mimetype='image', name='file_name.jpg')
# Upload link
item = dataset.items.upload(local_path=link)
```
  
You can open an item uploaded to Dataloop by opening it in a viewer.  

```python
show
item.open_in_web()
```
  
  
### Additional upload options  
  
Additional upload options include using buffer, pillow, openCV, and NdArray - see our complete documentation for code examples.  
  
## Upload Items and Annotations Metadata  
You can upload items as a table using a pandas data frame that will let you upload items with info (annotations, metadata such as confidence, filename, etc.) attached to it.  

```python
import pandas
import dtlpy as dl
dataset = dl.datasets.get(dataset_id='id')  # Get dataset
to_upload = list()
# First item and info attached:
to_upload.append({'local_path': r"E:\TypesExamples\000000000064.jpg",  # Item file path
                  'local_annotations_path': r"E:\TypesExamples\000000000776.json",  # Annotations file path
                  'remote_path': "/first",  # Dataset folder to upload the item to
                  'remote_name': 'f.jpg',  # Dataset folder name
                  'item_metadata': {'user': {'dummy': 'fir'}}})  # Added user metadata
# Second item and info attached:
to_upload.append({'local_path': r"E:\TypesExamples\000000000776.jpg",  # Item file path
                  'local_annotations_path': r"E:\TypesExamples\000000000776.json",  # Annotations file path
                  'remote_path': "/second",  # Dataset folder to upload the item to
                  'remote_name': 's.jpg',  # Dataset folder name
                  'item_metadata': {'user': {'dummy': 'sec'}}})  # Added user metadata
df = pandas.DataFrame(to_upload)  # Make data into table
items = dataset.items.upload(local_path=df,
                             overwrite=True)  # Upload table to platform
```
