# Interface: IStructure

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IStructure`**

## Implemented by

- [`APIStructureV2`](../classes/APIStructureV2.md)

## Table of contents

### Properties

- [clientId](IStructure.md#clientid)
- [createdAt](IStructure.md#createdat)
- [updatedAt](IStructure.md#updatedat)
- [updatedBy](IStructure.md#updatedby)
- [id](IStructure.md#id)
- [order](IStructure.md#order)
- [arcs](IStructure.md#arcs)
- [name](IStructure.md#name)
- [ontologyId](IStructure.md#ontologyid)
- [creator](IStructure.md#creator)

## Properties

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

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Overrides

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### order

• **order**: `string`[]

___

### arcs

• **arcs**: [`string`, `string`][]

___

### name

• **name**: `string`

___

### ontologyId

• **ontologyId**: `string`

___

### creator

• **creator**: `string`

The creator of the Entity.

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)
