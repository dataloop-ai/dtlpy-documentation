# Interface: ILabelTreeNode

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`ILabelTreeNode`**

## Implemented by

- [`APILabelTreeNodeV2`](../classes/APILabelTreeNodeV2.md)

## Table of contents

### Properties

- [id](ILabelTreeNode.md#id)
- [clientId](ILabelTreeNode.md#clientid)
- [createdAt](ILabelTreeNode.md#createdat)
- [updatedAt](ILabelTreeNode.md#updatedat)
- [updatedBy](ILabelTreeNode.md#updatedby)
- [parent](ILabelTreeNode.md#parent)
- [root](ILabelTreeNode.md#root)
- [ontologyId](ILabelTreeNode.md#ontologyid)
- [path](ILabelTreeNode.md#path)
- [value](ILabelTreeNode.md#value)
- [hasChildren](ILabelTreeNode.md#haschildren)
- [depth](ILabelTreeNode.md#depth)
- [creator](ILabelTreeNode.md#creator)

## Properties

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Inherited from

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### createdAt

• `Optional` **createdAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was created.

#### Inherited from

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### updatedAt

• `Optional` **updatedAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was last updated.

#### Inherited from

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)

___

### parent

• **parent**: `string`

___

### root

• **root**: `string`

___

### ontologyId

• **ontologyId**: `string`

___

### path

• **path**: `string`

___

### value

• **value**: [`APILabelV2`](../classes/APILabelV2.md)

___

### hasChildren

• `Optional` **hasChildren**: `boolean`

___

### depth

• **depth**: `number`

___

### creator

• **creator**: `string`

The creator of the Entity.

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)
