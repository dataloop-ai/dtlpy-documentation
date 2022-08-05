# Getting Started  
## Installations and environment creation:  
### Install Python  
Python version 3.6 to 3.9 needs to be installed on your system using this official website. Earlier or later versions are not supported.  
  
### Install the dtlpy package  
Install the plugin using pip, write the following command and press ENTER:  
Please make sure you have pip installed on your computer (you can verify this by typing the command 'pip help' in your terminal); otherwise, download pip.  
pip install dtlpy  
  
Alternatively, install pip from the source by cloning the GitHub repo, then run the following command:  
python setup.py install  
##Login  
To log in, type the command below :  
  

```python
dl.login()
```
Since the login token expires after 24 hours,you can add this to the beginning of your python script :  

```python
if dl.token_expired():
    dl.login()
```
Once your browser opens the Login  screen, type the credentials below or login with Google.  
Please wait for the "Login Successful" tab to appear, then close the tab.  
  
##M2M Login  
Long-running SDK jobs require API authentication.  
The M2M flow allows machines to obtain valid, signed JWT (authentication token) and automatically refresh it, without the need for a real user account UI login.  
  
M2M Login is recommended when you want to:  
    - run commands on the platform without an ongoing internet connection  
    - run API commands directly from an external system to Dataloop  
  
## Log In Via SDK with M2M :  
1. Create a bot user with a unique name:  
Create a bot user with developer permissions to be used for every M2M login.  
You only need to perform this step if this is your first time logging in.  
  

```python
import dtlpy as dl
# use browser login to create the bot
dl.login()
project = dl.projects.get(project_name='myProject')  # get your project
myBot = project.bots.create(name='my-unique-name', return_credentials=True)
```
Now make  sure to save the bot's email and password for future logins:  

```python
print("the bot email is " + myBot.email)
print("the bot password is " + myBot.password)
```
2. Log in to the SDK with your new bot:  

```python
import dtlpy as dl
# Login to Dataloop platform
dl.login_m2m(email=email, password=password)
```
##Create & Get a Project  

```python
project = dl.projects.create(project_name='my-new-project')
project = dl.projects.get(project_name='my-project')
```
##Create & Get a Dataset  

```python
project.datasets.create(dataset_name='my-dataset-name')
dataset = project.datasets.get(dataset_name='my-dataset-name')
```
##Upload items  

```python
dataset.items.upload(local_path="/path/to/image.jpg")
# Upload items to a specific folder in the dataset
dataset.items.upload(local_path="/path/to/image.jpg", remote_path="/path/to/dataset/folder")
```
##Get Item / items-list  

```python
# Get a single item
item = dataset.items.get(item_id='my_item_Id')
# Get all items and iterate through them
pages = dataset.items.list()
# Go over all item and print the properties
for page in pages:
    for item in page:
        item.print()
```
##Filters includes join and all operations  
  

```python
# Filter all items with an annotation that has a label in the list
filters = dl.Filters()
# Filter items with dog OR cat labels
filters.add_join(field='label', values=['dog', 'cat'], operator=dl.FILTERS_OPERATIONS_IN)
# optional - return results sorted by ascending file name
filters.sort_by(field='filename')
# Get filtered items list in a page object
pages = dataset.items.list(filters=filters)
# Count the items
print('Number of items in dataset: {}'.format(pages.items_count))
```
##Add metadata to the item  

```python
item.metadata['user'] = dict()
item.metadata['user']['MyKey'] = 'MyValue'
item.update()
```
##Upload annotations (with Dataloop Builder)  
  

```python
# Upload box annotation
builder.add(annotation_definition=dl.Box(top=10, left=10, bottom=100, right=100, label='labelName'))
item.annotations.upload(builder)
```
##Upload segmentation annotation  

```python
mask = np.zeros(shape=(item.height, item.width), dtype=np.uint8)
mask[50:100, 200:250] = builder.add(annotation_definition=dl.Segmentation(geo=mask, label='label1'))
```
##Get annotations + list (pages)  
  

```python
# getting the item
item = dl.items.get(item_id='item_id')
# now getting the items annotations list
for ann in item.annotations.list():
    print(ann)
# we can also get only annotated items from a dataset then print out the annotations that were created by a
# specific user.
dataset = dl.datasets.get(dataset_id='dataset_id')
# creating the annotated items filter
ItemFilter = dl.Filters()
ItemFilter.add(field='annotated', values=True)
# creating the annotation level filter
annotation_filter = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
annotation_filter.add(field='creator', values='sewar.d@dataloop.ai')
pages = dataset.items.list(filters=ItemFilter)
for page in pages:
    for item in page:
        for ann in item.annotations.list(annotation_filter):
            print(ann)
```
##Uannotation update includes metadata  

```python
annotation.metadata['user'] = dict()
annotation.metadata['user']['MyKey'] = 'MyValue'
annotation.update()
```
##load annotations from JSON file  
### Loading a COCO json :  
  

```python
path = r'path-to-json'
converter = dl.Converter()
converter.upload_local_dataset(
    from_format=dl.AnnotationFormat.COCO,
    dataset=dataset,
    local_annotations_path=path)
```
###Loading it based on your json format:  
In this example we iterate over the json file,filter the item from the platform based on it’s name,then update it’s metadata and upload annotations.  
  

```python
path = r'path-to-json'
ds = dl.datasets.get(dataset_id='ds_ID')
# load the json
with open(json_path, 'r', encoding="utf8") as f:
    data = json.load(f)
    # filter the items in the dataset based on a key\ID\name..
    namefilter = dl.Filters()
    namefilter.resource = dl.FILTERS_RESOURCE_ITEM
    namefilter.add(field='name', values=data['img_name'])
    pages = dataset.items.list(filters=namefilter)
    # pbar to track the progress
    pbar = tqdm.tqdm(total=pages.items_count)
    # going over the filter result
    for page in pages:
        for item in page:
            # now updating the metadata
            item.metadata['user'] = dict()
            item.metadata['user']['camera_dict'] = data['camera_dict']
            item.metadata['user']['name'] = data['name']
            item.update()
            # for the same item we'll update the annotations
            for i_ann in range(len(data['annotations'])):
                label = data['annotations'][i_ann]['object_type']
                top = data['annotations'][i_ann]['top'][0]
                left = data['annotations'][i_ann]['left'][0]
                bottom = data['annotations'][i_ann]['bottom'][0]
                right = data['annotations'][i_ann]['right'][1]
                angle = data['annotations'][i_ann]['bbox_angle_deg']
                builder.add(
                    annotation_definition=dl.Box(top=top, left=left, bottom=bottom, right=right, label=label,
                                                 angle=angle))
                item.annotations.upload(builder)
```
##Creating an annotation task and adding items to it  

```python
task = dataset.tasks.create(
    task_name='task_name',
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'])
filters = dl.Filters(field='dir', values='/my/folder/directory')
task.add_items(
    filters=filters, assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'])
```
