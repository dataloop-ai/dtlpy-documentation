# Interface: RecipePayloadV2

## Table of contents

### Properties

- [title](RecipePayloadV2.md#title)
- [projectIds](RecipePayloadV2.md#projectids)
- [description](RecipePayloadV2.md#description)
- [taskIds](RecipePayloadV2.md#taskids)
- [ontology](RecipePayloadV2.md#ontology)
- [labelScript](RecipePayloadV2.md#labelscript)
- [toolsSettings](RecipePayloadV2.md#toolssettings)
- [uiSettings](RecipePayloadV2.md#uisettings)
- [metadata](RecipePayloadV2.md#metadata)

## Properties

### title

• **title**: `string`

___

### projectIds

• **projectIds**: `string`[]

___

### description

• `Optional` **description**: `string`

___

### taskIds

• `Optional` **taskIds**: `string`[]

___

### ontology

• **ontology**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `ontologyId` | `string` |
| `labelScope?` | [`ILabelScope`](ILabelScope.md) |
| `attributes?` | `string`[] |
| `structureIds?` | `string`[] |

___

### labelScript

• `Optional` **labelScript**: `string`

___

### toolsSettings

• `Optional` **toolsSettings**: `Dictionary`

___

### uiSettings

• `Optional` **uiSettings**: `Dictionary`

___

### metadata

• `Optional` **metadata**: [`IRecipeMetaData`](IRecipeMetaData.md)
