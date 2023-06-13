# Class: Items

[repositories](./repositories.md).Items

Items repository.

The Items class allows you to manage items in datasets.

## Hierarchy

- [`Repository`](Repository.md)

  ↳ **`Items`**

## Implements

- [`IBundle`](../interfaces/IBundle.md)<[`SDKItem`](SDKItem.md)>

## Table of contents

### Constructors

- [constructor](Items.md#constructor)

### Methods

- [create](Items.md#create)
- [delete](Items.md#delete)
- [fetch](Items.md#fetch)
- [get](Items.md#get)
- [query](Items.md#query)
- [stream](Items.md#stream)
- [update](Items.md#update)

## Constructors

### constructor

• **new Items**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](Repository.md)
.[constructor](Repository.md#constructor)

## Methods

### create

▸ **create**(`payload`): `Promise`<[`SDKItem`](SDKItem.md)>

Creates a new item in the Items repository.

**`Example`**

```ts
const file = new File(['content'], 'filename.txt', { type: 'text/plain' })
const binariesItemPayload = {
    file: file,
    path: 'path/to/item',
    metadata: {
        key: 'value'
    },
    binaries: true
}

const item = await sdk.items.create(binariesItemPayload)
```

#### Parameters

| Name                 | Type      | Description                                         |
| :------------------- | :-------- | :-------------------------------------------------- |
| `payload`            | `Object`  | The payload for the item.                           |
| `payload.binaries?`  | `boolean` | Whether to upload the item to the Binaries dataset. |
| `payload.datasetId?` | `string`  | The id of the dataset to create the item in.        |
| `payload.file`       | `File`    | The file to upload.                                 |
| `payload.metadata?`  | `any`     | The metadata to add to the item.                    |
| `payload.path?`      | `string`  | The path to the item.                               |

#### Returns

`Promise`<[`SDKItem`](SDKItem.md)>

- A promise that resolves with the created item.

___

### delete

▸ **delete**(`payload?`): `Promise`<`void`>

Deletes an item from the repository.
If the itemId is not provided, the active itemId is used.
If the datasetId is not provided, the active datasetId is used.

**`Example`**

```ts
// delete an item with ID 'item1' in dataset with ID 'dataset1'
await dl.items.delete({ itemId: 'item1', datasetId: 'dataset1' });
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload?` | `Object` | The payload containing the itemId and datasetId of the item to be deleted. |
| `payload.datasetId?` | `string` | - |
| `payload.itemId` | `string` | - |

#### Returns

`Promise`<`void`>

- A promise that resolves once the item is deleted.

#### Implementation of

IBundle.delete

___

### fetch

▸ **fetch**(`id?`): `Promise`<`any`>

Fetches the raw contents of an item by id. When the id is not provided, it uses the active item.

**`Example`**

```ts
// Given a text file with the contents "hello world"
const rawItem = await dl.items.fetch('a-txt-file-id')
console.log(rawItem)
// logs: "hello world"
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id?` | `string` | The id of the item to be fetched. |

#### Returns

`Promise`<`any`>

- A promise that resolves to the content data.

#### Implementation of

IBundle.fetch

___

### get

▸ **get**(`id?`): `Promise`<[`SDKItem`](SDKItem.md)>

Gets an item by id. When the id is not provided, it returns the active item.

**`Example`**

```ts
const activeItem = await dl.items.get()
```

**`Example`**

```ts
const item = await dl.items.get('item-id-123')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id?` | `string` | The id of the item to retrieve. |

#### Returns

`Promise`<[`SDKItem`](SDKItem.md)>

- A promise that resolves to the item data.

#### Implementation of

IBundle.get

___

### query

▸ **query**(`payload?`): `Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKItem`](SDKItem.md)>>

Lists all items by filter.
When no payload is provided, it returns all the items in the active dataset.

**`Example`**

```ts
const pagedResponse = await dl.items.query()
const itemsArray = pagedResponse.items
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload?` | `Object` | contains DQL filter. |
| `payload.filter` | `DQL`<[`SDKItem`](SDKItem.md)> | - |

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKItem`](SDKItem.md)>>

- Returns a Promise that resolves to a paged response object of items.

#### Implementation of

IBundle.query

___

### stream

▸ **stream**(`url?`): `Promise`<`string`>

Retrieves the stream of an item by an item's stream URL.

**`Example`**

```ts
const stream = await dl.items.stream('https://gate.dataloop.ai/api/v1/items/item-id/stream')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `url?` | `string` | The stream url of the item. |

#### Returns

`Promise`<`string`>

- A promise that resolves to the stream's string.

#### Implementation of

IBundle.stream

___

### update

▸ **update**(`fieldsToUpdate`): `Promise`<[`SDKItem`](SDKItem.md)>

Update an existing item.

**`Example`**

```ts
const updatedItem = await dl.items.update({
    id: "item-1",
    name: "Updated item name"
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `fieldsToUpdate` | `Partial`<[`SDKItem`](SDKItem.md)> | The fields to update on the item. |

#### Returns

`Promise`<[`SDKItem`](SDKItem.md)>

- The updated item.

#### Implementation of

IBundle.update

*Note:* To update the `system` object in `metadata` field, one needs to pass `system: true` in the updated item object.

Example:

```ts
const updatedItem = await dl.items.update({
    id: "item-1",
    name: "Updated item name",
    system: true,
    metadata: {
       system: {
           audioSpeakers: { "Label 1": "Label 1 New Value" } 
       }
    }
})
```

In this example, we are updating `audioSpeakers` value of the system object by passing `system: true` at the top level of the updated item object.
