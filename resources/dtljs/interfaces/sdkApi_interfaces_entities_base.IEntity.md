# Interface: IEntity

[interfaces](./index.md).IEntity

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- **`IEntity`**

  ↳ [`IAnnotation`](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md)

  ↳ [`IDataset`](sdkApi_interfaces_entities_iDataset.IDataset.md)

  ↳ [`IItem`](sdkApi_interfaces_entities_iItem.IItem.md)

  ↳ [`IProject`](sdkApi_interfaces_entities_iProject.IProject.md)

  ↳ [`ITask`](sdkApi_interfaces_entities_iTask.ITask.md)

  ↳ [`IContributor`](sdkApi_interfaces_entities_iUser.IContributor.md)

## Table of contents

### Properties

- [clientId](sdkApi_interfaces_entities_base.IEntity.md#clientid)
- [createdAt](sdkApi_interfaces_entities_base.IEntity.md#createdat)
- [creator](sdkApi_interfaces_entities_base.IEntity.md#creator)
- [id](sdkApi_interfaces_entities_base.IEntity.md#id)
- [updatedAt](sdkApi_interfaces_entities_base.IEntity.md#updatedat)
- [updatedBy](sdkApi_interfaces_entities_base.IEntity.md#updatedby)

## Properties

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

___

### createdAt

• `Optional` **createdAt**: `IDate`

The date and time when the Entity was created.

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

___

### updatedAt

• `Optional` **updatedAt**: `IDate`

The date and time when the Entity was last updated.

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.
