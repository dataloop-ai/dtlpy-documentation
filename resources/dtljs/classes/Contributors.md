# Class: Contributors

[repositories](./repositories.md).Contributors

Contributors repository.

The Contributors class allows the user to manage contributors.

## Hierarchy

- [`Repository`](Repository.md)

  ↳ **`Contributors`**

## Implements

- [`IBundle`](../interfaces/IBundle.md)<[`SDKContributor`](SDKContributor.md)>

## Table of contents

### Constructors

- [constructor](Contributors.md#constructor)

### Methods

- [create](Contributors.md#create)
- [delete](Contributors.md#delete)
- [get](Contributors.md#get)
- [query](Contributors.md#query)

## Constructors

### constructor

• **new Contributors**(`agent`)

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

▸ **create**(`payload`): `Promise`<[`SDKContributor`](SDKContributor.md)>

Adds a contributor to the project.

**`Example`**

```ts
const contributor = await dl.contributors.create({
    email: 'user@dataloop.ai',
    role: 'annotator'
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Object` | The payload of the contributor to be added. |
| `payload.email` | `string` | The email of the contributor to be added. |
| `payload.role` | `string` | The role of the contributor to be added. |

#### Returns

`Promise`<[`SDKContributor`](SDKContributor.md)>

- A promise that resolves to the added contributor.

___

### delete

▸ **delete**(`id`): `Promise`<`void`>

Removes a contributor from the project.

**`Example`**

```ts
await dl.contributors.delete('user@dataloop.ai')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `id` | `string` | The id (email) of the contributor to be removed. |

#### Returns

`Promise`<`void`>

___

### get

▸ **get**(`contributorId?`): `Promise`<[`SDKContributor`](SDKContributor.md)>

Retrieves a contributor.

**`Example`**

```ts
const contributor = await dl.contributors.get('user@dataloop.ai')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `contributorId?` | `string` | The id (email) of the contributor to be retrieved. |

#### Returns

`Promise`<[`SDKContributor`](SDKContributor.md)>

- A promise that resolves to the retrieved contributor.

___

### query

▸ **query**(`payload?`): `Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKContributor`](SDKContributor.md)>>

Lists all the contributors of the active project.

**`Example`**

```ts
const pagedResponse = await dl.contributors.query()
const contributors = pagedResponse.items
```

#### Parameters

| Name | Type |
| :------ | :------ |
| `payload?` | `any` |

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKContributor`](SDKContributor.md)>>

Returns a Promise that resolves to a paged response object of contributors.
