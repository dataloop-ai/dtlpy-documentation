# Interface: IOntology

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IOntology`**

## Implemented by

- [`APIOntologyV2`](../classes/APIOntologyV2.md)

## Table of contents

### Properties

- [id](IOntology.md#id)
- [clientId](IOntology.md#clientid)
- [creator](IOntology.md#creator)
- [createdAt](IOntology.md#createdat)
- [updatedAt](IOntology.md#updatedat)
- [updatedBy](IOntology.md#updatedby)
- [title](IOntology.md#title)
- [roots](IOntology.md#roots)
- [metadata](IOntology.md#metadata)
- [attributes](IOntology.md#attributes)
- [projectIds](IOntology.md#projectids)
- [system](IOntology.md#system)
- [structureIds](IOntology.md#structureids)

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

### title

• **title**: `string`

___

### roots

• `Optional` **roots**: `string`[]

___

### metadata

• **metadata**: `Dictionary`

___

### attributes

• `Optional` **attributes**: `string`[]

___

### projectIds

• `Optional` **projectIds**: `string`[]

___

### system

• `Optional` **system**: `boolean`

___

### structureIds

• `Optional` **structureIds**: `string`[]
