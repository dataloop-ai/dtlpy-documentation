# Class: APIOntologyV2

An interface representing an Entity object.

**`Interface`**

IEntity

## Implements

- [`IOntology`](../interfaces/IOntology.md)

## Table of contents

### Properties

- [attributes](APIOntologyV2.md#attributes)
- [id](APIOntologyV2.md#id)
- [metadata](APIOntologyV2.md#metadata)
- [roots](APIOntologyV2.md#roots)
- [title](APIOntologyV2.md#title)
- [creator](APIOntologyV2.md#creator)
- [structureIds](APIOntologyV2.md#structureids)
- [createdAt](APIOntologyV2.md#createdat)
- [updatedAt](APIOntologyV2.md#updatedat)
- [updatedBy](APIOntologyV2.md#updatedby)
- [v2](APIOntologyV2.md#v2)

### Constructors

- [constructor](APIOntologyV2.md#constructor)

### Methods

- [toJSON](APIOntologyV2.md#tojson)

## Properties

### attributes

• **attributes**: `string`[]

#### Implementation of

[IOntology](../interfaces/IOntology.md).[attributes](../interfaces/IOntology.md#attributes)

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Implementation of

[IOntology](../interfaces/IOntology.md).[id](../interfaces/IOntology.md#id)

___

### metadata

• **metadata**: `OntologyMetadata`

#### Implementation of

[IOntology](../interfaces/IOntology.md).[metadata](../interfaces/IOntology.md#metadata)

___

### roots

• **roots**: `string`[]

#### Implementation of

[IOntology](../interfaces/IOntology.md).[roots](../interfaces/IOntology.md#roots)

___

### title

• **title**: `string`

#### Implementation of

[IOntology](../interfaces/IOntology.md).[title](../interfaces/IOntology.md#title)

___

### creator

• **creator**: `string`

The creator of the Entity.

#### Implementation of

[IOntology](../interfaces/IOntology.md).[creator](../interfaces/IOntology.md#creator)

___

### structureIds

• **structureIds**: `string`[]

#### Implementation of

[IOntology](../interfaces/IOntology.md).[structureIds](../interfaces/IOntology.md#structureids)

___

### createdAt

• `Optional` **createdAt**: `Date`

The date and time when the Entity was created.

#### Implementation of

[IOntology](../interfaces/IOntology.md).[createdAt](../interfaces/IOntology.md#createdat)

___

### updatedAt

• `Optional` **updatedAt**: `Date`

The date and time when the Entity was last updated.

#### Implementation of

[IOntology](../interfaces/IOntology.md).[updatedAt](../interfaces/IOntology.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Implementation of

[IOntology](../interfaces/IOntology.md).[updatedBy](../interfaces/IOntology.md#updatedby)

___

### v2

• **v2**: ``true``

## Constructors

### constructor

• **new APIOntologyV2**(`ontology`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `ontology` | `Partial`<[`APIOntologyV2`](APIOntologyV2.md)\> |

## Methods

### toJSON

▸ **toJSON**(): `Object`

#### Returns

`Object`

| Name | Type |
| :------ | :------ |
| `id` | `string` |
| `creator` | `string` |
| `title` | `string` |
| `roots` | `string`[] |
| `structureIds` | `string`[] |
| `metadata` | `OntologyMetadata` |
| `attributes` | `string`[] |
| `createdAt` | `Date` |
| `updatedAt` | `Date` |
| `updatedBy` | `string` |
| `v2` | ``true`` |
