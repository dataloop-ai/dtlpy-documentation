# Interface: IProject

[interfaces](./index.md).IProject

An interface representing a Project object, extending the IEntity interface.

**`Interface`**

IProject

## Hierarchy

- [`IEntity`](sdkApi_interfaces_entities_base.IEntity.md)

  ↳ **`IProject`**

## Implemented by

- [`SDKProject`](../classes/sdkApi_interfaces_entities_iProject.SDKProject.md)

## Table of contents

### Properties

- [account](sdkApi_interfaces_entities_iProject.IProject.md#account)
- [accountId](sdkApi_interfaces_entities_iProject.IProject.md#accountid)
- [clientId](sdkApi_interfaces_entities_iProject.IProject.md#clientid)
- [contributors](sdkApi_interfaces_entities_iProject.IProject.md#contributors)
- [createdAt](sdkApi_interfaces_entities_iProject.IProject.md#createdat)
- [creator](sdkApi_interfaces_entities_iProject.IProject.md#creator)
- [datasetsCount](sdkApi_interfaces_entities_iProject.IProject.md#datasetscount)
- [groups](sdkApi_interfaces_entities_iProject.IProject.md#groups)
- [id](sdkApi_interfaces_entities_iProject.IProject.md#id)
- [isBlocked](sdkApi_interfaces_entities_iProject.IProject.md#isblocked)
- [name](sdkApi_interfaces_entities_iProject.IProject.md#name)
- [org](sdkApi_interfaces_entities_iProject.IProject.md#org)
- [orgId](sdkApi_interfaces_entities_iProject.IProject.md#orgid)
- [role](sdkApi_interfaces_entities_iProject.IProject.md#role)
- [updatedAt](sdkApi_interfaces_entities_iProject.IProject.md#updatedat)
- [updatedBy](sdkApi_interfaces_entities_iProject.IProject.md#updatedby)

## Properties

### account

• `Optional` **account**: `IAccount`

The account associated with the project.

___

### accountId

• `Optional` **accountId**: `string`

The account ID associated with the project.

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[clientId](sdkApi_interfaces_entities_base.IEntity.md#clientid)

___

### contributors

• `Optional` **contributors**: `IUser`[]

The project contributors.

___

### createdAt

• **createdAt**: `IDate`

The creation date.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[createdAt](sdkApi_interfaces_entities_base.IEntity.md#createdat)

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[creator](sdkApi_interfaces_entities_base.IEntity.md#creator)

___

### datasetsCount

• `Optional` **datasetsCount**: `number`

The count of datasets associated with the project.

___

### groups

• `Optional` **groups**: `IGroup`[]

The project groups.

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[id](sdkApi_interfaces_entities_base.IEntity.md#id)

___

### isBlocked

• **isBlocked**: `boolean`

Indicates if the project is blocked.

___

### name

• **name**: `string`

The project name.

___

### org

• `Optional` **org**: `IOrg`

The organization associated with the project.

___

### orgId

• `Optional` **orgId**: `string`

The organization ID associated with the project.

___

### role

• `Optional` **role**: `string`

The role of the project.

___

### updatedAt

• **updatedAt**: `IDate`

The last update date.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedAt](sdkApi_interfaces_entities_base.IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedBy](sdkApi_interfaces_entities_base.IEntity.md#updatedby)
