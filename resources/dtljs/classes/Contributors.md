# Class: Contributors

[appLib/SDKDrivers/xFrameDriver/contributors](../modules/appLib_SDKDrivers_xFrameDriver_contributors.md).Contributors

Contributors repository.

The Contributors class allows the user to manage contributors.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Contributors`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<[`SDKContributor`](sdkApi_interfaces_entities_iUser.SDKContributor.md)\>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_contributors.Contributors.md#constructor)

### Methods

- [create](appLib_SDKDrivers_xFrameDriver_contributors.Contributors.md#create)
- [crudReq](appLib_SDKDrivers_xFrameDriver_contributors.Contributors.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_contributors.Contributors.md#crudreqsync)
- [delete](appLib_SDKDrivers_xFrameDriver_contributors.Contributors.md#delete)
- [get](appLib_SDKDrivers_xFrameDriver_contributors.Contributors.md#get)
- [query](appLib_SDKDrivers_xFrameDriver_contributors.Contributors.md#query)

## Constructors

### constructor

• **new Contributors**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### create

▸ **create**(`payload`): `Promise`<[`SDKContributor`](sdkApi_interfaces_entities_iUser.SDKContributor.md)\>

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

`Promise`<[`SDKContributor`](sdkApi_interfaces_entities_iUser.SDKContributor.md)\>

- A promise that resolves to the added contributor.

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

▸ **delete**(`id`): `Promise`<`void`\>

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

`Promise`<`void`\>

#### Implementation of

IBundle.delete

___

### get

▸ **get**(`contributorId?`): `Promise`<[`SDKContributor`](sdkApi_interfaces_entities_iUser.SDKContributor.md)\>

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

`Promise`<[`SDKContributor`](sdkApi_interfaces_entities_iUser.SDKContributor.md)\>

- A promise that resolves to the retrieved contributor.

#### Implementation of

IBundle.get

___

### query

▸ **query**(`payload?`): `Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<[`SDKContributor`](sdkApi_interfaces_entities_iUser.SDKContributor.md)\>\>

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

`Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<[`SDKContributor`](sdkApi_interfaces_entities_iUser.SDKContributor.md)\>\>

Returns a Promise that resolves to a paged response object of contributors.

#### Implementation of

IBundle.query
