# Entities

## Organization


### _class_ CacheAction(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ MemberOrgRole(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ Organization(members: [list](https://docs.python.org/3/library/stdtypes.html#list), groups: [list](https://docs.python.org/3/library/stdtypes.html#list), account: [dict](https://docs.python.org/3/library/stdtypes.html#dict), created_at, updated_at, id, name, logo_url, plan, owner, created_by, client_api: ApiClient, repositories=NOTHING)
Bases: `BaseEntity`

Organization entity


#### add_member(email, role: ~dtlpy.entities.organization.MemberOrgRole = <enum 'MemberOrgRole'>)
Add members to your organization. Read about members and groups [here]([https://dataloop.ai/docs/org-members-groups](https://dataloop.ai/docs/org-members-groups)).

Prerequisities: To add members to an organization, you must be in the role of an “owner” in that organization.


* **Parameters**

    
    * **email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the member’s email


    * **role** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – MemberOrgRole.ADMIN, MemberOrgRole.OWNER, MemberOrgRole.MEMBER



* **Returns**

    True if successful or error if unsuccessful



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### cache_action(mode=CacheAction.APPLY, pod_type=PodType.SMALL)
Open the organizations in web platform


* **Parameters**

    
    * **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – dl.CacheAction.APPLY or dl.CacheAction.DESTROY


    * **pod_type** (*dl.PodType*) – dl.PodType.SMALL, dl.PodType.MEDIUM, dl.PodType.HIGH



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### delete_member(user_id: [str](https://docs.python.org/3/library/stdtypes.html#str), sure: [bool](https://docs.python.org/3/library/functions.html#bool) = False, really: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Delete member from the Organization.

Prerequisites: Must be an organization “owner” to delete members.


* **Parameters**

    
    * **user_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – user id


    * **sure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Are you sure you want to delete?


    * **really** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Really really sure?



* **Returns**

    True if success and error if not



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### _classmethod_ from_json(_json, client_api, is_fetched=True)
Build a Project entity object from a json


* **Parameters**

    
    * **is_fetched** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is Entity fetched from Platform


    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – _json response from host


    * **client_api** (*dl.ApiClient*) – ApiClient entity



* **Returns**

    Organization object



* **Return type**

    dtlpy.entities.organization.Organization



#### list_groups()
List all organization groups (groups that were created within the organization).

Prerequisites: You must be an organization “owner” to use this method.


* **Returns**

    groups list



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)



#### list_members(role: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[MemberOrgRole] = None)
List all organization members.

Prerequisites: You must be an organization “owner” to use this method.


* **Parameters**

    **role** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – MemberOrgRole.ADMIN, MemberOrgRole.OWNER, MemberOrgRole.MEMBER



* **Returns**

    projects list



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)



#### open_in_web()
Open the organizations in web platform


#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(plan: [str](https://docs.python.org/3/library/stdtypes.html#str))
Update Organization.

Prerequisities: You must be an Organization **superuser** to update an organization.


* **Parameters**

    **plan** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – OrganizationsPlans.FREEMIUM, OrganizationsPlans.PREMIUM



* **Returns**

    organization object



#### update_member(email: [str](https://docs.python.org/3/library/stdtypes.html#str), role: MemberOrgRole = MemberOrgRole.MEMBER)
Update member role.

Prerequisities: You must be an organization “owner” to update a member’s role.


* **Parameters**

    
    * **email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the member’s email


    * **role** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – MemberOrgRole.ADMIN, MemberOrgRole.OWNER, MemberOrgRole.MEMBER



* **Returns**

    json of the member fields



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



### _class_ OrganizationsPlans(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ PodType(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

### Integration


### _class_ Integration(id, name, type, org, created_at, created_by, update_at, client_api: ApiClient, project=None)
Bases: `BaseEntity`

Integration object


#### delete(sure: [bool](https://docs.python.org/3/library/functions.html#bool) = False, really: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Delete integrations from the Organization


* **Parameters**

    
    * **sure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – are you sure you want to delete?


    * **really** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – really really?



* **Returns**

    True



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### _classmethod_ from_json(_json: [dict](https://docs.python.org/3/library/stdtypes.html#dict), client_api: ApiClient, is_fetched=True)
Build a Integration entity object from a json


* **Parameters**

    
    * **_json** – _json response from host


    * **client_api** – ApiClient entity


    * **is_fetched** – is Entity fetched from Platform



* **Returns**

    Integration object



#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(new_name: [str](https://docs.python.org/3/library/stdtypes.html#str))
Update the integrations name


* **Parameters**

    **new_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – new name


## Project


### _class_ MemberRole(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ Project(contributors, created_at, creator, id, name, org, updated_at, role, account, is_blocked, feature_constraints, client_api: ApiClient, repositories=NOTHING)
Bases: `BaseEntity`

Project entity


#### add_member(email, role: MemberRole = MemberRole.DEVELOPER)
Add a member to the project.


* **Parameters**

    
    * **email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – member email


    * **role** – The required role for the user. Use the enum dl.MemberRole



* **Returns**

    dict that represent the user



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### checkout()
Checkout (switch) to a project to work on.


#### delete(sure=False, really=False)
Delete the project forever!


* **Parameters**

    
    * **sure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Are you sure you want to delete?


    * **really** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Really really sure?



* **Returns**

    True if success, error if not



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### _classmethod_ from_json(_json, client_api, is_fetched=True)
Build a Project object from a json


* **Parameters**

    
    * **is_fetched** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is Entity fetched from Platform


    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – _json response from host


    * **client_api** (*dl.ApiClient*) – ApiClient entity



* **Returns**

    Project object



* **Return type**

    dtlpy.entities.project.Project



#### list_members(role: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[MemberRole] = None)
List the project members.


* **Parameters**

    **role** – The required role for the user. Use the enum dl.MemberRole



* **Returns**

    list of the project members



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)



#### open_in_web()
Open the project in web platform


#### remove_member(email)
Remove a member from the project.


* **Parameters**

    **email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – member email



* **Returns**

    dict that represents the user



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### to_json()
Returns platform _json format of project object


* **Returns**

    platform json format of project object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(system_metadata=False)
Update the project


* **Parameters**

    **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - True, if you want to change metadata system



* **Returns**

    Project object



* **Return type**

    dtlpy.entities.project.Project



#### update_member(email, role: MemberRole = MemberRole.DEVELOPER)
Update member’s information/details from the project.


* **Parameters**

    
    * **email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – member email


    * **role** – The required role for the user. Use the enum dl.MemberRole



* **Returns**

    dict that represent the user



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)


### User


### _class_ User(created_at, updated_at, name, last_name, username, avatar, email, role, type, org, id, project, client_api=None, users=None)
Bases: `BaseEntity`

User entity


#### _classmethod_ from_json(_json, project, client_api, users=None)
Build a User entity object from a json


* **Parameters**

    
    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – _json response from host


    * **project** (*dtlpy.entities.project.Project*) – project entity


    * **client_api** – ApiClient entity


    * **users** – Users repository



* **Returns**

    User object



* **Return type**

    dtlpy.entities.user.User



#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)


## Dataset


### _class_ Dataset(id, url, name, annotated, creator, projects, items_count, metadata, directoryTree, export, expiration_options, index_driver, created_at, items_url, readable_type, access_level, driver, readonly, client_api: ApiClient, project=None, datasets=None, repositories=NOTHING, ontology_ids=None, labels=None, directory_tree=None, recipe=None, ontology=None)
Bases: `BaseEntity`

Dataset object


#### add_label(label_name, color=None, children=None, attributes=None, display_label=None, label=None, recipe_id=None, ontology_id=None, icon_path=None)
Add single label to dataset

**Prerequisites**: You must have a dataset with items that are related to the annotations. The relationship between the dataset and annotations is shown in the name. You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **label_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – str - label name


    * **color** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) – RGB color of the annotation, e.g (255,0,0) or ‘#ff0000’ for red


    * **children** – children (sub labels). list of sub labels of this current label, each value is either dict or dl.Label


    * **attributes** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – add attributes to the labels


    * **display_label** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – name that display label


    * **label** (*dtlpy.entities.label.Label*) – label object


    * **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional recipe id


    * **ontology_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional ontology id


    * **icon_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to image to be display on label



* **Returns**

    label entity



* **Return type**

    dtlpy.entities.label.Label


**Example**:

```python
dataset.add_label(label_name='person', color=(34, 6, 231), attributes=['big', 'small'])
```


#### add_labels(label_list, ontology_id=None, recipe_id=None)
Add labels to dataset

**Prerequisites**: You must have a dataset with items that are related to the annotations. The relationship between the dataset and annotations is shown in the name. You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **label_list** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – a list of labels to add to the dataset’s ontology. each value should be a dict, dl.Label or a string


    * **ontology_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional ontology id


    * **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional recipe id



* **Returns**

    label entities


**Example**:

```python
dataset.add_labels(label_list=label_list)
```


#### checkout()
Checkout the dataset


#### clone(clone_name, filters=None, with_items_annotations=True, with_metadata=True, with_task_annotations_status=True)
Clone dataset

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **clone_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – new dataset name


    * **filters** (*dtlpy.entities.filters.Filters*) – Filters entity or a query dict


    * **with_items_annotations** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – clone all item’s annotations


    * **with_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – clone metadata


    * **with_task_annotations_status** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – clone task annotations status



* **Returns**

    dataset object



* **Return type**

    dtlpy.entities.dataset.Dataset


**Example**:

```python
dataset = dataset.clone(dataset_id='dataset_id',
              clone_name='dataset_clone_name',
              with_metadata=True,
              with_items_annotations=False,
              with_task_annotations_status=False)
```


#### delete(sure=False, really=False)
Delete a dataset forever!

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **sure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – are you sure you want to delete?


    * **really** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – really really?



* **Returns**

    True is success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
is_deleted = dataset.delete(sure=True, really=True)
```


#### delete_attributes(keys: [list](https://docs.python.org/3/library/stdtypes.html#list), recipe_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, ontology_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Delete a bulk of attributes


* **Parameters**

    
    * **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – recipe id


    * **ontology_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – ontology id


    * **keys** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – Keys of attributes to delete



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### delete_labels(label_names)
Delete labels from dataset’s ontologies

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    **label_names** – label object/ label name / list of label objects / list of label names


**Example**:

```python
dataset.delete_labels(label_names=['myLabel1', 'Mylabel2'])
```


#### download(filters=None, local_path=None, file_types=None, annotation_options: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[ViewAnnotationOptions] = None, annotation_filters=None, overwrite=False, to_items_folder=True, thickness=1, with_text=False, without_relative_path=None, alpha=1, export_version=ExportVersion.V1)
Download dataset by filters.
Filtering the dataset for items and save them local
Optional - also download annotation, mask, instance and image mask of the item

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **filters** (*dtlpy.entities.filters.Filters*) – Filters entity or a dictionary containing filters parameters


    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local folder or filename to save to.


    * **file_types** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – a list of file type to download. e.g [‘video/webm’, ‘video/mp4’, ‘image/jpeg’, ‘image/png’]


    * **annotation_options** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – type of download annotations: list(dl.ViewAnnotationOptions)


    * **annotation_filters** (*dtlpy.entities.filters.Filters*) – Filters entity to filter annotations for download


    * **overwrite** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - default = False to overwrite the existing files


    * **to_items_folder** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Create ‘items’ folder and download items to it


    * **thickness** ([*int*](https://docs.python.org/3/library/functions.html#int)) – optional - line thickness, if -1 annotation will be filled, default =1


    * **with_text** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - add text to annotations, default = False


    * **without_relative_path** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool - download items without the relative path from platform


    * **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) – opacity value [0 1], default 1


    * **export_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – V2 - exported items will have original extension in filename, V1 - no original extension in filenames



* **Returns**

    List of local_path per each downloaded item


**Example**:

```python
dataset.download(local_path='local_path',
                 annotation_options=[dl.ViewAnnotationOptions.JSON, dl.ViewAnnotationOptions.MASK],
                 overwrite=False,
                 thickness=1,
                 with_text=False,
                 alpha=1,
                 save_locally=True
                 )
