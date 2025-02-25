# Interface: IProject

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

- [id](IProject.md#id)
- [clientId](IProject.md#clientid)
- [creator](IProject.md#creator)
- [updatedBy](IProject.md#updatedby)
- [name](IProject.md#name)
- [accountId](IProject.md#accountid)
- [orgId](IProject.md#orgid)
- [createdAt](IProject.md#createdat)
- [updatedAt](IProject.md#updatedat)
- [contributors](IProject.md#contributors)
- [groups](IProject.md#groups)
- [datasetsCount](IProject.md#datasetscount)
- [role](IProject.md#role)
- [org](IProject.md#org)
- [account](IProject.md#account)
- [isBlocked](IProject.md#isblocked)

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

The project name.

___

### accountId

• `Optional` **accountId**: `string`

The account ID associated with the project.

___

### orgId

• `Optional` **orgId**: `string`

The organization ID associated with the project.

___

### createdAt

• **createdAt**: [`IDate`](../modules.md#idate)

The creation date.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### updatedAt

• **updatedAt**: [`IDate`](../modules.md#idate)

The last update date.

#### Overrides

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### contributors

• `Optional` **contributors**: [`IUser`](IUser.md)[]

The project contributors.

___

### groups

• `Optional` **groups**: [`IGroup`](IGroup.md)[]

The project groups.

___

### datasetsCount

• `Optional` **datasetsCount**: `number`

The count of datasets associated with the project.

___

### role

• `Optional` **role**: `string`

The role of the project.

___

### org

• `Optional` **org**: [`IOrg`](IOrg.md)

The organization associated with the project.

___

### account

• `Optional` **account**: [`IAccount`](IAccount.md)

The account associated with the project.

___

### isBlocked

• **isBlocked**: `boolean`

Indicates if the project is blocked.
