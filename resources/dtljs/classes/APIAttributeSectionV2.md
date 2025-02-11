# Class: APIAttributeSectionV2

An interface representing an Entity object.

**`Interface`**

IEntity

## Implements

- [`IAttributeSection`](../interfaces/IAttributeSection.md)

## Table of contents

### Properties

- [creator](APIAttributeSectionV2.md#creator)
- [id](APIAttributeSectionV2.md#id)
- [key](APIAttributeSectionV2.md#key)
- [ontologyId](APIAttributeSectionV2.md#ontologyid)
- [type](APIAttributeSectionV2.md#type)
- [range](APIAttributeSectionV2.md#range)
- [scope](APIAttributeSectionV2.md#scope)
- [values](APIAttributeSectionV2.md#values)
- [hierarchy](APIAttributeSectionV2.md#hierarchy)

### Constructors

- [constructor](APIAttributeSectionV2.md#constructor)

## Properties

### creator

• **creator**: `string`

The creator of the Entity.

#### Implementation of

[IAttributeSection](../interfaces/IAttributeSection.md).[creator](../interfaces/IAttributeSection.md#creator)

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Implementation of

[IAttributeSection](../interfaces/IAttributeSection.md).[id](../interfaces/IAttributeSection.md#id)

___

### key

• **key**: `string`

#### Implementation of

[IAttributeSection](../interfaces/IAttributeSection.md).[key](../interfaces/IAttributeSection.md#key)

___

### ontologyId

• **ontologyId**: `string`

#### Implementation of

[IAttributeSection](../interfaces/IAttributeSection.md).[ontologyId](../interfaces/IAttributeSection.md#ontologyid)

___

### type

• **type**: `AttributeType`

#### Implementation of

[IAttributeSection](../interfaces/IAttributeSection.md).[type](../interfaces/IAttributeSection.md#type)

___

### range

• `Optional` **range**: [`IAttributeRange`](../interfaces/IAttributeRange.md)

#### Implementation of

[IAttributeSection](../interfaces/IAttributeSection.md).[range](../interfaces/IAttributeSection.md#range)

___

### scope

• `Optional` **scope**: [`ILabelScope`](../interfaces/ILabelScope.md)

#### Implementation of

[IAttributeSection](../interfaces/IAttributeSection.md).[scope](../interfaces/IAttributeSection.md#scope)

___

### values

• `Optional` **values**: `string`[]

#### Implementation of

[IAttributeSection](../interfaces/IAttributeSection.md).[values](../interfaces/IAttributeSection.md#values)

___

### hierarchy

• `Optional` **hierarchy**: [`IAttributeHierarchy`](../interfaces/IAttributeHierarchy.md)

#### Implementation of

[IAttributeSection](../interfaces/IAttributeSection.md).[hierarchy](../interfaces/IAttributeSection.md#hierarchy)

## Constructors

### constructor

• **new APIAttributeSectionV2**(`attribute`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `attribute` | [`APIAttributeSectionV2`](APIAttributeSectionV2.md) |
