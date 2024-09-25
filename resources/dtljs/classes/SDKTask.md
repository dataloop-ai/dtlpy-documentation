# Class: SDKTask

[sdkApi/interfaces/entities/iTask](../modules/sdkApi_interfaces_entities_iTask.md).SDKTask

A class representing a Task object.

**`Implements`**

## Implements

- [`ITask`](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md)

## Table of contents

### Constructors

- [constructor](sdkApi_interfaces_entities_iTask.SDKTask.md#constructor)

### Properties

- [assignmentIds](sdkApi_interfaces_entities_iTask.SDKTask.md#assignmentids)
- [createdAt](sdkApi_interfaces_entities_iTask.SDKTask.md#createdat)
- [creator](sdkApi_interfaces_entities_iTask.SDKTask.md#creator)
- [datasetId](sdkApi_interfaces_entities_iTask.SDKTask.md#datasetid)
- [dueDate](sdkApi_interfaces_entities_iTask.SDKTask.md#duedate)
- [forReview](sdkApi_interfaces_entities_iTask.SDKTask.md#forreview)
- [hasParent](sdkApi_interfaces_entities_iTask.SDKTask.md#hasparent)
- [id](sdkApi_interfaces_entities_iTask.SDKTask.md#id)
- [issues](sdkApi_interfaces_entities_iTask.SDKTask.md#issues)
- [itemStatus](sdkApi_interfaces_entities_iTask.SDKTask.md#itemstatus)
- [name](sdkApi_interfaces_entities_iTask.SDKTask.md#name)
- [progress](sdkApi_interfaces_entities_iTask.SDKTask.md#progress)
- [projectId](sdkApi_interfaces_entities_iTask.SDKTask.md#projectid)
- [query](sdkApi_interfaces_entities_iTask.SDKTask.md#query)
- [recipeId](sdkApi_interfaces_entities_iTask.SDKTask.md#recipeid)
- [spec](sdkApi_interfaces_entities_iTask.SDKTask.md#spec)
- [status](sdkApi_interfaces_entities_iTask.SDKTask.md#status)
- [taskOwner](sdkApi_interfaces_entities_iTask.SDKTask.md#taskowner)
- [updatedAt](sdkApi_interfaces_entities_iTask.SDKTask.md#updatedat)

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

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[assignmentIds](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#assignmentids)

___

### createdAt

• **createdAt**: `Date`

The date and time when the task was created.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[createdAt](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#createdat)

___

### creator

• **creator**: `string`

The creator of the task.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[creator](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#creator)

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the task belongs to.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[datasetId](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#datasetid)

___

### dueDate

• **dueDate**: `number`

The due date of the task.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[dueDate](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#duedate)

___

### forReview

• **forReview**: `number`

The number of items that need to be reviewed.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[forReview](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#forreview)

___

### hasParent

• **hasParent**: `boolean`

Whether the task has a parent task.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[hasParent](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#hasparent)

___

### id

• **id**: `string`

The unique identifier of the task.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[id](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#id)

___

### issues

• **issues**: `number`

The number of issues associated with the task.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[issues](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#issues)

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

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[itemStatus](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#itemstatus)

___

### name

• **name**: `string`

The name of the task.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[name](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#name)

___

### progress

• **progress**: `number`

The progress of the task.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[progress](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#progress)

___

### projectId

• **projectId**: `string`

The ID of the project the task belongs to.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[projectId](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#projectid)

___

### query

• **query**: `string`

The query associated with the task.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[query](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#query)

___

### recipeId

• **recipeId**: `string`

The ID of the recipe associated with the task.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[recipeId](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#recipeid)

___

### spec

• **spec**: `any`

The task's spec.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[spec](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#spec)

___

### status

• **status**: `string`

The status of the task.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[status](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#status)

___

### taskOwner

• **taskOwner**: `string`

The task owner.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[taskOwner](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#taskowner)

___

### updatedAt

• **updatedAt**: `Date`

The date and time when the task was last updated.

#### Implementation of

[ITask](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md).[updatedAt](../interfaces/sdkApi_interfaces_entities_iTask.ITask.md#updatedat)
