# Interface: IOrg

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IOrg`**

## Implemented by

- [`SDKOrg`](../classes/SDKOrg.md)

## Table of contents

### Properties

- [id](IOrg.md#id)
- [clientId](IOrg.md#clientid)
- [creator](IOrg.md#creator)
- [updatedBy](IOrg.md#updatedby)
- [name](IOrg.md#name)
- [createdAt](IOrg.md#createdat)
- [updatedAt](IOrg.md#updatedat)
- [owner](IOrg.md#owner)
- [groups](IOrg.md#groups)
- [members](IOrg.md#members)
- [plan](IOrg.md#plan)
- [account](IOrg.md#account)
- [role](IOrg.md#role)
- [industry](IOrg.md#industry)
- [size](IOrg.md#size)

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

### groups

• **groups**: [`IGroup`](IGroup.md)[]

___

### members

• **members**: [`IUser`](IUser.md)[]

___

### plan

• **plan**: ``"freemium"`` \| ``"premium"``

___

### account

• `Optional` **account**: [`IAccount`](IAccount.md)

___

### role

• `Optional` **role**: `string`

___

### industry

• **industry**: `string`

___

### size

• **size**: `string`
