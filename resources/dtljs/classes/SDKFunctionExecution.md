# Class: SDKFunctionExecution

[sdkApi/interfaces/entities/iExecution](../modules/sdkApi_interfaces_entities_iExecution.md).SDKFunctionExecution

A representation of a function execution

## Table of contents

### Constructors

- [constructor](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md#constructor)

### Properties

- [app](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md#app)
- [createdAt](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md#createdat)
- [duration](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md#duration)
- [functionName](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md#functionname)
- [id](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md#id)
- [latestStatus](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md#lateststatus)
- [projectId](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md#projectid)
- [serviceId](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md#serviceid)
- [time](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md#time)

## Constructors

### constructor

• **new SDKFunctionExecution**(`execution?`)

Creates an instance of SDKFunctionExecution.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `execution?` | `Partial`<[`SDKFunctionExecution`](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md)\> | The execution to create |

## Properties

### app

• **app**: `string`

The name of the app the function is associated with

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
