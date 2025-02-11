# Class: SDKAccount

An interface representing an Entity object.

**`Interface`**

IEntity

## Implements

- [`IAccount`](../interfaces/IAccount.md)

## Table of contents

### Constructors

- [constructor](SDKAccount.md#constructor)

### Properties

- [createdAt](SDKAccount.md#createdat)
- [id](SDKAccount.md#id)
- [name](SDKAccount.md#name)
- [org](SDKAccount.md#org)
- [owner](SDKAccount.md#owner)
- [updatedAt](SDKAccount.md#updatedat)

## Constructors

### constructor

• **new SDKAccount**(`init?`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `init?` | `Partial`<[`SDKAccount`](SDKAccount.md)\> |

## Properties

### createdAt

• **createdAt**: `string` \| `number`

The date and time when the Entity was created.

#### Implementation of

[IAccount](../interfaces/IAccount.md).[createdAt](../interfaces/IAccount.md#createdat)

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Implementation of

[IAccount](../interfaces/IAccount.md).[id](../interfaces/IAccount.md#id)

___

### name

• **name**: `string`

#### Implementation of

[IAccount](../interfaces/IAccount.md).[name](../interfaces/IAccount.md#name)

___

### org

• **org**: `string` \| [`SDKOrg`](SDKOrg.md)

#### Implementation of

[IAccount](../interfaces/IAccount.md).[org](../interfaces/IAccount.md#org)

___

### owner

• **owner**: `string` \| [`SDKUser`](SDKUser.md)

#### Implementation of

[IAccount](../interfaces/IAccount.md).[owner](../interfaces/IAccount.md#owner)

___

### updatedAt

• **updatedAt**: `string` \| `number`

The date and time when the Entity was last updated.

#### Implementation of

[IAccount](../interfaces/IAccount.md).[updatedAt](../interfaces/IAccount.md#updatedat)
