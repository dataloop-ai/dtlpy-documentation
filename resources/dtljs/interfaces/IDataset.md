# Interface: IDataset

[interfaces](./index.md).IDataset

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

- [annotated](IDataset.md#annotated)
- [clientId](IDataset.md#clientid)
- [createdAt](IDataset.md#createdat)
- [creator](IDataset.md#creator)
- [directoryTree](IDataset.md#directorytree)
- [driver](IDataset.md#driver)
- [error](IDataset.md#error)
- [export](IDataset.md#export)
- [id](IDataset.md#id)
- [indexDriver](IDataset.md#indexdriver)
- [items](IDataset.md#items)
- [itemsCount](IDataset.md#itemscount)
- [metadata](IDataset.md#metadata)
- [name](IDataset.md#name)
- [projects](IDataset.md#projects)
- [readableType](IDataset.md#readabletype)
- [readonly](IDataset.md#readonly)
- [shareLevel](IDataset.md#sharelevel)
- [updatedAt](IDataset.md#updatedat)
- [updatedBy](IDataset.md#updatedby)
- [url](IDataset.md#url)

## Properties

### annotated

• **annotated**: `number`

The number of items in the dataset that have been annotated

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### createdAt

• **createdAt**: `IDate`

The date the dataset was created

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### creator

• **creator**: `string`

The dataset creator

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### directoryTree

• **directoryTree**: `string`

The URL of the dataset's directory tree

___

### driver

• **driver**: `string`

The dataset's driver

___

### error

• `Optional` **error**: `any`

The dataset's error

___

### export

• **export**: `Object`

The URLs of the dataset's exports

#### Type declaration

| Name | Type |
| :------ | :------ |
| `json` | `string` |
| `zip` | `string` |

___

### id

• **id**: `string`

The unique identifier of the dataset

#### Overrides

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### indexDriver

• `Optional` **indexDriver**: ``"v1"`` \| ``"v2"``

The dataset's index driver

___

### items

• **items**: `string`

The URL of the dataset's items

___

### itemsCount

• **itemsCount**: `number`

The number of items in the dataset

___

### metadata

• `Optional` **metadata**: `any`

The dataset metadata

___

### name

• **name**: `string`

The name of the dataset

___

### projects

• **projects**: `string`[]

The list of projects the dataset belongs to

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

### updatedAt

• `Optional` **updatedAt**: `IDate`

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

### url

• **url**: `string`

The URL of the dataset
