# Interface: IProject

[interfaces](./index.md).IProject

An interface representing a Project object, extending the IEntity interface.

**`Interface`**

IProject

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IProject`**

## Implemented by

- [`SDKProject`](../classes/SDKProject.md)

## Table of contents

### Properties

- [account](IProject.md#account)
- [accountId](IProject.md#accountid)
- [clientId](IProject.md#clientid)
- [contributors](IProject.md#contributors)
- [createdAt](IProject.md#createdat)
- [creator](IProject.md#creator)
- [datasetsCount](IProject.md#datasetscount)
- [groups](IProject.md#groups)
- [id](IProject.md#id)
- [isBlocked](IProject.md#isblocked)
- [name](IProject.md#name)
- [org](IProject.md#org)
- [orgId](IProject.md#orgid)
- [role](IProject.md#role)
- [updatedAt](IProject.md#updatedat)
- [updatedBy](IProject.md#updatedby)

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

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### contributors

• `Optional` **contributors**: `IUser`[]

The project contributors.

___

### createdAt

• **createdAt**: `IDate`

The creation date.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

#### Inherited from

[IEntity](IEntity.md).[creator](IEntity.md#creator)

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

[IEntity](IEntity.md).[id](IEntity.md#id)

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

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)
