# Interface: IItem

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

- [id](IItem.md#id)
- [clientId](IItem.md#clientid)
- [creator](IItem.md#creator)
- [updatedAt](IItem.md#updatedat)
- [updatedBy](IItem.md#updatedby)
- [filename](IItem.md#filename)
- [name](IItem.md#name)
- [url](IItem.md#url)
- [type](IItem.md#type)
- [datasetId](IItem.md#datasetid)
- [dir](IItem.md#dir)
- [hidden](IItem.md#hidden)
- [createdAt](IItem.md#createdat)
- [thumbnail](IItem.md#thumbnail)
- [stream](IItem.md#stream)
- [annotations](IItem.md#annotations)
- [metadata](IItem.md#metadata)
- [annotated](IItem.md#annotated)

## Properties

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Inherited from

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

#### Inherited from

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### updatedAt

• `Optional` **updatedAt**: [`IDate`](../modules.md#idate)

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

### filename

• **filename**: `string`

The filename of the Item.

___

### name

• **name**: `string`

The display name of the Item.

___

### url

• **url**: `string`

The URL of the Item.

___

### type

• **type**: ``"file"`` \| ``"dir"``

The type of the Item, either 'file' or 'dir'.

___

### datasetId

• **datasetId**: `string`

The identifier of the dataset to which the Item belongs.

___

### dir

• **dir**: `string`

The directory path of the Item.

___

### hidden

• `Optional` **hidden**: `boolean`

A flag indicating whether the Item should be hidden.

___

### createdAt

• **createdAt**: [`IDate`](../modules.md#idate)

The date and time when the Item was created.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### thumbnail

• **thumbnail**: `string`

The URL of the Item's thumbnail image.

___

### stream

• **stream**: `string`

The URL of the Item's stream.

___

### annotations

• **annotations**: `string`

The URL of the Item's annotations.

___

### metadata

• `Optional` **metadata**: `Dictionary`

Additional metadata for the Item, represented as a dictionary.

___

### annotated

• **annotated**: `boolean` \| ``"discarded"``

A flag indicating whether the Item has been annotated, or 'discarded' if
the annotations were discarded.
