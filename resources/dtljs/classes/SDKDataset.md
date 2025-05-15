# Class: SDKDataset

Represents a dataset instance within the SDK.

**`Implements`**

## Implements

- [`IDataset`](../interfaces/IDataset.md)

## Table of contents

### Constructors

- [constructor](SDKDataset.md#constructor)

### Properties

- [annotated](SDKDataset.md#annotated)
- [annotations](SDKDataset.md#annotations)
- [attributes](SDKDataset.md#attributes)
- [classes](SDKDataset.md#classes)
- [createdAt](SDKDataset.md#createdat)
- [creator](SDKDataset.md#creator)
- [directoryTree](SDKDataset.md#directorytree)
- [driver](SDKDataset.md#driver)
- [export](SDKDataset.md#export)
- [id](SDKDataset.md#id)
- [items](SDKDataset.md#items)
- [itemsCount](SDKDataset.md#itemscount)
- [name](SDKDataset.md#name)
- [projects](SDKDataset.md#projects)
- [metadata](SDKDataset.md#metadata)
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
| `dataset` | `Partial`<[`SDKDataset`](SDKDataset.md)\> |

## Properties

### annotated

• **annotated**: `number`

The number of items in the dataset that have been annotated

#### Implementation of

[IDataset](../interfaces/IDataset.md).[annotated](../interfaces/IDataset.md#annotated)

___

### annotations

• **annotations**: `DatasetClassInfo`[]

#### Implementation of

[IDataset](../interfaces/IDataset.md).[annotations](../interfaces/IDataset.md#annotations)

___

### attributes

• **attributes**: `string`[]

#### Implementation of

[IDataset](../interfaces/IDataset.md).[attributes](../interfaces/IDataset.md#attributes)

___

### classes

• **classes**: `Object`

#### Index signature

▪ [p: `string`]: `string`

#### Implementation of

[IDataset](../interfaces/IDataset.md).[classes](../interfaces/IDataset.md#classes)

___

### createdAt

• **createdAt**: [`IDate`](../modules.md#idate)

The date the dataset was created

#### Implementation of

[IDataset](../interfaces/IDataset.md).[createdAt](../interfaces/IDataset.md#createdat)

___

### creator

• **creator**: `string`

The dataset creator

#### Implementation of

[IDataset](../interfaces/IDataset.md).[creator](../interfaces/IDataset.md#creator)

___

### directoryTree

• **directoryTree**: `string`

The URL of the dataset's directory tree

#### Implementation of

[IDataset](../interfaces/IDataset.md).[directoryTree](../interfaces/IDataset.md#directorytree)

___

### driver

• **driver**: `string`

The dataset's driver

#### Implementation of

[IDataset](../interfaces/IDataset.md).[driver](../interfaces/IDataset.md#driver)

___

### export

• **export**: `Object`

The URLs of the dataset's exports

#### Type declaration

| Name | Type |
| :------ | :------ |
| `zip` | `string` |
| `json` | `string` |

#### Implementation of

[IDataset](../interfaces/IDataset.md).[export](../interfaces/IDataset.md#export)

___

### id

• **id**: `string`

The unique identifier of the dataset

#### Implementation of

[IDataset](../interfaces/IDataset.md).[id](../interfaces/IDataset.md#id)

___

### items

• **items**: `string`

The URL of the dataset's items

#### Implementation of

[IDataset](../interfaces/IDataset.md).[items](../interfaces/IDataset.md#items)

___

### itemsCount

• **itemsCount**: `number`

The number of items in the dataset

#### Implementation of

[IDataset](../interfaces/IDataset.md).[itemsCount](../interfaces/IDataset.md#itemscount)

___

### name

• **name**: `string`

The name of the dataset

#### Implementation of

[IDataset](../interfaces/IDataset.md).[name](../interfaces/IDataset.md#name)

___

### projects

• **projects**: `string`[]

The projects the dataset belongs to

#### Implementation of

[IDataset](../interfaces/IDataset.md).[projects](../interfaces/IDataset.md#projects)

___

### metadata

• `Optional` **metadata**: `any`

The dataset metadata

#### Implementation of

[IDataset](../interfaces/IDataset.md).[metadata](../interfaces/IDataset.md#metadata)

___

### readableType

• **readableType**: `string`

The type of the dataset

#### Implementation of

[IDataset](../interfaces/IDataset.md).[readableType](../interfaces/IDataset.md#readabletype)

___

### shareLevel

• **shareLevel**: ``"private"`` \| ``"project"``

The share level of the dataset

#### Implementation of

[IDataset](../interfaces/IDataset.md).[shareLevel](../interfaces/IDataset.md#sharelevel)

___

### url

• **url**: `string`

The URL of the dataset

#### Implementation of

[IDataset](../interfaces/IDataset.md).[url](../interfaces/IDataset.md#url)
