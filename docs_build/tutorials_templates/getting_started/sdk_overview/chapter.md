# Dataloop SDK Overview

Dataloop provides an end-to-end platform that supports the entire AI lifecycle, from development to production.
By leveraging both a data management and annotation platform, deep learning data generation is streamlined, resulting in
accelerated automated pipeline production and reduced engineering time and costs.

The Dataloop platform is built upon an extensive Python SDK that provides full control over your projects and code. It
allows you to automate CRUD (Create, Read, Update, Delete) operations within the platform for

* Projects
* Datasets
* Items
* Annotations
* Metadata

## About this guide

The Getting Started guide provides the developer with an efficient SDK on-boarding experience and covers the following:

1. [Installing the prerequisite software](#installing-prerequisite-software)
2. [Login to the platform through SDK](#sdk-login)
3. [Create a project](#to-create-a-new-project)
4. [Get existing project](#to-select-the-new-project)
5. [Add & Update Project Members](#adding-and-updating-project-members)
6. [Create Dataset](#to-create-a-new-dataset)
7. [Get Dataset](#to-select-the-dataset)
8. [Upload items](#uploading-items)
9. [Get items](#getting-items)
10. [Annotate item (labels and classification)](#annotating-items)
11. [Upload annotation](#classification)
12. [Filter items](#creating-filters)
13. [Working with Item Metadata](#working-with-item-metadata)
14. [Create Task](#creating-tasks)
15. [Logout](#logging-out)

## Installing Prerequisite Software

The **Dataloop SDK** requires several prerequisite software packages to be installed on your system before it can be
used.

<section class="infoBox" style='background-color:#eff2f9'>
<p style="display:inline;font-size:15px;color:#3452ff">&#9432;</p>
<p style="display:inline;color:black">The scope of this guide does not cover detailed external software installation issues. Please use the provided software vendor website links for further installation information and troubleshooting related to your OS.</p>
</section>

### **Python**

Python **3.6 or later** must be installed in order to use the SDK.

#### To download Python:

1. Visit [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. From the **Downloads** page, **select** your desired OS and proceed with the download.
3. Once the download is complete, you can proceed to **install** the software.

### Dataloop SDK Package

### pip

The SDK package requires **pip** to be installed on your system. **pip** Is the package installer for **Python**. If
Python was installed from [python.org](https://www.python.org/) as described above, **pip** should already be installed.

You can check if **pip** is installed on your system.

#### To verify if pip exists on your system:

**Run** the following from the Command Line:

```
pip --version
```

If **pip** isn’t already installed, you can bootstrap it from the standard library.

#### To bootstrap pip:

**Run** the following from the Command Line:

```
python3 -m ensurepip --default-pip
```

### DTLPY Package

Once you have verified that **pip** is installed, the **Dataloop SDK Package** can be installed.

#### To install the Dataloop SDK Package:

**Run** the following from the **Command Line:**

```
pip install dtlpy
```

Once the SDK Package is successfully installed, a **confirmation message** is displayed:

```
Successfully installed dtlpy-1.64.9
```

## SDK Login

Once the **Dataloop SDK Package** is installed, you can login to the SDK.

To log in to the Dataloop SDK:

1. **Open** a Python Shell.
2. **Run** the following Python command:

```python
import dtlpy as dl

dl.login()
```

Login tokens **expire** after **24hours**, therefore the following expression can be added at the start of the command:

```python
if dl.token_expired():
    dl.login()
```

A web browser login screen is displayed:

![alt_text](../../../assets/log_in/login.png "image_tooltip")

3. **Enter** your credentials, or alternatively login using a Google account.

Once your credentials have been verified a **confirmation message** is displayed:

![alt_text](../../../assets/log_in/login_successful.png "image_tooltip")

## Machine-to-Machine Login

Long-running SDK jobs require API authentication.
The M2M flow allows machines to obtain valid, signed JWT (authentication token) and automatically refresh it, without
the need for a web browser login.

M2M Login is recommended when you want to:
- run commands on the platform without an ongoing internet connection
- run API commands directly from an external system to Dataloop


<section class="infoBox" style='background-color:#eff2f9'>
<p style="display:inline;font-size:15px;color:#3452ff">&#9432;</p>
<p style="display:inline;color:black">This can be done with your email and password (signup with a password), or using project bots (which is NOT is the scope of this tutorial).</p>
</section>

## Login Using API Key

You can also manage and create API keys in theplatform and login using that key from the SDK.
Read more about API keys [here](https://docs.dataloop.ai/docs/rest-api-connection#api-keys), once you have an API key,
perform login using the SDK:

```python
dl.login_api_key(api_key="<api_key>")
```

Replace `<api_key>` with your generated key.
Note that when using API keys in a Python script, it's recommended to store them as environment variables and access them using os.environ, rather than hardcoding them directly in your code, to enhance security and prevent accidental exposure.

```python
import os
dl.login_api_key(api_key=os.environ['DTLPY_API_KEY'])
```


## Datasets

In Dataloop, a dataset is a collection of **items** (files), their respective **metadata**, and **annotations**.
Datasets have a file system structure and are organized into folders and subfolders at multiple levels.

There are **3 types** of datasets:

1. **Master** - The original dataset which manages the actual binaries.
2. **Clone** - Contains pointers to original files, which enables management of virtual items that do not replicate the
   binaries of the underlying storage once cloned or copied. When cloning a dataset, users can decide if the new copy
   will overwrite the original metadata and annotations.
3. **Merge** - Several datasets can be merged into one, allowing multiple annotations to be combined into the same
   dataset.

## Creating a New Dataset

Before a new dataset can be created, at least one project must exist.

### To create a new project:

**Run** the following command to create a new project named: **My-First-Project**:

```python
project = dl.projects.create(project_name='My-First-Project')
`````

The new project is **created**.

The new project must be selected prior to creating a new associated dataset.

### To select the new project:

**Run** the following command to select the new project named created in the above step:

```python
project = dl.projects.get(project_name='My-First-Project')
```

The new project is **selected**.

A project can also be referenced in the above command via its unique project_id.

### To select the new project using a project_id:

**Run** The following command to select the new project by referencing the **project_id**:

```python
project = dl.projects.get(project_id='e4a5e5b3-a22a-4b59-9b76-30417a0859d9')
```

The new project is **selected**.

### Adding & Updating Project Members

Once your project is created, you can add members as well as their roles (Annotation Manager, Developer, Annotator):

```python
project.add_member(email='email-id', role=dl.MemberRole.Developer)
```

Similarly, you can update member's information or remove them altogether from the project:

```python
project.update_member(email='email-id', role=dl.MemberRole.Developer)
project.remove_member(email='email-id')
```

To learn more about the different roles and hierarchy, visit
our [documentation](https://dataloop.ai/docs/contributor-roles).

### To create a new dataset:

**Run** the following command to create a new dataset named My-First-Dataset associated with the project
My-First-Project:

```python
project.datasets.create(dataset_name='My-First-Dataset')
```

Confirmation of the successfully created dataset is **displayed**:

```python
Dataset(id='632c24ae3444a86f029acb47', url='https://gate.dataloop.ai/api/v1/datasets/632c1194120a7571664d0de3',
        name='My-First-Dataset', creator='JohnDoe@gmail.com', items_count=0, expiration_options=None, index_driver='v1',
        created_at='2022-09-22T07:41:08.324Z')
```

<section class="infoBox" style='background-color:#eff2f9'>
<p style="display:inline;font-size:15px;color:#3452ff">&#9432;</p>
<p style="display:inline;color:black">Your Dataset ID will differ from the example above.</p>
</section>

## Uploading items

Items (files) can be **uploaded to datasets** in a file system structure and are organized into folders and subfolders.
Individual items or entire folders can be uploaded.

Before items can be uploaded, the dataset to which the items will be uploaded must be selected.

### To select the dataset:

**Run** the following command to initialize a new instance **(dataset)** of the new dataset **(My-First-Dataset)** in
order to upload items:

```python
dataset = project.datasets.get(dataset_name='My-First-Dataset')
```

Confirmation of the new instance of the selected dataset is **displayed**:

```
Dataset(id='632c24ae3444a86f029acb47', url='https://gate.dataloop.ai/api/v1/datasets/632c1194120a7571664d0de3', name='My-First-Dataset', creator='JohnDoe@gmail.com', items_count=0, expiration_options=None, index_driver='v1', created_at='2022-09-22T07:41:08.324Z')
```

If the selected dataset does not exist the following error message is **displayed**:

```
dtlpy.exceptions.NotFound: ('404', "Dataset not found. Name: 'My-First-Dataset')
```

Once the dataset instance has been successfully initialized, items can be uploaded.

The structure of the **Upload Item Command** is:

```
dataset.items.upload(local_path='/path/to/file.extension')
```

<section class="infoBox" style='background-color:#eff2f9'>
<p style="display:inline;font-size:15px;color:#3452ff">&#9432;</p>
<p style="display:inline;color:black">Directory paths look different in Windows and in Linux, Windows require an "r" at the beginning.</p>
</section>

### To upload an item to a dataset:

1. **Create** a local directory in your file explorer. For this example, **C:\UploadDemo** is used.
2. **Run** The following command to upload an image file from a local directory:

```python
dataset.items.upload(local_path=r'C:\UploadDemo\test1.jpg')
```

> :warning: Ensure the path and file exists before running the command.


Confirmation of the completed upload is **displayed**:

```
Upload Items: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.54it/s]
Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/'632c24ae3444a86f029acb47', created_at='2022-09-22T10:18:03.000Z', dataset_id='632c24ae3444a86f029acb47', filename='/test1.jpg', name='test.jpg', type='file', id='632dadf7b28a0c0da317dfc8', spec=None, creator='JohnDoe@gmail.com', _description=None, annotations_count=0)
```

The **Item ID** of the uploaded file is 632dadf7b28a0c0da317dfc8. This ID is used when **Listing/Getting** items (
See [Getting Items](#getting-items)).


<section class="infoBox" style='background-color:#eff2f9'>
<p style="display:inline;font-size:15px;color:#3452ff">&#9432;</p>
<p style="display:inline;color:black">Your Item ID will differ from the example above.</p>
</section>

If the item to upload is not found, the following **error message** is **displayed**:

```
dtlpy.exceptions.NotFound: ('404', 'Unknown local path: C:\\UploadDemo\\test1.jpg')
```

<section class="infoBox" style='background-color:#eff2f9'>
<p style="display:inline;font-size:15px;color:#3452ff">&#9432;</p>
<p style="display:inline;color:black">By default, files are uploaded to the root directory. Items can be uploaded to an existing folder within a dataset using the remote_path argument (Not in the scope of this guide).</p>
</section>

### <span style="text-decoration:underline;">Exercise 1</span>

1. Write the commands to **Upload** a 2nd image (**test2.jpg**) file item to **My-First-Dataset.**

## Getting Items

Items can be retrieved from a dataset individually using the **item ID**. Alternatively, all items can be retrieved
using a loop.

### Getting a Single Item

The command structure of **Getting a Single Item** is:

```python
item = dataset.items.get(item_id='my_item_id')
item.print()
```

#### To get a single item:

1. **Run** the following command to set an instance of a single item object (**item_1**) from the dataset (*
   *My-First-Dataset**) by specifying an **item ID**:

```python
item_1 = dataset.items.get(item_id='632c365b6002b1266e007830')
```

<section class="infoBox" style='background-color:#eff2f9'>
<p style="display:inline;font-size:15px;color:#3452ff">&#9432;</p>
<p style="display:inline;color:black">Your Item ID will differ from the example above.</p>
</section>

2. **Run** the following command to print the specified item:

```python
item_1.print()
```

The item details are **displayed** including the following:

* Filename
* Creator of the item
* Created timestamp
* Dataset ID of the item

### <span style="text-decoration:underline;">Exercise 2</span>

1. Write the commands to **print** the details of the 2nd uploaded item (**Test2**). Name the item object **item_2**

<section class="infoBox" style='background-color:#eff2f9'>
<img src="https://i.postimg.cc/6QyTynzr/bulb-on.png" id="bulb" width=9>
<p style="display:inline;color:black">Remember: The ID of the item (Test2) must be identified first.</p>
</section>

### Getting All Items

All item details in a dataset can be printed using a loop.

#### To get all items:

Run the following command to loop through the dataset and print all item details:

```python
pages = dataset.items.list()
for item in pages.all():
    item.print()
```

or:

```python
pages = dataset.items.list()
for page in pages:
    for item in page:
        item.print()
```

All dataset item details are **displayed**.

## Annotating Items

Dataset items are annotated using **Labels**. A **Label** is composed of various **Label Settings** and **Instructions**
that are defined by a dataset’s **Recipe**. For example, an image or video file item can contain 1 label defined as
a [Classification](#classification) to categorize the entire image and multiple other labels defined
as [Point Markers](#point-markers) to identify specific objects in an image/video file item.

### Classification

**Classifications** are used to categorize an entire image or scene (in the case of a video file). For example, a
**Classification** label can be used to classify product images under categories, subcategories, and characteristics,
such
as men’s clothes, polo shirts, etc.

The SDK can add **Classification** labels to an **Item** using 2 steps.

1. **Adding** a label to a dataset’s **Recipe**.
2. **Adding** the label to an item as a **Classification**.

#### To Add a Classification Label to a Dataset Recipe:

1. Run the following command to add a **Label** (**Person**) to the **My-First-Dataset** dataset recipe.

```python
dataset.add_label(label_name='Person')
```

The label is created and its **Properties** are displayed.

```
[Label(tag='Person', display_data={}, color='#0214a7', display_label='Person', attributes=[], children=[])]
```

2. **Run** the following commands to **Annotate** and **Upload** the label (**Person**) as a **Classification** to the
   item (**item_1**):

```python
builder = item_1.annotations.builder()
builder.add(annotation_definition=dl.Classification(label='Person'))
item_1.annotations.upload(builder)
```

The label is annotated as a **Classification** to **item_1**.

## Point Markers

A **Point Marker** is used to identify specific objects in an image or video item. For example, an image of a person's
face can
contain multiple **Point Marker** labels specifying the person’s eyes, mouth, ears, etc.

**Point Marker** commands accept 2 coordinate input parameters (x,y) which specify where the label is plotted on the
image.

The SDK can add **Point Marker** labels to an **Item** using 2 steps.

1. **Adding** a label to a dataset’s **Recipe**.
2. **Adding** the label to an item as a **Point Marker**.

### To Add/Upload a Point Marker Label to a Dataset Recipe:

1. **Run** the following command to add a Label (**Ear**) to the **My-First-Dataset** dataset recipe.

```python
dataset.add_label(label_name='Ear')
```

The label is created its **Properties** are displayed.

```
[Label(tag='Ear', display_data={}, color='#0214a7', display_label='Person', attributes=[], children=[])]
```

2. **Run** the following commands to **Annotate** and **Upload** the label (**Ear**) as 2 **Point Markers** to the
   item (**item_1**):

```python
builder = item_1.annotations.builder()
builder.add(annotation_definition=dl.Point(x=80, y=80, label='Ear'))
builder.add(annotation_definition=dl.Point(x=120, y=120, label='Ear'))
item_1.annotations.upload(builder)
```

The label is annotated as 2 **Point Markers** to **item_1**.

<section class="infoBox" style='background-color:#eff2f9'>
<p style="display:inline;font-size:15px;color:#3452ff">&#9432;</p>
<p style="display:inline;color:black">Other Label Types include Box, Cube, Polygon etc.</p>
</section>

### <span style="text-decoration:underline;">Exercise 3</span>

1. **Annotate** 3 items (use **item_2** from [Exercise 2](#span-styletext-decorationunderlineexercise-2span)) with the *
   *Classification** of '**Face**'.
2. **Annotate** 2 random **Point Marker** annotations with the label '**Eye**' to an item (use **item_2**
   from [Exercise 2](#span-styletext-decorationunderlineexercise-2span)).

<section class="infoBox" style='background-color:#eff2f9'>
<img src="https://i.postimg.cc/6QyTynzr/bulb-on.png" id="bulb" width=9>
<p style="display:inline;color:black">Remember: The label must first be added to the Recipe of the dataset.</p>
</section>

## Working with Filters

The SDK supports the filtering of item data. You can filter items by creating **Filter Queries** that define the
**Parameters** of the filter. For example, you can create a **Filter Query** that filters item data on a specific field
name, or by an item’s annotation label.

Multiple **Parameters** can be added to a **Filter Query**, for example, you can include a parameter that filters for
all items that include **Point Marker Annotation** types that are **Labelled** as ’**Ear**’.

### Creating Filters

The first step is to create a **Filter Query**.

#### To Create a Filter Query:

1. **Run** the following command to create a **Filter Query** named **my_filter**

```python
my_filter = dl.Filters()
```

The **Filter Query** is created.

Once the **Filter Query** is created, **Filter Parameters** can be added.

#### To Add a Filter Parameter:

2. **Run** the following command to add a **Filter Parameter** to **my_filter** that filters for all items that include
   **Point Marker Annotation** types:

```python
my_filter.add_join(field='type', values='point')
```

The **Filter Parameter** is created.

<section class="infoBox" style='background-color:#eff2f9'>
<p style="display:inline;font-size:15px;color:#3452ff">&#9432;</p>
<p style="display:inline;color:black">Other Fields can be used as Filter Parameters including id, dataset_id, etc.</p>
</section>


Additional **Filter Parameter**s can be added to the **Filter Query.**

To add additional filter parameters:

3. **Run** the following command to add **Additional Filter Parameter** to **my_filter** that filters for all items that
   include a **Label** value of **‘Ear’**.

```python
my_filter.add_join(field='label', values='Ear')
```

The **Additional Filter Parameter** is added.

The created **Filter Query** can be **applied** to the dataset and **displayed**.

#### To Apply the Filter Query:

4. **Run** the following commands to **Apply** the **Filter Query** to the **dataset** and **display** the filtered
   item(s):

```python
pages = dataset.items.list(filters=my_filter)
for item in pages.all():
    item.print()
```

The **Filter Query** is **applied** to the **dataset**and the filtered item(s) details are **displayed**:

```
Iterate Pages:   0%|                                                                                                                                                                        | 0/1 [00:00<?, ?it/s]Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/632c24ae3444a86f029acb47', created_at='2022-09-23T13:00:39.000Z', dataset_id='632c24ae3444a86f029acb47', filename='/test1.jpg', name='test1.jpg', type='file', id='632dadf7b28a0c0da317dfc8', spec=None, creator='JohnDoe@gmail.com', _description=None, annotations_count=7)
Iterate Pages: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 169.70it/s]
>>>
```

## Using Filters to Replace Data

Filters can be used to **Replace** existing item data. For example, you can **Create** and **Apply** a **Filter Query**
that returns a **subset** of item data that includes a particular **Classification** such as ‘Person’ and **Replace** it
with another value, such as ‘Adult’, across the entire **subset**.

The first step is to **Create** a new **Filter Query** with a **Filter Parameter** that filters for all items that
include a **Label** value of **‘Person’**.

### To Create the Replacement Filter Query:

1. **Run** the following commands to **create** the Replacement **Filter Query** and **Filter Parameter**:

```python
person_filter = dl.Filters(resource=dl.FILTERS_RESOURCE_ITEM)
person_filter.add_join(field='label', values='Person')
```

The Replacement **Filter Query** and **Filter Parameter** are **created**.

The **new label** can be added with the value ‘Adult’.

2. **Run** the following commands to **create** the **new label**:

```python
dataset.add_label(label_name='Adult')
pages = dataset.items.list(filters=person_filter)
```

The **new label** is **created**.

The existing label can be deleted and replaced with the **new label**.

3. **Run** the following commands to **delete** the **existing label** and **Add** the **new label**:

```python
import dtlpy as dl

person_ann_filter = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
person_ann_filter.add(field='label', values='Person')

for item in pages.all():
    item.annotations.delete(filters=person_ann_filter)
    annotations = item.annotations.builder()
    annotations.add(annotation_definition=dl.Classification(label='Adult'))
    item.annotations.upload(annotations)
```

All instances of the old label are replaced in each item with the **new label**.

### <span style="text-decoration:underline;">Exercise 4</span>

1. **Create** and **Apply** a **Filter Query** (use **item_2**
   from [Exercise 3](#span-styletext-decorationunderlineexercise-3span)) that filters items and returns all items that
   include **Point Marker Annotations** that are labeled **‘Eye’**.
2. **Create** and **Apply** a **Filter Query** (use **item_2**
   from [Exercise 3](#span-styletext-decorationunderlineexercise-3span)) that filters the items with the **‘Face’**
   classification, deletes the label, and replaces it with the label **‘Person’**.

## Working with Item Metadata

**Metadata** is a dictionary attribute used with items, annotations, and other entities of the Dataloop system, for
example, **Recipes**.

You can add any keys and values to both item and annotation **user metadata** sections using the SDK. This **user
metadata** can be used for data filtering, sorting, etc.

### Adding a New User Metadata Field to an Item

The following example will demonstrate adding a new user **metadata field** named **Date&Time** to the item named
**test1**, which in this case has an **item ID** = 632dadf7b28a0c0da317dfc8

<section class="infoBox" style='background-color:#eff2f9'>
<p style="display:inline;font-size:15px;color:#3452ff">&#9432;</p>
<p style="display:inline;color:black">Your Item ID will differ from the example above. See Get a Single Item.</p>
</section>


The first step is to **import** the **datetime** module.

#### To Import the datetime Module:

**Run** the following commands to import the **datetime module**:

```python
import datetime
```

The **datetime** module is imported.

An instance of item **test1** can be **created**.

**Create** an [instance](#to-get-a-single-item)of item **test1** named **item_1**.

```python
item_1 = dataset.items.get(item_id='632dadf7b28a0c0da317dfc8')
```

An instance of item **test1** named **item_1** is created.

The current date can be **assigned** to a new field in the item’s metadata named **Date&Time** and the item can be *
*updated**.

#### To Assign the Current Date to a New Metadata Field:

**Run** the following commands to assign the date to a new **metadata field** and **update** the item:

```python
now = datetime.datetime.now().isoformat()
# modify metadata for the item
item_1.metadata['user'] = dict()
# add it to the item's metadata
item_1.metadata['user']['dateTime'] = now
# update the item
item_1 = item_1.update()
```

The date is **assigned** to the new **metadata field** and the item is **updated**.

**Metadata fields** can also be created for a subset of items at once using **filters**.

#### To Create Metadata fields for Multiple Items using Filters:

**Run** the following commands to **create metadata fields** for **a subset** of **items** that include the label *
*‘Person’** using a **filter**:

```python
filters = dl.Filters()
filters.add_join(field='label', values='Person')
now = datetime.datetime.now().isoformat()
dataset.items.update(filters=filters, update_values={'user': {'dateTime': now}})
```

The date is **assigned** to the new **metadata field** and **all items** that include the label **‘Person’** are *
*updated**.

### <span style="text-decoration:underline;">Exercise 5</span>

1. For the filtered items with the **classification ‘Adult’**
   from [Exercise 4](#span-styletext-decorationunderlineexercise-4span), add a new
   field called ‘date’ In the item’s **user metadata** and assign it the current date.

## Creating Tasks

A **Task** is used to initiate annotations. A **Task** requires defining the included data items, the assignee(s), and
other options such as due date, etc.

### To Create a Task

**Run** the following commands to **create** a **Task** containing items with the label **‘Person’** (from the previous
example).

```python
task = dataset.tasks.create(task_name='test',
                            due_date=datetime.datetime(day=15, month=7, year=2022).timestamp(),
                            assignee_ids=['JohnDoe@gmail.com'],
                            filters=filters)
```

The task is **created**.

### <span style="text-decoration:underline;">Exercise 6</span>

1. Create a **Task** that contains those items from [Exercise 5](#span-styletext-decorationunderlineexercise-5span), ie
   all the items **filtered**
   for the classification **‘Adult’**

## Logging out

To Logout **Run** the following command to **Logout** of the SDK:

```python
dl.logout()
```

