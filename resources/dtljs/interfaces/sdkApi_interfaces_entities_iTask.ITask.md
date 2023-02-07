# Interface: ITask

[interfaces](./index.md).ITask

An interface representing a Task object, extending the IEntity interface.

**`Interface`**

ITask

## Hierarchy

- [`IEntity`](sdkApi_interfaces_entities_base.IEntity.md)

  ↳ **`ITask`**

## Implemented by

- [`SDKTask`](../classes/sdkApi_interfaces_entities_iTask.SDKTask.md)

## Table of contents

### Properties

- [assignmentIds](sdkApi_interfaces_entities_iTask.ITask.md#assignmentids)
- [availableActions](sdkApi_interfaces_entities_iTask.ITask.md#availableactions)
- [clientId](sdkApi_interfaces_entities_iTask.ITask.md#clientid)
- [createdAt](sdkApi_interfaces_entities_iTask.ITask.md#createdat)
- [creator](sdkApi_interfaces_entities_iTask.ITask.md#creator)
- [datasetId](sdkApi_interfaces_entities_iTask.ITask.md#datasetid)
- [dueDate](sdkApi_interfaces_entities_iTask.ITask.md#duedate)
- [error](sdkApi_interfaces_entities_iTask.ITask.md#error)
- [forReview](sdkApi_interfaces_entities_iTask.ITask.md#forreview)
- [hasParent](sdkApi_interfaces_entities_iTask.ITask.md#hasparent)
- [id](sdkApi_interfaces_entities_iTask.ITask.md#id)
- [issues](sdkApi_interfaces_entities_iTask.ITask.md#issues)
- [itemStatus](sdkApi_interfaces_entities_iTask.ITask.md#itemstatus)
- [metadata](sdkApi_interfaces_entities_iTask.ITask.md#metadata)
- [name](sdkApi_interfaces_entities_iTask.ITask.md#name)
- [priority](sdkApi_interfaces_entities_iTask.ITask.md#priority)
- [progress](sdkApi_interfaces_entities_iTask.ITask.md#progress)
- [projectId](sdkApi_interfaces_entities_iTask.ITask.md#projectid)
- [query](sdkApi_interfaces_entities_iTask.ITask.md#query)
- [recipeId](sdkApi_interfaces_entities_iTask.ITask.md#recipeid)
- [spec](sdkApi_interfaces_entities_iTask.ITask.md#spec)
- [status](sdkApi_interfaces_entities_iTask.ITask.md#status)
- [taskOwner](sdkApi_interfaces_entities_iTask.ITask.md#taskowner)
- [updatedAt](sdkApi_interfaces_entities_iTask.ITask.md#updatedat)
- [updatedBy](sdkApi_interfaces_entities_iTask.ITask.md#updatedby)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[clientId](sdkApi_interfaces_entities_base.IEntity.md#clientid)

___

### createdAt

• **createdAt**: `Date`

The date and time when the task was created.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[createdAt](sdkApi_interfaces_entities_base.IEntity.md#createdat)

___

### creator

• **creator**: `string`

The creator of the task.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[creator](sdkApi_interfaces_entities_base.IEntity.md#creator)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[id](sdkApi_interfaces_entities_base.IEntity.md#id)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedAt](sdkApi_interfaces_entities_base.IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedBy](sdkApi_interfaces_entities_base.IEntity.md#updatedby)
