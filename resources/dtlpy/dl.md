# Repositories

## Organizations


### _class_ Organizations(client_api: ApiClient)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Organizations Repository

Read our [documentation](https://dataloop.ai/docs/org-setup) and [SDK documentation](https://dataloop.ai/docs/sdk-org) to learn more about Organizations in the Dataloop platform.


#### add_member(email: [str](https://docs.python.org/3/library/stdtypes.html#str), role: [MemberOrgRole](entities.md#dtlpy.entities.organization.MemberOrgRole) = MemberOrgRole.MEMBER, organization_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Organization](entities.md#dtlpy.entities.organization.Organization)] = None)
Add members to your organization. Read about members and groups [here](https://dataloop.ai/docs/org-members-groups).

**Prerequisities**: To add members to an organization, you must be an *owner* in that organization.

You must provide at least ONE of the following params: organization, organization_name, or organization_id.


* **Parameters**

    
    * **email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the member’s email


    * **role** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – MemberOrgRole.ADMIN, MemberOrgRole.OWNER, MemberOrgRole.MEMBER


    * **organization_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization id


    * **organization_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization name


    * **organization** (*entities.Organization*) – Organization object



* **Returns**

    True if successful or error if unsuccessful



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = dl.organizations.add_member(email='user@domain.com',
                            organization_id='organization_id',
                            role=dl.MemberOrgRole.MEMBER)
```


#### cache_action(organization_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Organization](entities.md#dtlpy.entities.organization.Organization)] = None, mode=CacheAction.APPLY, pod_type=PodType.SMALL)
Add or remove Cache for the org

**Prerequisites**: You must be an organization *owner*

You must provide at least ONE of the following params: organization, organization_name, or organization_id.


* **Parameters**

    
    * **organization_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization id


    * **organization_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization name


    * **organization** (*entities.Organization*) – Organization object


    * **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – dl.CacheAction.APPLY or dl.CacheAction.DESTROY


    * **pod_type** (*entities.PodType*) – dl.PodType.SMALL, dl.PodType.MEDIUM, dl.PodType.HIGH



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = dl.organizations.enable_cache(organization_id='organization_id',
                              mode=dl.CacheAction.APPLY)
```


#### delete_member(user_id: [str](https://docs.python.org/3/library/stdtypes.html#str), organization_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Organization](entities.md#dtlpy.entities.organization.Organization)] = None, sure: [bool](https://docs.python.org/3/library/functions.html#bool) = False, really: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Delete member from the Organization.

**Prerequisites**: Must be an organization *owner* to delete members.

You must provide at least ONE of the following params: organization_id, organization_name, organization.


* **Parameters**

    
    * **user_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – user id


    * **organization_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization id


    * **organization_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization name


    * **organization** (*entities.Organization*) – Organization object


    * **sure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Are you sure you want to delete?


    * **really** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Really really sure?



* **Returns**

    True if success and error if not



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = dl.organizations.delete_member(user_id='user_id',
                                organization_id='organization_id',
                                sure=True,
                                really=True)
```


#### get(organization_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, fetch: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[bool](https://docs.python.org/3/library/functions.html#bool)] = None)
Get Organization object to be able to use it in your code.

**Prerequisites**: You must be a **superuser** to use this method.

You must provide at least ONE of the following params: organization_name or organization_id.


* **Parameters**

    
    * **organization_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id


    * **organization_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by name


    * **fetch** – optional - fetch entity from platform, default taken from cookie



* **Returns**

    Organization object



* **Return type**

    [dtlpy.entities.organization.Organization](entities.md#dtlpy.entities.organization.Organization)


**Example**:

```python
org = dl.organizations.get(organization_id='organization_id')
```


#### list()
Lists all the organizations in Dataloop.

**Prerequisites**: You must be a **superuser** to use this method.


* **Returns**

    List of Organization objects



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
organizations = dl.organizations.list()
```


#### list_groups(organization: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Organization](entities.md#dtlpy.entities.organization.Organization)] = None, organization_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
List all organization groups (groups that were created within the organization).

**Prerequisites**: You must be an organization *owner* to use this method.

You must provide at least ONE of the following params: organization, organization_name, or organization_id.


* **Parameters**

    
    * **organization** (*entities.Organization*) – Organization object


    * **organization_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization id


    * **organization_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization name



* **Returns**

    groups list



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
groups_list = dl.organizations.list_groups(organization_id='organization_id')
```


#### list_integrations(organization: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Organization](entities.md#dtlpy.entities.organization.Organization)] = None, organization_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, only_available=False)
List all organization integrations with external cloud storage.

**Prerequisites**: You must be an organization *owner* to use this method.

You must provide at least ONE of the following params: organization_id, organization_name, or organization.


* **Parameters**

    
    * **organization** (*entities.Organization*) – Organization object


    * **organization_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization id


    * **organization_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization name


    * **only_available** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if True list only the available integrations



* **Returns**

    integrations list



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
list_integrations = dl.organizations.list_integrations(organization='organization-entity',
                                    only_available=True)
```


#### list_members(organization: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Organization](entities.md#dtlpy.entities.organization.Organization)] = None, organization_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, role: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[MemberOrgRole](entities.md#dtlpy.entities.organization.MemberOrgRole)] = None)
List all organization members.

**Prerequisites**: You must be an organization *owner* to use this method.

You must provide at least ONE of the following params: organization_id, organization_name, or organization.


* **Parameters**

    
    * **organization** (*entities.Organization*) – Organization object


    * **organization_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization id


    * **organization_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization name


    * **role** (*entities.MemberOrgRole*) – MemberOrgRole.ADMIN, MemberOrgRole.OWNER, MemberOrgRole.MEMBER



* **Returns**

    projects list



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
list_members = dl.organizations.list_members(organization='organization-entity',
                            role=dl.MemberOrgRole.MEMBER)
```


#### update(plan: [str](https://docs.python.org/3/library/stdtypes.html#str), organization: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Organization](entities.md#dtlpy.entities.organization.Organization)] = None, organization_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Update an organization.

**Prerequisites**: You must be a **superuser** to update an organization.

You must provide at least ONE of the following params: organization, organization_name, or organization_id.


* **Parameters**

    
    * **plan** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – OrganizationsPlans.FREEMIUM, OrganizationsPlans.PREMIUM


    * **organization** (*entities.Organization*) – Organization object


    * **organization_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization id


    * **organization_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization name



* **Returns**

    organization object



* **Return type**

    [dtlpy.entities.organization.Organization](entities.md#dtlpy.entities.organization.Organization)


**Example**:

```python
org = dl.organizations.update(organization='organization-entity',
                        plan=dl.OrganizationsPlans.FREEMIUM)
```


#### update_member(email: [str](https://docs.python.org/3/library/stdtypes.html#str), role: [MemberOrgRole](entities.md#dtlpy.entities.organization.MemberOrgRole) = MemberOrgRole.MEMBER, organization_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, organization: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Organization](entities.md#dtlpy.entities.organization.Organization)] = None)
Update member role.

**Prerequisites**: You must be an organization *owner* to update a member’s role.

You must provide at least ONE of the following params: organization, organization_name, or organization_id.


* **Parameters**

    
    * **email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the member’s email


    * **role** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – MemberOrgRole.ADMIN, MemberOrgRole.OWNER, MemberOrgRole.MEMBER


    * **organization_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization id


    * **organization_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Organization name


    * **organization** (*entities.Organization*) – Organization object



* **Returns**

    json of the member fields



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)


**Example**:

```python
member_json = dl.organizations.update_member(email='user@domain.com',
                                organization_id='organization_id',
                                 role=dl.MemberOrgRole.MEMBER)
```

### Integrations

Integrations Repository


### _class_ Integrations(client_api: ApiClient, org: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Organization](entities.md#dtlpy.entities.organization.Organization)] = None, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Integrations Repository

The Integrations class allows you to manage data integrtion from your external storage (e.g., S3, GCS, Azure) into your Dataloop’s Dataset storage, as well as sync data in your Dataloop’s Datasets with data in your external storage.

For more information on Organization Storgae Integration see the [Dataloop documentation](https://dataloop.ai/docs/organization-integrations)  and [SDK External Storage](https://dataloop.ai/docs/sdk-sync-storage).


#### create(integrations_type: [ExternalStorage](entities.md#dtlpy.entities.driver.ExternalStorage), name: [str](https://docs.python.org/3/library/stdtypes.html#str), options: [dict](https://docs.python.org/3/library/stdtypes.html#dict))
Create an integration between an external storage and the organization.

**Examples for options include**:
s3 - {key: “”, secret: “”};
gcs - {key: “”, secret: “”, content: “”};
azureblob - {key: “”, secret: “”, clientId: “”, tenantId: “”};
key_value - {key: “”, value: “”}
aws-sts - {key: “”, secret: “”, roleArns: “”}

**Prerequisites**: You must be an *owner* in the organization.


* **Parameters**

    
    * **integrations_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – integrations type dl.ExternalStorage


    * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – integrations name


    * **options** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – dict of storage secrets



* **Returns**

    success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
project.integrations.create(integrations_type=dl.ExternalStorage.S3,
                name='S3ntegration',
                options={key: "Access key ID", secret: "Secret access key"})
```


#### delete(integrations_id: [str](https://docs.python.org/3/library/stdtypes.html#str), sure: [bool](https://docs.python.org/3/library/functions.html#bool) = False, really: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Delete integrations from the organization.

**Prerequisites**: You must be an organization *owner* to delete an integration.


* **Parameters**

    
    * **integrations_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – integrations id


    * **sure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Are you sure you want to delete?


    * **really** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Really really sure?



* **Returns**

    success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
project.integrations.delete(integrations_id='integrations_id', sure=True, really=True)
```


#### get(integrations_id: [str](https://docs.python.org/3/library/stdtypes.html#str))
Get organization integrations. Use this method to access your integration and be able to use it in your code.

**Prerequisites**: You must be an *owner* in the organization.


* **Parameters**

    **integrations_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – integrations id



* **Returns**

    Integration object



* **Return type**

    [dtlpy.entities.integration.Integration](entities.md#dtlpy.entities.integration.Integration)


**Example**:

```python
project.integrations.get(integrations_id='integrations_id')
```


#### list(only_available=False)
List all the organization’s integrations with external storage.

**Prerequisites**: You must be an *owner* in the organization.


* **Parameters**

    **only_available** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if True list only the available integrations.



* **Returns**

    groups list



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
project.integrations.list(only_available=True)
```


#### update(new_name: [str](https://docs.python.org/3/library/stdtypes.html#str), integrations_id: [str](https://docs.python.org/3/library/stdtypes.html#str))
Update the integration’s name.

**Prerequisites**: You must be an *owner* in the organization.


* **Parameters**

    
    * **new_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – new name


    * **integrations_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – integrations id



* **Returns**

    Integration object



* **Return type**

    [dtlpy.entities.integration.Integration](entities.md#dtlpy.entities.integration.Integration)


**Example**:

```python
project.integrations.update(integrations_id='integrations_id', new_name="new_integration_name")
```

## Projects


### _class_ Projects(client_api: ApiClient, org=None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Projects Repository

The Projects class allows the user to manage projects and their properties.

For more information on Projects see the [Dataloop documentation](https://dataloop.ai/docs/project#)  and [SDK documentation](https://dataloop.ai/docs/sdk-projects).


#### add_member(email: [str](https://docs.python.org/3/library/stdtypes.html#str), project_id: [str](https://docs.python.org/3/library/stdtypes.html#str), role: [MemberRole](entities.md#dtlpy.entities.project.MemberRole) = MemberRole.DEVELOPER)
Add a member to the project.

**Prerequisites**: You must be in the role of an *owner* to add a member to a project.


* **Parameters**

    
    * **email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – member email


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Id of the project


    * **role** – The required role for the user. Use the enum dl.MemberRole



* **Returns**

    dict that represent the user



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)


**Example**:

```python
user_json = dl.projects.add_member(project_id='project_id', email='user@dataloop.ai', role=dl.MemberRole.DEVELOPER)
```


#### checkout(identifier: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, project_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None)
Checkout (switch) to a project to work on.

**Prerequisites**: All users can open a project in the web.

You must provide at least ONE of the following params: project_id, project_name.


* **Parameters**

    
    * **identifier** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – project name or partial id that you wish to switch


    * **project_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Name of the project


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Id of the project


    * **project** ([*dtlpy.entities.project.Project*](entities.md#dtlpy.entities.project.Project)) – project object


**Example**:

```python
dl.projects.checkout(project_id='project_id')
```


#### create(project_name: [str](https://docs.python.org/3/library/stdtypes.html#str), checkout: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Create a new project.

**Prerequisites**: Any user can create a project.


* **Parameters**

    
    * **project_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Name of the project


    * **checkout** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – set the project as a default project object (cookies)



* **Returns**

    Project object



* **Return type**

    [dtlpy.entities.project.Project](entities.md#dtlpy.entities.project.Project)


**Example**:

```python
project = dl.projects.create(project_name='project_name')
```


#### delete(project_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, sure: [bool](https://docs.python.org/3/library/functions.html#bool) = False, really: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Delete a project forever!

**Prerequisites**: You must be in the role of an *owner* to delete a project.


* **Parameters**

    
    * **project_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by name


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id


    * **sure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Are you sure you want to delete?


    * **really** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Really really sure?



* **Returns**

    True if success, error if not



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
is_deleted = dl.projects.delete(project_id='project_id', sure=True, really=True)
```


#### get(project_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, checkout: [bool](https://docs.python.org/3/library/functions.html#bool) = False, fetch: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[bool](https://docs.python.org/3/library/functions.html#bool)] = None, log_error=True)
Get a Project object.

**Prerequisites**: You must be in the role of an *owner* to get a project object.

You must check out to a project or provide at least one of the following params: project_id, project_name


* **Parameters**

    
    * **project_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by name


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id


    * **checkout** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – set the project as a default project object (cookies)


    * **fetch** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - fetch entity from platform (True), default taken from cookie


    * **log_error** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - show the logs errors



* **Returns**

    Project object



* **Return type**

    [dtlpy.entities.project.Project](entities.md#dtlpy.entities.project.Project)


**Example**:

```python
project = dl.projects.get(project_id='project_id')
```


#### list()
Get the user’s project list

**Prerequisites**: You must be a **superuser** to list all users’ projects.


* **Returns**

    List of Project objects


**Example**:

```python
projects = dl.projects.list()
```


#### list_members(project: [Project](entities.md#dtlpy.entities.project.Project), role: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[MemberRole](entities.md#dtlpy.entities.project.MemberRole)] = None)
Get a list of the project members.

**Prerequisites**: You must be in the role of an *owner* to list project members.


* **Parameters**

    
    * **project** ([*dtlpy.entities.project.Project*](entities.md#dtlpy.entities.project.Project)) – Project object


    * **role** – The required role for the user. Use the enum dl.MemberRole



* **Returns**

    list of the project members



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
users_jsons_list = dl.projects.list_members(project_id='project_id', role=dl.MemberRole.DEVELOPER)
```


#### open_in_web(project_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None)
Open the project in our web platform.

**Prerequisites**: All users can open a project in the web.


* **Parameters**

    
    * **project_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Name of the project


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Id of the project


    * **project** ([*dtlpy.entities.project.Project*](entities.md#dtlpy.entities.project.Project)) – project object


**Example**:

```python
dl.projects.open_in_web(project_id='project_id')
```


#### remove_member(email: [str](https://docs.python.org/3/library/stdtypes.html#str), project_id: [str](https://docs.python.org/3/library/stdtypes.html#str))
Remove a member from the project.

**Prerequisites**: You must be in the role of an *owner* to delete a member from a project.


* **Parameters**

    
    * **email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – member email


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Id of the project



* **Returns**

    dict that represents the user



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)


**Example**:

```python
user_json = dl.projects.remove_member(project_id='project_id', email='user@dataloop.ai')
```


#### update(project: [Project](entities.md#dtlpy.entities.project.Project), system_metadata: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Update a project information (e.g., name, member roles, etc.).

**Prerequisites**: You must be in the role of an *owner* to add a member to a project.


* **Parameters**

    
    * **project** ([*dtlpy.entities.project.Project*](entities.md#dtlpy.entities.project.Project)) – project object


    * **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - True, if you want to change metadata system



* **Returns**

    Project object



* **Return type**

    [dtlpy.entities.project.Project](entities.md#dtlpy.entities.project.Project)


**Example**:

```python
project = dl.projects.delete(project='project_entity')
```


#### update_member(email: [str](https://docs.python.org/3/library/stdtypes.html#str), project_id: [str](https://docs.python.org/3/library/stdtypes.html#str), role: [MemberRole](entities.md#dtlpy.entities.project.MemberRole) = MemberRole.DEVELOPER)
Update member’s information/details in the project.

**Prerequisites**: You must be in the role of an *owner* to update a member.


* **Parameters**

    
    * **email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – member email


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Id of the project


    * **role** – The required role for the user. Use the enum dl.MemberRole



* **Returns**

    dict that represent the user



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)


**Example**:

```python
user_json = = dl.projects.update_member(project_id='project_id', email='user@dataloop.ai', role=dl.MemberRole.DEVELOPER)
```

## Datasets

Datasets Repository


### _class_ Datasets(client_api: ApiClient, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Datasets Repository

The Datasets class allows the user to manage datasets. Read more about datasets in our [documentation](https://dataloop.ai/docs/dataset) and [SDK documentation](https://dataloop.ai/docs/sdk-create-dataset).


#### checkout(identifier: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None)
Checkout (switch) to a dataset to work on it.

**Prerequisites**: You must be an *owner* or *developer* to use this method.

You must provide at least ONE of the following params: dataset_id, dataset_name.


* **Parameters**

    
    * **identifier** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – project name or partial id that you wish to switch


    * **dataset_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Name of the dataset


    * **dataset_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Id of the dataset


    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset object


**Example**:

```python
project.datasets.checkout(dataset_id='dataset_id')
```


#### clone(dataset_id: [str](https://docs.python.org/3/library/stdtypes.html#str), clone_name: [str](https://docs.python.org/3/library/stdtypes.html#str), filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, with_items_annotations: [bool](https://docs.python.org/3/library/functions.html#bool) = True, with_metadata: [bool](https://docs.python.org/3/library/functions.html#bool) = True, with_task_annotations_status: [bool](https://docs.python.org/3/library/functions.html#bool) = True)
Clone a dataset. Read more about cloning datatsets and items in our [documentation](https://dataloop.ai/docs/clone-merge-dataset#cloned-dataset) and [SDK documentation](https://dataloop.ai/docs/sdk-create-dataset#clone-dataset).

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **dataset_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – id of the dataset you wish to clone


    * **clone_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – new dataset name


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a query dict


    * **with_items_annotations** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – true to clone with items annotations


    * **with_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – true to clone with metadata


    * **with_task_annotations_status** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – true to clone with task annotations’ status



* **Returns**

    dataset object



* **Return type**

    [dtlpy.entities.dataset.Dataset](entities.md#dtlpy.entities.dataset.Dataset)


**Example**:

```python
dataset = project.datasets.clone(dataset_id='dataset_id',
                      clone_name='dataset_clone_name',
                      with_metadata=True,
                      with_items_annotations=False,
                      with_task_annotations_status=False)
```


#### create(dataset_name: [str](https://docs.python.org/3/library/stdtypes.html#str), labels=None, attributes=None, ontology_ids=None, driver: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Driver](entities.md#dtlpy.entities.driver.Driver)] = None, driver_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, checkout: [bool](https://docs.python.org/3/library/functions.html#bool) = False, expiration_options: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[ExpirationOptions](entities.md#dtlpy.entities.dataset.ExpirationOptions)] = None, index_driver: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[IndexDriver](entities.md#dtlpy.entities.dataset.IndexDriver)] = None, recipe_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Create a new dataset

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **dataset_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Name of the dataset


    * **labels** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – dictionary of {tag: color} or list of label entities


    * **attributes** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – dataset’s ontology’s attributes


    * **ontology_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – optional - dataset ontology


    * **driver** ([*dtlpy.entities.driver.Driver*](entities.md#dtlpy.entities.driver.Driver)) – optional - storage driver Driver object or driver name


    * **driver_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - driver id


    * **checkout** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – set the dataset as a default dataset object (cookies)


    * **expiration_options** ([*ExpirationOptions*](entities.md#dtlpy.entities.dataset.ExpirationOptions)) – dl.ExpirationOptions object that contain definitions for dataset like MaxItemDays


    * **index_driver** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – dl.IndexDriver, dataset driver version


    * **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - recipe id



* **Returns**

    Dataset object



* **Return type**

    [dtlpy.entities.dataset.Dataset](entities.md#dtlpy.entities.dataset.Dataset)


**Example**:

```python
dataset = project.datasets.create(dataset_name='dataset_name', ontology_ids='ontology_ids')
```


#### delete(dataset_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, sure: [bool](https://docs.python.org/3/library/functions.html#bool) = False, really: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Delete a dataset forever!

**Prerequisites**: You must be an *owner* or *developer* to use this method.

**Example**:

```python
is_deleted = project.datasets.delete(dataset_id='dataset_id', sure=True, really=True)
```


* **Parameters**

    
    * **dataset_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by name


    * **dataset_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id


    * **sure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Are you sure you want to delete?


    * **really** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Really really sure?



* **Returns**

    True is success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### directory_tree(dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None, dataset_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Get dataset’s directory tree.

**Prerequisites**: You must be an *owner* or *developer* to use this method.

You must provide at least ONE of the following params: dataset, dataset_name, dataset_id.


* **Parameters**

    
    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset object


    * **dataset_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Name of the dataset


    * **dataset_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Id of the dataset



* **Returns**

    DirectoryTree


**Example**:

```python
directory_tree = project.datasets.directory_tree(dataset='dataset_entity')
```


#### _static_ download_annotations(dataset: [Dataset](entities.md#dtlpy.entities.dataset.Dataset), local_path: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, annotation_options: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[ViewAnnotationOptions](entities.md#dtlpy.entities.annotation.ViewAnnotationOptions)] = None, annotation_filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, overwrite: [bool](https://docs.python.org/3/library/functions.html#bool) = False, thickness: [int](https://docs.python.org/3/library/functions.html#int) = 1, with_text: [bool](https://docs.python.org/3/library/functions.html#bool) = False, remote_path: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, include_annotations_in_output: [bool](https://docs.python.org/3/library/functions.html#bool) = True, export_png_files: [bool](https://docs.python.org/3/library/functions.html#bool) = False, filter_output_annotations: [bool](https://docs.python.org/3/library/functions.html#bool) = False, alpha: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[float](https://docs.python.org/3/library/functions.html#float)] = None, export_version=ExportVersion.V1)
Download dataset’s annotations by filters.

You may filter the dataset both for items and for annotations and download annotations.

Optional – download annotations as: mask, instance, image mask of the item.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset object


    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local folder or filename to save to.


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **annotation_options** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – type of download annotations: list(dl.ViewAnnotationOptions)


    * **annotation_filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity to filter annotations for download


    * **overwrite** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - default = False to overwrite the existing files


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
file_path = project.datasets.download_annotations(dataset='dataset_entity',
                                     local_path='local_path',
                                     annotation_options=dl.ViewAnnotationOptions,
                                     overwrite=False,
                                     thickness=1,
                                     with_text=False,
                                     alpha=1
                                     )
```


#### get(dataset_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, checkout: [bool](https://docs.python.org/3/library/functions.html#bool) = False, fetch: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[bool](https://docs.python.org/3/library/functions.html#bool)] = None)
Get dataset by name or id.

**Prerequisites**: You must be an *owner* or *developer* to use this method.

You must provide at least ONE of the following params: dataset_id, dataset_name.


* **Parameters**

    
    * **dataset_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by name


    * **dataset_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id


    * **checkout** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – set the dataset as a default dataset object (cookies)


    * **fetch** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - fetch entity from platform (True), default taken from cookie



* **Returns**

    Dataset object



* **Return type**

    [dtlpy.entities.dataset.Dataset](entities.md#dtlpy.entities.dataset.Dataset)


**Example**:

```python
dataset = project.datasets.get(dataset_id='dataset_id')
```


#### list(name=None, creator=None)
List all datasets.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – list by name


    * **creator** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – list by creator



* **Returns**

    List of datasets



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
datasets = project.datasets.list(name='name')
```


#### merge(merge_name: [str](https://docs.python.org/3/library/stdtypes.html#str), dataset_ids: list, project_ids: [str](https://docs.python.org/3/library/stdtypes.html#str), with_items_annotations: [bool](https://docs.python.org/3/library/functions.html#bool) = True, with_metadata: [bool](https://docs.python.org/3/library/functions.html#bool) = True, with_task_annotations_status: [bool](https://docs.python.org/3/library/functions.html#bool) = True, wait: [bool](https://docs.python.org/3/library/functions.html#bool) = True)
Merge a dataset. See our [SDK docs](https://dataloop.ai/docs/sdk-create-dataset#merge-datasets) for more information.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **merge_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – new dataset name


    * **dataset_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list id’s of the datatsets you wish to merge


    * **project_ids** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the project id that include the datasets


    * **with_items_annotations** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – true to merge with items annotations


    * **with_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – true to merge with metadata


    * **with_task_annotations_status** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – true to merge with task annotations’ status


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait for the command to finish



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = project.datasets.merge(dataset_ids=['dataset_id1','dataset_id2'],
                      merge_name='dataset_merge_name',
                      with_metadata=True,
                      with_items_annotations=False,
                      with_task_annotations_status=False)
```


#### open_in_web(dataset_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None)
Open the dataset in web platform.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **dataset_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Name of the dataset


    * **dataset_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Id of the dataset


    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset object


**Example**:

```python
project.datasets.open_in_web(dataset_id='dataset_id')
```


#### set_readonly(state: [bool](https://docs.python.org/3/library/functions.html#bool), dataset: [Dataset](entities.md#dtlpy.entities.dataset.Dataset))
Set dataset readonly mode.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **state** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – state to update readonly mode


    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset object


**Example**:

```python
project.datasets.set_readonly(dataset='dataset_entity', state=True)
```


#### sync(dataset_id: [str](https://docs.python.org/3/library/stdtypes.html#str), wait: [bool](https://docs.python.org/3/library/functions.html#bool) = True)
Sync dataset with external storage.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **dataset_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The Id of the dataset to sync


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait for the command to finish



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = project.datasets.sync(dataset_id='dataset_id')
```


#### update(dataset: [Dataset](entities.md#dtlpy.entities.dataset.Dataset), system_metadata: [bool](https://docs.python.org/3/library/functions.html#bool) = False, patch: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)] = None)
Update dataset field.

**Prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset object


    * **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – True, if you want to change metadata system


    * **patch** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – Specific patch request



* **Returns**

    Dataset object



* **Return type**

    [dtlpy.entities.dataset.Dataset](entities.md#dtlpy.entities.dataset.Dataset)


**Example**:

```python
dataset = project.datasets.update(dataset='dataset_entity')
```


#### upload_annotations(dataset, local_path, filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, clean=False, remote_root_path='/', export_version=ExportVersion.V1)
Upload annotations to dataset.

Example for remote_root_path: If the item filepath is a/b/item and
remote_root_path is /a the start folder will be b instead of a

**Prerequisites**: You must have a dataset with items that are related to the annotations. The relationship between the dataset and annotations is shown in the name. You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset to upload to


    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – str - local folder where the annotations files is


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **clean** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – True to remove the old annotations


    * **remote_root_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the remote root path to match remote and local items


    * **export_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – exported items will have original extension in filename, V1 - no original extension in filenames


**Example**:

```python
project.datasets.upload_annotations(dataset='dataset_entity',
                                     local_path='local_path',
                                     clean=False,
                                     export_version=dl.ExportVersion.V1
                                     )
```

### Drivers


### _class_ Drivers(client_api: ApiClient, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Drivers Repository

The Drivers class allows users to manage drivers that are used to connect with external storage. Read more about external storage in our [documentation](https://dataloop.ai/docs/storage) and [SDK documentation](https://dataloop.ai/docs/sdk-sync-storage).


#### create(name: [str](https://docs.python.org/3/library/stdtypes.html#str), driver_type: [ExternalStorage](entities.md#dtlpy.entities.driver.ExternalStorage), integration_id: [str](https://docs.python.org/3/library/stdtypes.html#str), bucket_name: [str](https://docs.python.org/3/library/stdtypes.html#str), integration_type: [ExternalStorage](entities.md#dtlpy.entities.driver.ExternalStorage), project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, allow_external_delete: [bool](https://docs.python.org/3/library/functions.html#bool) = True, region: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, storage_class: [str](https://docs.python.org/3/library/stdtypes.html#str) = '', path: [str](https://docs.python.org/3/library/stdtypes.html#str) = '')
Create a storage driver.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the driver name


    * **driver_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – ExternalStorage.S3, ExternalStorage.GCS, ExternalStorage.AZUREBLOB


    * **integration_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the integration id


    * **bucket_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the external bucket name


    * **integration_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – ExternalStorage.S3, ExternalStorage.GCS, ExternalStorage.AZUREBLOB, ExternalStorage.AWS_STS


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – project id


    * **allow_external_delete** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – true to allow deleting files from external storage when files are deleted in your Dataloop storage


    * **region** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – relevant only for s3 - the bucket region


    * **storage_class** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – rilevante only for s3


    * **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Optional. By default path is the root folder. Path is case sensitive integration



* **Returns**

    driver object



* **Return type**

    [dtlpy.entities.driver.Driver](entities.md#dtlpy.entities.driver.Driver)


**Example**:

```python
project.drivers.create(name='driver_name',
           driver_type=dl.ExternalStorage.S3,
           integration_id='integration_id',
           bucket_name='bucket_name',
           project_id='project_id',
           region='ey-west-1')
```


#### delete(driver_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, driver_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, sure: [bool](https://docs.python.org/3/library/functions.html#bool) = False, really: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Delete a driver forever!

**Prerequisites**: You must be an *owner* or *developer* to use this method.

**Example**:

```python
project.drivers.delete(dataset_id='dataset_id', sure=True, really=True)
```


* **Parameters**

    
    * **driver_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by name


    * **driver_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id


    * **sure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Are you sure you want to delete?


    * **really** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Really really sure?



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)



#### get(driver_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, driver_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Get a Driver object to use in your code.

**Prerequisites**: You must be in the role of an *owner* or *developer*.

You must provide at least ONE of the following params: driver_name, driver_id.


* **Parameters**

    
    * **driver_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by name


    * **driver_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id



* **Returns**

    Driver object



* **Return type**

    [dtlpy.entities.driver.Driver](entities.md#dtlpy.entities.driver.Driver)


**Example**:

```python
project.drivers.get(driver_id='driver_id')
```


#### list()
Get the project’s drivers list.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Returns**

    List of Drivers objects



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
project.drivers.list()
```

## Items


### _class_ Items(client_api: ApiClient, datasets: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[Datasets] = None, dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None, dataset_id=None, items_entity=None, project=None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Items Repository

The Items class allows you to manage items in your datasets. For information on actions related to items see [Organizing Your Dataset](https:/dataloop.ai/docs/sdk-organize-dataset), [Item Metadata](https://dataloop.ai/docs/sdk-add-item-metadata), and [Item Metadata-Based Filtering](https://dataloop.ai/docs/sdk-custom-filter-metadata).


#### clone(item_id: [str](https://docs.python.org/3/library/stdtypes.html#str), dst_dataset_id: [str](https://docs.python.org/3/library/stdtypes.html#str), remote_filepath: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, metadata: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)] = None, with_annotations: [bool](https://docs.python.org/3/library/functions.html#bool) = True, with_metadata: [bool](https://docs.python.org/3/library/functions.html#bool) = True, with_task_annotations_status: [bool](https://docs.python.org/3/library/functions.html#bool) = False, allow_many: [bool](https://docs.python.org/3/library/functions.html#bool) = False, wait: [bool](https://docs.python.org/3/library/functions.html#bool) = True)
Clone item. Read more about cloning datatsets and items in our [documentation](https://dataloop.ai/docs/clone-merge-dataset#cloned-dataset) and [SDK documentation](https://dataloop.ai/docs/sdk-create-dataset#clone-dataset).

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **item_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – item to clone


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

    [dtlpy.entities.item.Item](entities.md#dtlpy.entities.item.Item)


**Example**:

```python
dataset.items.clone(item_id='item_id',
        dst_dataset_id='dist_dataset_id',
        with_metadata=True,
        with_task_annotations_status=False,
        with_annotations=False)
```


#### delete(filename: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, item_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None)
Delete item from platform.

**Prerequisites**: You must be in the role of an *owner* or *developer*.

You must provide at least ONE of the following params: item id, filename, filters.


* **Parameters**

    
    * **filename** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search item by remote path


    * **item_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search item by id


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – optional - delete items by filter



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
dataset.items.delete(item_id='item_id')
```


#### download(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, items=None, local_path: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, file_types: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[list] = None, save_locally: [bool](https://docs.python.org/3/library/functions.html#bool) = True, to_array: [bool](https://docs.python.org/3/library/functions.html#bool) = False, annotation_options: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[ViewAnnotationOptions](entities.md#dtlpy.entities.annotation.ViewAnnotationOptions)] = None, annotation_filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, overwrite: [bool](https://docs.python.org/3/library/functions.html#bool) = False, to_items_folder: [bool](https://docs.python.org/3/library/functions.html#bool) = True, thickness: [int](https://docs.python.org/3/library/functions.html#int) = 1, with_text: [bool](https://docs.python.org/3/library/functions.html#bool) = False, without_relative_path=None, avoid_unnecessary_annotation_download: [bool](https://docs.python.org/3/library/functions.html#bool) = False, include_annotations_in_output: [bool](https://docs.python.org/3/library/functions.html#bool) = True, export_png_files: [bool](https://docs.python.org/3/library/functions.html#bool) = False, filter_output_annotations: [bool](https://docs.python.org/3/library/functions.html#bool) = False, alpha: [float](https://docs.python.org/3/library/functions.html#float) = 1, export_version=ExportVersion.V1)
Download dataset items by filters.

Filters the dataset for items and saves them locally.

Optional – download annotation, mask, instance, and image mask of the item.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **items** (*List**[*[*dtlpy.entities.item.Item*](entities.md#dtlpy.entities.item.Item)*] or *[*dtlpy.entities.item.Item*](entities.md#dtlpy.entities.item.Item)) – download Item entity or item_id (or a list of item)


    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local folder or filename to save to.


    * **file_types** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – a list of file type to download. e.g [‘video/webm’, ‘video/mp4’, ‘image/jpeg’, ‘image/png’]


    * **save_locally** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool. save to disk or return a buffer


    * **to_array** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – returns Ndarray when True and local_path = False


    * **annotation_options** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – download annotations options:  list(dl.ViewAnnotationOptions)


    * **annotation_filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity to filter annotations for download


    * **overwrite** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - default = False


    * **to_items_folder** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – Create ‘items’ folder and download items to it


    * **thickness** ([*int*](https://docs.python.org/3/library/functions.html#int)) – optional - line thickness, if -1 annotation will be filled, default =1


    * **with_text** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - add text to annotations, default = False


    * **without_relative_path** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool - download items without the relative path from platform


    * **avoid_unnecessary_annotation_download** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – default - False


    * **include_annotations_in_output** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – default - False , if export should contain annotations


    * **export_png_files** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – default - if True, semantic annotations should be exported as png files


    * **filter_output_annotations** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – default - False, given an export by filter - determine if to filter out annotations


    * **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) – opacity value [0 1], default 1


    * **export_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – exported items will have original extension in filename, V1 - no original extension in filenames



* **Returns**

    generator of local_path per each downloaded item



* **Return type**

    generator or single item


**Example**:

```python
dataset.items.download(local_path='local_path',
                     annotation_options=dl.ViewAnnotationOptions,
                     overwrite=False,
                     thickness=1,
                     with_text=False,
                     alpha=1,
                     save_locally=True
                     )
```


#### get(filepath: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, item_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, fetch: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[bool](https://docs.python.org/3/library/functions.html#bool)] = None, is_dir: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Get Item object

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **filepath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by remote path


    * **item_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id


    * **fetch** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - fetch entity from platform, default taken from cookie


    * **is_dir** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – True if you want to get an item from dir type



* **Returns**

    Item object



* **Return type**

    [dtlpy.entities.item.Item](entities.md#dtlpy.entities.item.Item)


**Example**:

```python
dataset.items.get(item_id='item_id')
```


#### get_all_items(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None)
Get all items in dataset.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – dl.Filters entity to filters items



* **Returns**

    list of all items



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
dataset.items.get_all_items()
```


#### list(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, page_offset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, page_size: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None)
List items in a dataset.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **page_offset** ([*int*](https://docs.python.org/3/library/functions.html#int)) – start page


    * **page_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) – page size



* **Returns**

    Pages object



* **Return type**

    [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)


**Example**:

```python
dataset.items.list(page_offset=0, page_size=100)
```


#### make_dir(directory, dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None)
Create a directory in a dataset.

**Prerequisites**: All users.


* **Parameters**

    
    * **directory** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – name of directory


    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset object



* **Returns**

    Item object



* **Return type**

    [dtlpy.entities.item.Item](entities.md#dtlpy.entities.item.Item)


**Example**:

```python
dataset.items.make_dir(directory='directory_name')
```


#### move_items(destination: [str](https://docs.python.org/3/library/stdtypes.html#str), filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, items=None, dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None)
Move items to another directory.
If directory does not exist we will create it

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **destination** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – destination directory


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – optional - either this or items. Query of items to move


    * **items** – optional - either this or filters. A list of items to move


    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset object



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
dataset.items.move_items(destination='directory_name')
```


#### open_in_web(filepath=None, item_id=None, item=None)
Open the item in web platform

**Prerequisites**: You must be in the role of an *owner* or *developer* or be an *annotation manager*/*annotator* with access to that item through task.


* **Parameters**

    
    * **filepath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – item file path


    * **item_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – item id


    * **item** ([*dtlpy.entities.item.Item*](entities.md#dtlpy.entities.item.Item)) – item entity


**Example**:

```python
dataset.items.open_in_web(item_id='item_id')
```


#### set_items_entity(entity)
Set the item entity type to [Artifact](https://dataloop.ai/docs/auto-annotation-service?#uploading-model-weights-as-artifacts), Item, or Codebase.


* **Parameters**

    **entity** (*entities.Item**, **entities.Artifact**, **entities.Codebase*) – entity type [entities.Item, entities.Artifact, entities.Codebase]



#### update(item: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Item](entities.md#dtlpy.entities.item.Item)] = None, filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, update_values=None, system_update_values=None, system_metadata: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Update item metadata.

**Prerequisites**: You must be in the role of an *owner* or *developer*.

You must provide at least ONE of the following params: update_values, system_update_values.


* **Parameters**

    
    * **item** ([*dtlpy.entities.item.Item*](entities.md#dtlpy.entities.item.Item)) – Item object


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – optional update filtered items by given filter


    * **update_values** – optional field to be updated and new values


    * **system_update_values** – values in system metadata to be updated


    * **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – True, if you want to update the metadata system



* **Returns**

    Item object



* **Return type**

    [dtlpy.entities.item.Item](entities.md#dtlpy.entities.item.Item)


**Example**:

```python
dataset.items.update(item='item_entity')
```


#### update_status(status: [ItemStatus](entities.md#dtlpy.entities.item.ItemStatus), items=None, item_ids=None, filters=None, dataset=None, clear=False)
Update item status in task

**Prerequisites**: You must be in the role of an *owner* or *developer* or *annotation manager* who has been assigned a task with the item.

You must provide at least ONE of the following params: items, item_ids, filters.


* **Parameters**

    
    * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – ItemStatus.COMPLETED, ItemStatus.APPROVED, ItemStatus.DISCARDED


    * **items** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of items


    * **item_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of items id


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset object


    * **clear** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – to delete status


**Example**:

```python
dataset.items.update_status(item_ids='item_id', status=dl.ItemStatus.COMPLETED)
```


#### upload(local_path: str, local_annotations_path: ~typing.Optional[str] = None, remote_path: str = '/', remote_name: ~typing.Optional[str] = None, file_types: ~typing.Optional[~dtlpy.repositories.items.Items.list] = None, overwrite: bool = False, item_metadata: ~typing.Optional[dict] = None, output_entity=<class 'dtlpy.entities.item.Item'>, no_output: bool = False, export_version: str = ExportVersion.V1, item_description: ~typing.Optional[str] = None)
Upload local file to dataset.
Local filesystem will remain unchanged.
If “\*” at the end of local_path (e.g. “/images/

```
*
```

”) items will be uploaded without the head directory.

**Prerequisites**: Any user can upload items.


* **Parameters**

    
    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – list of local file, local folder, BufferIO, numpy.ndarray or url to upload


    * **local_annotations_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to dataloop format annotations json files.


    * **remote_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – remote path to save.


    * **remote_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – remote base name to save. when upload numpy.ndarray as local path, remote_name with .jpg or .png ext is mandatory


    * **file_types** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of file type to upload. e.g [‘.jpg’, ‘.png’]. default is all


    * **item_metadata** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – metadata dict to upload to item or ExportMetadata option to export metadata from annotation file


    * **overwrite** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - default = False


    * **output_entity** – output type


    * **no_output** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – do not return the items after upload


    * **export_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – exported items will have original extension in filename, V1 - no original extension in filenames


    * **item_description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – add a string description to the uploaded item



* **Returns**

    Output (generator/single item)



* **Return type**

    generator or single item


**Example**:

```python
dataset.items.upload(local_path='local_path',
                     local_annotations_path='local_annotations_path',
                     overwrite=True,
                     item_metadata={'Hellow': 'Word'}
                     )
```

## Annotations


### _class_ Annotations(client_api: ApiClient, item=None, dataset=None, dataset_id=None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Annotations Repository

The Annotation class allows you to manage the annotations of data items. For information on annotations explore our
documentation at:
[Classification SDK](https://dataloop.ai/docs/sdk-classify-item),
[Annotation Labels and Attributes](https://dataloop.ai/docs/sdk-annotation-ontology),
[Show Video with Annotations](https://dataloop.ai/docs/sdk-show-videos).


#### builder()
Create Annotation collection.

**Prerequisites**: You must have an item to be annotated. You must have the role of an *owner* or *developer*

    or be assigned a task that includes that item as an *annotation manager* or *annotator*.


* **Returns**

    Annotation collection object



* **Return type**

    [dtlpy.entities.annotation_collection.AnnotationCollection](entities.md#dtlpy.entities.annotation_collection.AnnotationCollection)


**Example**:

```python
annotation_collection = item.annotations.builder()
```


#### delete(annotation: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Annotation](entities.md#dtlpy.entities.annotation.Annotation)] = None, annotation_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None)
Remove an annotation from item.

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or
*developer* or be assigned a task that includes that item as an *annotation manager* or *annotator*.


* **Parameters**

    
    * **annotation** ([*dtlpy.entities.annotation.Annotation*](entities.md#dtlpy.entities.annotation.Annotation)) – Annotation object


    * **annotation_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The id of the annotation


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters



* **Returns**

    True/False



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
is_deleted = item.annotations.delete(annotation_id='annotation_id')
```


#### download(filepath: [str](https://docs.python.org/3/library/stdtypes.html#str), annotation_format: [ViewAnnotationOptions](entities.md#dtlpy.entities.annotation.ViewAnnotationOptions) = ViewAnnotationOptions.JSON, img_filepath: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, height: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[float](https://docs.python.org/3/library/functions.html#float)] = None, width: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[float](https://docs.python.org/3/library/functions.html#float)] = None, thickness: [int](https://docs.python.org/3/library/functions.html#int) = 1, with_text: [bool](https://docs.python.org/3/library/functions.html#bool) = False, alpha: [float](https://docs.python.org/3/library/functions.html#float) = 1)
Save annotation to file.

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or
*developer* or be assigned a task that includes that item as an *annotation manager* or *annotator*.


* **Parameters**

    
    * **filepath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Target download directory


    * **annotation_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the format that want to download ,options: list(dl.ViewAnnotationOptions)


    * **img_filepath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – img file path - needed for img_mask


    * **height** ([*float*](https://docs.python.org/3/library/functions.html#float)) – optional - image height


    * **width** ([*float*](https://docs.python.org/3/library/functions.html#float)) – optional - image width


    * **thickness** ([*int*](https://docs.python.org/3/library/functions.html#int)) – optional - line thickness, default=1


    * **with_text** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - draw annotation with text, default = False


    * **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) – opacity value [0 1], default 1



* **Returns**

    file path to where save the annotations



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)


**Example**:

```python
file_path = item.annotations.download(
              filepath='file_path',
              annotation_format=dl.ViewAnnotationOptions.MASK,
              img_filepath='img_filepath',
              height=100,
              width=100,
              thickness=1,
              with_text=False,
              alpha=1)
```


#### get(annotation_id: [str](https://docs.python.org/3/library/stdtypes.html#str))
Get a single annotation.

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or
*developer* or be assigned a task that includes that item as an *annotation manager* or *annotator*.


* **Parameters**

    **annotation_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – The id of the annotation



* **Returns**

    Annotation object or None



* **Returns**

    Annotation object or None



* **Return type**

    [dtlpy.entities.annotation.Annotation](entities.md#dtlpy.entities.annotation.Annotation)


**Example**:

```python
annotation = item.annotations.get(annotation_id='annotation_id')
```


#### list(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, page_offset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, page_size: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None)
List Annotations of a specific item. You must get the item first and then list the annotations with the desired filters.

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or
*developer* or be assigned a task that includes that item as an *annotation manager* or *annotator*.


* **Parameters**

    
    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **page_offset** ([*int*](https://docs.python.org/3/library/functions.html#int)) – starting page


    * **page_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) – size of page



* **Returns**

    Pages object



* **Return type**

    [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)


**Example**:

```python
annotations = item.annotations.list(filters=dl.Filters(
                             resource=dl.FiltersResource.ANNOTATION,
                             field='type',
                             values='box'),
          page_size=100,
          page_offset=0)
```


#### show(image=None, thickness: [int](https://docs.python.org/3/library/functions.html#int) = 1, with_text: [bool](https://docs.python.org/3/library/functions.html#bool) = False, height: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[float](https://docs.python.org/3/library/functions.html#float)] = None, width: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[float](https://docs.python.org/3/library/functions.html#float)] = None, annotation_format: [ViewAnnotationOptions](entities.md#dtlpy.entities.annotation.ViewAnnotationOptions) = ViewAnnotationOptions.MASK, alpha: [float](https://docs.python.org/3/library/functions.html#float) = 1)
Show annotations. To use this method, you must get the item first and then show the annotations with
the desired filters. The method returns an array showing all the annotations.

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or
*developer* or be assigned a task that includes that item as an *annotation manager* or *annotator*.


* **Parameters**

    
    * **image** (*ndarray*) – empty or image to draw on


    * **thickness** ([*int*](https://docs.python.org/3/library/functions.html#int)) – optional - line thickness, default=1


    * **with_text** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – add label to annotation


    * **height** ([*float*](https://docs.python.org/3/library/functions.html#float)) – item height


    * **width** ([*float*](https://docs.python.org/3/library/functions.html#float)) – item width


    * **annotation_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the format that want to show ,options: list(dl.ViewAnnotationOptions)


    * **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float)) – opacity value [0 1], default 1



* **Returns**

    ndarray of the annotations



* **Return type**

    ndarray


**Example**:

```python
image = item.annotations.show(image='nd array',
          thickness=1,
          with_text=False,
          height=100,
          width=100,
          annotation_format=dl.ViewAnnotationOptions.MASK,
          alpha=1)
```


#### update(annotations, system_metadata=False)
Update an existing annotation. For example, you may change the annotation’s label and then use the update method.

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or

    *developer* or be assigned a task that includes that item as an *annotation manager* or *annotator*.


* **Parameters**

    
    * **annotations** ([*dtlpy.entities.annotation.Annotation*](entities.md#dtlpy.entities.annotation.Annotation)) – Annotation object


    * **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool - True, if you want to change metadata system



* **Returns**

    True if successful or error if unsuccessful



* **Return type**

    bool

    **Example**:



```python
annotations = item.annotations.update(annotation='annotation')
```


#### update_status(annotation: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Annotation](entities.md#dtlpy.entities.annotation.Annotation)] = None, annotation_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, status: [AnnotationStatus](entities.md#dtlpy.entities.annotation.AnnotationStatus) = AnnotationStatus.ISSUE)
Set status on annotation.

**Prerequisites**: You must have an item that has been annotated. You must have the role of an *owner* or
*developer* or be assigned a task that includes that item as an *annotation manager*.


* **Parameters**

    
    * **annotation** ([*dtlpy.entities.annotation.Annotation*](entities.md#dtlpy.entities.annotation.Annotation)) – Annotation object


    * **annotation_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - annotation id to set status


    * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – can be AnnotationStatus.ISSUE, APPROVED, REVIEW, CLEAR



* **Returns**

    Annotation object



* **Return type**

    [dtlpy.entities.annotation.Annotation](entities.md#dtlpy.entities.annotation.Annotation)


**Example**:

```python
annotation = item.annotations.update_status(annotation_id='annotation_id', status=dl.AnnotationStatus.ISSUE)
```


#### upload(annotations)
Upload a new annotation/annotations. You must first create the annotation using the annotation *builder* method.

**Prerequisites**: Any user can upload annotations.


* **Parameters**

    **annotations** (*List**[*[*dtlpy.entities.annotation.Annotation*](entities.md#dtlpy.entities.annotation.Annotation)*] or *[*dtlpy.entities.annotation.Annotation*](entities.md#dtlpy.entities.annotation.Annotation)) – list or


single annotation of type Annotation
:return: list of annotation objects
:rtype: entities.AnnotationCollection

**Example**:

```python
annotations = item.annotations.upload(annotations='builder')
```

## Recipes


### _class_ Recipes(client_api: ApiClient, dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Recipes Repository

The Recipes class allows you to manage recipes and their properties. For more information on Recipes, see our [documentation](https://dataloop.ai/docs/ontology) and [SDK documentation](https://dataloop.ai/docs/sdk-recipe).


#### clone(recipe: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Recipe](entities.md#dtlpy.entities.recipe.Recipe)] = None, recipe_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, shallow: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
> Clone recipe.

> **Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **recipe** ([*dtlpy.entities.recipe.Recipe*](entities.md#dtlpy.entities.recipe.Recipe)) – Recipe object


    * **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Recipe id


    * **shallow** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – If True, link to existing ontology, clones all ontologies that are linked to the recipe as well



* **Returns**

    Cloned ontology object



* **Return type**

    [dtlpy.entities.recipe.Recipe](entities.md#dtlpy.entities.recipe.Recipe)


**Example**:

> ```python
> dataset.recipes.clone(recipe_id='recipe_id')
> ```


#### create(project_ids=None, ontology_ids=None, labels=None, recipe_name=None, attributes=None, annotation_instruction_file=None)
Create a new Recipe.
Note: If the param ontology_ids is None, an ontology will be created first.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **project_ids** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – project ids


    * **ontology_ids** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)* or *[*list*](https://docs.python.org/3/library/stdtypes.html#list)) – ontology ids


    * **labels** – labels


    * **recipe_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – recipe name


    * **attributes** – attributes


    * **annotation_instruction_file** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – file path or url of the recipe instruction



* **Returns**

    Recipe entity



* **Return type**

    [dtlpy.entities.recipe.Recipe](entities.md#dtlpy.entities.recipe.Recipe)


**Example**:

```python
dataset.recipes.create(recipe_name='My Recipe', labels=labels))
```


#### delete(recipe_id: [str](https://docs.python.org/3/library/stdtypes.html#str), force: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Delete recipe from platform.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – recipe id


    * **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – force delete recipe



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
dataset.recipes.delete(recipe_id='recipe_id')
```


#### get(recipe_id: [str](https://docs.python.org/3/library/stdtypes.html#str))
Get a Recipe object to use in your code.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – recipe id



* **Returns**

    Recipe object



* **Return type**

    [dtlpy.entities.recipe.Recipe](entities.md#dtlpy.entities.recipe.Recipe)


**Example**:

```python
dataset.recipes.get(recipe_id='recipe_id')
```


#### list(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None)
List recipes for a dataset.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters



* **Returns**

    list of all recipes



* **Retype**

    list


**Example**:

```python
dataset.recipes.list()
```


#### open_in_web(recipe: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Recipe](entities.md#dtlpy.entities.recipe.Recipe)] = None, recipe_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Open the recipe in web platform.

**Prerequisites**: All users.


* **Parameters**

    
    * **recipe** ([*dtlpy.entities.recipe.Recipe*](entities.md#dtlpy.entities.recipe.Recipe)) – recipe entity


    * **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – recipe id


**Example**:

```python
dataset.recipes.open_in_web(recipe_id='recipe_id')
```


#### update(recipe: [Recipe](entities.md#dtlpy.entities.recipe.Recipe), system_metadata=False)
Update recipe.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **recipe** ([*dtlpy.entities.recipe.Recipe*](entities.md#dtlpy.entities.recipe.Recipe)) – Recipe object


    * **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – True, if you want to change metadata system



* **Returns**

    Recipe object



* **Return type**

    [dtlpy.entities.recipe.Recipe](entities.md#dtlpy.entities.recipe.Recipe)


**Example**:

```python
dataset.recipes.update(recipe='recipe_entity')
```

### Ontologies


### _class_ Ontologies(client_api: ApiClient, recipe: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Recipe](entities.md#dtlpy.entities.recipe.Recipe)] = None, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None, dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Ontologies Repository

The Ontologies class allows users to manage ontologies and their properties. Read more about ontology in our [SDK docs](https://dataloop.ai/docs/sdk-ontology).


#### create(labels, title=None, project_ids=None, attributes=None)
Create a new ontology.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **labels** – recipe tags


    * **title** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – ontology title, name


    * **project_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – recipe project/s


    * **attributes** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – recipe attributes



* **Returns**

    Ontology object



* **Return type**

    [dtlpy.entities.ontology.Ontology](entities.md#dtlpy.entities.ontology.Ontology)


**Example**:

```python
recipe.ontologies.create(labels='labels_entity',
                      title='new_ontology',
                      project_ids='project_ids')
```


#### delete(ontology_id)
Delete Ontology from the platform.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    **ontology_id** – ontology id



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
recipe.ontologies.delete(ontology_id='ontology_id')
```


#### delete_attributes(ontology_id, keys: list)
Delete a bulk of attributes


* **Parameters**

    
    * **ontology_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – ontology id


    * **keys** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – Keys of attributes to delete



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
ontology.delete_attributes(['1'])
```


#### get(ontology_id: [str](https://docs.python.org/3/library/stdtypes.html#str))
Get Ontology object to use in your code.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    **ontology_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – ontology id



* **Returns**

    Ontology object



* **Return type**

    [dtlpy.entities.ontology.Ontology](entities.md#dtlpy.entities.ontology.Ontology)


**Example**:

```python
recipe.ontologies.get(ontology_id='ontology_id')
```


#### _static_ labels_to_roots(labels)
Converts labels dictionary to a list of platform representation of labels.


* **Parameters**

    **labels** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – labels dict



* **Returns**

    platform representation of labels



#### list(project_ids=None)
List ontologies for recipe

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    **project_ids** – 



* **Returns**

    list of all the ontologies


**Example**:

```python
recipe.ontologies.list(project_ids='project_ids')
```


#### update(ontology: [Ontology](entities.md#dtlpy.entities.ontology.Ontology), system_metadata=False)
> Update the Ontology metadata.

> **Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **ontology** ([*dtlpy.entities.ontology.Ontology*](entities.md#dtlpy.entities.ontology.Ontology)) – Ontology object


    * **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool - True, if you want to change metadata system



* **Returns**

    Ontology object



* **Return type**

    [dtlpy.entities.ontology.Ontology](entities.md#dtlpy.entities.ontology.Ontology)


**Example**:

> ```python
> recipe.ontologies.delete(ontology='ontology_entity')
> ```


#### update_attributes(ontology_id: [str](https://docs.python.org/3/library/stdtypes.html#str), title: [str](https://docs.python.org/3/library/stdtypes.html#str), key: [str](https://docs.python.org/3/library/stdtypes.html#str), attribute_type: AttributesTypes, scope: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[list] = None, optional: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[bool](https://docs.python.org/3/library/functions.html#bool)] = None, values: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[list] = None, attribute_range: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[AttributesRange] = None)
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
ontology.update_attributes(key='1',
                           title='checkbox',
                           attribute_type=dl.AttributesTypes.CHECKBOX,
                           values=[1,2,3])
```

## Tasks


### _class_ Tasks(client_api: ApiClient, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None, dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Tasks Repository

The Tasks class allows the user to manage tasks and their properties. For more information, read in our SDK documentation about [Creating Tasks](https://dataloop.ai/docs/sdk-create-task), [Redistributing and Reassigning Tasks](https://dataloop.ai/docs/sdk-redistribute-task), and [Task Assignment](https://dataloop.ai/docs/sdk-task-assigment).


#### add_items(task: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Task](entities.md#dtlpy.entities.task.Task)] = None, task_id=None, filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, items=None, assignee_ids=None, query=None, workload=None, limit=None, wait=True)
Add items to a Task.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned to be *owner* of the annotation task.


* **Parameters**

    
    * **task** ([*dtlpy.entities.task.Task*](entities.md#dtlpy.entities.task.Task)) – task object


    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the Id of the task


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **items** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of items (item Ids or objects) to add to the task


    * **assignee_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list to assignee who works in the task


    * **query** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – query to filter the items for the task


    * **workload** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of WorkloadUnit objects. Customize distribution (percentage) between the task assignees. For example: [dl.WorkloadUnit([annotator@hi.com](mailto:annotator@hi.com), 80), dl.WorkloadUnit([annotator2@hi.com](mailto:annotator2@hi.com), 20)]


    * **limit** ([*int*](https://docs.python.org/3/library/functions.html#int)) – the limit items that task can include


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until add items will to finish



* **Returns**

    task entity



* **Return type**

    [dtlpy.entities.task.Task](entities.md#dtlpy.entities.task.Task)


**Example**:

```python
dataset.tasks.add_items(task= 'task_entity',
                    items = [items])
```


#### create(task_name, due_date=None, assignee_ids=None, workload=None, dataset=None, task_owner=None, task_type='annotation', task_parent_id=None, project_id=None, recipe_id=None, assignments_ids=None, metadata=None, filters=None, items=None, query=None, available_actions=None, wait=True, check_if_exist: [Filters](entities.md#dtlpy.entities.filters.Filters) = False, limit=None, batch_size=None, max_batch_workload=None, allowed_assignees=None, priority=TaskPriority.MEDIUM)
Create a new Task (Annotation or QA).

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned to be *owner* of the annotation task.


* **Parameters**

    
    * **task_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the name of the task


    * **due_date** ([*float*](https://docs.python.org/3/library/functions.html#float)) – date by which the task should be finished; for example, due_date=datetime.datetime(day=1, month=1, year=2029).timestamp()


    * **assignee_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list the task assignees (contributors) that should be working on the task. Provide a list of users’ emails


    * **workload** (*List**[*[*WorkloadUnit*](entities.md#dtlpy.entities.assignment.WorkloadUnit)*] **List**[*[*WorkloadUnit*](entities.md#dtlpy.entities.assignment.WorkloadUnit)*]*) – list of WorkloadUnit objects. Customize distribution (percentage) between the task assignees. For example: [dl.WorkloadUnit([annotator@hi.com](mailto:annotator@hi.com), 80), dl.WorkloadUnit([annotator2@hi.com](mailto:annotator2@hi.com), 20)]


    * **dataset** (*entities.Dataset*) – dataset object, the dataset that refer to the task


    * **task_owner** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – task owner. Provide user email


    * **task_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – task type “annotation” or “qa”


    * **task_parent_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional if type is qa - parent annotation task id


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the Id of the project where task will be created


    * **recipe_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – recipe id for the task


    * **assignments_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – assignments ids to the task


    * **metadata** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – metadata for the task


    * **filters** (*entities.Filters*) – dl.Filters entity to filter items for the task


    * **items** (*List**[**entities.Item**]*) – list of items (item Id or objects) to insert to the task


    * **query** (*dict DQL*) – filter items for the task


    * **available_actions** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of available actions (statuses) that will be available for the task items; The default statuses are: “Completed” and “Discarded”


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until create task finish


    * **check_if_exist** (*entities.Filters*) – dl.Filters check if task exist according to filter


    * **limit** ([*int*](https://docs.python.org/3/library/functions.html#int)) – the limit items that the task can include


    * **batch_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) – Pulling batch size (items), use with pulling allocation method. Restrictions - Min 3, max 100


    * **max_batch_workload** ([*int*](https://docs.python.org/3/library/functions.html#int)) – max_batch_workload: Max items in assignment, use with pulling allocation method. Restrictions - Min batchSize + 2, max batchSize \* 2


    * **allowed_assignees** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list the task assignees (contributors) that should be working on the task. Provide a list of users’ emails


    * **priority** (*entities.TaskPriority*) – priority of the task options in entities.TaskPriority



* **Returns**

    Task object



* **Return type**

    [dtlpy.entities.task.Task](entities.md#dtlpy.entities.task.Task)


**Example**:

```python
dataset.tasks.create(task= 'task_entity',
                    due_date = datetime.datetime(day= 1, month= 1, year= 2029).timestamp(),
                    assignee_ids =[ 'annotator1@dataloop.ai', 'annotator2@dataloop.ai'])
```


#### create_qa_task(task: [Task](entities.md#dtlpy.entities.task.Task), assignee_ids, due_date=None, filters=None, items=None, query=None, workload=None, metadata=None, available_actions=None, wait=True, batch_size=None, max_batch_workload=None, allowed_assignees=None, priority=TaskPriority.MEDIUM)
Create a new QA Task.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned to be *owner* of the annotation task.


* **Parameters**

    
    * **task** ([*dtlpy.entities.task.Task*](entities.md#dtlpy.entities.task.Task)) – the parent annotation task object


    * **assignee_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list the QA task assignees (contributors) that should be working on the task. Provide a list of users’ emails


    * **due_date** ([*float*](https://docs.python.org/3/library/functions.html#float)) – date by which the QA task should be finished; for example, due_date=datetime.datetime(day=1, month=1, year=2029).timestamp()


    * **filters** (*entities.Filters*) – dl.Filters entity to filter items for the task


    * **items** (*List**[**entities.Item**]*) – list of items (item Id or objects) to insert to the task


    * **query** (*dict DQL*) – filter items for the task


    * **workload** (*List**[*[*WorkloadUnit*](entities.md#dtlpy.entities.assignment.WorkloadUnit)*]*) – list of WorkloadUnit objects. Customize distribution (percentage) between the task assignees. For example: [dl.WorkloadUnit([annotator@hi.com](mailto:annotator@hi.com), 80), dl.WorkloadUnit([annotator2@hi.com](mailto:annotator2@hi.com), 20)]


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

    [dtlpy.entities.task.Task](entities.md#dtlpy.entities.task.Task)


**Example**:

```python
dataset.tasks.create_qa_task(task= 'task_entity',
                            due_date = datetime.datetime(day= 1, month= 1, year= 2029).timestamp(),
                            assignee_ids =[ 'annotator1@dataloop.ai', 'annotator2@dataloop.ai'])
```


#### delete(task: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Task](entities.md#dtlpy.entities.task.Task)] = None, task_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, task_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, wait: [bool](https://docs.python.org/3/library/functions.html#bool) = True)
Delete the Task.

**Prerequisites**: You must be in the role of an *owner* or *developer* or *annotation manager* who created that task.


* **Parameters**

    
    * **task** ([*dtlpy.entities.task.Task*](entities.md#dtlpy.entities.task.Task)) – the task object


    * **task_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the name of the task


    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the Id of the task


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until delete task finish



* **Returns**

    True is success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
dataset.tasks.delete(task_id='task_id')
```


#### get(task_name=None, task_id=None)
Get a Task object to use in your code.

**Prerequisites**: You must be in the role of an *owner* or *developer* or *annotation manager* who has been assigned the task.


* **Parameters**

    
    * **task_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by name


    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id



* **Returns**

    task object



* **Return type**

    [dtlpy.entities.task.Task](entities.md#dtlpy.entities.task.Task)


**Example**:

```python
dataset.tasks.get(task_id='task_id')
```


#### get_items(task_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, task_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None, filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None)
Get the task items to use in your code.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned to be *owner* of the annotation task.

If a filters param is provided, you will receive a PagedEntity output of the task items. If no filter is provided, you will receive a list of the items.


* **Parameters**

    
    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the Id of the task


    * **task_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the name of the task


    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset object that refer to the task


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters



* **Returns**

    list of the items or PagedEntity output of items



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list) or [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)


**Example**:

```python
dataset.tasks.get_items(task_id= 'task_id')
```


#### list(project_ids=None, status=None, task_name=None, pages_size=None, page_offset=None, recipe=None, creator=None, assignments=None, min_date=None, max_date=None, filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None)
List all tasks.

**Prerequisites**: You must be in the role of an *owner* or *developer* or *annotation manager* who has been assigned the task.


* **Parameters**

    
    * **project_ids** – search tasks by given list of project ids


    * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – search tasks by a given task status


    * **task_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – search tasks by a given task name


    * **pages_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) – pages size of the output generator


    * **page_offset** ([*int*](https://docs.python.org/3/library/functions.html#int)) – page offset of the output generator


    * **recipe** ([*dtlpy.entities.recipe.Recipe*](entities.md#dtlpy.entities.recipe.Recipe)) – Search tasks that use a given recipe. Provide the required recipe object


    * **creator** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – search tasks created by a given creator (user email)


    * **assignments** (*dtlpy.entities.assignment.Assignment recipe*) – assignments object


    * **min_date** (*double*) – search all tasks created AFTER a given date, use a milliseconds format. For example: 1661780622008


    * **max_date** (*double*) – search all tasks created BEFORE a given date, use a milliseconds format. For example: 1661780622008


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – dl.Filters entity to filters tasks using DQL



* **Returns**

    List of Task objects


**Example**:

```python
dataset.tasks.list(project_ids='project_ids',pages_size=100, page_offset=0)
```


#### open_in_web(task_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, task_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, task: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Task](entities.md#dtlpy.entities.task.Task)] = None)
Open the task in the web platform.

**Prerequisites**: You must be in the role of an *owner* or *developer* or *annotation manager* who has been assigned the task.


* **Parameters**

    
    * **task_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the name of the task


    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the Id of the task


    * **task** ([*dtlpy.entities.task.Task*](entities.md#dtlpy.entities.task.Task)) – the task object


**Example**:

```python
dataset.tasks.open_in_web(task_id='task_id')
```


#### query(filters=None, project_ids=None)
List all tasks by filter.

**Prerequisites**: You must be in the role of an *owner* or *developer* or *annotation manager* who has been assigned the task.


* **Parameters**

    
    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **project_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of project ids of the required tasks



* **Returns**

    Paged entity - task pages generator



* **Return type**

    [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)


**Example**:

```python
dataset.tasks.query(project_ids='project_ids')
```


#### remove_items(task: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Task](entities.md#dtlpy.entities.task.Task)] = None, task_id=None, filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, query=None, items=None, wait=True)
remove items from Task.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned to be *owner* of the annotation task.


* **Parameters**

    
    * **task** ([*dtlpy.entities.task.Task*](entities.md#dtlpy.entities.task.Task)) – task object


    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the Id of the task


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **query** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – query to filter the items use it


    * **items** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of items to add to the task


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until remove items finish



* **Returns**

    True if success and an error if failed



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Examples**:

```python
dataset.tasks.remove_items(task= 'task_entity',
                            items = [items])
```


#### set_status(status: [str](https://docs.python.org/3/library/stdtypes.html#str), operation: [str](https://docs.python.org/3/library/stdtypes.html#str), task_id: [str](https://docs.python.org/3/library/stdtypes.html#str), item_ids: [List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#str)])
Update an item status within a task.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned to be *owner* of the annotation task.


* **Parameters**

    
    * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – string the describes the status


    * **operation** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the status action need ‘create’ or ‘delete’


    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the Id of the task


    * **item_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – List[str] id items ids



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
dataset.tasks.set_status(task_id= 'task_id', status='complete', operation='create')
```


#### update(task: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Task](entities.md#dtlpy.entities.task.Task)] = None, system_metadata=False)
Update a Task.

**Prerequisites**: You must be in the role of an *owner* or *developer* or *annotation manager* who created that task.


* **Parameters**

    
    * **task** ([*dtlpy.entities.task.Task*](entities.md#dtlpy.entities.task.Task)) – the task object


    * **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – True, if you want to change metadata system



* **Returns**

    Task object



* **Return type**

    [dtlpy.entities.task.Task](entities.md#dtlpy.entities.task.Task)


**Example**:

```python
dataset.tasks.update(task='task_entity')
```

### Assignments


### _class_ Assignments(client_api: ApiClient, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None, task: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Task](entities.md#dtlpy.entities.task.Task)] = None, dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None, project_id=None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Assignments Repository

The Assignments class allows users to manage assignments and their properties. Read more about [Task Assignment](https://dataloop.ai/docs/sdk-task-assigment) in our SDK documentation.


#### create(assignee_id: [str](https://docs.python.org/3/library/stdtypes.html#str), task: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Task](entities.md#dtlpy.entities.task.Task)] = None, filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, items: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[list] = None)
Create a new assignment.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Parameters**

    
    * **assignee_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the email of the user that want to assign the assignment


    * **task** ([*dtlpy.entities.task.Task*](entities.md#dtlpy.entities.task.Task)) – the task object that include the assignment


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **items** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of items (item Id or objects) to insert to the assignment



* **Returns**

    Assignment object



* **Return type**

    dtlpy.entities.assignment.Assignment assignment


**Example**:

```python
assignment = task.assignments.create(assignee_id='annotator1@dataloop.ai')
```


#### get(assignment_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, assignment_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Get Assignment object to use it in your code.


* **Parameters**

    
    * **assignment_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by name


    * **assignment_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id



* **Returns**

    Assignment object



* **Return type**

    [dtlpy.entities.assignment.Assignment](entities.md#dtlpy.entities.assignment.Assignment)


**Example**:

```python
assignment = task.assignments.get(assignment_id='assignment_id')
```


#### get_items(assignment: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Assignment](entities.md#dtlpy.entities.assignment.Assignment)] = None, assignment_id=None, assignment_name=None, dataset=None, filters=None)
Get all the items in the assignment.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Parameters**

    
    * **assignment** ([*dtlpy.entities.assignment.Assignment*](entities.md#dtlpy.entities.assignment.Assignment)) – assignment object


    * **assignment_id** – the Id of the assignment


    * **assignment_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the name of the assignment


    * **dataset** ([*dtlpy.entities.dataset.Dataset*](entities.md#dtlpy.entities.dataset.Dataset)) – dataset object, the dataset that refer to the assignment


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters



* **Returns**

    pages of the items



* **Return type**

    [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)


**Example**:

```python
items = task.assignments.get_items(assignment_id='assignment_id')
```


#### list(project_ids: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[list](https://docs.python.org/3/library/stdtypes.html#list)] = None, status: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, assignment_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, assignee_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, pages_size: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, page_offset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, task_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None)
Get Assignment list to be able to use it in your code.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Parameters**

    
    * **project_ids** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – search assignment by given list of project ids


    * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – search assignment by a given task status


    * **assignment_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – search assignment by a given assignment name


    * **assignee_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the user email that assignee the assignment to it


    * **pages_size** ([*int*](https://docs.python.org/3/library/functions.html#int)) – pages size of the output generator


    * **page_offset** ([*int*](https://docs.python.org/3/library/functions.html#int)) – page offset of the output generator


    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – search assignment by given task id



* **Returns**

    List of Assignment objects



* **Return type**

    miscellaneous.List[[dtlpy.entities.assignment.Assignment](entities.md#dtlpy.entities.assignment.Assignment)]


**Example**:

```python
assignments = task.assignments.list(status='complete', assignee_id='user@dataloop.ai', pages_size=100, page_offset=0)
```


#### open_in_web(assignment_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, assignment_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, assignment: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Open the assignment in the platform.

**Prerequisites**: All users.


* **Parameters**

    
    * **assignment_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the name of the assignment


    * **assignment_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the Id of the assignment


    * **assignment** ([*dtlpy.entities.assignment.Assignment*](entities.md#dtlpy.entities.assignment.Assignment)) – assignment object


**Example**:

```python
task.assignments.open_in_web(assignment_id='assignment_id')
```


#### reassign(assignee_id: [str](https://docs.python.org/3/library/stdtypes.html#str), assignment: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Assignment](entities.md#dtlpy.entities.assignment.Assignment)] = None, assignment_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, task: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Task](entities.md#dtlpy.entities.task.Task)] = None, task_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, wait: [bool](https://docs.python.org/3/library/functions.html#bool) = True)
Reassign an assignment.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Parameters**

    
    * **assignee_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the email of the user that want to assign the assignment


    * **assignment** ([*dtlpy.entities.assignment.Assignment*](entities.md#dtlpy.entities.assignment.Assignment)) – assignment object


    * **assignment_id** – the Id of the assignment


    * **task** ([*dtlpy.entities.task.Task*](entities.md#dtlpy.entities.task.Task)) – task object


    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the Id of the task that include the assignment


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until reassign assignment finish



* **Returns**

    Assignment object



* **Return type**

    [dtlpy.entities.assignment.Assignment](entities.md#dtlpy.entities.assignment.Assignment)


**Example**:

```python
assignment = task.assignments.reassign(assignee_ids='annotator1@dataloop.ai')
```


#### redistribute(workload: [Workload](entities.md#dtlpy.entities.assignment.Workload), assignment: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Assignment](entities.md#dtlpy.entities.assignment.Assignment)] = None, assignment_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, task: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Task](entities.md#dtlpy.entities.task.Task)] = None, task_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, wait: [bool](https://docs.python.org/3/library/functions.html#bool) = True)
Redistribute an assignment.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.

**Example**:


* **Parameters**

    
    * **workload** ([*dtlpy.entities.assignment.Workload*](entities.md#dtlpy.entities.assignment.Workload)) – list of WorkloadUnit objects. Customize distribution (percentage) between the task assignees. For example: [dl.WorkloadUnit([annotator@hi.com](mailto:annotator@hi.com), 80), dl.WorkloadUnit([annotator2@hi.com](mailto:annotator2@hi.com), 20)]


    * **assignment** ([*dtlpy.entities.assignment.Assignment*](entities.md#dtlpy.entities.assignment.Assignment)) – assignment object


    * **assignment_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the Id of the assignment


    * **task** ([*dtlpy.entities.task.Task*](entities.md#dtlpy.entities.task.Task)) – the task object that include the assignment


    * **task_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the Id of the task that include the assignment


    * **wait** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait until redistribute assignment finish



* **Returns**

    Assignment object



* **Return type**

    dtlpy.entities.assignment.Assignment assignment


```python
assignment = task.assignments.redistribute(workload=dl.Workload([dl.WorkloadUnit(assignee_id="annotator1@dataloop.ai", load=50),
                                                    dl.WorkloadUnit(assignee_id="annotator2@dataloop.ai", load=50)]))
```


#### set_status(status: [str](https://docs.python.org/3/library/stdtypes.html#str), operation: [str](https://docs.python.org/3/library/stdtypes.html#str), item_id: [str](https://docs.python.org/3/library/stdtypes.html#str), assignment_id: [str](https://docs.python.org/3/library/stdtypes.html#str))
Set item status within assignment.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Parameters**

    
    * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – string the describes the status


    * **operation** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the status action need ‘create’ or ‘delete’


    * **item_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – item id that want to set his status


    * **assignment_id** – the Id of the assignment



* **Returns**

    True id success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = task.assignments.set_status(assignment_id='assignment_id',
                            status='complete',
                            operation='created',
                            item_id='item_id')
```


#### update(assignment: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Assignment](entities.md#dtlpy.entities.assignment.Assignment)] = None, system_metadata: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Update an assignment.

**Prerequisites**: You must be in the role of an *owner*, *developer*, or *annotation manager* who has been assigned as *owner* of the annotation task.


* **Parameters**

    
    * **assignment** (*dtlpy.entities.assignment.Assignment assignment*) – assignment entity


    * **system_metadata** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – True, if you want to change metadata system



* **Returns**

    Assignment object



* **Return type**

    dtlpy.entities.assignment.Assignment assignment


**Example**:

```python
assignment = task.assignments.update(assignment='assignment_entity', system_metadata=False)
```

## Packages


### _class_ LocalServiceRunner(client_api: ApiClient, packages, cwd=None, multithreading=False, concurrency=10, package: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Package](entities.md#dtlpy.entities.package.Package)] = None, module_name='default_module', function_name='run', class_name='ServiceRunner', entry_point='main.py', mock_file_path=None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Service Runner Class


#### get_field(field_name, field_type, mock_json, project=None, mock_inputs=None)
Get field in mock json.


* **Parameters**

    
    * **field_name** – field name


    * **field_type** – field type


    * **mock_json** – mock json


    * **project** – project


    * **mock_inputs** – mock inputs



* **Returns**

    


#### get_mainpy_run_service()
Get mainpy run service


* **Returns**

    


#### run_local_project(project=None)
Run local project


* **Parameters**

    **project** – project entity



### _class_ Packages(client_api: ApiClient, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Packages Repository

The Packages class allows users to manage packages (code used for running in Dataloop’s FaaS) and their properties. Read more about [Packages](https://dataloop.ai/docs/faas-package).


#### build(package: [Package](entities.md#dtlpy.entities.package.Package), module_name=None, init_inputs=None, local_path=None, from_local=None)
Instantiate a module from the package code. Returns a loaded instance of the runner class


* **Parameters**

    
    * **package** – Package entity


    * **module_name** – Name of the module to build the runner class


    * **init_inputs** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – dictionary of the class init variables (if exists). will be used to init the module class


    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local path of the package (if from_local=False - codebase will be downloaded)


    * **from_local** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – bool. if true - codebase will not be downloaded (only use local files)



* **Returns**

    dl.BaseServiceRunner



#### build_requirements(filepath)
Build a requirement list (list of packages your code requires to run) from a file path. **The file listing the requirements MUST BE a txt file**.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    **filepath** – path of the requirements file



* **Returns**

    a list of dl.PackageRequirement



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)



#### _static_ build_trigger_dict(actions, name='default_module', filters=None, function='run', execution_mode: [TriggerExecutionMode](entities.md#dtlpy.entities.trigger.TriggerExecutionMode) = 'Once', type_t: [TriggerType](entities.md#dtlpy.entities.trigger.TriggerType) = 'Event')
Build a trigger dictionary to trigger FaaS. Read more about [FaaS Triggers](https://dataloop.ai/docs/faas-trigger).

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **actions** – list of dl.TriggerAction


    * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – trigger name


    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **function** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – function name


    * **execution_mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – execution mode dl.TriggerExecutionMode


    * **type_t** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – trigger type dl.TriggerType



* **Returns**

    trigger dict



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)


**Example**:

```python
project.packages.build_trigger_dict(actions=dl.TriggerAction.CREATED,
                                  function='run',
                                  execution_mode=dl.TriggerExecutionMode.ONCE)
```


#### _static_ check_cls_arguments(cls, missing, function_name, function_inputs)
Check class arguments. This method checks that the package function is correct.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **cls** – packages class


    * **missing** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of the missing params


    * **function_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – name of function


    * **function_inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of function inputs



#### checkout(package: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Package](entities.md#dtlpy.entities.package.Package)] = None, package_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, package_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Checkout (switch) to a package.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **package** ([*dtlpy.entities.package.Package*](entities.md#dtlpy.entities.package.Package)) – package entity


    * **package_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package id


    * **package_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package name


**Example**:

```python
project.packages.checkout(package='package_entity')
```


#### delete(package: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Package](entities.md#dtlpy.entities.package.Package)] = None, package_name=None, package_id=None)
Delete a Package object.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **package** ([*dtlpy.entities.package.Package*](entities.md#dtlpy.entities.package.Package)) – package entity


    * **package_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package id


    * **package_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package name



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
project.packages.delete(package_name='package_name')
```


#### deploy(package_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, package_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, package: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Package](entities.md#dtlpy.entities.package.Package)] = None, service_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, revision: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, init_input: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[List](https://docs.python.org/3/library/typing.html#typing.List)[FunctionIO], FunctionIO, [dict](https://docs.python.org/3/library/stdtypes.html#dict)]] = None, runtime: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[KubernetesRuntime, [dict](https://docs.python.org/3/library/stdtypes.html#dict)]] = None, sdk_version: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, agent_versions: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)] = None, bot: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[Bot](entities.md#dtlpy.entities.bot.Bot), [str](https://docs.python.org/3/library/stdtypes.html#str)]] = None, pod_type: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[InstanceCatalog](entities.md#dtlpy.entities.service.InstanceCatalog)] = None, verify: [bool](https://docs.python.org/3/library/functions.html#bool) = True, checkout: [bool](https://docs.python.org/3/library/functions.html#bool) = False, module_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, run_execution_as_process: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[bool](https://docs.python.org/3/library/functions.html#bool)] = None, execution_timeout: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, drain_time: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, on_reset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, max_attempts: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, force: [bool](https://docs.python.org/3/library/functions.html#bool) = False, secrets: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[list] = None, \*\*kwargs)
Deploy a package. A service is required to run the code in your package.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **package_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package id


    * **package_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package name


    * **package** ([*dtlpy.entities.package.Package*](entities.md#dtlpy.entities.package.Package)) – package entity


    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service name


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – project id


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


    * **checkout** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – checkout


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

    [dtlpy.entities.service.Service](entities.md#dtlpy.entities.service.Service)


**Example**:

```python
project.packages.deploy(service_name=package_name,
                        execution_timeout=3 * 60 * 60,
                        module_name=module.name,
                        runtime=dl.KubernetesRuntime(
                            concurrency=10,
                            pod_type=dl.InstanceCatalog.REGULAR_S,
                            autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                min_replicas=1,
                                max_replicas=20,
                                queue_length=20
                            )
                        )
                    )
```


#### deploy_from_file(project, json_filepath)
Deploy package and service from a JSON file.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **project** ([*dtlpy.entities.project.Project*](entities.md#dtlpy.entities.project.Project)) – project entity


    * **json_filepath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path of the file to deploy



* **Returns**

    the package and the services


**Example**:

```python
project.packages.deploy_from_file(project='project_entity', json_filepath='json_filepath')
```


#### _static_ generate(name=None, src_path: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, service_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, package_type='default_package_type')
Generate a new package. Provide a file path to a JSON file with all the details of the package and service to generate the package.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – name


    * **src_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – source file path


    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service name


    * **package_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package type from PackageCatalog


**Example**:

```python
project.packages.generate(name='package_name',
                          src_path='src_path')
```


#### get(package_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, package_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, checkout: [bool](https://docs.python.org/3/library/functions.html#bool) = False, fetch=None)
Get Package object to use in your code.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **package_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package id


    * **package_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package name


    * **checkout** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – set the package as a default package object (cookies)


    * **fetch** – optional - fetch entity from platform, default taken from cookie



* **Returns**

    Package object



* **Return type**

    [dtlpy.entities.package.Package](entities.md#dtlpy.entities.package.Package)


**Example**:

```python
project.packages.get(package_id='package_id')
```


#### list(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
List project packages.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – project id



* **Returns**

    Paged entity



* **Return type**

    [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)


**Example**:

```python
project.packages.list()
```


#### open_in_web(package: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Package](entities.md#dtlpy.entities.package.Package)] = None, package_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, package_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Open the package in the web platform.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **package** ([*dtlpy.entities.package.Package*](entities.md#dtlpy.entities.package.Package)) – package entity


    * **package_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package id


    * **package_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package name


**Example**:

```python
project.packages.open_in_web(package_id='package_id')
```


#### pull(package: [Package](entities.md#dtlpy.entities.package.Package), version=None, local_path=None, project_id=None)
Pull (download) the package to a local path.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **package** ([*dtlpy.entities.package.Package*](entities.md#dtlpy.entities.package.Package)) – package entity


    * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the package version to pull


    * **local_path** – the path of where to save the package


    * **project_id** – the project id that include the package



* **Returns**

    local path where the package pull



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)


**Example**:

```python
project.packages.pull(package='package_entity', local_path='local_path')
```


#### push(project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, package_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, src_path: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, codebase: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[GitCodebase, ItemCodebase, FilesystemCodebase]] = None, modules: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[List](https://docs.python.org/3/library/typing.html#typing.List)[[PackageModule](entities.md#dtlpy.entities.package_module.PackageModule)]] = None, is_global: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[bool](https://docs.python.org/3/library/functions.html#bool)] = None, checkout: [bool](https://docs.python.org/3/library/functions.html#bool) = False, revision_increment: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, version: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, ignore_sanity_check: [bool](https://docs.python.org/3/library/functions.html#bool) = False, service_update: [bool](https://docs.python.org/3/library/functions.html#bool) = False, service_config: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)] = None, slots: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[List](https://docs.python.org/3/library/typing.html#typing.List)[[PackageSlot](entities.md#dtlpy.entities.package_slot.PackageSlot)]] = None, requirements: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[List](https://docs.python.org/3/library/typing.html#typing.List)[PackageRequirement]] = None, package_type=None, metadata=None)
Push your local package to the UI.

**Prerequisites**: You must be in the role of an *owner* or *developer*.

Project will be taken in the following hierarchy:
project(input) -> project_id(input) -> self.project(context) -> checked out


* **Parameters**

    
    * **project** ([*dtlpy.entities.project.Project*](entities.md#dtlpy.entities.project.Project)) – optional - project entity to deploy to. default from context or checked-out


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - project id to deploy to. default from context or checked-out


    * **package_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package name


    * **src_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to package codebase


    * **codebase** (*dtlpy.entities.codebase.Codebase*) – codebase object


    * **modules** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of modules PackageModules of the package


    * **is_global** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – is package is global or local


    * **checkout** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – checkout package to local dir


    * **revision_increment** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - str - version bumping method - major/minor/patch - default = None


    * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – semver version f the package


    * **ignore_sanity_check** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – NOT RECOMMENDED - skip code sanity check before pushing


    * **service_update** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - bool - update the service


:param dict service_config : Service object as dict. Contains the spec of the default service to create.
:param list slots: optional - list of slots PackageSlot of the package
:param list requirements: requirements - list of package requirements
:param str package_type: default ‘faas’, options: ‘app’, ‘ml
:param dict metadata: dictionary of system and user metadata


* **Returns**

    Package object



* **Return type**

    [dtlpy.entities.package.Package](entities.md#dtlpy.entities.package.Package)


**Example**:

```python
project.packages.push(package_name='package_name',
                        modules=[module],
                        version='1.0.0',
                        src_path=os.getcwd()
                    )
```


#### revisions(package: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Package](entities.md#dtlpy.entities.package.Package)] = None, package_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Get the package revisions history.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **package** ([*dtlpy.entities.package.Package*](entities.md#dtlpy.entities.package.Package)) – package entity


    * **package_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package id


**Example**:

```python
project.packages.revisions(package='package_entity')
```


#### test_local_package(cwd: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, concurrency: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, package: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Package](entities.md#dtlpy.entities.package.Package)] = None, module_name: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'default_module', function_name: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'run', class_name: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'ServiceRunner', entry_point: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'main.py', mock_file_path: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Test local package in local environment.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **cwd** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – path to the file


    * **concurrency** ([*int*](https://docs.python.org/3/library/functions.html#int)) – the concurrency of the test


    * **package** ([*dtlpy.entities.package.Package*](entities.md#dtlpy.entities.package.Package)) – entities.package


    * **module_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – module name


    * **function_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – function name


    * **class_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – class name


    * **entry_point** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the file to run like main.py


    * **mock_file_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the mock file that have the inputs



* **Returns**

    list created by the function that tested the output



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
project.packages.test_local_package(cwd='path_to_package',
                                    package='package_entity',
                                    function_name='run')
```


#### update(package: [Package](entities.md#dtlpy.entities.package.Package), revision_increment: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Update Package changes to the platform.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    
    * **package** ([*dtlpy.entities.package.Package*](entities.md#dtlpy.entities.package.Package)) – 


    * **revision_increment** – optional - str - version bumping method - major/minor/patch - default = None



* **Returns**

    Package object



* **Return type**

    [dtlpy.entities.package.Package](entities.md#dtlpy.entities.package.Package)


**Example**:

```python
project.packages.delete(package='package_entity')
```

### Codebases


### _class_ Codebases(client_api: ApiClient, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None, dataset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Dataset](entities.md#dtlpy.entities.dataset.Dataset)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Codebase Repository

The Codebases class allows the user to manage codebases and their properties. The codebase is the code the user uploads for the user’s packages to run. Read more about [codebase](https://dataloop.ai/docs/tutorial-ui?#1-codebase) in our FaaS (function as a service).


#### clone_git(codebase: Codebase, local_path: [str](https://docs.python.org/3/library/stdtypes.html#str))
Clone code base

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **codebase** (*dtlpy.entities.codebase.Codebase*) – codebase object


    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local path



* **Returns**

    path where the clone will be



* **Return type**

    str

    **Example**:



```python
package.codebases.clone_git(codebase='codebase_entity', local_path='local_path')
```


#### get(codebase_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, codebase_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, version: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Get a Codebase object to use in your code.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.

**Example**:

```python
package.codebases.get(codebase_name='codebase_name')
```


* **Parameters**

    
    * **codebase_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by name


    * **codebase_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id


    * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – codebase version. default is latest. options: “all”, “latest” or ver number - “10”



* **Returns**

    Codebase object



#### _static_ get_current_version(all_versions_pages, zip_md)
This method returns the current version of the codebase and other versions found.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **all_versions_pages** (*codebase*) – codebase object


    * **zip_md** – zipped file of codebase



* **Returns**

    current version and all versions found of codebase



* **Return type**

    [int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)


**Example**:

```python
package.codebases.get_current_version(all_versions_pages='codebase_entity', zip_md='path')
```


#### list()
List all codebases.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.

**Example**:

```python
package.codebases.list()
```


* **Returns**

    Paged entity



* **Return type**

    [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)



#### list_versions(codebase_name: [str](https://docs.python.org/3/library/stdtypes.html#str))
List all codebase versions.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.

**Example**:

```python
package.codebases.list_versions(codebase_name='codebase_name')
```


* **Parameters**

    **codebase_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – code base name



* **Returns**

    list of versions



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)



#### pack(directory: [str](https://docs.python.org/3/library/stdtypes.html#str), name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, extension: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'zip', description: [str](https://docs.python.org/3/library/stdtypes.html#str) = '', ignore_directories: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[List](https://docs.python.org/3/library/typing.html#typing.List)[[str](https://docs.python.org/3/library/stdtypes.html#str)]] = None)
Zip a local code directory and post to codebases.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **directory** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local directory to pack


    * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – codebase name


    * **extension** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the extension of the file


    * **description** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – codebase description


    * **ignore_directories** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – directories to ignore.



* **Returns**

    Codebase object



* **Return type**

    dtlpy.entities.codebase.Codebase


**Example**:

```python
package.codebases.pack(directory='path_dir', name='codebase_name')
```


#### pull_git(codebase, local_path)
Pull (download) a codebase.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **codebase** (*dtlpy.entities.codebase.Codebase*) – codebase object


    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local path



* **Returns**

    path where the Pull will be



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)


**Example**:

```python
package.codebases.pull_git(codebase='codebase_entity', local_path='local_path')
```


#### unpack(codebase: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[Codebase] = None, codebase_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, codebase_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, local_path: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, version: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Unpack codebase locally. Download source code and unzip.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **codebase** (*dtlpy.entities.codebase.Codebase*) – dl.Codebase object


    * **codebase_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – search by name


    * **codebase_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – search by id


    * **local_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – local path to save codebase


    * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – codebase version to unpack. default - latest



* **Returns**

    String (dirpath)



* **Return type**

    [str](https://docs.python.org/3/library/stdtypes.html#str)


**Example**:

```python
package.codebases.unpack(codebase='codebase_entity', local_path='local_path')
```

## Services


### _class_ ServiceLog(_json: [dict](https://docs.python.org/3/library/stdtypes.html#dict), service: [Service](entities.md#dtlpy.entities.service.Service), services: Services, start=None, follow=None, execution_id=None, function_name=None, replica_id=None, system=False)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Service Log


#### view(until_completed)
View logs


* **Parameters**

    **until_completed** – 



### _class_ Services(client_api: ApiClient, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None, package: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Package](entities.md#dtlpy.entities.package.Package)] = None, project_id=None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Services Repository

The Services class allows the user to manage services and their properties. Services are created from the packages users create. See our documentation for more information about [services](https://dataloop.ai/docs/faas-service).


#### activate_slots(service: [Service](entities.md#dtlpy.entities.service.Service), project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, task_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, org_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, user_email: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, slots: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[List](https://docs.python.org/3/library/typing.html#typing.List)[[PackageSlot](entities.md#dtlpy.entities.package_slot.PackageSlot)]] = None, role=None, prevent_override: [bool](https://docs.python.org/3/library/functions.html#bool) = True, visible: [bool](https://docs.python.org/3/library/functions.html#bool) = True, icon: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'fas fa-magic', \*\*kwargs)
Activate service slots (creates buttons in the UI that activate services).

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **service** ([*dtlpy.entities.service.Service*](entities.md#dtlpy.entities.service.Service)) – service entity


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
setting = package.services.activate_slots(service='service_entity',
                                project_id='project_id',
                                slots=List[entities.PackageSlot],
                                icon='fas fa-magic')
```


#### checkout(service: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Service](entities.md#dtlpy.entities.service.Service)] = None, service_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, service_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Checkout (switch) to a service.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **service** ([*dtlpy.entities.service.Service*](entities.md#dtlpy.entities.service.Service)) – Service entity


    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service name


    * **service_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service id


**Example**:

```python
package.services.checkout(service_id='service_id')
```


#### delete(service_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, service_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Delete Service object

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.

You must provide at least ONE of the following params: service_id, service_name.


* **Parameters**

    
    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – by name


    * **service_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – by id



* **Returns**

    True



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
is_deleted = package.services.delete(service_id='service_id')
```


#### deploy(service_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, package: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Package](entities.md#dtlpy.entities.package.Package)] = None, bot: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[Bot](entities.md#dtlpy.entities.bot.Bot), [str](https://docs.python.org/3/library/stdtypes.html#str)]] = None, revision: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, init_input: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[[List](https://docs.python.org/3/library/typing.html#typing.List)[FunctionIO], FunctionIO, [dict](https://docs.python.org/3/library/stdtypes.html#dict)]] = None, runtime: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Union](https://docs.python.org/3/library/typing.html#typing.Union)[KubernetesRuntime, [dict](https://docs.python.org/3/library/stdtypes.html#dict)]] = None, pod_type: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[InstanceCatalog](entities.md#dtlpy.entities.service.InstanceCatalog)] = None, sdk_version: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, agent_versions: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)] = None, verify: [bool](https://docs.python.org/3/library/functions.html#bool) = True, checkout: [bool](https://docs.python.org/3/library/functions.html#bool) = False, module_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, driver_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, func: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Callable](https://docs.python.org/3/library/typing.html#typing.Callable)] = None, run_execution_as_process: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[bool](https://docs.python.org/3/library/functions.html#bool)] = None, execution_timeout: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, drain_time: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, max_attempts: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, on_reset: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, force: [bool](https://docs.python.org/3/library/functions.html#bool) = False, secrets: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[list] = None, \*\*kwargs)
Deploy service.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – name


    * **package** ([*dtlpy.entities.package.Package*](entities.md#dtlpy.entities.package.Package)) – package entity


    * **bot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – bot email


    * **revision** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – package revision of version


    * **init_input** – config to run at startup


    * **runtime** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – runtime resources


    * **pod_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pod type dl.InstanceCatalog


    * **sdk_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
        * optional - string - sdk version



    * **agent_versions** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
        * dictionary - - optional -versions of sdk



    * **verify** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true, verify the inputs


    * **checkout** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true, checkout (switch) to service


    * **module_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – module name


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – project id


    * **driver_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – driver id


    * **func** (*Callable*) – function to deploy


    * **run_execution_as_process** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true, run execution as process


    * **execution_timeout** ([*int*](https://docs.python.org/3/library/functions.html#int)) – execution timeout in seconds


    * **drain_time** ([*int*](https://docs.python.org/3/library/functions.html#int)) – drain time in seconds


    * **max_attempts** ([*int*](https://docs.python.org/3/library/functions.html#int)) – maximum execution retries in-case of a service reset


    * **on_reset** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – what happens on reset


    * **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - if true, terminate old replicas immediately


    * **secrets** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)) – list of the integrations ids


    * **kwargs** – list of additional arguments



* **Returns**

    Service object



* **Return type**

    [dtlpy.entities.service.Service](entities.md#dtlpy.entities.service.Service)


**Example**:

```python
service = package.services.deploy(service_name=package_name,
                        execution_timeout=3 * 60 * 60,
                        module_name=module.name,
                        runtime=dl.KubernetesRuntime(
                            concurrency=10,
                            pod_type=dl.InstanceCatalog.REGULAR_S,
                            autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                min_replicas=1,
                                max_replicas=20,
                                queue_length=20
                            )
                        )
                    )
```


#### deploy_from_local_folder(cwd=None, service_file=None, bot=None, checkout=False, force=False)
Deploy from local folder in local environment.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **cwd** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - package working directory. Default=cwd


    * **service_file** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - service file. Default=None


    * **bot** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – bot


    * **checkout** – checkout


    * **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - terminate old replicas immediately



* **Returns**

    Service object



* **Return type**

    [dtlpy.entities.service.Service](entities.md#dtlpy.entities.service.Service)


**Example**:

```python
service = package.services.deploy_from_local_folder(cwd='file_path',
                                          service_file='service_file')
```


#### execute(service: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Service](entities.md#dtlpy.entities.service.Service)] = None, service_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, service_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, sync: [bool](https://docs.python.org/3/library/functions.html#bool) = False, function_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, stream_logs: [bool](https://docs.python.org/3/library/functions.html#bool) = False, execution_input=None, resource=None, item_id=None, dataset_id=None, annotation_id=None, project_id=None)
Execute a function on an existing service.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **service** ([*dtlpy.entities.service.Service*](entities.md#dtlpy.entities.service.Service)) – service entity


    * **service_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service id


    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service name


    * **sync** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait for function to end


    * **function_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – function name to run


    * **stream_logs** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – prints logs of the new execution. only works with sync=True


    * **execution_input** – input dictionary or list of FunctionIO entities


    * **resource** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – dl.PackageInputType - input type.


    * **item_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – str - optional - input to function


    * **dataset_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – str - optional - input to function


    * **annotation_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – str - optional - input to function


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – str - resource’s project



* **Returns**

    entities.Execution



* **Return type**

    [dtlpy.entities.execution.Execution](entities.md#dtlpy.entities.execution.Execution)


**Example**:

```python
execution = package.services.execute(service='service_entity',
                        function_name='run',
                        item_id='item_id',
                        project_id='project_id')
```


#### get(service_name=None, service_id=None, checkout=False, fetch=None)
Get service to use in your code.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by name


    * **service_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – optional - search by id


    * **checkout** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true, checkout (switch) to service


    * **fetch** – optional - fetch entity from platform, default taken from cookie



* **Returns**

    Service object



* **Return type**

    [dtlpy.entities.service.Service](entities.md#dtlpy.entities.service.Service)


**Example**:

```python
service = package.services.get(service_id='service_id')
```


#### list(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None)
List all services (services can be listed for a package or for a project).

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters



* **Returns**

    Paged entity



* **Return type**

    [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)


**Example**:

```python
services = package.services.list()
```


#### log(service, size=100, checkpoint=None, start=None, end=None, follow=False, text=None, execution_id=None, function_name=None, replica_id=None, system=False, view=True, until_completed=True)
Get service logs.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **service** ([*dtlpy.entities.service.Service*](entities.md#dtlpy.entities.service.Service)) – service object


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

    ServiceLog


**Example**:

```python
service_logs = package.services.log(service='service_entity')
```


#### name_validation(name: [str](https://docs.python.org/3/library/stdtypes.html#str))
Validation service name.

**Prerequisites**: You must be in the role of an *owner* or *developer*.


* **Parameters**

    **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service name


**Example**:

```python
package.services.name_validation(name='name')
```


#### open_in_web(service: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Service](entities.md#dtlpy.entities.service.Service)] = None, service_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, service_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Open the service in web platform

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service name


    * **service_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service id


    * **service** ([*dtlpy.entities.service.Service*](entities.md#dtlpy.entities.service.Service)) – service entity


**Example**:

```python
package.services.open_in_web(service_id='service_id')
```


#### pause(service_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, service_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, force: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Pause service.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.

You must provide at least ONE of the following params: service_id, service_name


* **Parameters**

    
    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service name


    * **service_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service id


    * **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - terminate old replicas immediately



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
success = package.services.pause(service_id='service_id')
```


#### resume(service_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, service_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, force: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Resume service.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.

You must provide at least ONE of the following params: service_id, service_name.


* **Parameters**

    
    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service name


    * **service_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service id


    * **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - terminate old replicas immediately



* **Returns**

    json of the service



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)


**Example**:

```python
service_json = package.services.resume(service_id='service_id')
```


#### revisions(service: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Service](entities.md#dtlpy.entities.service.Service)] = None, service_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Get service revisions history.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.

You must provide at leats ONE of the following params: service, service_id


* **Parameters**

    
    * **service** ([*dtlpy.entities.service.Service*](entities.md#dtlpy.entities.service.Service)) – Service entity


    * **service_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service id


**Example**:

```python
service_revision = package.services.revisions(service_id='service_id')
```


#### status(service_name=None, service_id=None)
Get service status.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.

You must provide at least ONE of the following params: service_id, service_name


* **Parameters**

    
    * **service_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service name


    * **service_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service id



* **Returns**

    status json



* **Return type**

    [dict](https://docs.python.org/3/library/stdtypes.html#dict)


**Example**:

```python
status_json = package.services.status(service_id='service_id')
```


#### update(service: [Service](entities.md#dtlpy.entities.service.Service), force: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Update service changes to platform.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a package.


* **Parameters**

    
    * **service** ([*dtlpy.entities.service.Service*](entities.md#dtlpy.entities.service.Service)) – Service entity


    * **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - terminate old replicas immediately



* **Returns**

    Service entity



* **Return type**

    [dtlpy.entities.service.Service](entities.md#dtlpy.entities.service.Service)


**Example**:

```python
service = package.services.update(service='service_entity')
```

### Bots


### _class_ Bots(client_api: ApiClient, project: [Project](entities.md#dtlpy.entities.project.Project))
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Bots Repository

The Bots class allows the user to manage bots and their properties. See our documentation for more information on [bots](https://dataloop.ai/docs/faas-bot).


#### create(name: [str](https://docs.python.org/3/library/stdtypes.html#str), return_credentials: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Create a new Bot.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    
    * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – bot name


    * **return_credentials** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – True will return the password when created



* **Returns**

    Bot object



* **Return type**

    [dtlpy.entities.bot.Bot](entities.md#dtlpy.entities.bot.Bot)


**Example**:

```python
service.bots.delete(name='bot', return_credentials=False)
```


#### delete(bot_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, bot_email: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Delete a Bot.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.

You must provide at least ONE of the following params: bot_id, bot_email


* **Parameters**

    
    * **bot_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – bot id to delete


    * **bot_email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – bot email to delete



* **Returns**

    True if successful



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
service.bots.delete(bot_id='bot_id')
```


#### get(bot_email: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, bot_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, bot_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Get a Bot object.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    
    * **bot_email** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – get bot by email


    * **bot_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – get bot by id


    * **bot_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – get bot by name



* **Returns**

    Bot object



* **Return type**

    [dtlpy.entities.bot.Bot](entities.md#dtlpy.entities.bot.Bot)


**Example**:

```python
service.bots.get(bot_id='bot_id')
```


#### list()
Get a project or package bots list.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Returns**

    List of Bots objects



* **Return type**

    [list](https://docs.python.org/3/library/stdtypes.html#list)


**Example**:

```python
bots_list = service.bots.list()
```

## Triggers


### _class_ Triggers(client_api: ApiClient, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None, service: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Service](entities.md#dtlpy.entities.service.Service)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, pipeline: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Triggers Repository

The Triggers class allows users to manage triggers and their properties. Triggers activate services. See our documentation for more information on [triggers](https://dataloop.ai/docs/faas-trigger).


#### create(service_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, trigger_type: [TriggerType](entities.md#dtlpy.entities.trigger.TriggerType) = TriggerType.EVENT, name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, webhook_id=None, function_name='run', project_id=None, active=True, filters=None, resource: [TriggerResource](entities.md#dtlpy.entities.trigger.TriggerResource) = TriggerResource.ITEM, actions: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[TriggerAction](entities.md#dtlpy.entities.trigger.TriggerAction)] = None, execution_mode: [TriggerExecutionMode](entities.md#dtlpy.entities.trigger.TriggerExecutionMode) = TriggerExecutionMode.ONCE, start_at=None, end_at=None, inputs=None, cron=None, pipeline_id=None, pipeline=None, pipeline_node_id=None, root_node_namespace=None, \*\*kwargs)
Create a Trigger. Can create two types: a cron trigger or an event trigger.
Inputs are different for each type

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.

Inputs for all types:


* **Parameters**

    
    * **service_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Id of services to be triggered


    * **trigger_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – can be cron or event. use enum dl.TriggerType for the full list


    * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – name of the trigger


    * **webhook_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – id for webhook to be called


    * **function_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the function name to be called when triggered (must be defined in the package)


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – project id where trigger will work


    * **active** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – optional - True/False, default = True, if true trigger is active


Inputs for event trigger:
:param dtlpy.entities.filters.Filters filters: optional - Item/Annotation metadata filters, default = none
:param str resource: optional - Dataset/Item/Annotation/ItemStatus, default = Item
:param str actions: optional - Created/Updated/Deleted, default = create
:param str execution_mode: how many times trigger should be activated; default is “Once”. enum dl.TriggerExecutionMode

Inputs for cron trigger:
:param start_at: iso format date string to start activating the cron trigger
:param end_at: iso format date string to end the cron activation
:param inputs: dictionary “name”:”val” of inputs to the function
:param str cron: cron spec specifying when it should run. more information: [https://en.wikipedia.org/wiki/Cron](https://en.wikipedia.org/wiki/Cron)
:param str pipeline_id: Id of pipeline to be triggered
:param pipeline: pipeline entity to be triggered
:param str pipeline_node_id: Id of pipeline root node to be triggered
:param root_node_namespace: namespace of pipeline root node to be triggered


* **Returns**

    Trigger entity



* **Return type**

    [dtlpy.entities.trigger.Trigger](entities.md#dtlpy.entities.trigger.Trigger)


**Example**:

```python
service.triggers.create(name='triggername',
                      execution_mode=dl.TriggerExecutionMode.ONCE,
                      resource='Item',
                      actions='Created',
                      function_name='run',
                      filters={'$and': [{'hidden': False},
                                        {'type': 'file'}]}
                      )
```


#### delete(trigger_id=None, trigger_name=None)
Delete Trigger object

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    
    * **trigger_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – trigger id


    * **trigger_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – trigger name



* **Returns**

    True is successful error if not



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

```python
service.triggers.delete(trigger_id='trigger_id')
```


#### get(trigger_id=None, trigger_name=None)
Get Trigger object

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    
    * **trigger_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – trigger id


    * **trigger_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – trigger name



* **Returns**

    Trigger entity



* **Return type**

    [dtlpy.entities.trigger.Trigger](entities.md#dtlpy.entities.trigger.Trigger)


**Example**:

```python
service.triggers.get(trigger_id='trigger_id')
```


#### list(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None)
List triggers of a project, package, or service.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters



* **Returns**

    Paged entity



* **Return type**

    [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)


**Example**:

```python
service.triggers.list()
```


#### name_validation(name: [str](https://docs.python.org/3/library/stdtypes.html#str))
This method validates the trigger name. If name is not valid, this method will return an error. Otherwise, it will not return anything.


* **Parameters**

    **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – trigger name



#### resource_information(resource, resource_type, action='Created')
Returns which function should run on an item (based on global triggers).

**Prerequisites**: You must be a **superuser** to run this method.


* **Parameters**

    
    * **resource** – ‘Item’ / ‘Dataset’ / etc


    * **resource_type** – dictionary of the resource object


    * **action** – ‘Created’ / ‘Updated’ / etc.


**Example**:

```python
service.triggers.resource_information(resource='Item', resource_type=item_object, action='Created')
```


#### update(trigger: [BaseTrigger](entities.md#dtlpy.entities.trigger.BaseTrigger))
Update trigger

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    **trigger** ([*dtlpy.entities.trigger.Trigger*](entities.md#dtlpy.entities.trigger.Trigger)) – Trigger entity



* **Returns**

    Trigger entity



* **Return type**

    [dtlpy.entities.trigger.Trigger](entities.md#dtlpy.entities.trigger.Trigger)


**Example**:

```python
service.triggers.update(trigger='trigger_entity')
```

## Executions


### _class_ Executions(client_api: ApiClient, service: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Service](entities.md#dtlpy.entities.service.Service)] = None, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Service Executions Repository

The Executions class allows the users to manage executions (executions of services) and their properties. See our documentation for more information about [executions](https://dataloop.ai/docs/faas-execution).


#### create(service_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, execution_input: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[list](https://docs.python.org/3/library/stdtypes.html#list)] = None, function_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, resource: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[PackageInputType](entities.md#dtlpy.entities.package_function.PackageInputType)] = None, item_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, dataset_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, annotation_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, sync: [bool](https://docs.python.org/3/library/functions.html#bool) = False, stream_logs: [bool](https://docs.python.org/3/library/functions.html#bool) = False, return_output: [bool](https://docs.python.org/3/library/functions.html#bool) = False, return_curl_only: [bool](https://docs.python.org/3/library/functions.html#bool) = False, timeout: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None)
Execute a function on an existing service

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    
    * **service_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service id to execute on


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


    * **return_curl_only** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – return the cURL of the creation WITHOUT actually do it


    * **timeout** ([*int*](https://docs.python.org/3/library/functions.html#int)) – int, seconds to wait until TimeoutError is raised. if <=0 - wait until done -
    by default wait take the service timeout



* **Returns**

    execution object



* **Return type**

    [dtlpy.entities.execution.Execution](entities.md#dtlpy.entities.execution.Execution)


**Example**:

```python
service.executions.create(function_name='function_name', item_id='item_id', project_id='project_id')
```


#### get(execution_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, sync: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Get Service execution object

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    
    * **execution_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – execution id


    * **sync** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true, wait for the execution to finish



* **Returns**

    Service execution object



* **Return type**

    [dtlpy.entities.execution.Execution](entities.md#dtlpy.entities.execution.Execution)


**Example**:

```python
service.executions.get(execution_id='execution_id')
```


#### increment(execution: [Execution](entities.md#dtlpy.entities.execution.Execution))
Increment the number of attempts that an execution is allowed to attempt to run a service that is not responding.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    **execution** ([*dtlpy.entities.execution.Execution*](entities.md#dtlpy.entities.execution.Execution)) – 



* **Returns**

    int



* **Return type**

    [int](https://docs.python.org/3/library/functions.html#int)


**Example**:

```python
service.executions.increment(execution='execution_entity')
```


#### list(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None)
List service executions

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – dl.Filters entity to filters items



* **Returns**

    Paged entity



* **Return type**

    [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)


**Example**:

```python
service.executions.list()
```


#### logs(execution_id: [str](https://docs.python.org/3/library/stdtypes.html#str), follow: [bool](https://docs.python.org/3/library/functions.html#bool) = True, until_completed: [bool](https://docs.python.org/3/library/functions.html#bool) = True)
executions logs

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    
    * **execution_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – execution id


    * **follow** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true, keep stream future logs


    * **until_completed** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – if true, wait until completed



* **Returns**

    executions logs


**Example**:

```python
service.executions.logs(execution_id='execution_id')
```


#### progress_update(execution_id: [str](https://docs.python.org/3/library/stdtypes.html#str), status: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[ExecutionStatus](entities.md#dtlpy.entities.execution.ExecutionStatus)] = None, percent_complete: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None, message: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, output: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, service_version: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Update Execution Progress.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    
    * **execution_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – execution id


    * **status** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – ExecutionStatus


    * **percent_complete** ([*int*](https://docs.python.org/3/library/functions.html#int)) – percent work done


    * **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – message


    * **output** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the output of the execution


    * **service_version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – service version



* **Returns**

    Service execution object



* **Return type**

    [dtlpy.entities.execution.Execution](entities.md#dtlpy.entities.execution.Execution)


**Example**:

```python
service.executions.progress_update(execution_id='execution_id', status='complete', percent_complete=100)
```


#### rerun(execution: [Execution](entities.md#dtlpy.entities.execution.Execution), sync: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Rerun execution

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    
    * **execution** ([*dtlpy.entities.execution.Execution*](entities.md#dtlpy.entities.execution.Execution)) – 


    * **sync** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – wait for the execution to finish



* **Returns**

    Execution object



* **Return type**

    [dtlpy.entities.execution.Execution](entities.md#dtlpy.entities.execution.Execution)


**Example**:

```python
service.executions.rerun(execution='execution_entity')
```


#### terminate(execution: [Execution](entities.md#dtlpy.entities.execution.Execution))
Terminate Execution

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    **execution** ([*dtlpy.entities.execution.Execution*](entities.md#dtlpy.entities.execution.Execution)) – 



* **Returns**

    execution object



* **Return type**

    [dtlpy.entities.execution.Execution](entities.md#dtlpy.entities.execution.Execution)


**Example**:

```python
service.executions.terminate(execution='execution_entity')
```


#### update(execution: [Execution](entities.md#dtlpy.entities.execution.Execution))
Update execution changes to platform

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    **execution** ([*dtlpy.entities.execution.Execution*](entities.md#dtlpy.entities.execution.Execution)) – execution entity



* **Returns**

    Service execution object



* **Return type**

    [dtlpy.entities.execution.Execution](entities.md#dtlpy.entities.execution.Execution)


**Example**:

```python
service.executions.update(execution='execution_entity')
```


#### wait(execution_id: [str](https://docs.python.org/3/library/stdtypes.html#str), timeout: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[int](https://docs.python.org/3/library/functions.html#int)] = None)
Get Service execution object.

**Prerequisites**: You must be in the role of an *owner* or *developer*. You must have a service.


* **Parameters**

    
    * **execution_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – execution id


    * **timeout** ([*int*](https://docs.python.org/3/library/functions.html#int)) – seconds to wait until TimeoutError is raised. if <=0 - wait until done - by default wait take the service timeout



* **Returns**

    Service execution object



* **Return type**

    [dtlpy.entities.execution.Execution](entities.md#dtlpy.entities.execution.Execution)


**Example**:

```python
service.executions.wait(execution_id='execution_id')
```

## Pipelines


### _class_ Pipelines(client_api: ApiClient, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Pipelines Repository

The Pipelines class allows users to manage pipelines and their properties. See our documentation for more information on [pipelines](https://dataloop.ai/docs/pipelines-overview).


#### create(name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, pipeline_json: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[dict](https://docs.python.org/3/library/stdtypes.html#dict)] = None)
Create a new pipeline.

**prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline name


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – project id


    * **pipeline_json** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)) – json containing the pipeline fields



* **Returns**

    Pipeline object



* **Return type**

    [dtlpy.entities.pipeline.Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)


**Example**:

```python
pipeline = project.pipelines.create(name='pipeline_name')
```


#### delete(pipeline: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)] = None, pipeline_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, pipeline_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
> Delete Pipeline object.

> **prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **pipeline** ([*dtlpy.entities.pipeline.Pipeline*](entities.md#dtlpy.entities.pipeline.Pipeline)) – pipeline entity


    * **pipeline_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline id


    * **pipeline_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline name



* **Returns**

    True if success



* **Return type**

    [bool](https://docs.python.org/3/library/functions.html#bool)


**Example**:

> ```python
> is_deleted = project.pipelines.delete(pipeline_id='pipeline_id')
> ```


#### execute(pipeline: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)] = None, pipeline_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, pipeline_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, execution_input=None)
Execute a pipeline and return the pipeline execution as an object.

**prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **pipeline** ([*dtlpy.entities.pipeline.Pipeline*](entities.md#dtlpy.entities.pipeline.Pipeline)) – pipeline entity


    * **pipeline_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline id


    * **pipeline_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline name


    * **execution_input** – list of the dl.FunctionIO or dict of pipeline input - example {‘item’: ‘item_id’}



* **Returns**

    entities.PipelineExecution object



* **Return type**

    [dtlpy.entities.pipeline_execution.PipelineExecution](entities.md#dtlpy.entities.pipeline_execution.PipelineExecution)


**Example**:

```python
pipeline_execution= project.pipelines.execute(pipeline='pipeline_entity', execution_input= {'item': 'item_id'} )
```


#### get(pipeline_name=None, pipeline_id=None, fetch=None)
Get Pipeline object to use in your code.

**prerequisites**: You must be an *owner* or *developer* to use this method.

You must provide at least ONE of the following params: pipeline_name, pipeline_id.


* **Parameters**

    
    * **pipeline_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline id


    * **pipeline_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline name


    * **fetch** – optional - fetch entity from platform, default taken from cookie



* **Returns**

    Pipeline object



* **Return type**

    [dtlpy.entities.pipeline.Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)


**Example**:

```python
pipeline = project.pipelines.get(pipeline_id='pipeline_id')
```


#### install(pipeline: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)] = None)
Install (start) a pipeline.

**prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    **pipeline** ([*dtlpy.entities.pipeline.Pipeline*](entities.md#dtlpy.entities.pipeline.Pipeline)) – pipeline entity



* **Returns**

    Composition object


**Example**:

```python
project.pipelines.install(pipeline='pipeline_entity')
```


#### list(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None, project_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
List project pipelines.

**prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters


    * **project_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – project id



* **Returns**

    Paged entity



* **Return type**

    [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)


**Example**:

```python
pipelines = project.pipelines.list()
```


#### open_in_web(pipeline: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)] = None, pipeline_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, pipeline_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Open the pipeline in web platform.

**prerequisites**: Must be *owner* or *developer* to use this method.


* **Parameters**

    
    * **pipeline** ([*dtlpy.entities.pipeline.Pipeline*](entities.md#dtlpy.entities.pipeline.Pipeline)) – pipeline entity


    * **pipeline_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline id


    * **pipeline_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline name


**Example**:

```python
project.pipelines.open_in_web(pipeline_id='pipeline_id')
```


#### pause(pipeline: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)] = None)
Pause a pipeline.

**prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    **pipeline** ([*dtlpy.entities.pipeline.Pipeline*](entities.md#dtlpy.entities.pipeline.Pipeline)) – pipeline entity



* **Returns**

    Composition object


**Example**:

```python
project.pipelines.pause(pipeline='pipeline_entity')
```


#### reset(pipeline: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)] = None, pipeline_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, pipeline_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, stop_if_running: [bool](https://docs.python.org/3/library/functions.html#bool) = False)
Reset pipeline counters.

**prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **pipeline** ([*dtlpy.entities.pipeline.Pipeline*](entities.md#dtlpy.entities.pipeline.Pipeline)) – pipeline entity - optional


    * **pipeline_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline_id -  optional


    * **pipeline_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline_name -  optional


    * **stop_if_running** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – If the pipeline is installed it will stop the pipeline and reset the counters.



* **Returns**

    bool


**Example**:

```python
success = project.pipelines.reset(pipeline='pipeline_entity')
```


#### stats(pipeline: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)] = None, pipeline_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, pipeline_name: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Get pipeline counters.

**prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **pipeline** ([*dtlpy.entities.pipeline.Pipeline*](entities.md#dtlpy.entities.pipeline.Pipeline)) – pipeline entity - optional


    * **pipeline_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline_id -  optional


    * **pipeline_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline_name -  optional



* **Returns**

    PipelineStats



* **Return type**

    dtlpy.entities.pipeline.PipelineStats


**Example**:

```python
pipeline_stats = project.pipelines.stats(pipeline='pipeline_entity')
```


#### update(pipeline: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)] = None)
Update pipeline changes to platform.

**prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    **pipeline** ([*dtlpy.entities.pipeline.Pipeline*](entities.md#dtlpy.entities.pipeline.Pipeline)) – pipeline entity



* **Returns**

    Pipeline object



* **Return type**

    [dtlpy.entities.pipeline.Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)


**Example**:

```python
pipeline = project.pipelines.update(pipeline='pipeline_entity')
```

### Pipeline Executions


### _class_ PipelineExecutions(client_api: ApiClient, project: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Project](entities.md#dtlpy.entities.project.Project)] = None, pipeline: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Pipeline](entities.md#dtlpy.entities.pipeline.Pipeline)] = None)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

PipelineExecutions Repository

The PipelineExecutions class allows users to manage pipeline executions. See our documentation for more information on [pipelines](https://dataloop.ai/docs/pipelines-overview).


#### create(pipeline_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, execution_input=None)
Execute a pipeline and return the execute.

**prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **pipeline_id** – pipeline id


    * **execution_input** – list of the dl.FunctionIO or dict of pipeline input - example {‘item’: ‘item_id’}



* **Returns**

    entities.PipelineExecution object



* **Return type**

    [dtlpy.entities.pipeline_execution.PipelineExecution](entities.md#dtlpy.entities.pipeline_execution.PipelineExecution)


**Example**:

```python
pipeline_execution = pipeline.pipeline_executions.create(pipeline_id='pipeline_id', execution_input={'item': 'item_id'})
```


#### get(pipeline_execution_id: [str](https://docs.python.org/3/library/stdtypes.html#str), pipeline_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Get Pipeline Execution object

**prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    
    * **pipeline_execution_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline execution id


    * **pipeline_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – pipeline id



* **Returns**

    PipelineExecution object



* **Return type**

    [dtlpy.entities.pipeline_execution.PipelineExecution](entities.md#dtlpy.entities.pipeline_execution.PipelineExecution)


**Example**:

```python
pipeline_executions = pipeline.pipeline_executions.get(pipeline_id='pipeline_id')
```


#### list(filters: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[Filters](entities.md#dtlpy.entities.filters.Filters)] = None)
List project pipeline executions.

**prerequisites**: You must be an *owner* or *developer* to use this method.


* **Parameters**

    **filters** ([*dtlpy.entities.filters.Filters*](entities.md#dtlpy.entities.filters.Filters)) – Filters entity or a dictionary containing filters parameters



* **Returns**

    Paged entity



* **Return type**

    [dtlpy.entities.paged_entities.PagedEntities](entities.md#dtlpy.entities.paged_entities.PagedEntities)


**Example**:

```python
pipeline_executions = pipeline.pipeline_executions.list()
```

## General Commands


### _class_ Commands(client_api: ApiClient)
Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

Service Commands repository


#### abort(command_id: [str](https://docs.python.org/3/library/stdtypes.html#str))
Abort Command


* **Parameters**

    **command_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – command id



* **Returns**

    


#### get(command_id: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None, url: [Optional](https://docs.python.org/3/library/typing.html#typing.Optional)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = None)
Get Service command object


* **Parameters**

    
    * **command_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 


    * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – command url



* **Returns**

    Command object



#### list()
List of commands


* **Returns**

    list of commands



#### wait(command_id, timeout=0, step=None, url=None, backoff_factor=0.1)
Wait for command to finish

backoff_factor: A backoff factor to apply between attempts after the second try
{backoff factor} \* (2 \*\* ({number of total retries} - 1))
seconds. If the backoff_factor is 0.1, then `sleep()` will sleep
for [0.0s, 0.2s, 0.4s, …] between retries. It will never be longer
than 8 sec


* **Parameters**

    
    * **command_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Command id to wait to


    * **timeout** ([*int*](https://docs.python.org/3/library/functions.html#int)) – int, seconds to wait until TimeoutError is raised. if 0 - wait until done


    * **step** ([*int*](https://docs.python.org/3/library/functions.html#int)) – int, seconds between polling


    * **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – url to the command


    * **backoff_factor** ([*float*](https://docs.python.org/3/library/functions.html#float)) – A backoff factor to apply between attempts after the second try



* **Returns**

    Command  object


### Download Commands

### Upload Commands
