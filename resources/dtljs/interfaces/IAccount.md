# Interface: IAccount

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IAccount`**

## Implemented by

- [`SDKAccount`](../classes/SDKAccount.md)

## Table of contents

### Properties

- [id](IAccount.md#id)
- [clientId](IAccount.md#clientid)
- [creator](IAccount.md#creator)
- [updatedBy](IAccount.md#updatedby)
- [name](IAccount.md#name)
- [createdAt](IAccount.md#createdat)
- [updatedAt](IAccount.md#updatedat)
- [org](IAccount.md#org)
- [owner](IAccount.md#owner)

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

### org

• **org**: `string` \| [`IOrg`](IOrg.md)

___

### owner

• **owner**: `string` \| [`IUser`](IUser.md)
