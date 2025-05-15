# Interface: IContributor

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

- [clientId](IContributor.md#clientid)
- [creator](IContributor.md#creator)
- [updatedAt](IContributor.md#updatedat)
- [updatedBy](IContributor.md#updatedby)
- [id](IContributor.md#id)
- [email](IContributor.md#email)
- [firstName](IContributor.md#firstname)
- [lastName](IContributor.md#lastname)
- [avatar](IContributor.md#avatar)
- [\_org](IContributor.md#_org)
- [orgRole](IContributor.md#orgrole)
- [lastLogin](IContributor.md#lastlogin)
- [groupRole](IContributor.md#grouprole)
- [type](IContributor.md#type)
- [interest](IContributor.md#interest)
- [boarded](IContributor.md#boarded)
- [timezone](IContributor.md#timezone)
- [project](IContributor.md#project)
- [role](IContributor.md#role)
- [inviteStatus](IContributor.md#invitestatus)
- [createdAt](IContributor.md#createdat)

## Properties

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

### updatedAt

• `Optional` **updatedAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was last updated.

#### Inherited from

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)

___

### id

• **id**: `string`

The unique identifier of the contributor (email)

#### Overrides

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### email

• **email**: `string`

The email address of the contributor

___

### firstName

• **firstName**: `string`

The first name of the contributor

___

### lastName

• **lastName**: `string`

The last name of the contributor

___

### avatar

• **avatar**: `string`

The URL of the avatar image of the contributor

___

### \_org

• **\_org**: `string`

The identifier of the organization the contributor belongs to

___

### orgRole

• **orgRole**: `string`

The role of the contributor within their organization

___

### lastLogin

• **lastLogin**: `number`

The timestamp of the last login of the contributor

___

### groupRole

• **groupRole**: `string`

The role of the contributor within a group

___

### type

• **type**: `string`

The type of the contributor

___

### interest

• **interest**: `string`

The areas of interest of the contributor (e.g. "dataManagement")

___

### boarded

• **boarded**: `boolean`

Whether the contributor has completed the onboarding process

___

### timezone

• `Optional` **timezone**: `string`

The timezone of the contributor

___

### project

• **project**: `string`

The identifier of the project the contributor is associated with

___

### role

• **role**: `string`

The role of the contributor within the project

___

### inviteStatus

• `Optional` **inviteStatus**: `string`

The status of the invitation sent to the contributor

___

### createdAt

• **createdAt**: [`IDate`](../modules.md#idate)

The date and time when the contributor was created

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)
