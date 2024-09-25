# Class: SDKProject

[sdkApi/interfaces/entities/iProject](../modules/sdkApi_interfaces_entities_iProject.md).SDKProject

Represents a project instance within the SDK.

**`Implements`**

IProject

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

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[account](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#account)

___

### contributors

• `Optional` **contributors**: `IUser`[]

The project contributors.

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[contributors](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#contributors)

___

### createdAt

• **createdAt**: `IDate`

The creation date.

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[createdAt](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#createdat)

___

### creator

• **creator**: `string`

The project creator.

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[creator](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#creator)

___

### datasetsCount

• `Optional` **datasetsCount**: `number`

The amount of datasets associated with the project.

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[datasetsCount](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#datasetscount)

___

### groups

• `Optional` **groups**: `IGroup`[]

The project groups.

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[groups](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#groups)

___

### id

• **id**: `string`

The project ID.

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[id](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#id)

___

### isBlocked

• **isBlocked**: `boolean`

Indicates if the project is blocked.

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[isBlocked](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#isblocked)

___

### name

• **name**: `string`

The project name.

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[name](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#name)

___

### org

• `Optional` **org**: `IOrg`

The organization associated with the project.

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[org](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#org)

___

### role

• `Optional` **role**: `string`

The role of the project.

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[role](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#role)

___

### updatedAt

• **updatedAt**: `IDate`

The last update date.

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[updatedAt](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#updatedat)

## Accessors

### accountId

• `get` **accountId**(): `string`

Gets the account ID associated with the project.

#### Returns

`string`

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[accountId](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#accountid)

___

### orgId

• `get` **orgId**(): `string`

Gets the organization ID associated with the project.

#### Returns

`string`

#### Implementation of

[IProject](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md).[orgId](../interfaces/sdkApi_interfaces_entities_iProject.IProject.md#orgid)
