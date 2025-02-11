# Class: SDKProject

Represents a project instance within the SDK.

**`Implements`**

IProject

## Implements

- [`IProject`](../interfaces/IProject.md)

## Table of contents

### Constructors

- [constructor](SDKProject.md#constructor)

### Properties

- [creator](SDKProject.md#creator)
- [id](SDKProject.md#id)
- [name](SDKProject.md#name)
- [createdAt](SDKProject.md#createdat)
- [updatedAt](SDKProject.md#updatedat)
- [contributors](SDKProject.md#contributors)
- [groups](SDKProject.md#groups)
- [datasetsCount](SDKProject.md#datasetscount)
- [role](SDKProject.md#role)
- [org](SDKProject.md#org)
- [account](SDKProject.md#account)
- [isBlocked](SDKProject.md#isblocked)

### Accessors

- [accountId](SDKProject.md#accountid)
- [orgId](SDKProject.md#orgid)

## Constructors

### constructor

• **new SDKProject**(`project`)

Creates an instance of SDKProject.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `project` | `any` | The project properties. |

## Properties

### creator

• **creator**: `string`

The project creator.

#### Implementation of

[IProject](../interfaces/IProject.md).[creator](../interfaces/IProject.md#creator)

___

### id

• **id**: `string`

The project ID.

#### Implementation of

[IProject](../interfaces/IProject.md).[id](../interfaces/IProject.md#id)

___

### name

• **name**: `string`

The project name.

#### Implementation of

[IProject](../interfaces/IProject.md).[name](../interfaces/IProject.md#name)

___

### createdAt

• **createdAt**: [`IDate`](../modules.md#idate)

The creation date.

#### Implementation of

[IProject](../interfaces/IProject.md).[createdAt](../interfaces/IProject.md#createdat)

___

### updatedAt

• **updatedAt**: [`IDate`](../modules.md#idate)

The last update date.

#### Implementation of

[IProject](../interfaces/IProject.md).[updatedAt](../interfaces/IProject.md#updatedat)

___

### contributors

• `Optional` **contributors**: [`IUser`](../interfaces/IUser.md)[]

The project contributors.

#### Implementation of

[IProject](../interfaces/IProject.md).[contributors](../interfaces/IProject.md#contributors)

___

### groups

• `Optional` **groups**: [`IGroup`](../interfaces/IGroup.md)[]

The project groups.

#### Implementation of

[IProject](../interfaces/IProject.md).[groups](../interfaces/IProject.md#groups)

___

### datasetsCount

• `Optional` **datasetsCount**: `number`

The amount of datasets associated with the project.

#### Implementation of

[IProject](../interfaces/IProject.md).[datasetsCount](../interfaces/IProject.md#datasetscount)

___

### role

• `Optional` **role**: `string`

The role of the project.

#### Implementation of

[IProject](../interfaces/IProject.md).[role](../interfaces/IProject.md#role)

___

### org

• `Optional` **org**: [`IOrg`](../interfaces/IOrg.md)

The organization associated with the project.

#### Implementation of

[IProject](../interfaces/IProject.md).[org](../interfaces/IProject.md#org)

___

### account

• `Optional` **account**: [`IAccount`](../interfaces/IAccount.md)

The account associated with the project.

#### Implementation of

[IProject](../interfaces/IProject.md).[account](../interfaces/IProject.md#account)

___

### isBlocked

• **isBlocked**: `boolean`

Indicates if the project is blocked.

#### Implementation of

[IProject](../interfaces/IProject.md).[isBlocked](../interfaces/IProject.md#isblocked)

## Accessors

### accountId

• `get` **accountId**(): `string`

Gets the account ID associated with the project.

#### Returns

`string`

#### Implementation of

[IProject](../interfaces/IProject.md).[accountId](../interfaces/IProject.md#accountid)

___

### orgId

• `get` **orgId**(): `string`

Gets the organization ID associated with the project.

#### Returns

`string`

#### Implementation of

[IProject](../interfaces/IProject.md).[orgId](../interfaces/IProject.md#orgid)
