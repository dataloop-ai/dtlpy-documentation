# Class: SDKDataset

[sdkApi/interfaces/entities/iDataset](../modules/sdkApi_interfaces_entities_iDataset.md).SDKDataset

Represents a dataset instance within the SDK.

**`Implements`**

## Implements

- [`IDataset`](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md)

## Table of contents

### Constructors

- [constructor](sdkApi_interfaces_entities_iDataset.SDKDataset.md#constructor)

### Properties

- [annotated](sdkApi_interfaces_entities_iDataset.SDKDataset.md#annotated)
- [createdAt](sdkApi_interfaces_entities_iDataset.SDKDataset.md#createdat)
- [creator](sdkApi_interfaces_entities_iDataset.SDKDataset.md#creator)
- [directoryTree](sdkApi_interfaces_entities_iDataset.SDKDataset.md#directorytree)
- [driver](sdkApi_interfaces_entities_iDataset.SDKDataset.md#driver)
- [export](sdkApi_interfaces_entities_iDataset.SDKDataset.md#export)
- [id](sdkApi_interfaces_entities_iDataset.SDKDataset.md#id)
- [items](sdkApi_interfaces_entities_iDataset.SDKDataset.md#items)
- [itemsCount](sdkApi_interfaces_entities_iDataset.SDKDataset.md#itemscount)
- [metadata](sdkApi_interfaces_entities_iDataset.SDKDataset.md#metadata)
- [name](sdkApi_interfaces_entities_iDataset.SDKDataset.md#name)
- [projects](sdkApi_interfaces_entities_iDataset.SDKDataset.md#projects)
- [readableType](sdkApi_interfaces_entities_iDataset.SDKDataset.md#readabletype)
- [shareLevel](sdkApi_interfaces_entities_iDataset.SDKDataset.md#sharelevel)
- [url](sdkApi_interfaces_entities_iDataset.SDKDataset.md#url)

## Constructors

### constructor

• **new SDKDataset**(`dataset`)

Creates an instance of SDKDataset.

#### Parameters

| Name | Type |
| :------ | :------ |
| `dataset` | `Partial`<[`SDKDataset`](sdkApi_interfaces_entities_iDataset.SDKDataset.md)\> |

## Properties

### annotated

• **annotated**: `number`

The number of items in the dataset that have been annotated

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[annotated](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#annotated)

___

### createdAt

• **createdAt**: `IDate`

The date the dataset was created

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[createdAt](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#createdat)

___

### creator

• **creator**: `string`

The dataset creator

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[creator](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#creator)

___

### directoryTree

• **directoryTree**: `string`

The URL of the dataset's directory tree

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[directoryTree](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#directorytree)

___

### driver

• **driver**: `string`

The dataset's driver

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[driver](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#driver)

___

### export

• **export**: `Object`

The URLs of the dataset's exports

#### Type declaration

| Name | Type |
| :------ | :------ |
| `json` | `string` |
| `zip` | `string` |

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[export](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#export)

___

### id

• **id**: `string`

The unique identifier of the dataset

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[id](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#id)

___

### items

• **items**: `string`

The URL of the dataset's items

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[items](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#items)

___

### itemsCount

• **itemsCount**: `number`

The number of items in the dataset

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[itemsCount](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#itemscount)

___

### metadata

• `Optional` **metadata**: `any`

The dataset metadata

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[metadata](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#metadata)

___

### name

• **name**: `string`

The name of the dataset

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[name](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#name)

___

### projects

• **projects**: `string`[]

The projects the dataset belongs to

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[projects](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#projects)

___

### readableType

• **readableType**: `string`

The type of the dataset

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[readableType](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#readabletype)

___

### shareLevel

• **shareLevel**: ``"private"`` \| ``"project"``

The share level of the dataset

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[shareLevel](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#sharelevel)

___

### url

• **url**: `string`

The URL of the dataset

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md).[url](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#url)
