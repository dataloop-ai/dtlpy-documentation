# Class: SDKGroup

An interface representing an Entity object.

**`Interface`**

IEntity

## Implements

- [`IGroup`](../interfaces/IGroup.md)

## Table of contents

### Constructors

- [constructor](SDKGroup.md#constructor)

### Properties

- [createdAt](SDKGroup.md#createdat)
- [id](SDKGroup.md#id)
- [members](SDKGroup.md#members)
- [name](SDKGroup.md#name)
- [org](SDKGroup.md#org)
- [owner](SDKGroup.md#owner)
- [updatedAt](SDKGroup.md#updatedat)

## Constructors

### constructor

• **new SDKGroup**(`init?`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `init?` | `Partial`<[`SDKGroup`](SDKGroup.md)\> |

## Properties

### createdAt

• **createdAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was created.

#### Implementation of

[IGroup](../interfaces/IGroup.md).[createdAt](../interfaces/IGroup.md#createdat)

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Implementation of

[IGroup](../interfaces/IGroup.md).[id](../interfaces/IGroup.md#id)

___

### members

• **members**: [`SDKUser`](SDKUser.md)[]

#### Implementation of

[IGroup](../interfaces/IGroup.md).[members](../interfaces/IGroup.md#members)

___

### name

• **name**: `string`

#### Implementation of

[IGroup](../interfaces/IGroup.md).[name](../interfaces/IGroup.md#name)

___

### org

• **org**: `string`

#### Implementation of

[IGroup](../interfaces/IGroup.md).[org](../interfaces/IGroup.md#org)

___

### owner

• **owner**: [`SDKUser`](SDKUser.md)

#### Implementation of

[IGroup](../interfaces/IGroup.md).[owner](../interfaces/IGroup.md#owner)

___

### updatedAt

• **updatedAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was last updated.

#### Implementation of

[IGroup](../interfaces/IGroup.md).[updatedAt](../interfaces/IGroup.md#updatedat)
