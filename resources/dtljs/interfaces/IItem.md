# Interface: IItem

[interfaces](./index.md).IItem

An interface representing an Item object, extending the IEntity interface.

**`Interface`**

IItem

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IItem`**

## Implemented by

- [`SDKItem`](../classes/SDKItem.md)

## Table of contents

### Properties

- [annotated](IItem.md#annotated)
- [annotations](IItem.md#annotations)
- [clientId](IItem.md#clientid)
- [createdAt](IItem.md#createdat)
- [creator](IItem.md#creator)
- [datasetId](IItem.md#datasetid)
- [dir](IItem.md#dir)
- [filename](IItem.md#filename)
- [hidden](IItem.md#hidden)
- [id](IItem.md#id)
- [metadata](IItem.md#metadata)
- [name](IItem.md#name)
- [stream](IItem.md#stream)
- [thumbnail](IItem.md#thumbnail)
- [type](IItem.md#type)
- [updatedAt](IItem.md#updatedat)
- [updatedBy](IItem.md#updatedby)
- [url](IItem.md#url)

## Properties

### annotated

• **annotated**: `boolean` \| ``"discarded"``

A flag indicating whether the Item has been annotated, or 'discarded' if
the annotations were discarded.

___

### annotations

• **annotations**: `string`

The URL of the Item's annotations.

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### createdAt

• **createdAt**: `IDate`

The date and time when the Item was created.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

#### Inherited from

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### datasetId

• **datasetId**: `string`

The identifier of the dataset to which the Item belongs.

___

### dir

• **dir**: `string`

The directory path of the Item.

___

### filename

• **filename**: `string`

The filename of the Item.

___

### hidden

• `Optional` **hidden**: `boolean`

A flag indicating whether the Item should be hidden.

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Inherited from

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### metadata

• `Optional` **metadata**: `Dictionary`

Additional metadata for the Item, represented as a dictionary.

___

### name

• **name**: `string`

The display name of the Item.

___

### stream

• **stream**: `string`

The URL of the Item's stream.

___

### thumbnail

• **thumbnail**: `string`

The URL of the Item's thumbnail image.

___

### type

• **type**: ``"file"`` \| ``"dir"``

The type of the Item, either 'file' or 'dir'.

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

The URL of the Item.
