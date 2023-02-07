# Interface: IItem

[interfaces](./index.md).IItem

An interface representing an Item object, extending the IEntity interface.

**`Interface`**

IItem

## Hierarchy

- [`IEntity`](sdkApi_interfaces_entities_base.IEntity.md)

  ↳ **`IItem`**

## Implemented by

- [`SDKItem`](../classes/sdkApi_interfaces_entities_iItem.SDKItem.md)

## Table of contents

### Properties

- [annotated](sdkApi_interfaces_entities_iItem.IItem.md#annotated)
- [annotations](sdkApi_interfaces_entities_iItem.IItem.md#annotations)
- [clientId](sdkApi_interfaces_entities_iItem.IItem.md#clientid)
- [createdAt](sdkApi_interfaces_entities_iItem.IItem.md#createdat)
- [creator](sdkApi_interfaces_entities_iItem.IItem.md#creator)
- [datasetId](sdkApi_interfaces_entities_iItem.IItem.md#datasetid)
- [dir](sdkApi_interfaces_entities_iItem.IItem.md#dir)
- [filename](sdkApi_interfaces_entities_iItem.IItem.md#filename)
- [hidden](sdkApi_interfaces_entities_iItem.IItem.md#hidden)
- [id](sdkApi_interfaces_entities_iItem.IItem.md#id)
- [metadata](sdkApi_interfaces_entities_iItem.IItem.md#metadata)
- [name](sdkApi_interfaces_entities_iItem.IItem.md#name)
- [stream](sdkApi_interfaces_entities_iItem.IItem.md#stream)
- [thumbnail](sdkApi_interfaces_entities_iItem.IItem.md#thumbnail)
- [type](sdkApi_interfaces_entities_iItem.IItem.md#type)
- [updatedAt](sdkApi_interfaces_entities_iItem.IItem.md#updatedat)
- [updatedBy](sdkApi_interfaces_entities_iItem.IItem.md#updatedby)
- [url](sdkApi_interfaces_entities_iItem.IItem.md#url)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[clientId](sdkApi_interfaces_entities_base.IEntity.md#clientid)

___

### createdAt

• **createdAt**: `IDate`

The date and time when the Item was created.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[createdAt](sdkApi_interfaces_entities_base.IEntity.md#createdat)

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[creator](sdkApi_interfaces_entities_base.IEntity.md#creator)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[id](sdkApi_interfaces_entities_base.IEntity.md#id)

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

The URL of the Item.
