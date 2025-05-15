# Class: SDKTask

A class representing a Task object.

**`Implements`**

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

#### Implementation of

[ITask](../interfaces/ITask.md).[assignmentIds](../interfaces/ITask.md#assignmentids)

___

### createdAt

• **createdAt**: `Date`

The date and time when the task was created.

#### Implementation of

[ITask](../interfaces/ITask.md).[createdAt](../interfaces/ITask.md#createdat)

___

### creator

• **creator**: `string`

The creator of the task.

#### Implementation of

[ITask](../interfaces/ITask.md).[creator](../interfaces/ITask.md#creator)

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the task belongs to.

#### Implementation of

[ITask](../interfaces/ITask.md).[datasetId](../interfaces/ITask.md#datasetid)

___

### dueDate

• **dueDate**: `number`

The due date of the task.

#### Implementation of

[ITask](../interfaces/ITask.md).[dueDate](../interfaces/ITask.md#duedate)

___

### forReview

• **forReview**: `number`

The number of items that need to be reviewed.

#### Implementation of

[ITask](../interfaces/ITask.md).[forReview](../interfaces/ITask.md#forreview)

___

### hasParent

• **hasParent**: `boolean`

Whether the task has a parent task.

#### Implementation of

[ITask](../interfaces/ITask.md).[hasParent](../interfaces/ITask.md#hasparent)

___

### id

• **id**: `string`

The unique identifier of the task.

#### Implementation of

[ITask](../interfaces/ITask.md).[id](../interfaces/ITask.md#id)

___

### issues

• **issues**: `number`

The number of issues associated with the task.

#### Implementation of

[ITask](../interfaces/ITask.md).[issues](../interfaces/ITask.md#issues)

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

#### Implementation of

[ITask](../interfaces/ITask.md).[itemStatus](../interfaces/ITask.md#itemstatus)

___

### name

• **name**: `string`

The name of the task.

#### Implementation of

[ITask](../interfaces/ITask.md).[name](../interfaces/ITask.md#name)

___

### progress

• **progress**: `number`

The progress of the task.

#### Implementation of

[ITask](../interfaces/ITask.md).[progress](../interfaces/ITask.md#progress)

___

### projectId

• **projectId**: `string`

The ID of the project the task belongs to.

#### Implementation of

[ITask](../interfaces/ITask.md).[projectId](../interfaces/ITask.md#projectid)

___

### query

• **query**: `string`

The query associated with the task.

#### Implementation of

[ITask](../interfaces/ITask.md).[query](../interfaces/ITask.md#query)

___

### recipeId

• **recipeId**: `string`

The ID of the recipe associated with the task.

#### Implementation of

[ITask](../interfaces/ITask.md).[recipeId](../interfaces/ITask.md#recipeid)

___

### spec

• **spec**: `any`

The task's spec.

#### Implementation of

[ITask](../interfaces/ITask.md).[spec](../interfaces/ITask.md#spec)

___

### status

• **status**: `string`

The status of the task.

#### Implementation of

[ITask](../interfaces/ITask.md).[status](../interfaces/ITask.md#status)

___

### taskOwner

• **taskOwner**: `string`

The task owner.

#### Implementation of

[ITask](../interfaces/ITask.md).[taskOwner](../interfaces/ITask.md#taskowner)

___

### updatedAt

• **updatedAt**: `Date`

The date and time when the task was last updated.

#### Implementation of

[ITask](../interfaces/ITask.md).[updatedAt](../interfaces/ITask.md#updatedat)
