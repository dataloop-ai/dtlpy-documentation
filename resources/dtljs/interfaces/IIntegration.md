# Interface: IIntegration

An interface representing a integration object.

**`Interface`**

IIntegration

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IIntegration`**

## Implemented by

- [`SDKIntegration`](../classes/SDKIntegration.md)

## Table of contents

### Properties

- [clientId](IIntegration.md#clientid)
- [updatedBy](IIntegration.md#updatedby)
- [id](IIntegration.md#id)
- [name](IIntegration.md#name)
- [createdAt](IIntegration.md#createdat)
- [updatedAt](IIntegration.md#updatedat)
- [type](IIntegration.md#type)
- [orgId](IIntegration.md#orgid)
- [iconUrl](IIntegration.md#iconurl)
- [creator](IIntegration.md#creator)
- [metadata](IIntegration.md#metadata)

## Properties

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)

___

### id

• **id**: `string`

The integration id

#### Overrides

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### name

• **name**: `string`

The integration name

___

### createdAt

• **createdAt**: `string` \| `number`

The date and time when the integration was created.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### updatedAt

• **updatedAt**: `string` \| `number`

The date and time when the integration was last updated.

#### Overrides

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### type

• **type**: `string`

The integration type

___

### orgId

• **orgId**: `string`

The organization id the integration belongs to

___

### iconUrl

• `Optional` **iconUrl**: `string`

The integration icon url

___

### creator

• **creator**: `string`

The user who created the integration

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### metadata

• `Optional` **metadata**: `any`

The integration metadata
