# Class: SDKProject

[dl.entities](./index.md).SDKProject

Represents a project instance within the SDK.

## Implements

- [`IProject`](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md)

## Table of contents

### Constructors

- [constructor](sdkApi_interfaces_entities_iProject.SDKProject.md#constructor)

### Properties

- [account](sdkApi_interfaces_entities_iProject.SDKProject.md#account)
- [contributors](sdkApi_interfaces_entities_iProject.SDKProject.md#contributors)
- [createdAt](sdkApi_interfaces_entities_iProject.SDKProject.md#createdat)
- [creator](sdkApi_interfaces_entities_iProject.SDKProject.md#creator)
- [datasetsCount](sdkApi_interfaces_entities_iProject.SDKProject.md#datasetscount)
- [groups](sdkApi_interfaces_entities_iProject.SDKProject.md#groups)
- [id](sdkApi_interfaces_entities_iProject.SDKProject.md#id)
- [isBlocked](sdkApi_interfaces_entities_iProject.SDKProject.md#isblocked)
- [name](sdkApi_interfaces_entities_iProject.SDKProject.md#name)
- [org](sdkApi_interfaces_entities_iProject.SDKProject.md#org)
- [role](sdkApi_interfaces_entities_iProject.SDKProject.md#role)
- [updatedAt](sdkApi_interfaces_entities_iProject.SDKProject.md#updatedat)

### Accessors

- [accountId](sdkApi_interfaces_entities_iProject.SDKProject.md#accountid)
- [orgId](sdkApi_interfaces_entities_iProject.SDKProject.md#orgid)

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
