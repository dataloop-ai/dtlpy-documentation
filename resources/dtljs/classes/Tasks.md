# Class: Tasks

[appLib/SDKDrivers/xFrameDriver/tasks](../modules/appLib_SDKDrivers_xFrameDriver_tasks.md).Tasks

Tasks repository.

The Tasks class allows the user to manage tasks and their properties.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Tasks`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<[`SDKTask`](sdkApi_interfaces_entities_iTask.SDKTask.md)\>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md#constructor)

### Methods

- [crudReq](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md#crudreqsync)
- [get](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md#get)
- [updateAssignees](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md#updateassignees)

## Constructors

### constructor

• **new Tasks**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### crudReq

▸ **crudReq**(`data`): `void`

Sends a CRUD request to the xFrame.

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `any` |

#### Returns

`void`

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[crudReq](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#crudreq)

___

### crudReqSync

▸ **crudReqSync**(`data`, `options?`): `Promise`<`any`\>

Sends a CRUD request to the xFrame.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `data` | `any` | The data to send. |
| `options` | `Object` |  |
| `options.timeout?` | `number` | an option to set the timeout for the request. |

#### Returns

`Promise`<`any`\>

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[crudReqSync](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#crudreqsync)

___

### get

▸ **get**(`taskId?`): `Promise`<[`SDKTask`](sdkApi_interfaces_entities_iTask.SDKTask.md)\>

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

`Promise`<[`SDKTask`](sdkApi_interfaces_entities_iTask.SDKTask.md)\>

- A promise that resolves to the retrieved task.

#### Implementation of

IBundle.get

___

### updateAssignees

▸ **updateAssignees**(`payload`): `Promise`<[`SDKTask`](sdkApi_interfaces_entities_iTask.SDKTask.md)\>

Updates the assignees of a task.

**`Example`**

```ts
const task = await dl.tasks.updateAssignees({
   taskId: 'taskId-123',
   action: 'add',
   assignees: ['test@dataloop.ai']
})
```

**`Example`**

```ts
const task = await dl.tasks.updateAssignees({
  taskId: 'taskId-123',
  action: 'remove',
  assignees: ['test@dataloop.ai']
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | [`SDKUpdateTaskAssigneesPayload`](../interfaces/sdkApi_interfaces_entities_iTask.SDKUpdateTaskAssigneesPayload.md) | The payload of the update assignees request. |

#### Returns

`Promise`<[`SDKTask`](sdkApi_interfaces_entities_iTask.SDKTask.md)\>

- A promise that resolves to the updated task.
