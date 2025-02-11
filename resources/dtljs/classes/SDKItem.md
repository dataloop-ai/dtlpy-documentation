# Class: SDKItem

Represents an item instance within the SDK.

**`Implements`**

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
- [filename](SDKItem.md#filename)
- [id](SDKItem.md#id)
- [metadata](SDKItem.md#metadata)
- [name](SDKItem.md#name)
- [stream](SDKItem.md#stream)
- [thumbnail](SDKItem.md#thumbnail)
- [type](SDKItem.md#type)
- [url](SDKItem.md#url)
- [executions](SDKItem.md#executions)
- [description](SDKItem.md#description)

## Constructors

### constructor

• **new SDKItem**(`item`)

Creates an instance of SDKItem.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `item` | `Partial`<[`SDKItem`](SDKItem.md)\> | The item properties. |

## Properties

### annotated

• **annotated**: `boolean` \| ``"discarded"``

Indicates whether the item has been annotated or discarded.

#### Implementation of

[IItem](../interfaces/IItem.md).[annotated](../interfaces/IItem.md#annotated)

___

### annotations

• **annotations**: `string`

The URL of the Item's annotations.

#### Implementation of

[IItem](../interfaces/IItem.md).[annotations](../interfaces/IItem.md#annotations)

___

### createdAt

• **createdAt**: `Date`

The date and time the item was created.

#### Implementation of

[IItem](../interfaces/IItem.md).[createdAt](../interfaces/IItem.md#createdat)

___

### creator

• **creator**: `string`

The creator of the item.

#### Implementation of

[IItem](../interfaces/IItem.md).[creator](../interfaces/IItem.md#creator)

___

### dataset

• **dataset**: `string`

The url of the dataset the item belongs to.

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the item belongs to.

#### Implementation of

[IItem](../interfaces/IItem.md).[datasetId](../interfaces/IItem.md#datasetid)

___

### dir

• **dir**: `string`

The directory the item is located in.

#### Implementation of

[IItem](../interfaces/IItem.md).[dir](../interfaces/IItem.md#dir)

___

### filename

• **filename**: `string`

The filename of the item.

#### Implementation of

[IItem](../interfaces/IItem.md).[filename](../interfaces/IItem.md#filename)

___

### id

• **id**: `string`

The unique ID of the item.

#### Implementation of

[IItem](../interfaces/IItem.md).[id](../interfaces/IItem.md#id)

___

### metadata

• **metadata**: `any`

The metadata associated with the item.

#### Implementation of

[IItem](../interfaces/IItem.md).[metadata](../interfaces/IItem.md#metadata)

___

### name

• **name**: `string`

The name of the item.

#### Implementation of

[IItem](../interfaces/IItem.md).[name](../interfaces/IItem.md#name)

___

### stream

• **stream**: `string`

The URL of the Item's stream.

#### Implementation of

[IItem](../interfaces/IItem.md).[stream](../interfaces/IItem.md#stream)

___

### thumbnail

• **thumbnail**: `string`

The URL of the item's thumbnail image.

#### Implementation of

[IItem](../interfaces/IItem.md).[thumbnail](../interfaces/IItem.md#thumbnail)

___

### type

• **type**: ``"file"`` \| ``"dir"``

The type of the item, either 'file' or 'dir'.

#### Implementation of

[IItem](../interfaces/IItem.md).[type](../interfaces/IItem.md#type)

___

### url

• **url**: `string`

The URL of the item.

#### Implementation of

[IItem](../interfaces/IItem.md).[url](../interfaces/IItem.md#url)

___

### executions

• `Optional` **executions**: [`SDKFunctionExecution`](SDKFunctionExecution.md)[]

The list of function executions associated with the item.

___

### description

• `Optional` **description**: `string`

Item description.
