# Class: SDKTask

[entities](./entities.md).SDKTask

A class representing a Task object.

## Implements

- [`ITask`](../interfaces/ITask.md)

## Table of contents

### Constructors

- [constructor](SDKTask.md#constructor)

### Properties

- [assignmentIds](SDKTask.md#assignmentids)
- [createdAt](SDKTask.md#createdat)
- [creator](SDKTask.md#creator)
- [datasetId](SDKTask.md#datasetid)
- [dueDate](SDKTask.md#duedate)
- [forReview](SDKTask.md#forreview)
- [hasParent](SDKTask.md#hasparent)
- [id](SDKTask.md#id)
- [issues](SDKTask.md#issues)
- [itemStatus](SDKTask.md#itemstatus)
- [name](SDKTask.md#name)
- [progress](SDKTask.md#progress)
- [projectId](SDKTask.md#projectid)
- [query](SDKTask.md#query)
- [recipeId](SDKTask.md#recipeid)
- [spec](SDKTask.md#spec)
- [status](SDKTask.md#status)
- [taskOwner](SDKTask.md#taskowner)
- [updatedAt](SDKTask.md#updatedat)

## Constructors

### constructor

• **new SDKTask**(`task`)

Creates an instance of SDKTask.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `task` | `any` | The task object. |

## Properties

### assignmentIds

• **assignmentIds**: `string`[]

The IDs of the assignments associated with the task.

___

### createdAt

• **createdAt**: `Date`

The date and time when the task was created.

___

### creator

• **creator**: `string`

The creator of the task.

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the task belongs to.

___

### dueDate

• **dueDate**: `number`

The due date of the task.

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

### name

• **name**: `string`

The name of the task.

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

The task owner.

___

### updatedAt

• **updatedAt**: `Date`

The date and time when the task was last updated.
