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
