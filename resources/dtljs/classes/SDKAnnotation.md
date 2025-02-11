# Class: SDKAnnotation<T\>

Represents an annotation instance within the SDK.

**`Implements`**

## Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

## Implements

- [`IAnnotation`](../interfaces/IAnnotation.md)

## Table of contents

### Constructors

- [constructor](SDKAnnotation.md#constructor)

### Properties

- [clientId](SDKAnnotation.md#clientid)
- [coordinates](SDKAnnotation.md#coordinates)
- [createdAt](SDKAnnotation.md#createdat)
- [creator](SDKAnnotation.md#creator)
- [datasetId](SDKAnnotation.md#datasetid)
- [annotationId](SDKAnnotation.md#annotationid)
- [id](SDKAnnotation.md#id)
- [itemId](SDKAnnotation.md#itemid)
- [label](SDKAnnotation.md#label)
- [labelSuggestions](SDKAnnotation.md#labelsuggestions)
- [metadata](SDKAnnotation.md#metadata)
- [type](SDKAnnotation.md#type)
- [updatedAt](SDKAnnotation.md#updatedat)
- [updatedBy](SDKAnnotation.md#updatedby)
- [attributes](SDKAnnotation.md#attributes)
- [description](SDKAnnotation.md#description)
- [data](SDKAnnotation.md#data)
- [labelColor](SDKAnnotation.md#labelcolor)
- [snapshots](SDKAnnotation.md#snapshots)

### Methods

- [toJSON](SDKAnnotation.md#tojson)

## Constructors

### constructor

• **new SDKAnnotation**<`T`\>(`annotation`)

Creates an instance of SDKAnnotation.

#### Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `annotation` | `any` | Annotation data to initialize the SDKAnnotation object with. |

## Properties

### clientId

• **clientId**: `string`

The client ID of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[clientId](../interfaces/IAnnotation.md#clientid)

___

### coordinates

• `Optional` **coordinates**: `any`

The coordinates of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[coordinates](../interfaces/IAnnotation.md#coordinates)

___

### createdAt

• **createdAt**: [`IDate`](../modules.md#idate)

The creation date of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[createdAt](../interfaces/IAnnotation.md#createdat)

___

### creator

• **creator**: `string`

The creator of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[creator](../interfaces/IAnnotation.md#creator)

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the annotation belongs to.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[datasetId](../interfaces/IAnnotation.md#datasetid)

___

### annotationId

• `Optional` **annotationId**: `string`

The annotation ID of the annotation.

___

### id

• **id**: `string`

The ID of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[id](../interfaces/IAnnotation.md#id)

___

### itemId

• **itemId**: `string`

The item ID of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[itemId](../interfaces/IAnnotation.md#itemid)

___

### label

• **label**: `string`

The label of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[label](../interfaces/IAnnotation.md#label)

___

### labelSuggestions

• **labelSuggestions**: `Object`

The label suggestions for the annotation.

#### Index signature

▪ [p: `string`]: `number`

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[labelSuggestions](../interfaces/IAnnotation.md#labelsuggestions)

___

### metadata

• **metadata**: `any`

The metadata of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[metadata](../interfaces/IAnnotation.md#metadata)

___

### type

• **type**: `string`

The type of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[type](../interfaces/IAnnotation.md#type)

___

### updatedAt

• **updatedAt**: [`IDate`](../modules.md#idate)

The last update date of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[updatedAt](../interfaces/IAnnotation.md#updatedat)

___

### updatedBy

• **updatedBy**: `string`

The last updater of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md).[updatedBy](../interfaces/IAnnotation.md#updatedby)

___

### attributes

• **attributes**: `string`[]

The attributes of the annotation.

___

### description

• `Optional` **description**: `string`

The description of the annotation.

___

### data

• `Optional` **data**: `T`

The data of the annotation.

___

### labelColor

• `Optional` **labelColor**: `string`

___

### snapshots

• **snapshots**: [`SnapshotService`](SnapshotService.md)<`T`\>

The snapshots of the annotation.

## Methods

### toJSON

▸ **toJSON**(): `Object`

Returns the annotation as a JSON object.

#### Returns

`Object`

| Name | Type |
| :------ | :------ |
| `clientId` | `string` |
| `coordinates` | `any` |
| `createdAt` | [`IDate`](../modules.md#idate) |
| `creator` | `string` |
| `datasetId` | `string` |
| `id` | `string` |
| `itemId` | `string` |
| `label` | `string` |
| `labelSuggestions` | { `[p: string]`: `number`;  } |
| `metadata` | `any` |
| `type` | `string` |
| `updatedAt` | [`IDate`](../modules.md#idate) |
| `updatedBy` | `string` |
| `attributes` | `string`[] |
| `description` | `string` |
| `labelColor` | `string` |
| `data` | `T` |
