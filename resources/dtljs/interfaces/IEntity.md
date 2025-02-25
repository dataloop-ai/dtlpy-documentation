# Interface: IEntity

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- **`IEntity`**

  ↳ [`IAnnotation`](IAnnotation.md)

  ↳ [`IRecipe`](IRecipe.md)

  ↳ [`ILabelTreeNode`](ILabelTreeNode.md)

  ↳ [`IOntology`](IOntology.md)

  ↳ [`IItem`](IItem.md)

  ↳ [`IStructure`](IStructure.md)

  ↳ [`IAttributeSection`](IAttributeSection.md)

  ↳ [`IExecution`](IExecution.md)

  ↳ [`IDataset`](IDataset.md)

  ↳ [`IProject`](IProject.md)

  ↳ [`IUser`](IUser.md)

  ↳ [`IContributor`](IContributor.md)

  ↳ [`IGroup`](IGroup.md)

  ↳ [`IAccount`](IAccount.md)

  ↳ [`IOrg`](IOrg.md)

  ↳ [`ITask`](ITask.md)

  ↳ [`IDriver`](IDriver.md)

  ↳ [`IIntegration`](IIntegration.md)

  ↳ [`IPipeline`](IPipeline.md)

## Table of contents

### Properties

- [id](IEntity.md#id)
- [clientId](IEntity.md#clientid)
- [creator](IEntity.md#creator)
- [createdAt](IEntity.md#createdat)
- [updatedAt](IEntity.md#updatedat)
- [updatedBy](IEntity.md#updatedby)

## Properties

### id

• **id**: `string`

A globally unique identifier for the Entity.

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

___

### createdAt

• `Optional` **createdAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was created.

___

### updatedAt

• `Optional` **updatedAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was last updated.

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.
