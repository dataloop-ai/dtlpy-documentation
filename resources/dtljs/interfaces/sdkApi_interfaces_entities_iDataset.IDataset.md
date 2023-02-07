# Interface: IDataset

[interfaces](./index.md).IDataset

An interface representing a Dataset object.

**`Interface`**

IDataset

## Hierarchy

- [`IEntity`](sdkApi_interfaces_entities_base.IEntity.md)

  ↳ **`IDataset`**

## Implemented by

- [`SDKDataset`](../classes/sdkApi_interfaces_entities_iDataset.SDKDataset.md)

## Table of contents

### Properties

- [annotated](sdkApi_interfaces_entities_iDataset.IDataset.md#annotated)
- [clientId](sdkApi_interfaces_entities_iDataset.IDataset.md#clientid)
- [createdAt](sdkApi_interfaces_entities_iDataset.IDataset.md#createdat)
- [creator](sdkApi_interfaces_entities_iDataset.IDataset.md#creator)
- [directoryTree](sdkApi_interfaces_entities_iDataset.IDataset.md#directorytree)
- [driver](sdkApi_interfaces_entities_iDataset.IDataset.md#driver)
- [error](sdkApi_interfaces_entities_iDataset.IDataset.md#error)
- [export](sdkApi_interfaces_entities_iDataset.IDataset.md#export)
- [id](sdkApi_interfaces_entities_iDataset.IDataset.md#id)
- [indexDriver](sdkApi_interfaces_entities_iDataset.IDataset.md#indexdriver)
- [items](sdkApi_interfaces_entities_iDataset.IDataset.md#items)
- [itemsCount](sdkApi_interfaces_entities_iDataset.IDataset.md#itemscount)
- [metadata](sdkApi_interfaces_entities_iDataset.IDataset.md#metadata)
- [name](sdkApi_interfaces_entities_iDataset.IDataset.md#name)
- [projects](sdkApi_interfaces_entities_iDataset.IDataset.md#projects)
- [readableType](sdkApi_interfaces_entities_iDataset.IDataset.md#readabletype)
- [readonly](sdkApi_interfaces_entities_iDataset.IDataset.md#readonly)
- [shareLevel](sdkApi_interfaces_entities_iDataset.IDataset.md#sharelevel)
- [updatedAt](sdkApi_interfaces_entities_iDataset.IDataset.md#updatedat)
- [updatedBy](sdkApi_interfaces_entities_iDataset.IDataset.md#updatedby)
- [url](sdkApi_interfaces_entities_iDataset.IDataset.md#url)

## Properties

### annotated

• **annotated**: `number`

The number of items in the dataset that have been annotated

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[clientId](sdkApi_interfaces_entities_base.IEntity.md#clientid)

___

### createdAt

• **createdAt**: `IDate`

The date the dataset was created

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[createdAt](sdkApi_interfaces_entities_base.IEntity.md#createdat)

___

### creator

• **creator**: `string`

The dataset creator

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[creator](sdkApi_interfaces_entities_base.IEntity.md#creator)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[id](sdkApi_interfaces_entities_base.IEntity.md#id)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedAt](sdkApi_interfaces_entities_base.IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedBy](sdkApi_interfaces_entities_base.IEntity.md#updatedby)

___

### url

• **url**: `string`

The URL of the dataset