```


#### download_annotations(local_path=None, filters=None, annotation_options: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[ViewAnnotationOptions] = None, annotation_filters=None, overwrite=False, thickness=1, with_text=False, remote_path=None, include_annotations_in_output=True, export_png_files=False, filter_output_annotations=False, alpha=1, export_version=ExportVersion.V1)
Download dataset by filters.
Filtering the dataset for items and save them local
Optional - also download annotation, mask, instance and image mask of the item

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local folder or filename to save to.


    * **filters** (*dtlpy.entities.filters.Filters*) – Filters entity or a dictionary containing filters parameters


    * **annotation_options** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*(**dtlpy.entities.annotation.ViewAnnotationOptions**)*) – download annotations options: list(dl.ViewAnnotationOptions)


    * **annotation_filters** (*dtlpy.entities.filters.Filters*) – Filters entity to filter annotations for download


    * **overwrite** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - default = False


    * **thickness** ([*int*](https://docs.python.org/3/library/functions.html#int)) – optional - line thickness, if -1 annotation will be filled, default =1


    * **with_text** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - add text to annotations, default = False


    * **remote_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – DEPRECATED and ignored


    * **include_annotations_in_output** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – default - False , if export should contain annotations


    * **export_png_files** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – default - if True, semantic annotations should be exported as png files


    * **filter_output_annotations** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – default - False, given an export by filter - determine if to filter out annotations


    * **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) – opacity value [0 1], default 1


    * **export_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – exported items will have original extension in filename, V1 - no original extension in filenames



* **Returns**

    local_path of the directory where all the downloaded item



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)


**Example**:

```python
local_path = dataset.download_annotations(dataset='dataset_entity',
                             local_path='local_path',
                             annotation_options=[dl.ViewAnnotationOptions.JSON, dl.ViewAnnotationOptions.MASK],
                             overwrite=False,
                             thickness=1,
                             with_text=False,
                             alpha=1
                             )
```


#### _classmethod_ from_json(project: Project, _json: [dict](https://docs.python.org/3/library/stdtypes.html#dict), client_api: ApiClient, datasets=None, is_fetched=True)
Build a Dataset entity object from a json


* **Parameters**

    
    * **project** – dataset’s project


    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – _json response from host


    * **client_api** – ApiClient entity


    * **datasets** – Datasets repository


    * **is_fetched** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is Entity fetched from Platform



* **Returns**

    Dataset object



* **Return type**

    dtlpy.entities.dataset.Dataset



#### get_recipe_ids()
Get dataset recipe Ids


* **Returns**

    list of recipe ids



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)



#### open_in_web()
Open the dataset in web platform


#### _static_ serialize_labels(labels_dict)
Convert hex color format to rgb


* **Parameters**

    **labels_dict** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – dict of labels



* **Returns**

    dict of converted labels



#### set_readonly(state: [bool](https://docs.python.org/3/library/functions.html#bool))
Set dataset readonly mode

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    **state** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – state


**Example**:

```python
dataset.set_readonly(state=True)
```


#### switch_recipe(recipe_id=None, recipe=None)
Switch the recipe that linked to the dataset with the given one


* **Parameters**

    
    * **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – recipe id


    * **recipe** (*dtlpy.entities.recipe.Recipe*) – recipe entity


**Example**:

```python
dataset.switch_recipe(recipe_id='recipe_id')
```


#### sync(wait=True)
Sync dataset with external storage

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait for the command to finish



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = dataset.sync()
```


#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(system_metadata=False)
Update dataset field

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool - True, if you want to change metadata system



* **Returns**

    Dataset object



* **Return type**

    dtlpy.entities.dataset.Dataset


**Example**:

```python
dataset = dataset.update()
```


#### update_attributes(title: [str](https://docs.python.org/3/library/stdtypes.html#str), key: [str](https://docs.python.org/3/library/stdtypes.html#str), attribute_type, recipe_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, ontology_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, scope: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[list](https://docs.python.org/3/library/stdtypes.html#list)] = None, optional: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[bool](https://docs.python.org/3/library/functions.html#bool)] = None, values: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[list](https://docs.python.org/3/library/stdtypes.html#list)] = None, attribute_range=None)
ADD a new attribute or update if exist


* **Parameters**

    
    * **ontology_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – ontology_id


    * **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – attribute title


    * **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the key of the attribute must br unique


    * **attribute_type** (*AttributesTypes*) – dl.AttributesTypes your attribute type


    * **scope** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of the labels or \* for all labels


    * **optional** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional attribute


    * **values** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of the attribute values ( for checkbox and radio button)


    * **attribute_range** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)* or **AttributesRange*) – dl.AttributesRange object



* **Returns**

    true in success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
dataset.update_attributes(ontology_id='ontology_id',
                          key='1',
                          title='checkbox',
                          attribute_type=dl.AttributesTypes.CHECKBOX,
                          values=[1,2,3])
```


#### update_label(label_name, color=None, children=None, attributes=None, display_label=None, label=None, recipe_id=None, ontology_id=None, upsert=False, icon_path=None)
Add single label to dataset

**Prerequisites**: You must have a dataset with items that are related to the annotations. The relationship between the dataset and annotations is shown in the name. You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **label_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – str - label name


    * **color** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) – color


    * **children** – children (sub labels)


    * **attributes** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – add attributes to the labels


    * **display_label** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – name that display label


    * **label** (*dtlpy.entities.label.Label*) – label


    * **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional recipe id


    * **ontology_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional ontology id


    * **icon_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to image to be display on label



* **Returns**

    label entity



* **Return type**

    dtlpy.entities.label.Label


**Example**:

```python
dataset.update_label(label_name='person', color=(34, 6, 231), attributes=['big', 'small'])
```


#### update_labels(label_list, ontology_id=None, recipe_id=None, upsert=False)
Add labels to dataset

**Prerequisites**: You must have a dataset with items that are related to the annotations. The relationship between the dataset and annotations is shown in the name. You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **label_list** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – label list


    * **ontology_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional ontology id


    * **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional recipe id


    * **upsert** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if True will add in case it does not existing



* **Returns**

    label entities



* **Return type**

    dtlpy.entities.label.Label


**Example**:

```python
dataset.update_labels(label_list=label_list)
```


#### upload_annotations(local_path, filters=None, clean=False, remote_root_path='/', export_version=ExportVersion.V1)
Upload annotations to dataset.

**Prerequisites**: You must have a dataset with items that are related to the annotations. The relationship between the dataset and annotations is shown in the name. You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – str - local folder where the annotations files is.


    * **filters** (*dtlpy.entities.filters.Filters*) – Filters entity or a dictionary containing filters parameters


    * **clean** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool - if True it remove the old annotations


    * **remote_root_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – str - the remote root path to match remote and local items


    * **export_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – V2 - exported items will have original extension in filename, V1 - no original extension in filenames


For example, if the item filepath is a/b/item and remote_root_path is /a the start folder will be b instead of a

**Example**:

```python
dataset.upload_annotations(dataset='dataset_entity',
                         local_path='local_path',
                         clean=False,
                         export_version=dl.ExportVersion.V1
                         )
```


### _class_ ExpirationOptions(item_max_days: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

ExpirationOptions object


### _class_ IndexDriver(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

### Driver


### _class_ Driver(bucket_name, creator, allow_external_delete, allow_external_modification, created_at, region, path, type, integration_id, integration_type, metadata, name, id, client_api: ApiClient, repositories=NOTHING)
Bases: `BaseEntity`

Driver entity


#### delete(sure=False, really=False)
Delete a driver forever!

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **sure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – are you sure you want to delete?


    * **really** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – really really?



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
driver.delete(sure=True, really=True)
```


#### _classmethod_ from_json(_json, client_api, is_fetched=True)
Build a Driver entity object from a json


* **Parameters**

    
    * **_json** – _json response from host


    * **client_api** – ApiClient entity


    * **is_fetched** – is Entity fetched from Platform



* **Returns**

    Driver object



#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



### _class_ ExternalStorage(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

## Item


### _class_ ExportMetadata(value)
Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ Item(annotations_link, dataset_url, thumbnail, created_at, dataset_id, annotated, metadata, filename, stream, name, type, url, id, hidden, dir, spec, creator, description, src_item, annotations_count, client_api: ApiClient, platform_dict, dataset, model, project, project_id, repositories=NOTHING)
Bases: `BaseEntity`

Item object


#### clone(dst_dataset_id=None, remote_filepath=None, metadata=None, with_annotations=True, with_metadata=True, with_task_annotations_status=False, allow_many=False, wait=True)
Clone item


* **Parameters**

    
    * **dst_dataset_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – destination dataset id


    * **remote_filepath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – complete filepath


    * **metadata** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – new metadata to add


    * **with_annotations** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – clone annotations


    * **with_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – clone metadata


    * **with_task_annotations_status** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – clone task annotations status


    * **allow_many** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool if True, using multiple clones in single dataset is allowed, (default=False)


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait for the command to finish



* **Returns**

    Item object



* **Return type**

    dtlpy.entities.item.Item


**Example**:

```python
item.clone(item_id='item_id',
        dst_dataset_id='dist_dataset_id',
        with_metadata=True,
        with_task_annotations_status=False,
        with_annotations=False)
```


#### delete()
Delete item from platform


* **Returns**

    True



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### download(local_path=None, file_types=None, save_locally=True, to_array=False, annotation_options: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[ViewAnnotationOptions] = None, overwrite=False, to_items_folder=True, thickness=1, with_text=False, annotation_filters=None, alpha=1, export_version=ExportVersion.V1)
Download dataset by filters.
Filtering the dataset for items and save them local
Optional - also download annotation, mask, instance and image mask of the item


