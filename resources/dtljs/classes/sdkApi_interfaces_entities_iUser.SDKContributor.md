# Class: SDKContributor

[dl.entities](./index.md).SDKContributor

Represents a contributor instance within the SDK.

## Implements

- [`IContributor`](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md)

## Table of contents

### Constructors

- [constructor](sdkApi_interfaces_entities_iUser.SDKContributor.md#constructor)

### Properties

- [\_org](sdkApi_interfaces_entities_iUser.SDKContributor.md#_org)
- [avatar](sdkApi_interfaces_entities_iUser.SDKContributor.md#avatar)
- [boarded](sdkApi_interfaces_entities_iUser.SDKContributor.md#boarded)
- [createdAt](sdkApi_interfaces_entities_iUser.SDKContributor.md#createdat)
- [email](sdkApi_interfaces_entities_iUser.SDKContributor.md#email)
- [firstName](sdkApi_interfaces_entities_iUser.SDKContributor.md#firstname)
- [groupRole](sdkApi_interfaces_entities_iUser.SDKContributor.md#grouprole)
- [id](sdkApi_interfaces_entities_iUser.SDKContributor.md#id)
- [interest](sdkApi_interfaces_entities_iUser.SDKContributor.md#interest)
- [inviteStatus](sdkApi_interfaces_entities_iUser.SDKContributor.md#invitestatus)
- [lastLogin](sdkApi_interfaces_entities_iUser.SDKContributor.md#lastlogin)
- [lastName](sdkApi_interfaces_entities_iUser.SDKContributor.md#lastname)
- [orgRole](sdkApi_interfaces_entities_iUser.SDKContributor.md#orgrole)
- [project](sdkApi_interfaces_entities_iUser.SDKContributor.md#project)
- [role](sdkApi_interfaces_entities_iUser.SDKContributor.md#role)
- [type](sdkApi_interfaces_entities_iUser.SDKContributor.md#type)

## Constructors

### constructor

• **new SDKContributor**(`contributor`)

Creates an instance of SDKContributor.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `contributor` | `Partial`<[`SDKContributor`](sdkApi_interfaces_entities_iUser.SDKContributor.md)> | The contributor properties. |

## Properties

### \_org

• **\_org**: `string`

The identifier of the organization the contributor belongs to

___

### avatar

• **avatar**: `string`

URL for the contributor's avatar

___

### boarded

• **boarded**: `boolean`

Indicates if the contributor has been onboarded

___

### createdAt

• **createdAt**: `number`

The date and time when the contributor was created

___

### email

• **email**: `string`

The contributor's email

___

### firstName

• **firstName**: `string`

The contributor's first name

___

### groupRole

• **groupRole**: `string`

The contributor's role within a group

___

### id

• **id**: `string`

The unique identifier for the contributor (email)

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

The date and time of the contributor's last login

___

### lastName

• **lastName**: `string`

The contributor's last name

___

### orgRole

• **orgRole**: `string`

The contributor's role within the organization

___

### project

• **project**: `string`

The identifier of the project the contributor is associated with

___

### role

• **role**: `string`

The contributor's role within the project

___

### type

• **type**: `string`

The type of the contributor
