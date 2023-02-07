# Interface: IContributor

[interfaces](./index.md).IContributor

An interface representing a Contributor object, extending the IEntity interface.

**`Interface`**

IContributor

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IContributor`**

## Implemented by

- [`SDKContributor`](../classes/SDKContributor.md)

## Table of contents

### Properties

- [\_org](IContributor.md#_org)
- [avatar](IContributor.md#avatar)
- [boarded](IContributor.md#boarded)
- [clientId](IContributor.md#clientid)
- [createdAt](IContributor.md#createdat)
- [creator](IContributor.md#creator)
- [email](IContributor.md#email)
- [firstName](IContributor.md#firstname)
- [groupRole](IContributor.md#grouprole)
- [id](IContributor.md#id)
- [interest](IContributor.md#interest)
- [inviteStatus](IContributor.md#invitestatus)
- [lastLogin](IContributor.md#lastlogin)
- [lastName](IContributor.md#lastname)
- [orgRole](IContributor.md#orgrole)
- [project](IContributor.md#project)
- [role](IContributor.md#role)
- [timezone](IContributor.md#timezone)
- [type](IContributor.md#type)
- [updatedAt](IContributor.md#updatedat)
- [updatedBy](IContributor.md#updatedby)

## Properties

### \_org

• **\_org**: `string`

The identifier of the organization the contributor belongs to

___

### avatar

• **avatar**: `string`

The URL of the avatar image of the contributor

___

### boarded

• **boarded**: `boolean`

Whether the contributor has completed the onboarding process

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### createdAt

• **createdAt**: `IDate`

The date and time when the contributor was created

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

#### Inherited from

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### email

• **email**: `string`

The email address of the contributor

___

### firstName

• **firstName**: `string`

The first name of the contributor

___

### groupRole

• **groupRole**: `string`

The role of the contributor within a group

___

### id

• **id**: `string`

The unique identifier of the contributor (email)

#### Overrides

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### interest

• **interest**: `UserInterestType`

The areas of interest of the contributor (e.g. "dataManagement")

___

### inviteStatus

• `Optional` **inviteStatus**: `string`

The status of the invitation sent to the contributor

___

### lastLogin

• **lastLogin**: `number`

The timestamp of the last login of the contributor

___

### lastName

• **lastName**: `string`

The last name of the contributor

___

### orgRole

• **orgRole**: `string`

The role of the contributor within their organization

___

### project

• **project**: `string`

The identifier of the project the contributor is associated with

___

### role

• **role**: `string`

The role of the contributor within the project

___

### timezone

• `Optional` **timezone**: `string`

The timezone of the contributor

___

### type

• **type**: `string`

The type of the contributor

___

### updatedAt

• `Optional` **updatedAt**: `IDate`

The date and time when the Entity was last updated.

#### Inherited from

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)
