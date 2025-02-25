# Interface: IDataset

An interface representing a Dataset object.

**`Interface`**

IDataset

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IDataset`**

## Implemented by

- [`SDKDataset`](../classes/SDKDataset.md)

## Table of contents

### Properties

- [clientId](IDataset.md#clientid)
- [updatedAt](IDataset.md#updatedat)
- [updatedBy](IDataset.md#updatedby)
- [id](IDataset.md#id)
- [name](IDataset.md#name)
- [annotations](IDataset.md#annotations)
- [annotated](IDataset.md#annotated)
- [classes](IDataset.md#classes)
- [attributes](IDataset.md#attributes)
- [itemsCount](IDataset.md#itemscount)
- [url](IDataset.md#url)
- [items](IDataset.md#items)
- [directoryTree](IDataset.md#directorytree)
- [creator](IDataset.md#creator)
- [projects](IDataset.md#projects)
- [export](IDataset.md#export)
- [metadata](IDataset.md#metadata)
- [clientObjectId](IDataset.md#clientobjectid)
- [maxClientObjectId](IDataset.md#maxclientobjectid)
- [createdAt](IDataset.md#createdat)
- [readableType](IDataset.md#readabletype)
- [readonly](IDataset.md#readonly)
- [shareLevel](IDataset.md#sharelevel)
- [driver](IDataset.md#driver)
- [error](IDataset.md#error)
- [indexDriver](IDataset.md#indexdriver)

## Properties

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### updatedAt

• `Optional` **updatedAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was last updated.

#### Inherited from

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)

___

### id

• **id**: `string`

The unique identifier of the dataset

#### Overrides

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### name

• **name**: `string`

The name of the dataset

___

### annotations

• **annotations**: `DatasetClassInfo`[]

___

### annotated

• **annotated**: `number`

The number of items in the dataset that have been annotated

___

### classes

• **classes**: `Object`

#### Index signature

▪ [label: `string`]: `string`

___

### attributes

• **attributes**: `string`[]

___

### itemsCount

• **itemsCount**: `number`

The number of items in the dataset

___

### url

• **url**: `string`

The URL of the dataset

___

### items

• **items**: `string`

The URL of the dataset's items

___

### directoryTree

• **directoryTree**: `string`

The URL of the dataset's directory tree

___

### creator

• **creator**: `string`

The dataset creator

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### projects

• **projects**: `string`[]

The list of projects the dataset belongs to

___

### export

• **export**: `Object`

The URLs of the dataset's exports

#### Type declaration

| Name | Type |
| :------ | :------ |
| `zip` | `string` |
| `json` | `string` |

___

### metadata

• `Optional` **metadata**: `any`

The dataset metadata

___

### clientObjectId

• `Optional` **clientObjectId**: `number`

___

### maxClientObjectId

• `Optional` **maxClientObjectId**: `number`

___

### createdAt

• **createdAt**: [`IDate`](../modules.md#idate)

The date the dataset was created

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### readableType

• **readableType**: `string`

The dataset type

___

### readonly

• `Optional` **readonly**: `boolean`

Whether the dataset is read-only

___

### shareLevel

• **shareLevel**: ``"private"`` \| ``"project"``

The dataset's share level

___

### driver

• **driver**: `string`

The dataset's driver

___

### error

• `Optional` **error**: `any`

The dataset's error

___

### indexDriver

• `Optional` **indexDriver**: ``"v1"`` \| ``"v2"``

The dataset's index driver
