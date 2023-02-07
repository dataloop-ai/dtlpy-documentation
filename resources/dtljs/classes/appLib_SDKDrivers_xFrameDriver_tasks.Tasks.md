# Class: Tasks

[dl.repositories](./index.md).Tasks

Tasks repository.

The Tasks class allows the user to manage tasks and their properties.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Tasks`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<[`SDKTask`](sdkApi_interfaces_entities_iTask.SDKTask.md)>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md#constructor)

### Methods

- [crudReq](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md#crudreqsync)
- [get](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md#get)

## Constructors

### constructor

• **new Tasks**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)
.[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### get

▸ **get**(`taskId?`): `Promise`<[`SDKTask`](sdkApi_interfaces_entities_iTask.SDKTask.md)>

Retrieves a task.

If the task id is not provided, the active task is returned.

**`Example`**

```ts
const activeTask = await dl.tasks.get()
```

**`Example`**

```ts
const task = await dl.tasks.get('taskId-123')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `taskId?` | `string` | The id of the task to be retrieved. |

#### Returns

`Promise`<[`SDKTask`](sdkApi_interfaces_entities_iTask.SDKTask.md)>

- A promise that resolves to the retrieved task.
