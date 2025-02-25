# Interface: IGroup

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IGroup`**

## Implemented by

- [`SDKGroup`](../classes/SDKGroup.md)

## Table of contents

### Properties

- [id](IGroup.md#id)
- [clientId](IGroup.md#clientid)
- [creator](IGroup.md#creator)
- [updatedBy](IGroup.md#updatedby)
- [name](IGroup.md#name)
- [createdAt](IGroup.md#createdat)
- [updatedAt](IGroup.md#updatedat)
- [owner](IGroup.md#owner)
- [members](IGroup.md#members)
- [org](IGroup.md#org)

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

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)

___

### name

• **name**: `string`

___

### createdAt

• **createdAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was created.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### updatedAt

• **updatedAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was last updated.

#### Overrides

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### owner

• **owner**: [`IUser`](IUser.md)

___

### members

• **members**: [`IUser`](IUser.md)[]

___

### org

• **org**: `string`
