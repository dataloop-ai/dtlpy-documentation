# Class: Executions

[appLib/SDKDrivers/xFrameDriver/executions](../modules/appLib_SDKDrivers_xFrameDriver_executions.md).Executions

Executions repository.

The Executions class allows the user to manage executions and their properties.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Executions`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<`SDKExecution`\>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_executions.Executions.md#constructor)

### Methods

- [create](appLib_SDKDrivers_xFrameDriver_executions.Executions.md#create)
- [crudReq](appLib_SDKDrivers_xFrameDriver_executions.Executions.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_executions.Executions.md#crudreqsync)
- [get](appLib_SDKDrivers_xFrameDriver_executions.Executions.md#get)

## Constructors

### constructor

• **new Executions**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### create

▸ **create**(`payload`): `Promise`<`SDKExecution`\>

Creates a new execution.

**`Example`**

const execution = await dl.executions.create({
 functionName: 'My Function',
 serviceName: 'My Service',
 input: { dataset_id: 'datasetId-123', name: 'My first input' },
})

To receive updates on the execution status, subscribe to the `DlEvent.EXECUTION_STATUS` event, which is triggered upon creation, success, and failure.

**`Example`**

await dl.on(DlEvent.EXECUTION_STATUS, (payload: { execution: SDKExecution, status: 'created' | 'success' | 'failed' }) => {
    console.log(`Execution ${payload.execution.id} status: ${payload.status}`)
    console.log(`Execution output`, payload.execution.output)
})

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | [`SDKExecutionPayload`](../interfaces/sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md) | An object containing the execution's payload. |

#### Returns

`Promise`<`SDKExecution`\>

- A promise that resolves to the created execution.

#### Implementation of

IBundle.create

___

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

▸ **get**(`executionId`): `Promise`<`SDKExecution`\>

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

`Promise`<`SDKExecution`\>

- A promise that resolves to the execution.

#### Implementation of

IBundle.get
