# Interface: ITask

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

- [clientId](ITask.md#clientid)
- [updatedBy](ITask.md#updatedby)
- [id](ITask.md#id)
- [creator](ITask.md#creator)
- [taskOwner](ITask.md#taskowner)
- [createdAt](ITask.md#createdat)
- [updatedAt](ITask.md#updatedat)
- [datasetId](ITask.md#datasetid)
- [recipeId](ITask.md#recipeid)
- [projectId](ITask.md#projectid)
- [hasParent](ITask.md#hasparent)
- [name](ITask.md#name)
- [dueDate](ITask.md#duedate)
- [query](ITask.md#query)
- [status](ITask.md#status)
- [assignmentIds](ITask.md#assignmentids)
- [metadata](ITask.md#metadata)
- [itemStatus](ITask.md#itemstatus)
- [spec](ITask.md#spec)
- [progress](ITask.md#progress)
- [forReview](ITask.md#forreview)
- [issues](ITask.md#issues)
- [error](ITask.md#error)
- [availableActions](ITask.md#availableactions)
- [priority](ITask.md#priority)

## Properties

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

### id

• **id**: `string`

The unique identifier of the task.

#### Overrides

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### creator

• **creator**: `string`

The creator of the task.

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### taskOwner

• **taskOwner**: `string`

The owner of the task.

___

### createdAt

• **createdAt**: `Date`

The date and time when the task was created.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### updatedAt

• **updatedAt**: `Date`

The date and time when the task was last updated.

#### Overrides

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the task belongs to.

___

### recipeId

• **recipeId**: `string`

The ID of the recipe associated with the task.

___

### projectId

• **projectId**: `string`

The ID of the project the task belongs to.

___

### hasParent

• **hasParent**: `boolean`

Whether the task has a parent task.

___

### name

• **name**: `string`

The name of the task.

___

### dueDate

• **dueDate**: `number`

The due date of the task.

___

### query

• **query**: `string`

The query associated with the task.

___

### status

• **status**: `string`

The status of the task.

___

### assignmentIds

• **assignmentIds**: `string`[]

The IDs of the assignments associated with the task.

___

### metadata

• `Optional` **metadata**: `any`

The task's metadata.

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

### spec

• **spec**: `any`

The task's spec.

___

### progress

• **progress**: `number`

The progress of the task.

___

### forReview

• **forReview**: `number`

The number of items that need to be reviewed.

___

### issues

• **issues**: `number`

The number of issues associated with the task.

___

### error

• `Optional` **error**: `any`

Task error.

___

### availableActions

• `Optional` **availableActions**: `any`[]

Available actions for the task.

___

### priority

• `Optional` **priority**: `number`

Task priority.
