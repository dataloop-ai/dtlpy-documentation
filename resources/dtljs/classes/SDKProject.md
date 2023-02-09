# Class: SDKProject

[entities](./entities.md).SDKProject

Represents a project instance within the SDK.

## Implements

- [`IProject`](../interfaces/IProject.md)

## Table of contents

### Constructors

- [constructor](SDKProject.md#constructor)

### Properties

- [account](SDKProject.md#account)
- [contributors](SDKProject.md#contributors)
- [createdAt](SDKProject.md#createdat)
- [creator](SDKProject.md#creator)
- [datasetsCount](SDKProject.md#datasetscount)
- [groups](SDKProject.md#groups)
- [id](SDKProject.md#id)
- [isBlocked](SDKProject.md#isblocked)
- [name](SDKProject.md#name)
- [org](SDKProject.md#org)
- [role](SDKProject.md#role)
- [updatedAt](SDKProject.md#updatedat)

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

### account

• `Optional` **account**: `IAccount`

The account associated with the project.

___

### contributors

• `Optional` **contributors**: `IUser`[]

The project contributors.

___

### createdAt

• **createdAt**: `IDate`

The date of creation.

___

### creator

• **creator**: `string`

The project creator.

___

### datasetsCount

• `Optional` **datasetsCount**: `number`

The amount of datasets associated with the project.

___

### groups

• `Optional` **groups**: `IGroup`[]

The project groups.

___

### id

• **id**: `string`

The project ID.

___

### isBlocked

• **isBlocked**: `boolean`

Indicates if the project is blocked.

___

### name

• **name**: `string`

The name of the project.

___

### org

• `Optional` **org**: `IOrg`

The organization associated with the project.

___

### role

• `Optional` **role**: `string`

The role of the project.

___

### updatedAt

• **updatedAt**: `IDate`

The last update date.

## Accessors

### accountId

• `get` **accountId**(): `string`

Gets the account ID associated with the project.

#### Returns

`string`

___

### orgId

• `get` **orgId**(): `string`

Gets the organization ID associated with the project.

#### Returns

`string`
