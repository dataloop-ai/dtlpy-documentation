# Class: APIRecipeV2

An interface representing an Entity object.

**`Interface`**

IEntity

## Implements

- [`IRecipe`](../interfaces/IRecipe.md)

## Table of contents

### Constructors

- [constructor](APIRecipeV2.md#constructor)

### Properties

- [description](APIRecipeV2.md#description)
- [id](APIRecipeV2.md#id)
- [createdAt](APIRecipeV2.md#createdat)
- [updatedAt](APIRecipeV2.md#updatedat)
- [updatedBy](APIRecipeV2.md#updatedby)
- [labelScript](APIRecipeV2.md#labelscript)
- [creator](APIRecipeV2.md#creator)
- [metadata](APIRecipeV2.md#metadata)
- [ontology](APIRecipeV2.md#ontology)
- [projectIds](APIRecipeV2.md#projectids)
- [taskIds](APIRecipeV2.md#taskids)
- [title](APIRecipeV2.md#title)
- [toolsSettings](APIRecipeV2.md#toolssettings)
- [uiSettings](APIRecipeV2.md#uisettings)
- [v2](APIRecipeV2.md#v2)

### Accessors

- [ontologyId](APIRecipeV2.md#ontologyid)
- [attributes](APIRecipeV2.md#attributes)

## Constructors

### constructor

• **new APIRecipeV2**(`recipe`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `recipe` | `Partial`<[`APIRecipeV2`](APIRecipeV2.md)\> |

## Properties

### description

• **description**: `string`

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[description](../interfaces/IRecipe.md#description)

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[id](../interfaces/IRecipe.md#id)

___

### createdAt

• `Optional` **createdAt**: `Date`

The date and time when the Entity was created.

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[createdAt](../interfaces/IRecipe.md#createdat)

___

### updatedAt

• `Optional` **updatedAt**: `Date`

The date and time when the Entity was last updated.

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[updatedAt](../interfaces/IRecipe.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[updatedBy](../interfaces/IRecipe.md#updatedby)

___

### labelScript

• **labelScript**: `string`

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[labelScript](../interfaces/IRecipe.md#labelscript)

___

### creator

• **creator**: `string`

The creator of the Entity.

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[creator](../interfaces/IRecipe.md#creator)

___

### metadata

• **metadata**: [`IRecipeMetaData`](../interfaces/IRecipeMetaData.md)

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[metadata](../interfaces/IRecipe.md#metadata)

___

### ontology

• **ontology**: [`IRecipeOntology`](../interfaces/IRecipeOntology.md)

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[ontology](../interfaces/IRecipe.md#ontology)

___

### projectIds

• **projectIds**: `string`[]

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[projectIds](../interfaces/IRecipe.md#projectids)

___

### taskIds

• **taskIds**: `string`[]

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[taskIds](../interfaces/IRecipe.md#taskids)

___

### title

• **title**: `string`

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[title](../interfaces/IRecipe.md#title)

___

### toolsSettings

• **toolsSettings**: `Dictionary`

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[toolsSettings](../interfaces/IRecipe.md#toolssettings)

___

### uiSettings

• **uiSettings**: `Dictionary`

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[uiSettings](../interfaces/IRecipe.md#uisettings)

___

### v2

• **v2**: ``true``

#### Implementation of

[IRecipe](../interfaces/IRecipe.md).[v2](../interfaces/IRecipe.md#v2)

## Accessors

### ontologyId

• `get` **ontologyId**(): `string`

#### Returns

`string`

___

### attributes

• `get` **attributes**(): `string`[]

#### Returns

`string`[]
