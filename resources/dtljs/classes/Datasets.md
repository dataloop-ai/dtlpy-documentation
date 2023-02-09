# Class: Datasets

[repositories](./repositories.md).Datasets

Datasets repository.

The Datasets class allows the user to manage datasets.

## Hierarchy

- [`Repository`](Repository.md)

  ↳ **`Datasets`**

## Implements

- [`IBundle`](../interfaces/IBundle.md)<[`SDKDataset`](SDKDataset.md)>

## Table of contents

### Constructors

- [constructor](Datasets.md#constructor)

### Methods

- [create](Datasets.md#create)
- [delete](Datasets.md#delete)
- [get](Datasets.md#get)
- [query](Datasets.md#query)
- [update](Datasets.md#update)

## Constructors

### constructor

• **new Datasets**(`agent`)

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

▸ **create**(`payload`): `Promise`<[`SDKDataset`](SDKDataset.md)>

Creates a new dataset.

**`Example`**

```ts
const dataset = await dl.datasets.create({
    name: 'My Dataset'
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Object` | An object containing the dataset's name. |
| `payload.name` | `string` | The name of the dataset to be created. |

#### Returns

`Promise`<[`SDKDataset`](SDKDataset.md)>

- A promise that resolves to the created dataset.

___

### delete

▸ **delete**(`datasetId`): `Promise`<`void`>

Deletes a dataset by id.

**`Example`**

```ts
await dl.datasets.delete('datasetId-123')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `datasetId` | `string` | The id of the dataset to be deleted. |

#### Returns

`Promise`<`void`>

- A promise that resolves when the dataset is deleted.

___

### get

▸ **get**(`datasetId?`): `Promise`<[`SDKDataset`](SDKDataset.md)>

Retrieves a dataset by id.

If the dataset id is not provided, the active dataset is returned.

**`Example`**

```ts
const activeDataset = await dl.datasets.get()
```

**`Example`**

```ts
const dataset = await dl.datasets.get('datasetId-123')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `datasetId?` | `string` | The id of the dataset to be retrieved. |

#### Returns

`Promise`<[`SDKDataset`](SDKDataset.md)>

- A promise that resolves to the retrieved dataset.

___

### query

▸ **query**(): `Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKDataset`](SDKDataset.md)>>

Retrieves a list of datasets.

**`Example`**

```ts
const pagedResponse = await dl.datasets.query()
const datasets = pagedResponse.items
```

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKDataset`](SDKDataset.md)>>

- Returns a Promise that resolves to a paged response object of datasets.

___

### update

▸ **update**(`payload`): `Promise`<[`SDKDataset`](SDKDataset.md)>

Updates a dataset --- *currently not supported*.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Partial`<[`SDKDataset`](SDKDataset.md)> | The fields to update on the dataset. |

#### Returns

`Promise`<[`SDKDataset`](SDKDataset.md)>

- A promise that resolves to the updated dataset.
