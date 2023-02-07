# Class: SDKItem

[dl.entities](./index.md).SDKItem

Represents an item instance within the SDK.

## Implements

- [`IItem`](../interfaces/sdkApi_interfaces_entities_iItem.IItem.md)

## Table of contents

### Constructors

- [constructor](sdkApi_interfaces_entities_iItem.SDKItem.md#constructor)

### Properties

- [annotated](sdkApi_interfaces_entities_iItem.SDKItem.md#annotated)
- [annotations](sdkApi_interfaces_entities_iItem.SDKItem.md#annotations)
- [createdAt](sdkApi_interfaces_entities_iItem.SDKItem.md#createdat)
- [creator](sdkApi_interfaces_entities_iItem.SDKItem.md#creator)
- [dataset](sdkApi_interfaces_entities_iItem.SDKItem.md#dataset)
- [datasetId](sdkApi_interfaces_entities_iItem.SDKItem.md#datasetid)
- [dir](sdkApi_interfaces_entities_iItem.SDKItem.md#dir)
- [executions](sdkApi_interfaces_entities_iItem.SDKItem.md#executions)
- [filename](sdkApi_interfaces_entities_iItem.SDKItem.md#filename)
- [id](sdkApi_interfaces_entities_iItem.SDKItem.md#id)
- [metadata](sdkApi_interfaces_entities_iItem.SDKItem.md#metadata)
- [name](sdkApi_interfaces_entities_iItem.SDKItem.md#name)
- [stream](sdkApi_interfaces_entities_iItem.SDKItem.md#stream)
- [thumbnail](sdkApi_interfaces_entities_iItem.SDKItem.md#thumbnail)
- [type](sdkApi_interfaces_entities_iItem.SDKItem.md#type)
- [url](sdkApi_interfaces_entities_iItem.SDKItem.md#url)

## Constructors

### constructor

• **new SDKItem**(`item`)

Creates an instance of SDKItem.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `item` | `Partial`<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)> | The item properties. |

## Properties

### annotated

• **annotated**: `boolean` \| ``"discarded"``

Indicates whether the item has been annotated or discarded.

___

### annotations

• **annotations**: `string`

The URL of the Item's annotations.

___

### createdAt

• **createdAt**: `Date`

The date and time the item was created.

___

### creator

• **creator**: `string`

The creator of the item.

___

### dataset

• **dataset**: `string`

The url of the dataset the item belongs to.

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the item belongs to.

___

### dir

• **dir**: `string`

The directory the item is located in.

___

### executions

• `Optional` **executions**: [`SDKFunctionExecution`](sdkApi_interfaces_entities_iExecution.SDKFunctionExecution.md)[]

The list of function executions associated with the item.

___

### filename

• **filename**: `string`

The filename of the item.

___

### id

• **id**: `string`

The unique ID of the item.

___

### metadata

• **metadata**: `any`

The metadata associated with the item.

___

### name

• **name**: `string`

The name of the item.

___

### stream

• **stream**: `string`

The URL of the Item's stream.

___

### thumbnail

• **thumbnail**: `string`

The URL of the item's thumbnail image.

___

### type

• **type**: ``"file"`` \| ``"dir"``

The type of the item, either 'file' or 'dir'.

___

### url

• **url**: `string`

The URL of the item.
