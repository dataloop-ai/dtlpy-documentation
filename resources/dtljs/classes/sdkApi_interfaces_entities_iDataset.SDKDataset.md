# Class: SDKDataset

[dl.entities](./index.md).SDKDataset

Represents a dataset instance within the SDK.

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
| `dataset` | `Partial`<[`SDKDataset`](sdkApi_interfaces_entities_iDataset.SDKDataset.md)> |

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

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md)
.[readableType](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#readabletype)

___

### shareLevel

• **shareLevel**: ``"private"`` \| ``"project"``

The share level of the dataset

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md)
.[shareLevel](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#sharelevel)

___

### url

• **url**: `string`

The URL of the dataset

#### Implementation of

[IDataset](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md)
.[url](../interfaces/sdkApi_interfaces_entities_iDataset.IDataset.md#url)
