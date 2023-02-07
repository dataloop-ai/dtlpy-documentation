# Class: Recipes

[dl.repositories](./index.md).Recipes

Recipes repository --- *currently not supported*

The Recipe class allows you to manage the recipes of the app.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Recipes`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<`APIRecipeV2`>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#constructor)

### Methods

- [clone](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#clone)
- [create](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#create)
- [crudReq](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#crudreqsync)
- [delete](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#delete)
- [get](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md#get)
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

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)
.[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### clone

▸ **clone**(`recipeId`): `Promise`<`APIRecipeV2`>

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

`Promise`<`APIRecipeV2`>

- A promise that resolves to the cloned recipe.

___

### create

▸ **create**(`payload`): `Promise`<`APIRecipeV2`>

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
| `payload` | `Partial`<`APIRecipeV2`> | The payload to create the recipe. |

#### Returns

`Promise`<`APIRecipeV2`>

- A promise that resolves to the created recipe.

___

### delete

▸ **delete**(`recipeId`): `Promise`<`void`>

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

`Promise`<`void`>

- A promise that resolves when the recipe has been deleted.

___

### get

▸ **get**(`id`): `Promise`<`APIRecipeV2`>

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
| `id` | `string` | The id of the recipe to get. |

#### Returns

`Promise`<`APIRecipeV2`>

- A promise that resolves to the queried recipe.

#### Implementation of

IBundle.get

___

### query

▸ **
query**(`payload?`): `Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<`APIRecipeV2`
> >

Lists all recipes.

**`Example`**

```ts
const pagedResponse = await dl.recipes.query({ projectIds: ['projectId-1'] })
const recipes = pagedResponse.items
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload?` | `Partial`<`APIRecipeV2`> | An Object containing the possible projectIds filter. |

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<`APIRecipeV2`>>

- A promise that resolves to a paged response with the queried recipes.

#### Implementation of

IBundle.query

___

### update

▸ **update**(`payload`): `Promise`<`APIRecipeV2`>

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
| `payload` | `Partial`<`APIRecipeV2`> | The payload to update the recipe. |

#### Returns

`Promise`<`APIRecipeV2`>

- A promise that resolves to the updated recipe.

#### Implementation of

IBundle.update
