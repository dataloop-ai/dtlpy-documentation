# Interface: IIntegration

[sdkApi/interfaces/entities/iIntegration](../modules/sdkApi_interfaces_entities_iIntegration.md).IIntegration

An interface representing a integration object.

**`Interface`**

IIntegration

## Hierarchy

- [`IEntity`](sdkApi_interfaces_entities_base.IEntity.md)

  ↳ **`IIntegration`**

## Table of contents

### Properties

- [clientId](sdkApi_interfaces_entities_iIntegration.IIntegration.md#clientid)
- [createdAt](sdkApi_interfaces_entities_iIntegration.IIntegration.md#createdat)
- [creator](sdkApi_interfaces_entities_iIntegration.IIntegration.md#creator)
- [iconUrl](sdkApi_interfaces_entities_iIntegration.IIntegration.md#iconurl)
- [id](sdkApi_interfaces_entities_iIntegration.IIntegration.md#id)
- [metadata](sdkApi_interfaces_entities_iIntegration.IIntegration.md#metadata)
- [name](sdkApi_interfaces_entities_iIntegration.IIntegration.md#name)
- [orgId](sdkApi_interfaces_entities_iIntegration.IIntegration.md#orgid)
- [type](sdkApi_interfaces_entities_iIntegration.IIntegration.md#type)
- [updatedAt](sdkApi_interfaces_entities_iIntegration.IIntegration.md#updatedat)
- [updatedBy](sdkApi_interfaces_entities_iIntegration.IIntegration.md#updatedby)

## Properties

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[clientId](sdkApi_interfaces_entities_base.IEntity.md#clientid)

___

### createdAt

• **createdAt**: `string` \| `number`

The date and time when the integration was created.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[createdAt](sdkApi_interfaces_entities_base.IEntity.md#createdat)

___

### creator

• **creator**: `string`

The user who created the integration

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[creator](sdkApi_interfaces_entities_base.IEntity.md#creator)

___

### iconUrl

• `Optional` **iconUrl**: `string`

The integration icon url

___

### id

• **id**: `string`

The integration id

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[id](sdkApi_interfaces_entities_base.IEntity.md#id)

___

### metadata

• `Optional` **metadata**: `any`

The integration metadata

___

### name

• **name**: `string`

The integration name

___

### orgId

• **orgId**: `string`

The organization id the integration belongs to

___

### type

• **type**: `string`

The integration type

___

### updatedAt

• **updatedAt**: `string` \| `number`

The date and time when the integration was last updated.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedAt](sdkApi_interfaces_entities_base.IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedBy](sdkApi_interfaces_entities_base.IEntity.md#updatedby)
