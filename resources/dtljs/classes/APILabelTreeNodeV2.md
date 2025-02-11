# Class: APILabelTreeNodeV2

An interface representing an Entity object.

**`Interface`**

IEntity

## Implements

- [`ILabelTreeNode`](../interfaces/ILabelTreeNode.md)

## Table of contents

### Constructors

- [constructor](APILabelTreeNodeV2.md#constructor)

### Properties

- [createdAt](APILabelTreeNodeV2.md#createdat)
- [updatedAt](APILabelTreeNodeV2.md#updatedat)
- [updatedBy](APILabelTreeNodeV2.md#updatedby)
- [depth](APILabelTreeNodeV2.md#depth)
- [id](APILabelTreeNodeV2.md#id)
- [ontologyId](APILabelTreeNodeV2.md#ontologyid)
- [parent](APILabelTreeNodeV2.md#parent)
- [path](APILabelTreeNodeV2.md#path)
- [root](APILabelTreeNodeV2.md#root)
- [value](APILabelTreeNodeV2.md#value)
- [creator](APILabelTreeNodeV2.md#creator)
- [hasChildren](APILabelTreeNodeV2.md#haschildren)

### Methods

- [identifier](APILabelTreeNodeV2.md#identifier)
- [isRoot](APILabelTreeNodeV2.md#isroot)

## Constructors

### constructor

• **new APILabelTreeNodeV2**(`labelTreeNode`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `labelTreeNode` | `Partial`<[`APILabelTreeNodeV2`](APILabelTreeNodeV2.md)\> |

## Properties

### createdAt

• `Optional` **createdAt**: `Date`

The date and time when the Entity was created.

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[createdAt](../interfaces/ILabelTreeNode.md#createdat)

___

### updatedAt

• `Optional` **updatedAt**: `Date`

The date and time when the Entity was last updated.

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[updatedAt](../interfaces/ILabelTreeNode.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[updatedBy](../interfaces/ILabelTreeNode.md#updatedby)

___

### depth

• **depth**: `number`

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[depth](../interfaces/ILabelTreeNode.md#depth)

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[id](../interfaces/ILabelTreeNode.md#id)

___

### ontologyId

• **ontologyId**: `string`

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[ontologyId](../interfaces/ILabelTreeNode.md#ontologyid)

___

### parent

• **parent**: `string`

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[parent](../interfaces/ILabelTreeNode.md#parent)

___

### path

• **path**: `string`

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[path](../interfaces/ILabelTreeNode.md#path)

___

### root

• **root**: `string`

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[root](../interfaces/ILabelTreeNode.md#root)

___

### value

• **value**: [`APILabelV2`](APILabelV2.md)

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[value](../interfaces/ILabelTreeNode.md#value)

___

### creator

• **creator**: `string`

The creator of the Entity.

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[creator](../interfaces/ILabelTreeNode.md#creator)

___

### hasChildren

• `Optional` **hasChildren**: `boolean`

#### Implementation of

[ILabelTreeNode](../interfaces/ILabelTreeNode.md).[hasChildren](../interfaces/ILabelTreeNode.md#haschildren)

## Methods

### identifier

▸ **identifier**(): `string`

#### Returns

`string`

___

### isRoot

▸ **isRoot**(): `boolean`

#### Returns

`boolean`
