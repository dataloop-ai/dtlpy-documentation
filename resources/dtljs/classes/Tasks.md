# Class: Tasks

[repositories](./repositories.md).Tasks

Tasks repository.

The Tasks class allows the user to manage tasks and their properties.

## Hierarchy

- [`Repository`](Repository.md)

  ↳ **`Tasks`**

## Implements

- [`IBundle`](../interfaces/IBundle.md)<[`SDKTask`](SDKTask.md)>

## Table of contents

### Constructors

- [constructor](Tasks.md#constructor)

### Methods

- [get](Tasks.md#get)

## Constructors

### constructor

• **new Tasks**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](Repository.md)
.[constructor](Repository.md#constructor)

## Methods

### get

▸ **get**(`taskId?`): `Promise`<[`SDKTask`](SDKTask.md)>

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

`Promise`<[`SDKTask`](SDKTask.md)>

- A promise that resolves to the retrieved task.
