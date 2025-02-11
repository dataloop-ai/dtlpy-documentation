# Interface: IBundle<T\>

A bundle is a collection of CRUD operations that can be performed on a resource.

**`Interface`**

IBundle

## Type parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `T` | `any` | The type of the resource. |

## Implemented by

- [`AppSettings`](../classes/AppSettings.md)

## Table of contents

### Properties

- [get](IBundle.md#get)
- [getByName](IBundle.md#getbyname)
- [create](IBundle.md#create)
- [createBulk](IBundle.md#createbulk)
- [update](IBundle.md#update)
- [updateBulk](IBundle.md#updatebulk)
- [delete](IBundle.md#delete)
- [deleteBulk](IBundle.md#deletebulk)
- [query](IBundle.md#query)
- [countByQuery](IBundle.md#countbyquery)
- [stream](IBundle.md#stream)
- [fetch](IBundle.md#fetch)
- [logs](IBundle.md#logs)
- [setStatus](IBundle.md#setstatus)
- [doesLabelHaveAttributes](IBundle.md#doeslabelhaveattributes)
- [calcLabelsHaveAttributes](IBundle.md#calclabelshaveattributes)
- [missingRequiredAttribute](IBundle.md#missingrequiredattribute)

## Properties

### get

• `Optional` **get**: (`payload`: [`ReadPayload`](../modules.md#readpayload)<`T`\>, `options?`: `any`) => `Promise`<`T`\>

#### Type declaration

▸ (`payload`, `options?`): `Promise`<`T`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | [`ReadPayload`](../modules.md#readpayload)<`T`\> |
| `options?` | `any` |

##### Returns

`Promise`<`T`\>

___

### getByName

• `Optional` **getByName**: (`payload`: `string`, `options?`: `any`) => `Promise`<`T`\>

#### Type declaration

▸ (`payload`, `options?`): `Promise`<`T`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `string` |
| `options?` | `any` |

##### Returns

`Promise`<`T`\>

___

### create

• `Optional` **create**: (`payload`: `any`, `options?`: `any`) => `Promise`<`T` \| `T`[]\>

#### Type declaration

▸ (`payload`, `options?`): `Promise`<`T` \| `T`[]\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `any` |
| `options?` | `any` |

##### Returns

`Promise`<`T` \| `T`[]\>

___

### createBulk

• `Optional` **createBulk**: (`payload`: `any`, `options?`: `any`) => `Promise`<`T`[]\>

#### Type declaration

▸ (`payload`, `options?`): `Promise`<`T`[]\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `any` |
| `options?` | `any` |

##### Returns

`Promise`<`T`[]\>

___

### update

• `Optional` **update**: (`payload`: `Partial`<`T`\>, `options?`: `any`) => `Promise`<`T` \| `T`[]\>

#### Type declaration

▸ (`payload`, `options?`): `Promise`<`T` \| `T`[]\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `Partial`<`T`\> |
| `options?` | `any` |

##### Returns

`Promise`<`T` \| `T`[]\>

___

### updateBulk

• `Optional` **updateBulk**: (`payload`: `T`[], `options?`: `any`) => `Promise`<`T`[]\>

#### Type declaration

▸ (`payload`, `options?`): `Promise`<`T`[]\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `T`[] |
| `options?` | `any` |

##### Returns

`Promise`<`T`[]\>

___

### delete

• `Optional` **delete**: (`payload`: [`DeletePayload`](../modules.md#deletepayload)<`T`\>, `options?`: `any`) => `Promise`<`string` \| `void`\>

#### Type declaration

▸ (`payload`, `options?`): `Promise`<`string` \| `void`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | [`DeletePayload`](../modules.md#deletepayload)<`T`\> |
| `options?` | `any` |

##### Returns

`Promise`<`string` \| `void`\>

___

### deleteBulk

• `Optional` **deleteBulk**: (`payload`: [`DeletePayload`](../modules.md#deletepayload)<`T`\>[], `options?`: `any`) => `Promise`<`void`\>

#### Type declaration

▸ (`payload`, `options?`): `Promise`<`void`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | [`DeletePayload`](../modules.md#deletepayload)<`T`\>[] |
| `options?` | `any` |

##### Returns

`Promise`<`void`\>

___

### query

• `Optional` **query**: (`payload`: `any`, `options?`: `any`) => `Promise`<[`IPagedResponse`](IPagedResponse.md)<`T`\>\>

#### Type declaration

▸ (`payload`, `options?`): `Promise`<[`IPagedResponse`](IPagedResponse.md)<`T`\>\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `any` |
| `options?` | `any` |

##### Returns

`Promise`<[`IPagedResponse`](IPagedResponse.md)<`T`\>\>

___

### countByQuery

• `Optional` **countByQuery**: (`payload`: `any`, `options?`: `any`) => `Promise`<`number`\>

#### Type declaration

▸ (`payload`, `options?`): `Promise`<`number`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `any` |
| `options?` | `any` |

##### Returns

`Promise`<`number`\>

___

### stream

• `Optional` **stream**: (`payload`: `any`, `options?`: `any`) => `Promise`<`any`\>

#### Type declaration

▸ (`payload`, `options?`): `Promise`<`any`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `any` |
| `options?` | `any` |

##### Returns

`Promise`<`any`\>

___

### fetch

• `Optional` **fetch**: (`payload`: `string`) => `Promise`<`any`\>

#### Type declaration

▸ (`payload`): `Promise`<`any`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `string` |

##### Returns

`Promise`<`any`\>

___

### logs

• `Optional` **logs**: (`payload`: `Partial`<`T`\>) => `Promise`<`any`\>

#### Type declaration

▸ (`payload`): `Promise`<`any`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `Partial`<`T`\> |

##### Returns

`Promise`<`any`\>

___

### setStatus

• `Optional` **setStatus**: (`payload`: `any`) => `Promise`<`void`\>

#### Type declaration

▸ (`payload`): `Promise`<`void`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `any` |

##### Returns

`Promise`<`void`\>

___

### doesLabelHaveAttributes

• `Optional` **doesLabelHaveAttributes**: (`payload`: `any`) => `Promise`<`boolean`\>

#### Type declaration

▸ (`payload`): `Promise`<`boolean`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `any` |

##### Returns

`Promise`<`boolean`\>

___

### calcLabelsHaveAttributes

• `Optional` **calcLabelsHaveAttributes**: (`payload`: `any`) => `Promise`<`void`\>

#### Type declaration

▸ (`payload`): `Promise`<`void`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `any` |

##### Returns

`Promise`<`void`\>

___

### missingRequiredAttribute

• `Optional` **missingRequiredAttribute**: (`payload`: `string`) => `Promise`<`boolean`\>

#### Type declaration

▸ (`payload`): `Promise`<`boolean`\>

##### Parameters

| Name | Type |
| :------ | :------ |
| `payload` | `string` |

##### Returns

`Promise`<`boolean`\>
