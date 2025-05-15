# Interface: IAttributeSection

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IAttributeSection`**

## Implemented by

- [`APIAttributeSectionV2`](../classes/APIAttributeSectionV2.md)

## Table of contents

### Properties

- [id](IAttributeSection.md#id)
- [clientId](IAttributeSection.md#clientid)
- [createdAt](IAttributeSection.md#createdat)
- [updatedAt](IAttributeSection.md#updatedat)
- [updatedBy](IAttributeSection.md#updatedby)
- [ontologyId](IAttributeSection.md#ontologyid)
- [scope](IAttributeSection.md#scope)
- [key](IAttributeSection.md#key)
- [type](IAttributeSection.md#type)
- [values](IAttributeSection.md#values)
- [range](IAttributeSection.md#range)
- [hierarchy](IAttributeSection.md#hierarchy)
- [creator](IAttributeSection.md#creator)

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

### createdAt

• `Optional` **createdAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was created.

#### Inherited from

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

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

### ontologyId

• **ontologyId**: `string`

___

### scope

• `Optional` **scope**: [`ILabelScope`](ILabelScope.md)

___

### key

• **key**: `string`

___

### type

• **type**: `AttributeType`

___

### values

• `Optional` **values**: `string`[]

___

### range

• `Optional` **range**: [`IAttributeRange`](IAttributeRange.md)

___

### hierarchy

• `Optional` **hierarchy**: [`IAttributeHierarchy`](IAttributeHierarchy.md)

___

### creator

• **creator**: `string`

The creator of the Entity.

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)
