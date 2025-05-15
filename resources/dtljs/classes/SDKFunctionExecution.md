# Class: SDKFunctionExecution

A representation of a function execution

## Table of contents

### Properties

- [app](SDKFunctionExecution.md#app)
- [functionName](SDKFunctionExecution.md#functionname)
- [latestStatus](SDKFunctionExecution.md#lateststatus)
- [time](SDKFunctionExecution.md#time)
- [id](SDKFunctionExecution.md#id)
- [createdAt](SDKFunctionExecution.md#createdat)
- [duration](SDKFunctionExecution.md#duration)
- [serviceId](SDKFunctionExecution.md#serviceid)
- [projectId](SDKFunctionExecution.md#projectid)

### Constructors

- [constructor](SDKFunctionExecution.md#constructor)

## Properties

### app

• **app**: `string`

The name of the app the function is associated with

___

### functionName

• **functionName**: `string`

The name of the function

___

### latestStatus

• `Optional` **latestStatus**: `ExecutionStatusReport`

The latest status report for the function execution

___

### time

• `Optional` **time**: `Date`

The timestamp for the function execution

___

### id

• `Optional` **id**: `string`

The unique identifier for the function execution

___

### createdAt

• `Optional` **createdAt**: `Date`

The timestamp for when the function execution was created

___

### duration

• `Optional` **duration**: `number`

The duration of the function execution

___

### serviceId

• `Optional` **serviceId**: `string`

The unique identifier for the service associated with the function

___

### projectId

• `Optional` **projectId**: `string`

The unique identifier for the project associated with the function

## Constructors

### constructor

• **new SDKFunctionExecution**(`execution?`)

Creates an instance of SDKFunctionExecution.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `execution?` | `Partial`<[`SDKFunctionExecution`](SDKFunctionExecution.md)\> | The execution to create |
