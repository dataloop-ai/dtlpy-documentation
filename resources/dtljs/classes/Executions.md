# Class: Executions

[repositories](./repositories.md).Executions

Executions repository.

The Executions class allows the user to manage executions and their properties.

## Hierarchy

- [`Repository`](Repository.md)

  ↳ **`Executions`**

## Implements

- [`IBundle`](../interfaces/IBundle.md)<`SDKExecution`>

## Table of contents

### Constructors

- [constructor](Executions.md#constructor)

### Methods

- [create](Executions.md#create)
- [get](Executions.md#get)

## Constructors

### constructor

• **new Executions**(`agent`)

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

▸ **create**(`payload`): `Promise`<`SDKExecution`>

Creates a new execution.

**`Example`**

```ts
const execution = await dl.executions.create({
    functionName: 'My Function',
    serviceName: 'My Service',
    input: { dataset_id: 'datasetId-123', name: 'My first input' },
})
```

* To receive updates on the execution status, subscribe to the `DlEvent.EXECUTION_STATUS` event, which is triggered upon creation, success, and failure.
```typescript
await dl.on(DlEvent.EXECUTION_STATUS, (payload: { execution: SDKExecution, status: 'created' | 'success' | 'failed' }) => {
    console.log(`Execution ${payload.execution.id} status: ${payload.status}`)
    console.log(`Execution output`, payload.execution.output)
})
```
#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | [`SDKExecutionPayload`](../interfaces/SDKExecutionPayload.md) | An object containing the execution's payload. |

#### Returns

`Promise`<`SDKExecution`>

- A promise that resolves to the created execution.

___

### get

▸ **get**(`executionId`): `Promise`<`SDKExecution`>

Retrieves an execution.

**`Example`**

```ts
const execution = await dl.executions.get('executionId-123')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `executionId` | `string` | The execution's id. |

#### Returns

`Promise`<`SDKExecution`>

- A promise that resolves to the execution.
