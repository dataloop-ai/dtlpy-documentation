# Interface: IContributor

[interfaces](./index.md).IContributor

An interface representing a Contributor object, extending the IEntity interface.

**`Interface`**

IContributor

## Hierarchy

- [`IEntity`](sdkApi_interfaces_entities_base.IEntity.md)

  ↳ **`IContributor`**

## Implemented by

- [`SDKContributor`](../classes/sdkApi_interfaces_entities_iUser.SDKContributor.md)

## Table of contents

### Properties

- [\_org](sdkApi_interfaces_entities_iUser.IContributor.md#_org)
- [avatar](sdkApi_interfaces_entities_iUser.IContributor.md#avatar)
- [boarded](sdkApi_interfaces_entities_iUser.IContributor.md#boarded)
- [clientId](sdkApi_interfaces_entities_iUser.IContributor.md#clientid)
- [createdAt](sdkApi_interfaces_entities_iUser.IContributor.md#createdat)
- [creator](sdkApi_interfaces_entities_iUser.IContributor.md#creator)
- [email](sdkApi_interfaces_entities_iUser.IContributor.md#email)
- [firstName](sdkApi_interfaces_entities_iUser.IContributor.md#firstname)
- [groupRole](sdkApi_interfaces_entities_iUser.IContributor.md#grouprole)
- [id](sdkApi_interfaces_entities_iUser.IContributor.md#id)
- [interest](sdkApi_interfaces_entities_iUser.IContributor.md#interest)
- [inviteStatus](sdkApi_interfaces_entities_iUser.IContributor.md#invitestatus)
- [lastLogin](sdkApi_interfaces_entities_iUser.IContributor.md#lastlogin)
- [lastName](sdkApi_interfaces_entities_iUser.IContributor.md#lastname)
- [orgRole](sdkApi_interfaces_entities_iUser.IContributor.md#orgrole)
- [project](sdkApi_interfaces_entities_iUser.IContributor.md#project)
- [role](sdkApi_interfaces_entities_iUser.IContributor.md#role)
- [timezone](sdkApi_interfaces_entities_iUser.IContributor.md#timezone)
- [type](sdkApi_interfaces_entities_iUser.IContributor.md#type)
- [updatedAt](sdkApi_interfaces_entities_iUser.IContributor.md#updatedat)
- [updatedBy](sdkApi_interfaces_entities_iUser.IContributor.md#updatedby)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[clientId](sdkApi_interfaces_entities_base.IEntity.md#clientid)

___

### createdAt

• **createdAt**: `IDate`

The date and time when the contributor was created

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[createdAt](sdkApi_interfaces_entities_base.IEntity.md#createdat)

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[creator](sdkApi_interfaces_entities_base.IEntity.md#creator)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[id](sdkApi_interfaces_entities_base.IEntity.md#id)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedAt](sdkApi_interfaces_entities_base.IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedBy](sdkApi_interfaces_entities_base.IEntity.md#updatedby)
