# Class: SnapshotService<T\>

## Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

## Table of contents

### Accessors

- [list](SnapshotService.md#list)
- [initSnapshot](SnapshotService.md#initsnapshot)

### Constructors

- [constructor](SnapshotService.md#constructor)

### Methods

- [delete](SnapshotService.md#delete)
- [get](SnapshotService.md#get)
- [generateTransformation](SnapshotService.md#generatetransformation)
- [create](SnapshotService.md#create)
- [update](SnapshotService.md#update)

## Accessors

### list

• `get` **list**(): [`SDKAnnotationSnapshot`](SDKAnnotationSnapshot.md)<`T`\>[]

#### Returns

[`SDKAnnotationSnapshot`](SDKAnnotationSnapshot.md)<`T`\>[]

___

### initSnapshot

• `get` **initSnapshot**(): [`SDKAnnotationSnapshot`](SDKAnnotationSnapshot.md)<`any`\>

#### Returns

[`SDKAnnotationSnapshot`](SDKAnnotationSnapshot.md)<`any`\>

## Constructors

### constructor

• **new SnapshotService**<`T`\>(`annotation`)

#### Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

#### Parameters

| Name | Type |
| :------ | :------ |
| `annotation` | [`SDKAnnotation`](SDKAnnotation.md)<`any`\> |

## Methods

### delete

▸ **delete**(`t`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `t` | [`SDKAnnotationSnapshot`](SDKAnnotationSnapshot.md)<`any`\> |

#### Returns

`void`

___

### get

▸ **get**(`frame`): [`SDKAnnotationSnapshot`](SDKAnnotationSnapshot.md)<`T`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `frame` | `number` |

#### Returns

[`SDKAnnotationSnapshot`](SDKAnnotationSnapshot.md)<`T`\>

___

### generateTransformation

▸ **generateTransformation**(`frame`, `interpolate`): `void`

Generate transformation for a range between previous and next fixed frames.
The interpolation function is called on each frame that needs to be transformed in the fixed range.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `frame` | `number` | a frame in the fixed range |
| `interpolate` | (`from`: [`IAnnotationSnapshot`](../interfaces/IAnnotationSnapshot.md)<`T`\>, `to`: [`IAnnotationSnapshot`](../interfaces/IAnnotationSnapshot.md)<`T`\>, `progress`: `number`) => `Required`<`Partial`<[`IAnnotationSnapshot`](../interfaces/IAnnotationSnapshot.md)<`T`\>\>, ``"data"``\> | the interpolation function to transform by |

#### Returns

`void`

___

### create

▸ **create**(`params`): [`SDKAnnotationSnapshot`](SDKAnnotationSnapshot.md)<`T`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `params` | [`IAnnotationSnapshot`](../interfaces/IAnnotationSnapshot.md)<`any`\> |

#### Returns

[`SDKAnnotationSnapshot`](SDKAnnotationSnapshot.md)<`T`\>

___

### update

▸ **update**(`params`): `Promise`<`void`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `params` | `Object` |
| `params.namedAttributes?` | `Object` |
| `params.namedAttributes.key` | `string` |
| `params.namedAttributes.value?` | `string` \| `number` \| `boolean` \| `string`[] |
| `params.label?` | `string` |
| `params.frame` | `number` |
| `params.untilSpecificFrame?` | `number` |
| `params.objectVisible?` | `boolean` |
| `params.data?` | `T` |

#### Returns

`Promise`<`void`\>
