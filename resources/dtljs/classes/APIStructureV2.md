# Class: APIStructureV2

An interface representing an Entity object.

**`Interface`**

IEntity

## Implements

- [`IStructure`](../interfaces/IStructure.md)

## Table of contents

### Constructors

- [constructor](APIStructureV2.md#constructor)

### Properties

- [createdAt](APIStructureV2.md#createdat)
- [updatedAt](APIStructureV2.md#updatedat)
- [updatedBy](APIStructureV2.md#updatedby)
- [arcs](APIStructureV2.md#arcs)
- [creator](APIStructureV2.md#creator)
- [id](APIStructureV2.md#id)
- [name](APIStructureV2.md#name)
- [ontologyId](APIStructureV2.md#ontologyid)
- [order](APIStructureV2.md#order)

## Constructors

### constructor

• **new APIStructureV2**(`structure`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `structure` | [`IStructure`](../interfaces/IStructure.md) |

## Properties

### createdAt

• `Optional` **createdAt**: `Date`

The date and time when the Entity was created.

#### Implementation of

[IStructure](../interfaces/IStructure.md).[createdAt](../interfaces/IStructure.md#createdat)

___

### updatedAt

• `Optional` **updatedAt**: `Date`

The date and time when the Entity was last updated.

#### Implementation of

[IStructure](../interfaces/IStructure.md).[updatedAt](../interfaces/IStructure.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Implementation of

[IStructure](../interfaces/IStructure.md).[updatedBy](../interfaces/IStructure.md#updatedby)

___

### arcs

• **arcs**: [`string`, `string`][]

#### Implementation of

[IStructure](../interfaces/IStructure.md).[arcs](../interfaces/IStructure.md#arcs)

___

### creator

• **creator**: `string`

The creator of the Entity.

#### Implementation of

[IStructure](../interfaces/IStructure.md).[creator](../interfaces/IStructure.md#creator)

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Implementation of

[IStructure](../interfaces/IStructure.md).[id](../interfaces/IStructure.md#id)

___

### name

• **name**: `string`

#### Implementation of

[IStructure](../interfaces/IStructure.md).[name](../interfaces/IStructure.md#name)

___

### ontologyId

• **ontologyId**: `string`

#### Implementation of

[IStructure](../interfaces/IStructure.md).[ontologyId](../interfaces/IStructure.md#ontologyid)

___

### order

• **order**: `string`[]

#### Implementation of

[IStructure](../interfaces/IStructure.md).[order](../interfaces/IStructure.md#order)
