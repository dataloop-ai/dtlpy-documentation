# Class: SDKContributor

Represents a contributor instance within the SDK.

**`Implements`**

## Implements

- [`IContributor`](../interfaces/IContributor.md)

## Table of contents

### Properties

- [\_org](SDKContributor.md#_org)
- [avatar](SDKContributor.md#avatar)
- [boarded](SDKContributor.md#boarded)
- [email](SDKContributor.md#email)
- [firstName](SDKContributor.md#firstname)
- [groupRole](SDKContributor.md#grouprole)
- [id](SDKContributor.md#id)
- [interest](SDKContributor.md#interest)
- [lastLogin](SDKContributor.md#lastlogin)
- [lastName](SDKContributor.md#lastname)
- [orgRole](SDKContributor.md#orgrole)
- [project](SDKContributor.md#project)
- [role](SDKContributor.md#role)
- [type](SDKContributor.md#type)
- [createdAt](SDKContributor.md#createdat)
- [inviteStatus](SDKContributor.md#invitestatus)

### Constructors

- [constructor](SDKContributor.md#constructor)

## Properties

### \_org

• **\_org**: `string`

The identifier of the organization the contributor belongs to

#### Implementation of

[IContributor](../interfaces/IContributor.md).[_org](../interfaces/IContributor.md#_org)

___

### avatar

• **avatar**: `string`

URL for the contributor's avatar

#### Implementation of

[IContributor](../interfaces/IContributor.md).[avatar](../interfaces/IContributor.md#avatar)

___

### boarded

• **boarded**: `boolean`

Indicates if the contributor has been onboarded

#### Implementation of

[IContributor](../interfaces/IContributor.md).[boarded](../interfaces/IContributor.md#boarded)

___

### email

• **email**: `string`

The contributor's email

#### Implementation of

[IContributor](../interfaces/IContributor.md).[email](../interfaces/IContributor.md#email)

___

### firstName

• **firstName**: `string`

The contributor's first name

#### Implementation of

[IContributor](../interfaces/IContributor.md).[firstName](../interfaces/IContributor.md#firstname)

___

### groupRole

• **groupRole**: `string`

The contributor's role within a group

#### Implementation of

[IContributor](../interfaces/IContributor.md).[groupRole](../interfaces/IContributor.md#grouprole)

___

### id

• **id**: `string`

The unique identifier for the contributor (email)

#### Implementation of

[IContributor](../interfaces/IContributor.md).[id](../interfaces/IContributor.md#id)

___

### interest

• **interest**: `string`

The areas of interest of the contributor (e.g. "dataManagement")

#### Implementation of

[IContributor](../interfaces/IContributor.md).[interest](../interfaces/IContributor.md#interest)

___

### lastLogin

• **lastLogin**: `number`

The date and time of the contributor's last login

#### Implementation of

[IContributor](../interfaces/IContributor.md).[lastLogin](../interfaces/IContributor.md#lastlogin)

___

### lastName

• **lastName**: `string`

The contributor's last name

#### Implementation of

[IContributor](../interfaces/IContributor.md).[lastName](../interfaces/IContributor.md#lastname)

___

### orgRole

• **orgRole**: `string`

The contributor's role within the organization

#### Implementation of

[IContributor](../interfaces/IContributor.md).[orgRole](../interfaces/IContributor.md#orgrole)

___

### project

• **project**: `string`

The identifier of the project the contributor is associated with

#### Implementation of

[IContributor](../interfaces/IContributor.md).[project](../interfaces/IContributor.md#project)

___

### role

• **role**: `string`

The contributor's role within the project

#### Implementation of

[IContributor](../interfaces/IContributor.md).[role](../interfaces/IContributor.md#role)

___

### type

• **type**: `string`

The type of the contributor

#### Implementation of

[IContributor](../interfaces/IContributor.md).[type](../interfaces/IContributor.md#type)

___

### createdAt

• **createdAt**: `number`

The date and time when the contributor was created

#### Implementation of

[IContributor](../interfaces/IContributor.md).[createdAt](../interfaces/IContributor.md#createdat)

___

### inviteStatus

• `Optional` **inviteStatus**: `string`

The status of the invitation sent to the contributor

#### Implementation of

[IContributor](../interfaces/IContributor.md).[inviteStatus](../interfaces/IContributor.md#invitestatus)

## Constructors

### constructor

• **new SDKContributor**(`contributor`)

Creates an instance of SDKContributor.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `contributor` | `Partial`<[`SDKContributor`](SDKContributor.md)\> | The contributor properties. |
