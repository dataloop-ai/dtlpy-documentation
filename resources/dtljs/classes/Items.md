# Class: Items

[appLib/SDKDrivers/xFrameDriver/items](../modules/appLib_SDKDrivers_xFrameDriver_items.md).Items

Items repository.

The Items class allows you to manage items in datasets.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Items`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_items.Items.md#constructor)

### Methods

- [countByQuery](appLib_SDKDrivers_xFrameDriver_items.Items.md#countbyquery)
- [create](appLib_SDKDrivers_xFrameDriver_items.Items.md#create)
- [crudReq](appLib_SDKDrivers_xFrameDriver_items.Items.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_items.Items.md#crudreqsync)
- [delete](appLib_SDKDrivers_xFrameDriver_items.Items.md#delete)
- [fetch](appLib_SDKDrivers_xFrameDriver_items.Items.md#fetch)
- [get](appLib_SDKDrivers_xFrameDriver_items.Items.md#get)
- [getByName](appLib_SDKDrivers_xFrameDriver_items.Items.md#getbyname)
- [query](appLib_SDKDrivers_xFrameDriver_items.Items.md#query)
- [stream](appLib_SDKDrivers_xFrameDriver_items.Items.md#stream)
- [update](appLib_SDKDrivers_xFrameDriver_items.Items.md#update)

## Constructors

### constructor

• **new Items**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### countByQuery

▸ **countByQuery**(`query`, `options?`): `Promise`<`number`\>

Counts the number of items by query.

**`Example`**

```ts
await dl.items.countByQuery({
  "resource": "items",
  "filter": {
    "$and": [
      {
        "annotated": true
      },
      {
        "hidden": false
      },
      {
        "type": "file"
      }
    ]
  }
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `query` | `DqlObj` | The query to count by. |
| `options` | `Object` | - |
| `options.timeout?` | `number` | - |

#### Returns

`Promise`<`number`\>

#### Implementation of

IBundle.countByQuery

___

### create

▸ **create**(`payload`, `options?`): `Promise`<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\>

Creates a new item in the Items repository.

**`Example`**

```ts
const file = new File(['content'], 'filename.txt', { type: 'text/plain' });
const itemPayload = {
   file: file,
   path: 'path/to/item',
   metadata: {
      key: 'value'
   },
   binaries: true
};

const item = await sdk.items.create(itemPayload);
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Object` | The payload for the item. |
| `payload.binaries?` | `boolean` | Whether to upload the item to the Binaries dataset. |
| `payload.datasetId?` | `string` | The id of the dataset to create the item in. |
| `payload.file` | `File` | The file to upload. |
| `payload.metadata?` | `any` | The metadata to add to the item. |
| `payload.overwrite?` | `boolean` | Whether to overwrite the item if it already exists. |
| `payload.path?` | `string` | The path to the item. |
| `options` | `Object` |  |
| `options.timeout?` | `number` | an option to set the timeout for the request. |

#### Returns

`Promise`<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\>

- A promise that resolves with the created item.

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

▸ **delete**(`payload?`): `Promise`<`void`\>

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

`Promise`<`void`\>

- A promise that resolves once the item is deleted.

#### Implementation of

IBundle.delete

___

### fetch

▸ **fetch**(`id?`, `options?`): `Promise`<`any`\>

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
| `options` | `Object` |  |
| `options.timeout?` | `number` | an option to set the timeout for the request. |

#### Returns

`Promise`<`any`\>

- A promise that resolves to the content data.

#### Implementation of

IBundle.fetch

___

### get

▸ **get**(`id?`, `options?`): `Promise`<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\>

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
| `options` | `Object` |  |
| `options.signed?` | `boolean` | an option to fetch the item stream by signed url. |
| `options.timeout?` | `number` | an option to set the timeout for the request. |

#### Returns

`Promise`<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\>

- A promise that resolves to the item data.

#### Implementation of

IBundle.get

___

### getByName

▸ **getByName**(`name?`, `options?`): `Promise`<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\>

Gets an item by name. When the name is not provided, it returns the active item.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `name?` | `string` | The name of the item to retrieve. |
| `options` | `Object` | - |
| `options.binaries?` | `boolean` | get the item from the binaries dataset. |
| `options.timeout?` | `number` | an option to set the timeout for the request. |

#### Returns

`Promise`<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\>

- A promise that resolves to the item data.

#### Implementation of

IBundle.getByName

___

### query

▸ **query**(`payload?`, `options?`): `Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\>\>

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
| `payload.filter` | `DQL`<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\> | - |
| `options` | `Object` |  |
| `options.timeout?` | `number` | an option to set the timeout for the request. |

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\>\>

- Returns a Promise that resolves to a paged response object of items.

#### Implementation of

IBundle.query

___

### stream

▸ **stream**(`url?`, `options?`): `Promise`<`string`\>

Retrieves the stream of an item by an item's stream URL.

**`Example`**

```ts
const stream = await dl.items.stream('https://gate.dataloop.ai/api/v1/items/item-id/stream')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `url?` | `string` | The stream url of the item. |
| `options` | `Object` |  |
| `options.signed?` | `boolean` | an option to fetch the item stream by signed url. |
| `options.timeout?` | `number` | - |

#### Returns

`Promise`<`string`\>

- A promise that resolves to the stream's string.

#### Implementation of

IBundle.stream

___

### update

▸ **update**(`fieldsToUpdate`, `options?`): `Promise`<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\>

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
| `fieldsToUpdate` | `Partial`<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\> & { `system?`: `boolean`  } | The fields to update on the item. |
| `options` | `Object` |  |
| `options.timeout?` | `number` | an option to set the timeout for the request. |

#### Returns

`Promise`<[`SDKItem`](sdkApi_interfaces_entities_iItem.SDKItem.md)\>

- The updated item.

#### Implementation of

IBundle.update
