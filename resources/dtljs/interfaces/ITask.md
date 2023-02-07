# Interface: ITask

[interfaces](./index.md).ITask

An interface representing a Task object, extending the IEntity interface.

**`Interface`**

ITask

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`ITask`**

## Implemented by

- [`SDKTask`](../classes/SDKTask.md)

## Table of contents

### Properties

- [assignmentIds](ITask.md#assignmentids)
- [availableActions](ITask.md#availableactions)
- [clientId](ITask.md#clientid)
- [createdAt](ITask.md#createdat)
- [creator](ITask.md#creator)
- [datasetId](ITask.md#datasetid)
- [dueDate](ITask.md#duedate)
- [error](ITask.md#error)
- [forReview](ITask.md#forreview)
- [hasParent](ITask.md#hasparent)
- [id](ITask.md#id)
- [issues](ITask.md#issues)
- [itemStatus](ITask.md#itemstatus)
- [metadata](ITask.md#metadata)
- [name](ITask.md#name)
- [priority](ITask.md#priority)
- [progress](ITask.md#progress)
- [projectId](ITask.md#projectid)
- [query](ITask.md#query)
- [recipeId](ITask.md#recipeid)
- [spec](ITask.md#spec)
- [status](ITask.md#status)
- [taskOwner](ITask.md#taskowner)
- [updatedAt](ITask.md#updatedat)
- [updatedBy](ITask.md#updatedby)

## Properties

### assignmentIds

• **assignmentIds**: `string`[]

The IDs of the assignments associated with the task.

___

### availableActions

• `Optional` **availableActions**: `any`[]

Available actions for the task.

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### createdAt

• **createdAt**: `Date`

The date and time when the task was created.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### creator

• **creator**: `string`

The creator of the task.

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the task belongs to.

___

### dueDate

• **dueDate**: `number`

The due date of the task.

___

### error

• `Optional` **error**: `any`

Task error.

___

### forReview

• **forReview**: `number`

The number of items that need to be reviewed.

___

### hasParent

• **hasParent**: `boolean`

Whether the task has a parent task.

___

### id

• **id**: `string`

The unique identifier of the task.

#### Overrides

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### issues

• **issues**: `number`

The number of issues associated with the task.

___

### itemStatus

• **itemStatus**: `Object`

The status of the items associated with the task.

#### Type declaration

| Name | Type |
| :------ | :------ |
| `approved?` | `number` |
| `completed?` | `number` |
| `remaining` | `number` |

___

### metadata

• `Optional` **metadata**: `any`

The task's metadata.

___

### name

• **name**: `string`

The name of the task.

___

### priority

• `Optional` **priority**: `number`

Task priority.

___

### progress

• **progress**: `number`

The progress of the task.

___

### projectId

• **projectId**: `string`

The ID of the project the task belongs to.

___

### query

• **query**: `string`

The query associated with the task.

___

### recipeId

• **recipeId**: `string`

The ID of the recipe associated with the task.

___

### spec

• **spec**: `any`

The task's spec.

___

### status

• **status**: `string`

The status of the task.

___

### taskOwner

• **taskOwner**: `string`

The owner of the task.

___

### updatedAt

• **updatedAt**: `Date`

The date and time when the task was last updated.

#### Overrides

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)
