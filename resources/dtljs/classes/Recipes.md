# Class: Recipes

[appLib/SDKDrivers/xFrameDriver/recipes](../modules/appLib_SDKDrivers_xFrameDriver_recipes.md).Recipes

Recipes repository --- *currently not supported*

The Recipe class allows you to manage the recipes of the app.

**`Implements`**

IBundle<APIRecipeV2>

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Recipes`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<`APIRecipeV2`\>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#constructor)

### Methods

- [calcLabelsHaveAttributes](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#calclabelshaveattributes)
- [clone](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#clone)
- [create](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#create)
- [crudReq](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#crudreqsync)
- [delete](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#delete)
- [doesLabelHaveAttributes](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#doeslabelhaveattributes)
- [get](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#get)
- [getLabelAttributes](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#getlabelattributes)
- [missingRequiredAttribute](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#missingrequiredattribute)
- [query](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#query)
- [update](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#update)

## Constructors

### constructor

• **new Recipes**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### calcLabelsHaveAttributes

▸ **calcLabelsHaveAttributes**(`payload`): `Promise`<`void`\>

Calculates the labels that have attributes on the studio's side.

**`Example`**

```ts
await dl.recipes.calcLabelsHaveAttributes({ label: 'label-1' })
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Object` |  |
| `payload.label` | `string` | The label to check. |
| `payload.recipeId?` | `string` | The id of the recipe to check. |

#### Returns

`Promise`<`void`\>

- A promise that resolves when the calculation is done.

#### Implementation of

IBundle.calcLabelsHaveAttributes

___

### clone

▸ **clone**(`recipeId`): `Promise`<`APIRecipeV2`\>

Clones a recipe.

**`Example`**

```ts
const recipe = await dl.recipes.clone('recipeId-1')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `recipeId` | `string` | The id of the recipe to clone. |

#### Returns

`Promise`<`APIRecipeV2`\>

- A promise that resolves to the cloned recipe.

___

### create

▸ **create**(`payload`): `Promise`<`APIRecipeV2`\>

Creates a new recipe.

**`Example`**

```ts
const recipe = await dl.recipes.create({
 title: 'My recipe'
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `any` | The payload to create the recipe. |

#### Returns

`Promise`<`APIRecipeV2`\>

- A promise that resolves to the created recipe.

#### Implementation of

IBundle.create

___

### crudReq

▸ **crudReq**(`data`): `void`

Sends a CRUD request to the xFrame.

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `any` |

#### Returns

`void`

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[crudReq](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#crudreq)

___

### crudReqSync

▸ **crudReqSync**(`data`, `options?`): `Promise`<`any`\>

Sends a CRUD request to the xFrame.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `data` | `any` | The data to send. |
| `options` | `Object` |  |
| `options.timeout?` | `number` | an option to set the timeout for the request. |

#### Returns

`Promise`<`any`\>

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[crudReqSync](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#crudreqsync)

___

### delete

▸ **delete**(`recipeId`): `Promise`<`void`\>

Deletes a specific recipe by its id.

**`Example`**

```ts
await dl.recipes.delete('recipeId-1')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `recipeId` | `string` | The id of the recipe to delete. |

#### Returns

`Promise`<`void`\>

- A promise that resolves when the recipe has been deleted.

#### Implementation of

IBundle.delete

___

### doesLabelHaveAttributes

▸ **doesLabelHaveAttributes**(`payload`): `Promise`<`boolean`\>

Checks if a label has attributes.

**`Example`**

```ts
const hasAttributes = await dl.recipes.doesLabelHaveAttributes({ label: 'label-1' })
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Object` |  |
| `payload.label` | `string` | The label to check. |
| `payload.recipeId?` | `string` | The id of the recipe to check. |

#### Returns

`Promise`<`boolean`\>

- A promise that resolves to a boolean indicating if the label has attributes.

#### Implementation of

IBundle.doesLabelHaveAttributes

___

### get

▸ **get**(`id?`): `Promise`<`APIRecipeV2`\>

Retrieves a recipe by id.

If the recipe id is not provided, the active recipe will be returned.

**`Example`**

```ts
const activeRecipe = await dl.recipes.get()
```

**`Example`**

```ts
const recipe = await dl.recipes.get('recipeId-1')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id?` | `string` | The id of the recipe to get. |

#### Returns

`Promise`<`APIRecipeV2`\>

- A promise that resolves to the queried recipe.

#### Implementation of

IBundle.get

___

### getLabelAttributes

▸ **getLabelAttributes**(`label`): `Promise`<`SDKAttributeInstruction`[]\>

Gets the attributes of a label.

**`Example`**

```ts
const attributes = await dl.recipes.getLabelAttributes('label-1')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `label` | `string` | The label to get the attributes of. |

#### Returns

`Promise`<`SDKAttributeInstruction`[]\>

- A promise that resolves to the attributes of the label.

___

### missingRequiredAttribute

▸ **missingRequiredAttribute**(`annotationId`): `Promise`<`boolean`\>

Checks if an annotation is missing a required attribute.

**`Example`**

```ts
const missing = await dl.recipes.missingRequiredAttribute('clientId-1')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `annotationId` | `string` | The clientId of the annotation to check. |

#### Returns

`Promise`<`boolean`\>

- A promise that resolves to a boolean indicating if the annotation is missing a required attribute.

#### Implementation of

IBundle.missingRequiredAttribute

___

### query

▸ **query**(`payload?`): `Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<`APIRecipeV2`\>\>

Lists all recipes.

**`Example`**

```ts
const pagedResponse = await dl.recipes.query({ projectIds: ['projectId-1'] })
const recipes = pagedResponse.items
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload?` | `Partial`<`APIRecipeV2`\> | An Object containing the possible projectIds filter. |

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<`APIRecipeV2`\>\>

- A promise that resolves to a paged response with the queried recipes.

#### Implementation of

IBundle.query

___

### update

▸ **update**(`payload`): `Promise`<`APIRecipeV2`\>

Updates a recipe.

**`Example`**

```ts
const recipe = await dl.recipes.update({
     id: 'recipeId-1',
     title: 'My updated recipe'
})
console.log(recipe.title) // 'My updated recipe'
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Partial`<`APIRecipeV2`\> | The payload to update the recipe. |

#### Returns

`Promise`<`APIRecipeV2`\>

- A promise that resolves to the updated recipe.

#### Implementation of

IBundle.update
