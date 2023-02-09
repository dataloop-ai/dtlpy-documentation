# Class: SDKItem

[entities](./entities.md).SDKItem

Represents an item instance within the SDK.

## Implements

- [`IItem`](../interfaces/IItem.md)

## Table of contents

### Constructors

- [constructor](SDKItem.md#constructor)

### Properties

- [annotated](SDKItem.md#annotated)
- [annotations](SDKItem.md#annotations)
- [createdAt](SDKItem.md#createdat)
- [creator](SDKItem.md#creator)
- [dataset](SDKItem.md#dataset)
- [datasetId](SDKItem.md#datasetid)
- [dir](SDKItem.md#dir)
- [executions](SDKItem.md#executions)
- [filename](SDKItem.md#filename)
- [id](SDKItem.md#id)
- [metadata](SDKItem.md#metadata)
- [name](SDKItem.md#name)
- [stream](SDKItem.md#stream)
- [thumbnail](SDKItem.md#thumbnail)
- [type](SDKItem.md#type)
- [url](SDKItem.md#url)

## Constructors

### constructor

• **new SDKItem**(`item`)

Creates an instance of SDKItem.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `item` | `Partial`<[`SDKItem`](SDKItem.md)> | The item properties. |

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

• `Optional` **executions**: [`SDKFunctionExecution`](SDKFunctionExecution.md)[]

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
