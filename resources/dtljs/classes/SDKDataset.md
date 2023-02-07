# Class: SDKDataset

[entities](./entities.md).SDKDataset

Represents a dataset instance within the SDK.

## Implements

- [`IDataset`](../interfaces/IDataset.md)

## Table of contents

### Constructors

- [constructor](SDKDataset.md#constructor)

### Properties

- [annotated](SDKDataset.md#annotated)
- [createdAt](SDKDataset.md#createdat)
- [creator](SDKDataset.md#creator)
- [directoryTree](SDKDataset.md#directorytree)
- [driver](SDKDataset.md#driver)
- [export](SDKDataset.md#export)
- [id](SDKDataset.md#id)
- [items](SDKDataset.md#items)
- [itemsCount](SDKDataset.md#itemscount)
- [metadata](SDKDataset.md#metadata)
- [name](SDKDataset.md#name)
- [projects](SDKDataset.md#projects)
- [readableType](SDKDataset.md#readabletype)
- [shareLevel](SDKDataset.md#sharelevel)
- [url](SDKDataset.md#url)

## Constructors

### constructor

• **new SDKDataset**(`dataset`)

Creates an instance of SDKDataset.

#### Parameters

| Name | Type |
| :------ | :------ |
| `dataset` | `Partial`<[`SDKDataset`](SDKDataset.md)> |

## Properties

### annotated

• **annotated**: `number`

The number of items in the dataset that have been annotated

___

### createdAt

• **createdAt**: `IDate`

The date the dataset was created

___

### creator

• **creator**: `string`

The dataset creator

___

### directoryTree

• **directoryTree**: `string`

The URL of the dataset's directory tree

___

### driver

• **driver**: `string`

The dataset's driver

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

The projects the dataset belongs to

___

### readableType

• **readableType**: `string`

The type of the dataset

#### Implementation of

[IDataset](../interfaces/IDataset.md)
.[readableType](../interfaces/IDataset.md#readabletype)

___

### shareLevel

• **shareLevel**: ``"private"`` \| ``"project"``

The share level of the dataset

#### Implementation of

[IDataset](../interfaces/IDataset.md)
.[shareLevel](../interfaces/IDataset.md#sharelevel)

___

### url

• **url**: `string`

The URL of the dataset

#### Implementation of

[IDataset](../interfaces/IDataset.md)
.[url](../interfaces/IDataset.md#url)
