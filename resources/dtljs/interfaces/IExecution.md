# Interface: IExecution

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IExecution`**

## Implemented by

- [`SDKExecution`](../classes/SDKExecution.md)

## Table of contents

### Properties

- [id](IExecution.md#id)
- [clientId](IExecution.md#clientid)
- [updatedBy](IExecution.md#updatedby)
- [createdAt](IExecution.md#createdat)
- [updatedAt](IExecution.md#updatedat)
- [creator](IExecution.md#creator)
- [attempts](IExecution.md#attempts)
- [maxAttempts](IExecution.md#maxattempts)
- [toTerminate](IExecution.md#toterminate)
- [input](IExecution.md#input)
- [output](IExecution.md#output)
- [feedbackQueue](IExecution.md#feedbackqueue)
- [status](IExecution.md#status)
- [statusLog](IExecution.md#statuslog)
- [latestStatus](IExecution.md#lateststatus)
- [duration](IExecution.md#duration)
- [projectId](IExecution.md#projectid)
- [functionName](IExecution.md#functionname)
- [serviceId](IExecution.md#serviceid)
- [triggerId](IExecution.md#triggerid)
- [serviceName](IExecution.md#servicename)
- [packageId](IExecution.md#packageid)
- [packageName](IExecution.md#packagename)
- [packageRevision](IExecution.md#packagerevision)
- [serviceVersion](IExecution.md#serviceversion)
- [pipeline](IExecution.md#pipeline)

## Properties

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Inherited from

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)

___

### createdAt

• **createdAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was created.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### updatedAt

• **updatedAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was last updated.

#### Overrides

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### creator

• **creator**: `string`

The creator of the Entity.

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### attempts

• **attempts**: `number`

___

### maxAttempts

• **maxAttempts**: `number`

___

### toTerminate

• **toTerminate**: `boolean`

___

### input

• **input**: `Dictionary`

___

### output

• `Optional` **output**: `Dictionary`

___

### feedbackQueue

• **feedbackQueue**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `exchange` | `string` |
| `routing` | `string` |

___

### status

• **status**: `ExecutionStatusReport`[]

___

### statusLog

• **statusLog**: `ExecutionStatusReport`[]

___

### latestStatus

• **latestStatus**: `ExecutionStatusReport`

___

### duration

• **duration**: `number`

___

### projectId

• **projectId**: `string`

___

### functionName

• `Optional` **functionName**: `string`

___

### serviceId

• **serviceId**: `string`

___

### triggerId

• `Optional` **triggerId**: `string`

___

### serviceName

• `Optional` **serviceName**: `string`

___

### packageId

• **packageId**: `string`

___

### packageName

• **packageName**: `string`

___

### packageRevision

• **packageRevision**: `number`

___

### serviceVersion

• **serviceVersion**: `number`

___

### pipeline

• `Optional` **pipeline**: `ExecutionPipelineStateReference`
