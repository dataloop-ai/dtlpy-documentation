# Class: SDKContributor

[sdkApi/interfaces/entities/iUser](../modules/sdkApi_interfaces_entities_iUser.md).SDKContributor

Represents a contributor instance within the SDK.

**`Implements`**

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
| `contributor` | `Partial`<[`SDKContributor`](sdkApi_interfaces_entities_iUser.SDKContributor.md)\> | The contributor properties. |

## Properties

### \_org

• **\_org**: `string`

The identifier of the organization the contributor belongs to

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[_org](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#_org)

___

### avatar

• **avatar**: `string`

URL for the contributor's avatar

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[avatar](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#avatar)

___

### boarded

• **boarded**: `boolean`

Indicates if the contributor has been onboarded

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[boarded](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#boarded)

___

### createdAt

• **createdAt**: `number`

The date and time when the contributor was created

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[createdAt](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#createdat)

___

### email

• **email**: `string`

The contributor's email

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[email](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#email)

___

### firstName

• **firstName**: `string`

The contributor's first name

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[firstName](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#firstname)

___

### groupRole

• **groupRole**: `string`

The contributor's role within a group

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[groupRole](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#grouprole)

___

### id

• **id**: `string`

The unique identifier for the contributor (email)

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[id](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#id)

___

### interest

• **interest**: `string`

The areas of interest of the contributor (e.g. "dataManagement")

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[interest](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#interest)

___

### inviteStatus

• `Optional` **inviteStatus**: `string`

The status of the invitation sent to the contributor

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[inviteStatus](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#invitestatus)

___

### lastLogin

• **lastLogin**: `number`

The date and time of the contributor's last login

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[lastLogin](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#lastlogin)

___

### lastName

• **lastName**: `string`

The contributor's last name

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[lastName](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#lastname)

___

### orgRole

• **orgRole**: `string`

The contributor's role within the organization

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[orgRole](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#orgrole)

___

### project

• **project**: `string`

The identifier of the project the contributor is associated with

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[project](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#project)

___

### role

• **role**: `string`

The contributor's role within the project

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[role](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#role)

___

### type

• **type**: `string`

The type of the contributor

#### Implementation of

[IContributor](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md).[type](../interfaces/sdkApi_interfaces_entities_iUser.IContributor.md#type)
