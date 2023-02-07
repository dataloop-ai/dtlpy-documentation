# Class: Projects

[dl.repositories](./index.md).Projects

Projects repository.

The Projects class allows the user to manage projects and their properties.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Projects`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<[`SDKProject`](sdkApi_interfaces_entities_iProject.SDKProject.md)>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_projects.Projects.md#constructor)

### Methods

- [create](appLib_SDKDrivers_xFrameDriver_projects.Projects.md#create)
- [crudReq](appLib_SDKDrivers_xFrameDriver_projects.Projects.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_projects.Projects.md#crudreqsync)
- [delete](appLib_SDKDrivers_xFrameDriver_projects.Projects.md#delete)
- [get](appLib_SDKDrivers_xFrameDriver_projects.Projects.md#get)
- [query](appLib_SDKDrivers_xFrameDriver_projects.Projects.md#query)
- [update](appLib_SDKDrivers_xFrameDriver_projects.Projects.md#update)

## Constructors

### constructor

• **new Projects**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)
.[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### create

▸ **create**(`payload`): `Promise`<[`SDKProject`](sdkApi_interfaces_entities_iProject.SDKProject.md)>

Creates a new project.

**`Example`**

```ts
const project = await dl.projects.create({
    name: 'My Project'
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Object` | An object containing the project's name. |
| `payload.name` | `string` | The name of the project to be created. |

#### Returns

`Promise`<[`SDKProject`](sdkApi_interfaces_entities_iProject.SDKProject.md)>

- A promise that resolves to the created project.

___

### delete

▸ **delete**(`projectId`): `Promise`<`void`>

Deletes a project.

**`Example`**

```ts
await dl.projects.delete('projectId-123')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `projectId` | `string` | The id of the project to be deleted. |

#### Returns

`Promise`<`void`>

- A promise that resolves when the project is deleted.

___

### get

▸ **get**(`projectId?`): `Promise`<[`SDKProject`](sdkApi_interfaces_entities_iProject.SDKProject.md)>

Gets a project by project id.

If the project id is not provided, the active project is returned.

**`Example`**

```ts
const projectById = await dl.projects.get('projectId-123')
const activeProject = await dl.projects.get()
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `projectId?` | `string` | The id of the project to be retrieved. |

#### Returns

`Promise`<[`SDKProject`](sdkApi_interfaces_entities_iProject.SDKProject.md)>

- A promise that resolves to the project.

#### Implementation of

IBundle.get

___

### query

▸ **
query**(): `Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<[`SDKProject`](sdkApi_interfaces_entities_iProject.SDKProject.md)>>

Lists all projects.

**`Example`**

```ts
const pagedResponse = await dl.projects.query()
const projects = pagedResponse.items
```

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<[`SDKProject`](sdkApi_interfaces_entities_iProject.SDKProject.md)>>

- Returns a Promise that resolves to a paged response object of projects.

#### Implementation of

IBundle.query

___

### update

▸ **update**(`payload`): `Promise`<[`SDKProject`](sdkApi_interfaces_entities_iProject.SDKProject.md)>

Updates a project.

**`Example`**

```ts
const project = await dl.projects.update({
    id: 'projectId-123',
    name: 'New Project Name'
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Object` | An object containing the project's id and name. |
| `payload.id` | `string` | The id of the project to be updated. |
| `payload.name` | `string` | The new name of the project. |

#### Returns

`Promise`<[`SDKProject`](sdkApi_interfaces_entities_iProject.SDKProject.md)>

- A promise that resolves to the updated project.

#### Implementation of

IBundle.update
