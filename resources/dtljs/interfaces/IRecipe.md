# Interface: IRecipe

An interface representing an Entity object.

**`Interface`**

IEntity

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IRecipe`**

## Implemented by

- [`APIRecipeV2`](../classes/APIRecipeV2.md)

## Table of contents

### Properties

- [id](IRecipe.md#id)
- [clientId](IRecipe.md#clientid)
- [title](IRecipe.md#title)
- [creator](IRecipe.md#creator)
- [projectIds](IRecipe.md#projectids)
- [description](IRecipe.md#description)
- [taskIds](IRecipe.md#taskids)
- [ontology](IRecipe.md#ontology)
- [labelScript](IRecipe.md#labelscript)
- [toolsSettings](IRecipe.md#toolssettings)
- [uiSettings](IRecipe.md#uisettings)
- [metadata](IRecipe.md#metadata)
- [createdAt](IRecipe.md#createdat)
- [updatedAt](IRecipe.md#updatedat)
- [updatedBy](IRecipe.md#updatedby)
- [v2](IRecipe.md#v2)

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

### title

• **title**: `string`

___

### creator

• **creator**: `string`

The creator of the Entity.

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### projectIds

• **projectIds**: `string`[]

___

### description

• **description**: `string`

___

### taskIds

• **taskIds**: `string`[]

___

### ontology

• **ontology**: [`IRecipeOntology`](IRecipeOntology.md)

___

### labelScript

• **labelScript**: `string`

___

### toolsSettings

• **toolsSettings**: `Dictionary`

___

### uiSettings

• **uiSettings**: `Dictionary`

___

### metadata

• **metadata**: [`IRecipeMetaData`](IRecipeMetaData.md)

___

### createdAt

• `Optional` **createdAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was created.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### updatedAt

• `Optional` **updatedAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was last updated.

#### Overrides

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Overrides

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)

___

### v2

• `Optional` **v2**: `boolean`
