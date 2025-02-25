# Class: SDKAnnotationSnapshot<T\>

## Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

## Implements

- [`IAnnotationSnapshot`](../interfaces/IAnnotationSnapshot.md)<`T`\>

## Table of contents

### Properties

- [fixed](SDKAnnotationSnapshot.md#fixed)
- [frame](SDKAnnotationSnapshot.md#frame)
- [objectVisible](SDKAnnotationSnapshot.md#objectvisible)
- [data](SDKAnnotationSnapshot.md#data)
- [label](SDKAnnotationSnapshot.md#label)
- [namedAttributes](SDKAnnotationSnapshot.md#namedattributes)
- [description](SDKAnnotationSnapshot.md#description)
- [annotationId](SDKAnnotationSnapshot.md#annotationid)

### Constructors

- [constructor](SDKAnnotationSnapshot.md#constructor)

### Methods

- [setAttributeByName](SDKAnnotationSnapshot.md#setattributebyname)

## Properties

### fixed

• **fixed**: `boolean`

#### Implementation of

[IAnnotationSnapshot](../interfaces/IAnnotationSnapshot.md).[fixed](../interfaces/IAnnotationSnapshot.md#fixed)

___

### frame

• **frame**: `number`

#### Implementation of

[IAnnotationSnapshot](../interfaces/IAnnotationSnapshot.md).[frame](../interfaces/IAnnotationSnapshot.md#frame)

___

### objectVisible

• `Optional` **objectVisible**: `boolean`

#### Implementation of

[IAnnotationSnapshot](../interfaces/IAnnotationSnapshot.md).[objectVisible](../interfaces/IAnnotationSnapshot.md#objectvisible)

___

### data

• `Optional` **data**: `T`

#### Implementation of

[IAnnotationSnapshot](../interfaces/IAnnotationSnapshot.md).[data](../interfaces/IAnnotationSnapshot.md#data)

___

### label

• `Optional` **label**: `string`

#### Implementation of

[IAnnotationSnapshot](../interfaces/IAnnotationSnapshot.md).[label](../interfaces/IAnnotationSnapshot.md#label)

___

### namedAttributes

• `Optional` **namedAttributes**: `Object`

#### Index signature

▪ [key: `string`]: `string` \| `number` \| `string`[] \| `boolean`

#### Implementation of

[IAnnotationSnapshot](../interfaces/IAnnotationSnapshot.md).[namedAttributes](../interfaces/IAnnotationSnapshot.md#namedattributes)

___

### description

• `Optional` **description**: `string`

#### Implementation of

[IAnnotationSnapshot](../interfaces/IAnnotationSnapshot.md).[description](../interfaces/IAnnotationSnapshot.md#description)

___

### annotationId

• `Optional` **annotationId**: `string`

#### Implementation of

[IAnnotationSnapshot](../interfaces/IAnnotationSnapshot.md).[annotationId](../interfaces/IAnnotationSnapshot.md#annotationid)

## Constructors

### constructor

• **new SDKAnnotationSnapshot**<`T`\>(`snapshot`)

#### Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

#### Parameters

| Name | Type |
| :------ | :------ |
| `snapshot` | `Partial`<[`IAnnotationSnapshot`](../interfaces/IAnnotationSnapshot.md)<`any`\>\> |

## Methods

### setAttributeByName

▸ **setAttributeByName**(`key`, `value`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `key` | `string` |
| `value` | `string` \| `number` \| `boolean` \| `string`[] |

#### Returns

`void`
