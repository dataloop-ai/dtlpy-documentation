# Class: SDKContributor

[entities](./entities.md).SDKContributor

Represents a contributor instance within the SDK.

## Implements

- [`IContributor`](../interfaces/IContributor.md)

## Table of contents

### Constructors

- [constructor](SDKContributor.md#constructor)

### Properties

- [\_org](SDKContributor.md#_org)
- [avatar](SDKContributor.md#avatar)
- [boarded](SDKContributor.md#boarded)
- [createdAt](SDKContributor.md#createdat)
- [email](SDKContributor.md#email)
- [firstName](SDKContributor.md#firstname)
- [groupRole](SDKContributor.md#grouprole)
- [id](SDKContributor.md#id)
- [interest](SDKContributor.md#interest)
- [inviteStatus](SDKContributor.md#invitestatus)
- [lastLogin](SDKContributor.md#lastlogin)
- [lastName](SDKContributor.md#lastname)
- [orgRole](SDKContributor.md#orgrole)
- [project](SDKContributor.md#project)
- [role](SDKContributor.md#role)
- [type](SDKContributor.md#type)

## Constructors

### constructor

• **new SDKContributor**(`contributor`)

Creates an instance of SDKContributor.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `contributor` | `Partial`<[`SDKContributor`](SDKContributor.md)> | The contributor properties. |

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
