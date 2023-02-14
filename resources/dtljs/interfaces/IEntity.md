# Interface: IEntity

[interfaces](./index.md).IEntity

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- **`IEntity`**

  ↳ [`IAnnotation`](IAnnotation.md)

  ↳ [`IDataset`](IDataset.md)

  ↳ [`IItem`](IItem.md)

  ↳ [`IProject`](IProject.md)

  ↳ [`ITask`](ITask.md)

  ↳ [`IContributor`](IContributor.md)

## Table of contents

### Properties

- [clientId](IEntity.md#clientid)
- [createdAt](IEntity.md#createdat)
- [creator](IEntity.md#creator)
- [id](IEntity.md#id)
- [updatedAt](IEntity.md#updatedat)
- [updatedBy](IEntity.md#updatedby)

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
