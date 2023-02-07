# Class: Projects

[repositories](./repositories.md).Projects

Projects repository.

The Projects class allows the user to manage projects and their properties.

## Hierarchy

- [`Repository`](Repository.md)

  ↳ **`Projects`**

## Implements

- [`IBundle`](../interfaces/IBundle.md)<[`SDKProject`](SDKProject.md)>

## Table of contents

### Constructors

- [constructor](Projects.md#constructor)

### Methods

- [create](Projects.md#create)
- [delete](Projects.md#delete)
- [get](Projects.md#get)
- [query](Projects.md#query)
- [update](Projects.md#update)

## Constructors

### constructor

• **new Projects**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](Repository.md)
.[constructor](Repository.md#constructor)

## Methods

### create

▸ **create**(`payload`): `Promise`<[`SDKProject`](SDKProject.md)>

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

`Promise`<[`SDKProject`](SDKProject.md)>

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

▸ **get**(`projectId?`): `Promise`<[`SDKProject`](SDKProject.md)>

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

`Promise`<[`SDKProject`](SDKProject.md)>

- A promise that resolves to the project.

#### Implementation of

IBundle.get

___

### query

▸ **query**(): `Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKProject`](SDKProject.md)>>

Lists all projects.

**`Example`**

```ts
const pagedResponse = await dl.projects.query()
const projects = pagedResponse.items
```

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKProject`](SDKProject.md)>>

- Returns a Promise that resolves to a paged response object of projects.

#### Implementation of

IBundle.query

___

### update

▸ **update**(`payload`): `Promise`<[`SDKProject`](SDKProject.md)>

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

`Promise`<[`SDKProject`](SDKProject.md)>

- A promise that resolves to the updated project.

#### Implementation of

IBundle.update