* **Parameters**

    
    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local folder or filename to save to.


    * **file_types** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – a list of file type to download. e.g [‘video/webm’, ‘video/mp4’, ‘image/jpeg’, ‘image/png’]


    * **save_locally** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool. save to disk or return a buffer


    * **to_array** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – returns Ndarray when True and local_path = False


    * **annotation_options** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – download annotations options:  list(dl.ViewAnnotationOptions)


    * **annotation_filters** (*dtlpy.entities.filters.Filters*) – Filters entity to filter annotations for download


    * **overwrite** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - default = False


    * **to_items_folder** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Create ‘items’ folder and download items to it


    * **thickness** ([*int*](https://docs.python.org/3/library/functions.html#int)) – optional - line thickness, if -1 annotation will be filled, default =1


    * **with_text** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - add text to annotations, default = False


    * **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) – opacity value [0 1], default 1


    * **export_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – exported items will have original extension in filename, V1 - no original extension in filenames



* **Returns**

    generator of local_path per each downloaded item



* **Return type**

    generator or single item


**Example**:

```python
item.download(local_path='local_path',
             annotation_options=dl.ViewAnnotationOptions.MASK,
             overwrite=False,
             thickness=1,
             with_text=False,
             alpha=1,
             save_locally=True
             )
```


#### _classmethod_ from_json(_json, client_api, dataset=None, project=None, model=None, is_fetched=True)
Build an item entity object from a json


* **Parameters**

    
    * **project** (*dtlpy.entities.project.Project*) – project entity


    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – _json response from host


    * **dataset** (*dtlpy.entities.dataset.Dataset*) – dataset in which the annotation’s item is located


    * **model** (*dtlpy.entities.dataset.Model*) – the model entity if item is an artifact of a model


    * **client_api** (*dlApiClient*) – ApiClient entity


    * **is_fetched** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is Entity fetched from Platform



* **Returns**

    Item object



* **Return type**

    dtlpy.entities.item.Item



#### move(new_path)
Move item from one folder to another in Platform
If the directory doesn’t exist it will be created


* **Parameters**

    **new_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – new full path to move item to.



* **Returns**

    True if update successfully



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### open_in_web()
Open the items in web platform


* **Returns**

    


#### set_description(text: [str](https://docs.python.org/3/library/stdtypes.html#str))
Update Item description


* **Parameters**

    **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – if None or “” description will be deleted


:return


#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(system_metadata=False)
Update items metadata


* **Parameters**

    **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool - True, if you want to change metadata system



* **Returns**

    Item object



* **Return type**

    dtlpy.entities.item.Item



#### update_status(status: [str](https://docs.python.org/3/library/stdtypes.html#str), clear: [bool](https://docs.python.org/3/library/functions.html#bool) = False, assignment_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, task_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
update item status


* **Parameters**

    
    * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – “completed” ,”approved” ,”discard”


    * **clear** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true delete status


    * **assignment_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – assignment id


    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – task id


:return :True/False
:rtype: bool

**Example**:

```python
item.update_status(status='complete',
                   operation='created',
                   task_id='task_id')
```


### _class_ ItemStatus(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ ModalityRefTypeEnum(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

State enum


### _class_ ModalityTypeEnum(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

State enum

### Item Link


### _class_ LinkTypeEnum(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

State enum

## Annotation


### _class_ Annotation(id, url, item_url, item, item_id, creator, created_at, updated_by, updated_at, type, source, dataset_url, platform_dict, metadata, fps, hash=None, dataset_id=None, status=None, object_id=None, automated=None, item_height=None, item_width=None, label_suggestions=None, annotation_definition: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[BaseAnnotationDefinition] = None, frames=None, current_frame=0, end_frame=0, end_time=0, start_frame=0, start_time=0, dataset=None, datasets=None, annotations=None, Annotation__client_api=None, items=None, recipe_2_attributes=None)
Bases: `BaseEntity`

Annotations object


#### add_frame(annotation_definition, frame_num=None, fixed=True, object_visible=True)
Add a frame state to annotation


* **Parameters**

    
    * **annotation_definition** – annotation type object - must be same type as annotation


    * **frame_num** ([*int*](https://docs.python.org/3/library/functions.html#int)) – frame number


    * **fixed** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is fixed


    * **object_visible** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – does the annotated object is visible



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = annotation.add_frame(frame_num=10,
                annotation_definition=dl.Box(top=10,left=10,bottom=100, right=100,label='labelName'))
                )
```


#### add_frames(annotation_definition, frame_num=None, end_frame_num=None, start_time=None, end_time=None, fixed=True, object_visible=True)
Add a frames state to annotation

**Prerequisites**: Any user can upload annotations.


* **Parameters**

    
    * **annotation_definition** – annotation type object - must be same type as annotation


    * **frame_num** ([*int*](https://docs.python.org/3/library/functions.html#int)) – first frame number


    * **end_frame_num** ([*int*](https://docs.python.org/3/library/functions.html#int)) – last frame number


    * **start_time** – starting time for video


    * **end_time** – ending time for video


    * **fixed** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is fixed


    * **object_visible** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – does the annotated object is visible



* **Returns**

    

**Example**:

```python
annotation.add_frames(frame_num=10,
                annotation_definition=dl.Box(top=10,left=10,bottom=100, right=100,label='labelName'))
                )
```


#### delete()
Remove an annotation from item

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or *developer* or be assigned a task that includes that item as an *annotation manager* or *annotator*.


* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
is_deleted = annotation.delete()
```


#### download(filepath: [str](https://docs.python.org/3/library/stdtypes.html#str), annotation_format: ViewAnnotationOptions = ViewAnnotationOptions.JSON, height: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[float](https://docs.python.org/3/library/functions.html#float)] = None, width: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[float](https://docs.python.org/3/library/functions.html#float)] = None, thickness: [int](https://docs.python.org/3/library/functions.html#int) = 1, with_text: [bool](https://docs.python.org/3/library/functions.html#bool) = False, alpha: [float](https://docs.python.org/3/library/functions.html#float) = 1)
Save annotation to file

**Prerequisites**: Any user can upload annotations.


* **Parameters**

    
    * **filepath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local path to where annotation will be downloaded to


    * **annotation_format** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – options: list(dl.ViewAnnotationOptions)


    * **height** ([*float*](https://docs.python.org/3/library/functions.html#float)) – image height


    * **width** ([*float*](https://docs.python.org/3/library/functions.html#float)) – image width


    * **thickness** ([*int*](https://docs.python.org/3/library/functions.html#int)) – line thickness


    * **with_text** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – get mask with text


    * **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) – opacity value [0 1], default 1



* **Returns**

    filepath



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)


**Example**:

```python
filepath = annotation.download(filepath='filepath', annotation_format=dl.ViewAnnotationOptions.MASK)
```


#### _classmethod_ from_json(_json, item=None, client_api=None, annotations=None, is_video=None, fps=None, item_metadata=None, dataset=None, is_audio=None)
Create an annotation object from platform json


* **Parameters**

    
    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – platform json


    * **item** (*dtlpy.entities.item.Item*) – item


    * **client_api** – ApiClient entity


    * **annotations** – 


    * **is_video** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is video


    * **fps** – video fps


    * **item_metadata** – item metadata


    * **dataset** – dataset entity


    * **is_audio** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is audio



* **Returns**

    annotation object



* **Return type**

    dtlpy.entities.annotation.Annotation



#### _classmethod_ new(item=None, annotation_definition=None, object_id=None, automated=True, metadata=None, frame_num=None, parent_id=None, start_time=None, item_height=None, item_width=None, end_time=None)
Create a new annotation object annotations

**Prerequisites**: Any user can upload annotations.


* **Parameters**

    
    * **item** (*dtlpy.entities.item.Items*) – item to annotate


    * **annotation_definition** – annotation type object


    * **object_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – object_id


    * **automated** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is automated


    * **metadata** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – metadata


    * **frame_num** ([*int*](https://docs.python.org/3/library/functions.html#int)) – optional - first frame number if video annotation


    * **parent_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – add parent annotation ID


    * **start_time** – optional - start time if video annotation


    * **item_height** ([*float*](https://docs.python.org/3/library/functions.html#float)) – annotation item’s height


    * **item_width** ([*float*](https://docs.python.org/3/library/functions.html#float)) – annotation item’s width


    * **end_time** – optional - end time if video annotation



* **Returns**

    annotation object



* **Return type**

    dtlpy.entities.annotation.Annotation


**Example**:

```python
annotation = annotation.new(item='item_entity,
                annotation_definition=dl.Box(top=10,left=10,bottom=100, right=100,label='labelName'))
                )
```


#### set_frame(frame)
Set annotation to frame state

**Prerequisites**: Any user can upload annotations.


* **Parameters**

    **frame** ([*int*](https://docs.python.org/3/library/functions.html#int)) – frame number



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = annotation.set_frame(frame=10)
```


#### show(image=None, thickness=None, with_text=False, height=None, width=None, annotation_format: ViewAnnotationOptions = ViewAnnotationOptions.MASK, color=None, label_instance_dict=None, alpha=1, frame_num=None)
Show annotations
mark the annotation of the image array and return it

**Prerequisites**: Any user can upload annotations.


* **Parameters**

    
    * **image** – empty or image to draw on


    * **thickness** ([*int*](https://docs.python.org/3/library/functions.html#int)) – line thickness


    * **with_text** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – add label to annotation


    * **height** ([*float*](https://docs.python.org/3/library/functions.html#float)) – height


    * **width** ([*float*](https://docs.python.org/3/library/functions.html#float)) – width


    * **annotation_format** (*dl.ViewAnnotationOptions*) – list(dl.ViewAnnotationOptions)


    * **color** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) – optional - color tuple


    * **label_instance_dict** – the instance labels


    * **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) – opacity value [0 1], default 1


    * **frame_num** ([*int*](https://docs.python.org/3/library/functions.html#int)) – for video annotation, show specific fame



* **Returns**

    list or single ndarray of the annotations


**Exampls**:

```python
image = annotation.show(image='ndarray',
                thickness=1,
                annotation_format=dl.VIEW_ANNOTATION_OPTIONS_MASK,
                )
```


#### to_json()
Convert annotation object to a platform json representatio


* **Returns**

    platform json



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(system_metadata=False)
Update an existing annotation in host.

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or *developer* or be assigned a task that includes that item as an *annotation manager* or *annotator*.


* **Parameters**

    **system_metadata** – True, if you want to change metadata system



* **Returns**

    Annotation object



* **Return type**

    dtlpy.entities.annotation.Annotation


**Example**:

```python
annotation = annotation.update()
```


#### update_status(status: AnnotationStatus = AnnotationStatus.ISSUE)
Set status on annotation

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or *developer* or be assigned a task that includes that item as an *annotation manager*.


* **Parameters**

    **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – can be AnnotationStatus.ISSUE, AnnotationStatus.APPROVED, AnnotationStatus.REVIEW, AnnotationStatus.CLEAR



* **Returns**

    Annotation object



* **Return type**

    dtlpy.entities.annotation.Annotation


**Example**:

```python
annotation = annotation.update_status(status=dl.AnnotationStatus.ISSUE)
```


#### upload()
Create a new annotation in host

**Prerequisites**: Any user can upload annotations.


* **Returns**

    Annotation entity



* **Return type**

    dtlpy.entities.annotation.Annotation



### _class_ AnnotationStatus(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ AnnotationType(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ ExportVersion(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ FrameAnnotation(annotation, annotation_definition, frame_num, fixed, object_visible, recipe_2_attributes=None, interpolation=False)
Bases: `BaseEntity`

FrameAnnotation object


#### _classmethod_ from_snapshot(annotation, _json, fps)
new frame state to annotation


* **Parameters**

    
    * **annotation** – annotation


    * **_json** – annotation type object - must be same type as annotation


    * **fps** – frame number



* **Returns**

    FrameAnnotation object



#### _classmethod_ new(annotation, annotation_definition, frame_num, fixed, object_visible=True)
new frame state to annotation


* **Parameters**

    
    * **annotation** – annotation


    * **annotation_definition** – annotation type object - must be same type as annotation


    * **frame_num** – frame number


    * **fixed** – is fixed


    * **object_visible** – does the annotated object is visible



* **Returns**

    FrameAnnotation object



#### show(\*\*kwargs)
Show annotation as ndarray
:param kwargs: see annotation definition
:return: ndarray of the annotation


### _class_ ViewAnnotationOptions(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

The Annotations file types to download (JSON, MASK, INSTANCE, ANNOTATION_ON_IMAGE, VTT, OBJECT_ID).

| State

 | Description

 |
| ----- | ----------- |
| JSON

  | Dataloop json format

 |
| MASK

  | PNG file that contains drawing annotations on it

 |
| INSTANCE

 | An image file that contains 2D annotations

       |
| ANNOTATION_ON_IMAGE

 | The source image with the annotations drawing in it

 |
| VTT

                 | An text file contains supplementary information about a web video

 |
| OBJECT_ID

           | An image file that contains 2D annotations

                        |
### Collection of Annotation entities


### _class_ AnnotationCollection(item=None, annotations=NOTHING, dataset=None, colors=None)
Bases: `BaseEntity`

Collection of Annotation entity


#### add(annotation_definition, object_id=None, frame_num=None, end_frame_num=None, start_time=None, end_time=None, automated=True, fixed=True, object_visible=True, metadata=None, parent_id=None, model_info=None)
Add annotations to collection


* **Parameters**

    
    * **annotation_definition** – dl.Polygon, dl.Segmentation, dl.Point, dl.Box etc


    * **object_id** – Object id (any id given by user). If video - must input to match annotations between frames


    * **frame_num** – video only, number of frame


    * **end_frame_num** – video only, the end frame of the annotation


    * **start_time** – video only, start time of the annotation


    * **end_time** – video only, end time of the annotation


    * **automated** – 


    * **fixed** – video only, mark frame as fixed


    * **object_visible** – video only, does the annotated object is visible


    * **metadata** – optional- metadata dictionary for annotation


    * **parent_id** – set a parent for this annotation (parent annotation ID)


    * **model_info** – optional - set model on annotation {‘name’,:’’, ‘confidence’:0}



* **Returns**

    


#### delete()
Remove an annotation from item

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or *developer* or be assigned a task that includes that item as an *annotation manager* or *annotator*.


* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
is_deleted = builder.delete()
```


#### download(filepath, img_filepath=None, annotation_format: ViewAnnotationOptions = ViewAnnotationOptions.JSON, height=None, width=None, thickness=1, with_text=False, orientation=0, alpha=1)
Save annotations to file

**Prerequisites**: Any user can upload annotations.


* **Parameters**

    
    * **filepath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to save annotation


    * **img_filepath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – img file path - needed for img_mask


    * **annotation_format** (*dl.ViewAnnotationOptions*) – how to show thw annotations. options: list(dl.ViewAnnotationOptions)


    * **height** ([*int*](https://docs.python.org/3/library/functions.html#int)) – height


    * **width** ([*int*](https://docs.python.org/3/library/functions.html#int)) – width


    * **thickness** ([*int*](https://docs.python.org/3/library/functions.html#int)) – thickness


    * **with_text** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – add a text to the image


    * **orientation** ([*int*](https://docs.python.org/3/library/functions.html#int)) – the image orientation


    * **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) – opacity value [0 1], default 1



* **Returns**

    file path of the downlaod annotation



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)


**Example**:

```python
filepath = builder.download(filepath='filepath', annotation_format=dl.ViewAnnotationOptions.MASK)
```


#### from_instance_mask(mask, instance_map=None)
convert annotation from instance mask format


* **Parameters**

    
    * **mask** – the mask annotation


    * **instance_map** – labels



#### _classmethod_ from_json(_json: [list](https://docs.python.org/3/library/stdtypes.html#list), item=None, is_video=None, fps=25, height=None, width=None, client_api=None, is_audio=None)
Create an annotation collection object from platform json


* **Parameters**

    
    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – platform json


    * **item** (*dtlpy.entities.item.Item*) – item


    * **client_api** – ApiClient entity


    * **is_video** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is video


    * **fps** – video fps


    * **height** ([*float*](https://docs.python.org/3/library/functions.html#float)) – height


    * **width** ([*float*](https://docs.python.org/3/library/functions.html#float)) – width


    * **is_audio** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is audio



* **Returns**

    annotation object



* **Return type**

    dtlpy.entities.annotation.Annotation



#### from_vtt_file(filepath)
convert annotation from vtt format


* **Parameters**

    **filepath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to the file



#### get_frame(frame_num)
Get frame


* **Parameters**

    **frame_num** ([*int*](https://docs.python.org/3/library/functions.html#int)) – frame num



* **Returns**

    AnnotationCollection



#### print(to_return=False, columns=None)

* **Parameters**

    
    * **to_return** – 


    * **columns** – 



#### show(image=None, thickness=None, with_text=False, height=None, width=None, annotation_format: ViewAnnotationOptions = ViewAnnotationOptions.MASK, label_instance_dict=None, color=None, alpha=1, frame_num=None)
Show annotations according to annotation_format

**Prerequisites**: Any user can upload annotations.


* **Parameters**

    
    * **image** (*ndarray*) – empty or image to draw on


    * **height** ([*int*](https://docs.python.org/3/library/functions.html#int)) – height


    * **width** ([*int*](https://docs.python.org/3/library/functions.html#int)) – width


    * **thickness** ([*int*](https://docs.python.org/3/library/functions.html#int)) – line thickness


    * **with_text** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – add label to annotation


    * **annotation_format** (*dl.ViewAnnotationOptions*) – how to show thw annotations. options: list(dl.ViewAnnotationOptions)


    * **label_instance_dict** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – instance label map {‘Label’: 1, ‘More’: 2}


    * **color** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) – optional - color tuple


    * **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) – opacity value [0 1], default 1


    * **frame_num** ([*int*](https://docs.python.org/3/library/functions.html#int)) – for video annotation, show specific frame



* **Returns**

    ndarray of the annotations


**Example**:

```python
image = builder.show(image='ndarray',
            thickness=1,
            annotation_format=dl.VIEW_ANNOTATION_OPTIONS_MASK,
            )
```


#### to_json()
Convert annotation object to a platform json representation


* **Returns**

    platform json



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(system_metadata=True)
Update an existing annotation in host.

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or *developer* or be assigned a task that includes that item as an *annotation manager* or *annotator*.


* **Parameters**

    **system_metadata** – True, if you want to change metadata system



* **Returns**

    Annotation object



* **Return type**

    dtlpy.entities.annotation.Annotation


**Example**:

```python
annotation = builder.update()
```


#### upload()
Create a new annotation in host

**Prerequisites**: Any user can upload annotations.


* **Returns**

    Annotation entity



* **Return type**

    dtlpy.entities.annotation.Annotation


**Example**:

```python
annotation = builder.upload()
```

### Annotation Definition

#### Box Annotation Definition


### _class_ Box(left=None, top=None, right=None, bottom=None, label=None, attributes=None, description=None, angle=None)
Bases: `BaseAnnotationDefinition`

Box annotation object
Can create a box using 2 point using: “top”, “left”, “bottom”, “right” (to form a box [(left, top), (right, bottom)])
For rotated box add the “angel”


#### _classmethod_ from_segmentation(mask, label, attributes=None)
Convert binary mask to Polygon


* **Parameters**

    
    * **mask** – binary mask (0,1)


    * **label** – annotation label


    * **attributes** – annotations list of attributes



* **Returns**

    Box annotations list  to each separated  segmentation



#### show(image, thickness, with_text, height, width, annotation_format, color, alpha=1)
Show annotation as ndarray
:param image: empty or image to draw on
:param thickness:
:param with_text: not required
:param height: item height
:param width: item width
:param annotation_format: options: list(dl.ViewAnnotationOptions)
:param color: color
:param alpha: opacity value [0 1], default 1
:return: ndarray

#### Classification Annotation Definition


### _class_ Classification(label, attributes=None, description=None)
Bases: `BaseAnnotationDefinition`

Classification annotation object


#### show(image, thickness, with_text, height, width, annotation_format, color, alpha=1)
Show annotation as ndarray
:param image: empty or image to draw on
:param thickness:
:param with_text: not required
:param height: item height
:param width: item width
:param annotation_format: options: list(dl.ViewAnnotationOptions)
:param color: color
:param alpha: opacity value [0 1], default 1
:return: ndarray

#### Cuboid Annotation Definition


### _class_ Cube(label, front_tl, front_tr, front_br, front_bl, back_tl, back_tr, back_br, back_bl, angle=None, attributes=None, description=None)
Bases: `BaseAnnotationDefinition`

Cube annotation object


#### _classmethod_ from_boxes_and_angle(front_left, front_top, front_right, front_bottom, back_left, back_top, back_right, back_bottom, label, angle=0, attributes=None)
Create cuboid by given front and back boxes with angle
the angle calculate fom the center of each box


#### show(image, thickness, with_text, height, width, annotation_format, color, alpha=1)
Show annotation as ndarray
:param image: empty or image to draw on
:param thickness:
:param with_text: not required
:param height: item height
:param width: item width
:param annotation_format: options: list(dl.ViewAnnotationOptions)
:param color: color
:param alpha: opacity value [0 1], default 1
:return: ndarray

#### Item Description Definition


### _class_ Description(text, description=None)
Bases: `BaseAnnotationDefinition`

Subtitle annotation object

#### Ellipse Annotation Definition


### _class_ Ellipse(x, y, rx, ry, angle, label, attributes=None, description=None)
Bases: `BaseAnnotationDefinition`

Ellipse annotation object


#### show(image, thickness, with_text, height, width, annotation_format, color, alpha=1)
Show annotation as ndarray
:param image: empty or image to draw on
:param thickness:
:param with_text: not required
:param height: item height
:param width: item width
:param annotation_format: options: list(dl.ViewAnnotationOptions)
:param color: color
:param alpha: opacity value [0 1], default 1
:return: ndarray

#### Note Annotation Definition


### _class_ Message(msg_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, creator: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, msg_time=None, body: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Note message object


### _class_ Note(left, top, right, bottom, label, attributes=None, messages=None, status='issue', assignee=None, create_time=None, creator=None, description=None)
Bases: `Box`

Note annotation object

#### Point Annotation Definition


### _class_ Point(x, y, label, attributes=None, description=None)
Bases: `BaseAnnotationDefinition`

Point annotation object


#### show(image, thickness, with_text, height, width, annotation_format, color, alpha=1)
Show annotation as ndarray
:param image: empty or image to draw on
:param thickness:
:param with_text: not required
:param height: item height
:param width: item width
:param annotation_format: options: list(dl.ViewAnnotationOptions)
:param color: color
:param alpha: opacity value [0 1], default 1
:return: ndarray

#### Polygon Annotation Definition


### _class_ Polygon(geo, label, attributes=None, description=None)
Bases: `BaseAnnotationDefinition`

Polygon annotation object


#### _classmethod_ from_segmentation(mask, label, attributes=None, epsilon=None, max_instances=1, min_area=0)
Convert binary mask to Polygon


* **Parameters**

    
    * **mask** – binary mask (0,1)


    * **label** – annotation label


    * **attributes** – annotations list of attributes


    * **epsilon** – from opencv: specifying the approximation accuracy. This is the maximum distance between the original curve and its approximation. if 0 all points are returns


    * **max_instances** – number of max instances to return. if None all wil be returned


    * **min_area** – remove polygons with area lower thn this threshold (pixels)



* **Returns**

    Polygon annotation



#### show(image, thickness, with_text, height, width, annotation_format, color, alpha=1)
Show annotation as ndarray
:param image: empty or image to draw on
:param thickness:
:param with_text: not required
:param height: item height
:param width: item width
:param annotation_format: options: list(dl.ViewAnnotationOptions)
:param color: color
:param alpha: opacity value [0 1], default 1
:return: ndarray

#### Polyline Annotation Definition


### _class_ Polyline(geo, label, attributes=None, description=None)
Bases: `BaseAnnotationDefinition`

Polyline annotation object


#### show(image, thickness, with_text, height, width, annotation_format, color, alpha=1)
Show annotation as ndarray
:param image: empty or image to draw on
:param thickness:
:param with_text: not required
:param height: item height
:param width: item width
:param annotation_format: options: list(dl.ViewAnnotationOptions)
:param color: color
:param alpha: opacity value [0 1], default 1
:return: ndarray

#### Pose Annotation Definition


### _class_ Pose(label, template_id, instance_id=None, attributes=None, points=None, description=None)
Bases: `BaseAnnotationDefinition`

Classification annotation object


#### show(image, thickness, with_text, height, width, annotation_format, color, alpha=1)
Show annotation as ndarray
:param image: empty or image to draw on
:param thickness:
:param with_text: not required
:param height: item height
:param width: item width
:param annotation_format: options: list(dl.ViewAnnotationOptions)
:param color: color
:param alpha: opacity value [0 1], default 1
:return: ndarray

#### Segmentation Annotation Definition


### _class_ Segmentation(geo, label, attributes=None, description=None, color=None)
Bases: `BaseAnnotationDefinition`

Segmentation annotation object


#### _classmethod_ from_polygon(geo, label, shape, attributes=None)

* **Parameters**

    
    * **geo** – list of x,y coordinates of the polygon ([[x,y],[x,y]…]


    * **label** – annotation’s label


    * **shape** – image shape (h,w)


    * **attributes** – 



* **Returns**

    


#### show(image, thickness, with_text, height, width, annotation_format, color, alpha=1)
Show annotation as ndarray
:param image: empty or image to draw on
:param thickness:
:param with_text: not required
:param height: item height
:param width: item width
:param annotation_format: options: list(dl.ViewAnnotationOptions)
:param color: color
:param alpha: opacity value [0 1], default 1
:return: ndarray


#### to_box()

* **Returns**

    Box annotations list  to each separated  segmentation


#### Audio Annotation Definition


### _class_ Subtitle(text, label, attributes=None, description=None)
Bases: `BaseAnnotationDefinition`

Subtitle annotation object

#### Undefined Annotation Definition


### _class_ UndefinedAnnotationType(type, label, coordinates, attributes=None, description=None)
Bases: `BaseAnnotationDefinition`

UndefinedAnnotationType annotation object


#### show(image, thickness, with_text, height, width, annotation_format, color, alpha=1)
Show annotation as ndarray
:param image: empty or image to draw on
:param thickness:
:param with_text: not required
:param height: item height
:param width: item width
:param annotation_format: options: list(dl.ViewAnnotationOptions)
:param color: color
:param alpha: opacity value [0 1], default 1
:return: ndarray

### Similarity


### _class_ Collection(type: CollectionTypes, name, items=None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Base Collection Entity


#### add(ref, type: SimilarityTypeEnum = SimilarityTypeEnum.ID)
Add item to collection
:param ref:
:param type: url, id


#### pop(ref)

* **Parameters**

    **ref** – 



#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



### _class_ CollectionItem(type: SimilarityTypeEnum, ref)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Base CollectionItem


### _class_ CollectionTypes(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ MultiView(name, items=None)
Bases: `Collection`

Multi Entity


#### _property_ items()
list of the collection items


#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



### _class_ MultiViewItem(type, ref)
Bases: `CollectionItem`

Single multi view item


### _class_ Similarity(ref, name=None, items=None)
Bases: `Collection`

Similarity Entity


#### _property_ items()
list of the collection items


#### _property_ target()
Target item for similarity


#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



### _class_ SimilarityItem(type, ref, target=False)
Bases: `CollectionItem`

Single similarity item


### _class_ SimilarityTypeEnum(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

State enum

## Filter


### _class_ Filters(field=None, values=None, operator: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[FiltersOperations] = None, method: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[FiltersMethod] = None, custom_filter=None, resource: FiltersResource = FiltersResource.ITEM, use_defaults=True, context=None, page_size=None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Filters entity to filter items from pages in platform


#### add(field, values, operator: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[FiltersOperations] = None, method: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[FiltersMethod] = None)
Add filter


* **Parameters**

    
    * **field** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Metadata field / attribute


    * **values** – field values


    * **operator** (*dl.FiltersOperations*) – optional - in, gt, lt, eq, ne


    * **method** (*dl.FiltersMethod*) – Optional - or/and


**Example**:

```python
filter.add(field='metadata.user', values=['1','2'], operator=dl.FiltersOperations.IN)
```


#### add_join(field, values, operator: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[FiltersOperations] = None, method: FiltersMethod = FiltersMethod.AND)
join a query to the filter


* **Parameters**

    
    * **field** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Metadata field / attribute


    * **values** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)* or *[*list*](https://docs.python.org/3/library/stdtypes.html#list)) – field values


    * **operator** (*dl.FiltersOperations*) – optional - in, gt, lt, eq, ne


    * **method** – optional - str - FiltersMethod.AND, FiltersMethod.OR


**Example**:

```python
filter.add_join(field='metadata.user', values=['1','2'], operator=dl.FiltersOperations.IN)
```


#### generate_url_query_params(url)
generate url query params


* **Parameters**

    **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 



#### has_field(field)
is filter has field


* **Parameters**

    **field** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – field to check



* **Returns**

    Ture is have it



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### open_in_web(resource)
Open the filter in the platform data browser (in a new web browser)


* **Parameters**

    **resource** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – dl entity to apply filter on. currently only supports dl.Dataset



#### platform_url(resource)
Build a url with filters param to open in web browser


* **Parameters**

    **resource** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – dl entity to apply filter on. currently only supports dl.Dataset



* **Returns**

    url string



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)



#### pop(field)
Pop filed


* **Parameters**

    **field** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – field to pop



#### pop_join(field)
Pop join


* **Parameters**

    **field** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – field to pop



#### prepare(operation=None, update=None, query_only=False, system_update=None, system_metadata=False)
To dictionary for platform call


* **Parameters**

    
    * **operation** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – operation


    * **update** – update


    * **query_only** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – query only


    * **system_update** – system update


    * **system_metadata** – True, if you want to change metadata system



* **Returns**

    dict of the filter



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### sort_by(field, value: FiltersOrderByDirection = FiltersOrderByDirection.ASCENDING)
sort the filter


* **Parameters**

    
    * **field** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – field to sort by it


    * **value** (*dl.FiltersOrderByDirection*) – FiltersOrderByDirection.ASCENDING, FiltersOrderByDirection.DESCENDING


**Example**:

```python
filter.sort_by(field='metadata.user', values=dl.FiltersOrderByDirection.ASCENDING)
```


### _class_ FiltersKnownFields(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ FiltersMethod(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ FiltersOperations(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ FiltersOrderByDirection(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ FiltersResource(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

## Recipe


### _class_ Recipe(id, creator, url, title, project_ids, description, ontology_ids, instructions, examples, custom_actions, metadata, ui_settings, client_api: ApiClient, dataset=None, project=None, repositories=NOTHING)
Bases: `BaseEntity`

Recipe object


#### add_instruction(annotation_instruction_file)
Add instruction to recipe


* **Parameters**

    **annotation_instruction_file** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – file path or url of the recipe instruction



#### clone(shallow=False)
> Clone Recipe


* **Parameters**

    **shallow** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – If True, link ot existing ontology, clones all ontology that are link to the recipe as well



* **Returns**

    Cloned ontology object



* **Return type**

    dtlpy.entities.recipe.Recipe



#### delete(force: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Delete recipe from platform


* **Parameters**

    **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – force delete recipe



* **Returns**

    True



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### _classmethod_ from_json(_json, client_api, dataset=None, project=None, is_fetched=True)
Build a Recipe entity object from a json


* **Parameters**

    
    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – _json response from host


    * **Dataset** (*dtlpy.entities.dataset.Dataset*) – Dataset entity


    * **project** (*dtlpy.entities.project.Project*) – project entity


    * **client_api** (*dl.ApiClient*) – ApiClient entity


    * **is_fetched** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is Entity fetched from Platform



* **Returns**

    Recipe object



#### get_annotation_template_id(template_name)
> Get annotation template id by template name


* **Parameters**

    **template_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 



* **Returns**

    template id or None if does not exist



#### open_in_web()
Open the recipes in web platform


* **Returns**

    


#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(system_metadata=False)
Update Recipe


* **Parameters**

    **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool - True, if you want to change metadata system



* **Returns**

    Recipe object



* **Return type**

    dtlpy.entities.recipe.Recipe


### Ontology


### _class_ Ontology(client_api: ApiClient, id, creator, url, title, labels, metadata, attributes, recipe=None, dataset=None, project=None, repositories=NOTHING, instance_map=None, color_map=None)
Bases: `BaseEntity`

Ontology object


#### add_label(label_name, color=None, children=None, attributes=None, display_label=None, label=None, add=True, icon_path=None, update_ontology=False)
Add a single label to ontology


* **Parameters**

    
    * **label_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – str - label name


    * **color** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) – color


    * **children** – children (sub labels)


    * **attributes** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – attributes


    * **display_label** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – display_label


    * **label** (*dtlpy.entities.label.Label*) – label


    * **add** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – to add or not


    * **icon_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to image to be display on label


    * **update_ontology** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – update the ontology, default = False for backward compatible



* **Returns**

    Label entity



* **Return type**

    dtlpy.entities.label.Label


**Example**:

```python
label = ontology.add_label(label_name='person', color=(34, 6, 231), attributes=['big', 'small'])
```


#### add_labels(label_list, update_ontology=False)
Adds a list of labels to ontology


* **Parameters**

    
    * **label_list** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of labels [{“value”: {“tag”: “tag”, “displayLabel”: “displayLabel”,
    “color”: “#color”, “attributes”: [attributes]}, “children”: [children]}]


    * **update_ontology** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – update the ontology, default = False for backward compatible



* **Returns**

    List of label entities added


**Example**:

```python
labels = ontology.add_labels(label_list=label_list)
```


#### _property_ color_map()
rgb}


* **Returns**

    dict



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



* **Type**

    Color mapping of labels, {label



#### delete()
Delete recipe from platform


* **Returns**

    True



#### delete_attributes(keys: [list](https://docs.python.org/3/library/stdtypes.html#list))
Delete a bulk of attributes


* **Parameters**

    **keys** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – Keys of attributes to delete



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = ontology.delete_attributes(['1'])
```


#### delete_labels(label_names)
Delete labels from ontology


* **Parameters**

    **label_names** – label object/ label name / list of label objects / list of label names



* **Returns**

    


#### _classmethod_ from_json(_json, client_api, recipe, dataset=None, project=None, is_fetched=True)
Build an Ontology entity object from a json


* **Parameters**

    
    * **is_fetched** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is Entity fetched from Platform


    * **project** (*dtlpy.entities.project.Project*) – project entity


    * **dataset** (*dtlpy.entities.dataset.Dataset*) – dataset


    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – _json response from host


    * **recipe** (*dtlpy.entities.recipe.Recipe*) – ontology’s recipe


    * **client_api** (*dl.ApiClient*) – ApiClient entity



* **Returns**

    Ontology object



* **Return type**

    dtlpy.entities.ontology.Ontology



#### _property_ instance_map()
instance mapping for creating instance mask


* **Return dictionary {label**

    map_id}



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(system_metadata=False)
Update items metadata


* **Parameters**

    **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool - True, if you want to change metadata system



* **Returns**

    Ontology object



#### update_attributes(title: [str](https://docs.python.org/3/library/stdtypes.html#str), key: [str](https://docs.python.org/3/library/stdtypes.html#str), attribute_type, scope: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[list](https://docs.python.org/3/library/stdtypes.html#list)] = None, optional: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[bool](https://docs.python.org/3/library/functions.html#bool)] = None, values: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[list](https://docs.python.org/3/library/stdtypes.html#list)] = None, attribute_range=None)
ADD a new attribute or update if exist


* **Parameters**

    
    * **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – attribute title


    * **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the key of the attribute must br unique


    * **attribute_type** (*AttributesTypes*) – dl.AttributesTypes your attribute type


    * **scope** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of the labels or \* for all labels


    * **optional** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional attribute


    * **values** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of the attribute values ( for checkbox and radio button)


    * **attribute_range** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)* or **AttributesRange*) – dl.AttributesRange object



* **Returns**

    true in success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### update_label(label_name, color=None, children=None, attributes=None, display_label=None, label=None, add=True, icon_path=None, upsert=False, update_ontology=False)
Update a single label to ontology


* **Parameters**

    
    * **label_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – str - label name


    * **color** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)) – color


    * **children** – children (sub labels)


    * **attributes** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – attributes


    * **display_label** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – display_label


    * **label** (*dtlpy.entities.label.Label*) – label


    * **add** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – to add or not


    * **icon_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to image to be display on label


    * **update_ontology** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – update the ontology, default = False for backward compatible


    * **upsert** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if True will add in case it does not existing



* **Returns**

    Label entity



* **Return type**

    dtlpy.entities.label.Label


**Example**:

```python
label = ontology.update_label(label_name='person', color=(34, 6, 231), attributes=['big', 'small'])
```


#### update_labels(label_list, upsert=False, update_ontology=False)
Update a list of labels to ontology


* **Parameters**

    
    * **label_list** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of labels [{“value”: {“tag”: “tag”, “displayLabel”: “displayLabel”, “color”: “#color”, “attributes”: [attributes]}, “children”: [children]}]


    * **upsert** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if True will add in case it does not existing


    * **update_ontology** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – update the ontology, default = False for backward compatible



* **Returns**

    List of label entities added


**Example**:

```python
labels = ontology.update_labels(label_list=label_list)
```

#### Label

## Task


### _class_ Task(name, status, project_id, metadata, id, url, task_owner, item_status, creator, due_date, dataset_id, spec, recipe_id, query, assignmentIds, annotation_status, progress, for_review, issues, updated_at, created_at, available_actions, total_items, priority, client_api, current_assignments=None, assignments=None, project=None, dataset=None, tasks=None, settings=None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Task object


#### add_items(filters=None, items=None, assignee_ids=None, workload=None, limit=None, wait=True, query=None)
Add items to Task


* **Parameters**

    
    * **filters** (*dtlpy.entities.filters.Filters*) – Filters entity or a dictionary containing filters parameters


    * **items** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of items (item Ids or objects) to add to the task


    * **assignee_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list to assignee who works in the task


    * **workload** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of WorkloadUnit objects. Customize distribution (percentage) between the task assignees. For example: [dl.WorkloadUnit([annotator@hi.com](mailto:annotator@hi.com), 80), dl.WorkloadUnit([annotator2@hi.com](mailto:annotator2@hi.com), 20)]


    * **limit** ([*int*](https://docs.python.org/3/library/functions.html#int)) – the limit items that task can include


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until add items will to finish


    * **query** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – query to filter the items for the task



* **Returns**

    task entity



* **Return type**

    dtlpy.entities.task.Task



#### create_assignment(assignment_name, assignee_id, items=None, filters=None)
Create a new assignment


* **Parameters**

    
    * **assignment_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – assignment name


    * **assignee_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the assignment assignees (contributors) that should be working on the task. Provide a user email


    * **items** (*List**[**entities.Item**]*) – list of items (item Id or objects) to insert to the task


    * **filters** (*dtlpy.entities.filters.Filters*) – Filters entity or a dictionary containing filters parameters



* **Returns**

    Assignment object



* **Return type**

    dtlpy.entities.assignment.Assignment assignment


**Example**:

```python
assignment = task.create_assignment(assignee_id='annotator1@dataloop.ai')
```


#### create_qa_task(due_date, assignee_ids, filters=None, items=None, query=None, workload=None, metadata=None, available_actions=None, wait=True, batch_size=None, max_batch_workload=None, allowed_assignees=None, priority=TaskPriority.MEDIUM)
Create a new QA Task


* **Parameters**

    
    * **due_date** ([*float*](https://docs.python.org/3/library/functions.html#float)) – date by which the QA task should be finished; for example, due_date=datetime.datetime(day=1, month=1, year=2029).timestamp()


    * **assignee_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list the QA task assignees (contributors) that should be working on the task. Provide a list of users’ emails


    * **filters** (*entities.Filters*) – dl.Filters entity to filter items for the task


    * **items** (*List**[**entities.Item**]*) – list of items (item Id or objects) to insert to the task


    * **query** (*dict DQL*) – filter items for the task


    * **workload** (*List**[**WorkloadUnit**]*) – list of WorkloadUnit objects. Customize distribution (percentage) between the task assignees. For example: [dl.WorkloadUnit([annotator@hi.com](mailto:annotator@hi.com), 80), dl.WorkloadUnit([annotator2@hi.com](mailto:annotator2@hi.com), 20)]


    * **metadata** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – metadata for the task


    * **available_actions** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of available actions (statuses) that will be available for the task items; The default statuses are: “Approved” and “Discarded”


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until create task finish


    * **batch_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Pulling batch size (items), use with pulling allocation method. Restrictions - Min 3, max 100


    * **max_batch_workload** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Max items in assignment, use with pulling allocation method. Restrictions - Min batchSize + 2, max batchSize \* 2


    * **allowed_assignees** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list the task assignees (contributors) that should be working on the task. Provide a list of users’ emails


    * **priority** (*entities.TaskPriority*) – priority of the task options in entities.TaskPriority



* **Returns**

    task object



* **Return type**

    dtlpy.entities.task.Task


**Example**:

```python
task = task.create_qa_task(due_date = datetime.datetime(day= 1, month= 1, year= 2029).timestamp(),
                    assignee_ids =[ 'annotator1@dataloop.ai', 'annotator2@dataloop.ai'])
```


#### delete(wait=True)
Delete task from platform


* **Parameters**

    **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until delete task finish



* **Returns**

    True



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### _classmethod_ from_json(_json, client_api, project=None, dataset=None)
Return the task object form the json


* **Parameters**

    
    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – platform json that describe the task


    * **client_api** – ApiClient object


    * **project** (*dtlpy.entities.project.Project*) – project object where task will create


    * **dataset** (*dtlpy.entities.dataset.Dataset*) – dataset object that refer to the task



* **Returns**

    


#### get_items(filters=None)
Get the task items


* **Parameters**

    **filters** (*dtlpy.entities.filters.Filters*) – Filters entity or a dictionary containing filters parameters



* **Returns**

    list of the items or PagedEntity output of items



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list) or dtlpy.entities.paged_entities.PagedEntities



#### open_in_web()
Open the task in web platform


* **Returns**

    


#### remove_items(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[Filters] = None, query=None, items=None, wait=True)
remove items from Task.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned to be *owner* of the annotation task.


* **Parameters**

    
    * **filters** (*dtlpy.entities.filters.Filters*) – Filters entity or a dictionary containing filters parameters


    * **query** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – query to filter the items use it


    * **items** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of items to add to the task


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until remove items finish



* **Returns**

    True if success and an error if failed



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### set_status(status: [str](https://docs.python.org/3/library/stdtypes.html#str), operation: [str](https://docs.python.org/3/library/stdtypes.html#str), item_ids: [List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#str)])
Update item status within task


* **Parameters**

    
    * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – string the describes the status


    * **operation** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the status action need ‘create’ or ‘delete’


    * **item_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – List[str] id items ids



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(system_metadata=False)
Update an Annotation Task


* **Parameters**

    **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – True, if you want to change metadata system



### _class_ TaskPriority(value)
Bases: [`int`](https://docs.python.org/3/library/functions.html#int), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

### Assignment


### _class_ Assignment(name, annotator, status, project_id, metadata, id, url, task_id, dataset_id, annotation_status, item_status, total_items, for_review, issues, client_api, task=None, assignments=None, project=None, dataset=None, datasets=None)
Bases: `BaseEntity`

Assignment object


#### get_items(dataset=None, filters=None)
Get all the items in the assignment

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Parameters**

    
    * **dataset** (*dtlpy.entities.dataset.Dataset*) – dataset object, the dataset that refer to the assignment


    * **filters** (*dtlpy.entities.filters.Filters*) – Filters entity or a dictionary containing filters parameters



* **Returns**

    pages of the items



* **Return type**

    dtlpy.entities.paged_entities.PagedEntities


**Example**:

```python
items = task.assignments.get_items()
```


#### open_in_web()
Open the assignment in web platform

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Returns**

    

**Example**:

```python
assignment.open_in_web()
```


#### reassign(assignee_id, wait=True)
Reassign an assignment

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Parameters**

    
    * **assignee_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the email of the user that want to assign the assignment


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until reassign assignment finish



* **Returns**

    Assignment object



* **Return type**

    dtlpy.entities.assignment.Assignment


**Example**:

```python
assignment = assignment.reassign(assignee_ids='annotator1@dataloop.ai')
```


#### redistribute(workload, wait=True)
Redistribute an assignment

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Parameters**

    
    * **workload** (*dtlpy.entities.assignment.Workload*) – list of WorkloadUnit objects. Customize distribution (percentage) between the task assignees. For example: [dl.WorkloadUnit([annotator@hi.com](mailto:annotator@hi.com), 80), dl.WorkloadUnit([annotator2@hi.com](mailto:annotator2@hi.com), 20)]


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until redistribute assignment finish



* **Returns**

    Assignment object



* **Return type**

    dtlpy.entities.assignment.Assignment assignment


**Example**:

```python
assignment = assignment.redistribute(workload=dl.Workload([dl.WorkloadUnit(assignee_id="annotator1@dataloop.ai", load=50),
                                             dl.WorkloadUnit(assignee_id="annotator2@dataloop.ai", load=50)]))
```


#### set_status(status: [str](https://docs.python.org/3/library/stdtypes.html#str), operation: [str](https://docs.python.org/3/library/stdtypes.html#str), item_id: [str](https://docs.python.org/3/library/stdtypes.html#str))
Set item status within assignment

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Parameters**

    
    * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – string the describes the status


    * **operation** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the status action need ‘create’ or ‘delete’


    * **item_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – item id that want to set his status



* **Returns**

    True id success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = assignment.set_status(status='complete',
                        operation='created',
                        item_id='item_id')
```


#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(system_metadata=False)
Update an assignment

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Parameters**

    **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – True, if you want to change metadata system



* **Returns**

    Assignment object



* **Return type**

    dtlpy.entities.assignment.Assignment assignment


**Example**:

```python
assignment = assignment.update(system_metadata=False)
```


### _class_ Workload(workload: [list](https://docs.python.org/3/library/stdtypes.html#list) = NOTHING)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Workload object


#### add(assignee_id)
add a assignee


* **Parameters**

    **assignee_id** – 



#### _classmethod_ generate(assignee_ids, loads=None)
generate the loads for the given assignee
:param assignee_ids:
:param loads:


### _class_ WorkloadUnit(assignee_id: [str](https://docs.python.org/3/library/stdtypes.html#str), load: [float](https://docs.python.org/3/library/functions.html#float) = 0)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

WorkloadUnit object

## Package


### _class_ Package(_dict)
Bases: `DlEntity`

Package object


#### build(module_name=None, init_inputs=None, local_path=None, from_local=None)
Instantiate a module from the package code. Returns a loaded instance of the runner class


* **Parameters**

    
    * **module_name** – Name of the module to build the runner class


    * **init_inputs** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – dictionary of the class init variables (if exists). will be used to init the module class


    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local path of the package (if from_local=False - codebase will be downloaded)


    * **from_local** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool. if true - codebase will not be downloaded (only use local files)



* **Returns**

    dl.BaseServiceRunner



#### checkout()
Checkout as package


* **Returns**

    


#### delete()
Delete Package object


* **Returns**

    True



#### deploy(service_name=None, revision=None, init_input=None, runtime=None, sdk_version=None, agent_versions=None, verify=True, bot=None, pod_type=None, module_name=None, run_execution_as_process=None, execution_timeout=None, drain_time=None, on_reset=None, max_attempts=None, force=False, secrets: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[list](https://docs.python.org/3/library/stdtypes.html#list)] = None, \*\*kwargs)
Deploy package


* **Parameters**

    
    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service name


    * **revision** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package revision - default=latest


    * **init_input** – config to run at startup


    * **runtime** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – runtime resources


    * **sdk_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
        * optional - string - sdk version



    * **agent_versions** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – 
        * dictionary - - optional -versions of sdk, agent runner and agent proxy



    * **bot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – bot email


    * **pod_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pod type dl.InstanceCatalog


    * **verify** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – verify the inputs


    * **module_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – module name


    * **run_execution_as_process** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – run execution as process


    * **execution_timeout** ([*int*](https://docs.python.org/3/library/functions.html#int)) – execution timeout


    * **drain_time** ([*int*](https://docs.python.org/3/library/functions.html#int)) – drain time


    * **on_reset** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – on reset


    * **max_attempts** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Maximum execution retries in-case of a service reset


    * **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - terminate old replicas immediately


    * **secrets** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of the integrations ids



* **Returns**

    Service object



* **Return type**

    dtlpy.entities.service.Service


**Example**:

```python
```

service: dl.Service = package.deploy(service_name=package_name,

    execution_timeout=3 \* 60 \* 60,
    module_name=module.name,
    runtime=dl.KubernetesRuntime(

    > concurrency=10,
    > pod_type=dl.InstanceCatalog.REGULAR_S,
    > autoscaler=dl.KubernetesRabbitmqAutoscaler(

    > > min_replicas=1,
    > > max_replicas=20,
    > > queue_length=20

    > )


#### _classmethod_ from_json(_json, client_api, project, is_fetched=True)
Turn platform representation of package into a package entity


* **Parameters**

    
    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – platform representation of package


    * **client_api** (*dl.ApiClient*) – ApiClient entity


    * **project** (*dtlpy.entities.project.Project*) – project entity


    * **is_fetched** – is Entity fetched from Platform



* **Returns**

    Package entity



* **Return type**

    dtlpy.entities.package.Package



#### _static_ get_ml_metadata(cls=None, available_methods=None, output_type=AnnotationType.CLASSIFICATION, input_type='image', default_configuration: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)] = None)
Create ML metadata for the package
:param cls: ModelAdapter class, to get the list of available_methods
:param available_methods: available user function on the adapter.  [‘load’, ‘save’, ‘predict’, ‘train’, ‘evaluate’]
:param output_type: annotation type the model create, e.g. dl.AnnotationType.CLASSIFICATION
:param input_type: input file type the model gets, one of [‘image’, ‘video’, ‘txt’]
:param default_configuration: default service configuration for the deployed services
:return:


#### open_in_web()
Open the package in web platform


#### pull(version=None, local_path=None)
Pull local package


* **Parameters**

    
    * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – version


    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local path


**Example**:

```python
path = package.pull(local_path='local_path')
```


#### push(codebase: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[GitCodebase, ItemCodebase]] = None, src_path: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, package_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, modules: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[list](https://docs.python.org/3/library/stdtypes.html#list)] = None, checkout: [bool](https://docs.python.org/3/library/functions.html#bool) = False, revision_increment: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, service_update: [bool](https://docs.python.org/3/library/functions.html#bool) = False, service_config: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)] = None, package_type='faas')
Push local package


* **Parameters**

    
    * **codebase** (*dtlpy.entities.codebase.Codebase*) – PackageCode object - defines how to store the package code


    * **checkout** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – save package to local checkout


    * **src_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – location of pacjage codebase folder to zip


    * **package_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – name of package


    * **modules** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of PackageModule


    * **revision_increment** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - str - version bumping method - major/minor/patch - default = None


    * **service_update** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - bool - update the service


:param dict service_config : Service object as dict. Contains the spec of the default service to create.
:param  str package_type: default is “faas”, one of “app”, “ml”
:return: package entity
:rtype: dtlpy.entities.package.Package

**Example**:

```python
package = packages.push(package_name='package_name',
                        modules=[module],
                        version='1.0.0',
                        src_path=os.getcwd())
```


#### test(cwd=None, concurrency=None, module_name='default_module', function_name='run', class_name='ServiceRunner', entry_point='main.py')
Test local package in local environment.


* **Parameters**

    
    * **cwd** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to the file


    * **concurrency** ([*int*](https://docs.python.org/3/library/functions.html#int)) – the concurrency of the test


    * **module_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – module name


    * **function_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – function name


    * **class_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – class name


    * **entry_point** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the file to run like main.py



* **Returns**

    list created by the function that tested the output



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
package.test(cwd='path_to_package',
            function_name='run')
```


#### to_json()
Turn Package entity into a platform representation of Package


* **Returns**

    platform json of package



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update()
Update Package changes to platform


* **Returns**

    Package entity



### _class_ RequirementOperator(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

### Package Function


### _class_ PackageFunction(outputs=NOTHING, name=NOTHING, description='', inputs=NOTHING, display_name=None, display_icon=None)
Bases: `BaseEntity`

Webhook object


### _class_ PackageInputType(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

### Package Module


### _class_ PackageModule(name=NOTHING, init_inputs=NOTHING, entry_point='main.py', class_name='ServiceRunner', functions=NOTHING)
Bases: `BaseEntity`

PackageModule object


#### add_function(function)

* **Parameters**

    **function** – 



#### _classmethod_ from_entry_point(entry_point)
Create a dl.PackageModule entity using decorator on the service class.


* **Parameters**

    **entry_point** – path to the python file with the runner class (relative to the package path)



* **Returns**

    

### Slot


### _class_ PackageSlot(module_name='default_module', function_name='run', display_name=None, display_scopes: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[list](https://docs.python.org/3/library/stdtypes.html#list)] = None, display_icon=None, post_action: SlotPostAction = NOTHING, default_inputs: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[list](https://docs.python.org/3/library/stdtypes.html#list)] = None, input_options: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[list](https://docs.python.org/3/library/stdtypes.html#list)] = None)
Bases: `BaseEntity`

Webhook object


### _class_ SlotDisplayScopeResource(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ SlotPostActionType(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ UiBindingPanel(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

### Codebase

## Service


### _class_ InstanceCatalog(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

The Service Pode size.

| State

               | Description

                                                       |
| ------------------- | ----------------------------------------------------------------- |
| REGULAR_XS

          | regular pod with extra small size

                                 |
| REGULAR_S

           | regular pod with small size

                                       |
| REGULAR_M

           | regular pod with medium size

                                      |
| REGULAR_L

           | regular pod with large size

                                       |
| REGULAR_XL

          | regular pod with extra large size

                                 |
| HIGHMEM_XS

          | highmem pod with extra small size

                                 |
| HIGHMEM_S

           | highmem pod with small size

                                       |
| HIGHMEM_M

           | highmem pod with medium size

                                      |
| HIGHMEM_L

           | highmem pod with large size

                                       |
| HIGHMEM_XL

          | highmem pod with extra large size

                                 |
| GPU_K80_S

           | GPU pod with small size

                                           |
| GPU_K80_M

           | GPU pod with medium size

                                          |

### _class_ KubernetesAutuscalerType(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

The Service Autuscaler Type (RABBITMQ, CPU).

| State

               | Description

                                                       |
| ------------------- | ----------------------------------------------------------------- |
| RABBITMQ

            | Service Autuscaler will be in RABBITMQ

                            |
| CPU

                 | Service Autuscaler will be in in local CPU

                        |

### _class_ OnResetAction(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

The Execution action when the service reset (RERUN, FAILED).

| State

               | Description

                                                       |
| ------------------- | ----------------------------------------------------------------- |
| RERUN

               | When the service resting rerun the execution

                      |
| FAILED

              | When the service resting fail the execution

                       |

### _class_ RuntimeType(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Service culture Runtime (KUBERNETES).

| State

               | Description

                                                       |
| ------------------- | ----------------------------------------------------------------- |
| KUBERNETES

          | Service run in kubernetes culture

                                 |

### _class_ Service(created_at, updated_at, creator, version, package_id, package_revision, bot, use_user_jwt, init_input, versions, module_name, name, url, id, active, driver_id, secrets, runtime: KubernetesRuntime, queue_length_limit, run_execution_as_process: [bool](https://docs.python.org/3/library/functions.html#bool), execution_timeout, drain_time, on_reset: OnResetAction, type: ServiceType, project_id, is_global, max_attempts, package, client_api: ApiClient, revisions=None, project=None, repositories=NOTHING)
Bases: `BaseEntity`

Service object


#### activate_slots(project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, task_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, org_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, user_email: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, slots=None, role=None, prevent_override: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visible: [bool](https://docs.python.org/3/library/functions.html#bool) = True, icon: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'fas fa-magic', \*\*kwargs)
Activate service slots


* **Parameters**

    
    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – project id


    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – task id


    * **dataset_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – dataset id


    * **org_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – org id


    * **user_email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – user email


    * **slots** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of entities.PackageSlot


    * **role** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – user role MemberOrgRole.ADMIN, MemberOrgRole.owner, MemberOrgRole.MEMBER


    * **prevent_override** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – True to prevent override


    * **visible** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – visible


    * **icon** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – icon


    * **kwargs** – all additional arguments



* **Returns**

    list of user setting for activated slots



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
setting = service.activate_slots(project_id='project_id',
                        slots=List[entities.PackageSlot],
                        icon='fas fa-magic')
```


#### checkout()
Checkout


* **Returns**

    


#### delete()
Delete Service object


* **Returns**

    True



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### execute(execution_input=None, function_name=None, resource=None, item_id=None, dataset_id=None, annotation_id=None, project_id=None, sync=False, stream_logs=True, return_output=True)
Execute a function on an existing service


* **Parameters**

    
    * **execution_input** (*List**[**FunctionIO**] or *[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – input dictionary or list of FunctionIO entities


    * **function_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – function name to run


    * **resource** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – input type.


    * **item_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - item id as input to function


    * **dataset_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - dataset id as input to function


    * **annotation_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - annotation id as input to function


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – resource’s project


    * **sync** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true, wait for function to end


    * **stream_logs** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – prints logs of the new execution. only works with sync=True


    * **return_output** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if True and sync is True - will return the output directly



* **Returns**

    execution object



* **Return type**

    dtlpy.entities.execution.Execution


**Example**:

```python
execution = service.execute(function_name='function_name', item_id='item_id', project_id='project_id')
```


#### _classmethod_ from_json(_json: [dict](https://docs.python.org/3/library/stdtypes.html#dict), client_api: ApiClient, package=None, project=None, is_fetched=True)
Build a service entity object from a json


* **Parameters**

    
    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – platform json


    * **client_api** (*dl.ApiClient*) – ApiClient entity


    * **package** (*dtlpy.entities.package.Package*) – package entity


    * **project** (*dtlpy.entities.project.Project*) – project entity


    * **is_fetched** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is Entity fetched from Platform



* **Returns**

    service object



* **Return type**

    dtlpy.entities.service.Service



#### log(size=None, checkpoint=None, start=None, end=None, follow=False, text=None, execution_id=None, function_name=None, replica_id=None, system=False, view=True, until_completed=True)
Get service logs


* **Parameters**

    
    * **size** ([*int*](https://docs.python.org/3/library/functions.html#int)) – size


    * **checkpoint** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – the information from the lst point checked in the service


    * **start** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – iso format time


    * **end** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – iso format time


    * **follow** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true, keep stream future logs


    * **text** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – text


    * **execution_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – execution id


    * **function_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – function name


    * **replica_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – replica id


    * **system** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – system


    * **view** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true, print out all the logs


    * **until_completed** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until completed



* **Returns**

    ServiceLog entity



* **Return type**

    [ServiceLog](repositories.md#dtlpy.repositories.services.ServiceLog)


**Example**:

```python
service_log = service.log()
```


#### open_in_web()
Open the service in web platform


* **Returns**

    


#### pause()

* **Returns**

    


#### resume()

* **Returns**

    


#### status()
Get Service status


* **Returns**

    status json



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update(force=False)
Update Service changes to platform


* **Parameters**

    **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – force update



* **Returns**

    Service entity



* **Return type**

    dtlpy.entities.service.Service



### _class_ ServiceType(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

The type of the service (SYSTEM).

| State

               | Description

                                                       |
| ------------------- | ----------------------------------------------------------------- |
| SYSTEM

              | Dataloop internal service

                                         |
### Bot


### _class_ Bot(created_at, updated_at, name, last_name, username, avatar, email, role, type, org, id, project, client_api=None, users=None, bots=None, password=None)
Bases: `User`

Bot entity


#### delete()
Delete the bot


* **Returns**

    True



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### _classmethod_ from_json(_json, project, client_api, bots=None)
Build a Bot entity object from a json


* **Parameters**

    
    * **_json** – _json response from host


    * **project** – project entity


    * **client_api** – ApiClient entity


    * **bots** – Bots repository



* **Returns**

    User object



#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)


## Trigger


### _class_ BaseTrigger(id, url, created_at, updated_at, creator, name, active, type, scope, is_global, input, function_name, service_id, webhook_id, pipeline_id, special, project_id, spec, operation, service, project, client_api: ApiClient, op_type='service', repositories=NOTHING)
Bases: `BaseEntity`

Trigger Entity


#### delete()
Delete Trigger object


* **Returns**

    True



#### _classmethod_ from_json(_json, client_api, project, service=None)
Build a trigger entity object from a json


* **Parameters**

    
    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – platform json


    * **client_api** (*dl.ApiClient*) – ApiClient entity


    * **project** (*dtlpy.entities.project.Project*) – project entity


    * **service** (*dtlpy.entities.service.Service*) – service entity



* **Returns**

    


#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update()
Update Trigger object


* **Returns**

    Trigger entity



### _class_ CronTrigger(id, url, created_at, updated_at, creator, name, active, type, scope, is_global, input, function_name, service_id, webhook_id, pipeline_id, special, project_id, spec, operation, service, project, client_api: ApiClient, op_type='service', repositories=NOTHING, start_at=None, end_at=None, cron=None)
Bases: `BaseTrigger`


#### _classmethod_ from_json(_json, client_api, project, service=None)
Build a trigger entity object from a json


* **Parameters**

    
    * **_json** – platform json


    * **client_api** – ApiClient entity


    * **project** – project entity


    * **service** – service entity



* **Returns**

    


#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



### _class_ Trigger(id, url, created_at, updated_at, creator, name, active, type, scope, is_global, input, function_name, service_id, webhook_id, pipeline_id, special, project_id, spec, operation, service, project, client_api: ApiClient, op_type='service', repositories=NOTHING, filters=None, execution_mode=TriggerExecutionMode.ONCE, actions=TriggerAction.CREATED, resource=TriggerResource.ITEM)
Bases: `BaseTrigger`

Trigger Entity


#### _classmethod_ from_json(_json, client_api, project, service=None)
Build a trigger entity object from a json


* **Parameters**

    
    * **_json** – platform json


    * **client_api** – ApiClient entity


    * **project** (*dtlpy.entities.project.Project*) – project entity


    * **service** (*dtlpy.entities.service.Service*) – service entity



* **Returns**

    


#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



### _class_ TriggerAction(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ TriggerExecutionMode(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ TriggerResource(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.


### _class_ TriggerType(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

## Execution


### _class_ Execution(id, url, creator, created_at, updated_at, input, output, feedback_queue, status, status_log, sync_reply_to, latest_status, function_name, duration, attempts, max_attempts, to_terminate: [bool](https://docs.python.org/3/library/functions.html#bool), trigger_id, service_id, project_id, service_version, package_id, package_name, client_api: ApiClient, service, project=None, repositories=NOTHING, pipeline: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)] = None)
Bases: `BaseEntity`

Service execution entity


#### _classmethod_ from_json(_json, client_api, project=None, service=None, is_fetched=True)

* **Parameters**

    
    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – platform json


    * **client_api** (*dl.ApiClient*) – ApiClient entity


    * **project** (*dtlpy.entities.project.Project*) – project entity


    * **service** (*dtlpy.entities.service.Service*) – 


    * **is_fetched** – is Entity fetched from Platform



#### increment()
Increment attempts


* **Returns**

    


#### logs(follow=False)
Print logs for execution


* **Parameters**

    **follow** – keep stream future logs



#### progress_update(status: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[ExecutionStatus] = None, percent_complete: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, message: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, output: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, service_version: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Update Execution Progress


* **Parameters**

    
    * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – ExecutionStatus


    * **percent_complete** ([*int*](https://docs.python.org/3/library/functions.html#int)) – percent complete


    * **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – message to update the progress state


    * **output** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – output


    * **service_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service version



* **Returns**

    Service execution object



#### rerun(sync: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Re-run


* **Returns**

    Execution object



#### terminate()
Terminate execution


* **Returns**

    execution object



#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update()
Update execution changes to platform


* **Returns**

    execution entity



#### wait()
Wait for execution


* **Returns**

    Service execution object



### _class_ ExecutionStatus(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

## Pipeline


### _class_ Pipeline(id, name, creator, org_id, connections, created_at, updated_at, start_nodes, project_id, composition_id, url, preview, description, revisions, project, client_api: ApiClient, repositories=NOTHING)
Bases: `BaseEntity`

Package object


#### delete()
Delete pipeline object


* **Returns**

    True



#### execute(execution_input=None)
execute a pipeline and return the execute


* **Parameters**

    **execution_input** – list of the dl.FunctionIO or dict of pipeline input - example {‘item’: ‘item_id’}



* **Returns**

    entities.PipelineExecution object



#### _classmethod_ from_json(_json, client_api, project, is_fetched=True)
Turn platform representation of pipeline into a pipeline entity


* **Parameters**

    
    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – platform representation of package


    * **client_api** (*dl.ApiClient*) – ApiClient entity


    * **project** (*dtlpy.entities.project.Project*) – project entity


    * **is_fetched** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is Entity fetched from Platform



* **Returns**

    Pipeline entity



* **Return type**

    dtlpy.entities.pipeline.Pipeline



#### install()
install pipeline


* **Returns**

    Composition entity



#### open_in_web()
Open the pipeline in web platform


* **Returns**

    


#### pause()
pause pipeline


* **Returns**

    Composition entity



#### reset(stop_if_running: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Resets pipeline counters


* **Parameters**

    **stop_if_running** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – If the pipeline is installed it will stop the pipeline and reset the counters.



* **Returns**

    bool



#### set_start_node(node: PipelineNode)
Set the start node of the pipeline


* **Parameters**

    **node** (*PipelineNode*) – node to be the start node



#### stats()
Get pipeline counters


* **Returns**

    PipelineStats



* **Return type**

    dtlpy.entities.pipeline.PipelineStats



#### to_json()
Turn Package entity into a platform representation of Package


* **Returns**

    platform json of package



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### update()
Update pipeline changes to platform


* **Returns**

    pipeline entity


### Pipeline Execution


### _class_ PipelineExecution(id, nodes, executions, status, created_at, updated_at, pipeline_id, max_attempts, pipeline, client_api: ApiClient, repositories=NOTHING)
Bases: `BaseEntity`

Package object


#### _classmethod_ from_json(_json, client_api, pipeline, is_fetched=True)
Turn platform representation of pipeline_execution into a pipeline_execution entity


* **Parameters**

    
    * **_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – platform representation of package


    * **client_api** (*dl.ApiClient*) – ApiClient entity


    * **pipeline** (*dtlpy.entities.pipeline.Pipeline*) – Pipeline entity


    * **is_fetched** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is Entity fetched from Platform



* **Returns**

    Pipeline entity



* **Return type**

    dtlpy.entities.pipeline.Pipeline



#### to_json()
Turn Package entity into a platform representation of Package


* **Returns**

    platform json of package



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)


## Other

### Pages


### _class_ PagedEntities(client_api: ApiClient, page_offset, page_size, filters, items_repository, has_next_page=False, total_pages_count=0, items_count=0, service_id=None, project_id=None, order_by_type=None, order_by_direction=None, execution_status=None, execution_resource_type=None, execution_resource_id=None, execution_function_name=None, list_function=None, items=[])
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Pages object


#### get_page(page_offset=None, page_size=None)
Get page


* **Parameters**

    
    * **page_offset** – page offset


    * **page_size** – page size



#### go_to_page(page=0)
Brings specified page of items from host


* **Parameters**

    **page** – page number



* **Returns**

    


#### next_page()
Brings the next page of items from host


* **Returns**

    


#### prev_page()
Brings the previous page of items from host


* **Returns**

    


#### process_result(result)

* **Parameters**

    **result** – json object



#### return_page(page_offset=None, page_size=None)
Return page


* **Parameters**

    
    * **page_offset** – page offset


    * **page_size** – page size


### Base Entity


### _class_ EntityScopeLevel(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

### Command


### _class_ Command(id, url, status, created_at, updated_at, type, progress, spec, error, client_api: ApiClient, repositories=NOTHING)
Bases: `BaseEntity`

Com entity


#### abort()
abort command


* **Returns**

    


#### _classmethod_ from_json(_json, client_api, is_fetched=True)
Build a Command entity object from a json


* **Parameters**

    
    * **_json** – _json response from host


    * **client_api** – ApiClient entity


    * **is_fetched** – is Entity fetched from Platform



* **Returns**

    Command object



#### in_progress()
Check if command is still in one of the in progress statuses


* **Returns**

    True if command still in progress



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### to_json()
Returns platform _json format of object


* **Returns**

    platform json format of object



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)



#### wait(timeout=0, step=None, backoff_factor=0.1)
Wait for Command to finish


* **Parameters**

    
    * **timeout** ([*int*](https://docs.python.org/3/library/functions.html#int)) – int, seconds to wait until TimeoutError is raised. if 0 - wait until done


    * **step** ([*int*](https://docs.python.org/3/library/functions.html#int)) – int, seconds between polling


    * **backoff_factor** ([*float*](https://docs.python.org/3/library/functions.html#float)) – A backoff factor to apply between attempts after the second try



* **Returns**

    Command  object



### _class_ CommandsStatus(value)
Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

An enumeration.

### Directory Tree


### _class_ DirectoryTree(_json)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Dataset DirectoryTree


### _class_ SingleDirectory(value, directory_tree, children=None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

DirectoryTree single directory
