# Class: SDKFunctionExecution

[entities](./entities.md).SDKFunctionExecution

A representation of a function execution

## Table of contents

### Constructors

- [constructor](SDKFunctionExecution.md#constructor)

### Properties

- [app](SDKFunctionExecution.md#app)
- [createdAt](SDKFunctionExecution.md#createdat)
- [duration](SDKFunctionExecution.md#duration)
- [functionName](SDKFunctionExecution.md#functionname)
- [id](SDKFunctionExecution.md#id)
- [latestStatus](SDKFunctionExecution.md#lateststatus)
- [projectId](SDKFunctionExecution.md#projectid)
- [serviceId](SDKFunctionExecution.md#serviceid)
- [time](SDKFunctionExecution.md#time)

## Constructors

### constructor

• **new SDKFunctionExecution**(`execution?`)

Creates an instance of SDKFunctionExecution.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `execution?` | `Partial`<[`SDKFunctionExecution`](SDKFunctionExecution.md) | The execution to create |

## Properties

### app

• **app**: `string`

The app the function is associated with

___

### createdAt

• `Optional` **createdAt**: `Date`

The timestamp for when the function execution was created

___

### duration

• `Optional` **duration**: `number`

The duration of the function execution

___

### functionName

• **functionName**: `string`

The name of the function

___

### id

• `Optional` **id**: `string`

The unique identifier for the function execution

___

### latestStatus

• `Optional` **latestStatus**: `ExecutionStatusReport`

The latest status report for the function execution

___

### projectId

• `Optional` **projectId**: `string`

The unique identifier for the project associated with the function

___

### serviceId

• `Optional` **serviceId**: `string`

The unique identifier for the service associated with the function

___

### time

• `Optional` **time**: `Date`

The timestamp for the function execution
