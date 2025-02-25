# Class: SDKOrg

An interface representing an Entity object.

**`Interface`**

IEntity

## Implements

- [`IOrg`](../interfaces/IOrg.md)

## Table of contents

### Constructors

- [constructor](SDKOrg.md#constructor)

### Properties

- [name](SDKOrg.md#name)
- [createdAt](SDKOrg.md#createdat)
- [updatedAt](SDKOrg.md#updatedat)
- [owner](SDKOrg.md#owner)
- [groups](SDKOrg.md#groups)
- [members](SDKOrg.md#members)
- [plan](SDKOrg.md#plan)
- [account](SDKOrg.md#account)
- [role](SDKOrg.md#role)
- [industry](SDKOrg.md#industry)
- [size](SDKOrg.md#size)
- [id](SDKOrg.md#id)
- [clientId](SDKOrg.md#clientid)
- [creator](SDKOrg.md#creator)
- [updatedBy](SDKOrg.md#updatedby)

## Constructors

### constructor

• **new SDKOrg**(`init?`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `init?` | `Partial`<[`SDKOrg`](SDKOrg.md)\> |

## Properties

### name

• **name**: `string`

#### Implementation of

[IOrg](../interfaces/IOrg.md).[name](../interfaces/IOrg.md#name)

___

### createdAt

• **createdAt**: `string` \| `number`

The date and time when the Entity was created.

#### Implementation of

[IOrg](../interfaces/IOrg.md).[createdAt](../interfaces/IOrg.md#createdat)

___

### updatedAt

• **updatedAt**: `string` \| `number`

The date and time when the Entity was last updated.

#### Implementation of

[IOrg](../interfaces/IOrg.md).[updatedAt](../interfaces/IOrg.md#updatedat)

___

### owner

• **owner**: [`SDKUser`](SDKUser.md)

#### Implementation of

[IOrg](../interfaces/IOrg.md).[owner](../interfaces/IOrg.md#owner)

___

### groups

• **groups**: [`SDKGroup`](SDKGroup.md)[]

#### Implementation of

[IOrg](../interfaces/IOrg.md).[groups](../interfaces/IOrg.md#groups)

___

### members

• **members**: [`SDKUser`](SDKUser.md)[]

#### Implementation of

[IOrg](../interfaces/IOrg.md).[members](../interfaces/IOrg.md#members)

___

### plan

• **plan**: ``"freemium"`` \| ``"premium"``

#### Implementation of

[IOrg](../interfaces/IOrg.md).[plan](../interfaces/IOrg.md#plan)

___

### account

• `Optional` **account**: [`SDKAccount`](SDKAccount.md)

#### Implementation of

[IOrg](../interfaces/IOrg.md).[account](../interfaces/IOrg.md#account)

___

### role

• `Optional` **role**: `OrgRole`

#### Implementation of

[IOrg](../interfaces/IOrg.md).[role](../interfaces/IOrg.md#role)

___

### industry

• **industry**: `OrgIndustry`

#### Implementation of

[IOrg](../interfaces/IOrg.md).[industry](../interfaces/IOrg.md#industry)

___

### size

• **size**: `OrgSize`

#### Implementation of

[IOrg](../interfaces/IOrg.md).[size](../interfaces/IOrg.md#size)

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Implementation of

[IOrg](../interfaces/IOrg.md).[id](../interfaces/IOrg.md#id)

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Implementation of

[IOrg](../interfaces/IOrg.md).[clientId](../interfaces/IOrg.md#clientid)

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

#### Implementation of

[IOrg](../interfaces/IOrg.md).[creator](../interfaces/IOrg.md#creator)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Implementation of

[IOrg](../interfaces/IOrg.md).[updatedBy](../interfaces/IOrg.md#updatedby)
