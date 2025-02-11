# Class: SDKExecution

An interface representing an Entity object.

**`Interface`**

IEntity

## Implements

- [`IExecution`](../interfaces/IExecution.md)

## Table of contents

### Constructors

- [constructor](SDKExecution.md#constructor)

### Properties

- [attempts](SDKExecution.md#attempts)
- [createdAt](SDKExecution.md#createdat)
- [creator](SDKExecution.md#creator)
- [duration](SDKExecution.md#duration)
- [feedbackQueue](SDKExecution.md#feedbackqueue)
- [id](SDKExecution.md#id)
- [input](SDKExecution.md#input)
- [latestStatus](SDKExecution.md#lateststatus)
- [maxAttempts](SDKExecution.md#maxattempts)
- [packageId](SDKExecution.md#packageid)
- [packageName](SDKExecution.md#packagename)
- [packageRevision](SDKExecution.md#packagerevision)
- [projectId](SDKExecution.md#projectid)
- [serviceId](SDKExecution.md#serviceid)
- [serviceVersion](SDKExecution.md#serviceversion)
- [status](SDKExecution.md#status)
- [statusLog](SDKExecution.md#statuslog)
- [toTerminate](SDKExecution.md#toterminate)
- [updatedAt](SDKExecution.md#updatedat)

## Constructors

### constructor

• **new SDKExecution**(`execution`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `execution` | `Partial`<[`SDKExecution`](SDKExecution.md)\> |

## Properties

### attempts

• **attempts**: `number`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[attempts](../interfaces/IExecution.md#attempts)

___

### createdAt

• **createdAt**: `Date`

The date and time when the Entity was created.

#### Implementation of

[IExecution](../interfaces/IExecution.md).[createdAt](../interfaces/IExecution.md#createdat)

___

### creator

• **creator**: `string`

The creator of the Entity.

#### Implementation of

[IExecution](../interfaces/IExecution.md).[creator](../interfaces/IExecution.md#creator)

___

### duration

• **duration**: `number`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[duration](../interfaces/IExecution.md#duration)

___

### feedbackQueue

• **feedbackQueue**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `exchange` | `string` |
| `routing` | `string` |

#### Implementation of

[IExecution](../interfaces/IExecution.md).[feedbackQueue](../interfaces/IExecution.md#feedbackqueue)

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Implementation of

[IExecution](../interfaces/IExecution.md).[id](../interfaces/IExecution.md#id)

___

### input

• **input**: `Dictionary`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[input](../interfaces/IExecution.md#input)

___

### latestStatus

• **latestStatus**: `ExecutionStatusReport`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[latestStatus](../interfaces/IExecution.md#lateststatus)

___

### maxAttempts

• **maxAttempts**: `number`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[maxAttempts](../interfaces/IExecution.md#maxattempts)

___

### packageId

• **packageId**: `string`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[packageId](../interfaces/IExecution.md#packageid)

___

### packageName

• **packageName**: `string`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[packageName](../interfaces/IExecution.md#packagename)

___

### packageRevision

• **packageRevision**: `number`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[packageRevision](../interfaces/IExecution.md#packagerevision)

___

### projectId

• **projectId**: `string`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[projectId](../interfaces/IExecution.md#projectid)

___

### serviceId

• **serviceId**: `string`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[serviceId](../interfaces/IExecution.md#serviceid)

___

### serviceVersion

• **serviceVersion**: `number`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[serviceVersion](../interfaces/IExecution.md#serviceversion)

___

### status

• **status**: `ExecutionStatusReport`[]

#### Implementation of

[IExecution](../interfaces/IExecution.md).[status](../interfaces/IExecution.md#status)

___

### statusLog

• **statusLog**: `ExecutionStatusReport`[]

#### Implementation of

[IExecution](../interfaces/IExecution.md).[statusLog](../interfaces/IExecution.md#statuslog)

___

### toTerminate

• **toTerminate**: `boolean`

#### Implementation of

[IExecution](../interfaces/IExecution.md).[toTerminate](../interfaces/IExecution.md#toterminate)

___

### updatedAt

• **updatedAt**: `Date`

The date and time when the Entity was last updated.

#### Implementation of

[IExecution](../interfaces/IExecution.md).[updatedAt](../interfaces/IExecution.md#updatedat)
