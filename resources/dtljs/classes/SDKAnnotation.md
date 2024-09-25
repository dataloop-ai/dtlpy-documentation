# Class: SDKAnnotation<T\>

[sdkApi/interfaces/entities/iAnnotation](../modules/sdkApi_interfaces_entities_iAnnotation.md).SDKAnnotation

Represents an annotation instance within the SDK.

**`Implements`**

## Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

## Implements

- [`IAnnotation`](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md)

## Table of contents

### Constructors

- [constructor](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#constructor)

### Properties

- [annotationId](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#annotationid)
- [attributes](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#attributes)
- [clientId](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#clientid)
- [coordinates](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#coordinates)
- [createdAt](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#createdat)
- [creator](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#creator)
- [data](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#data)
- [datasetId](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#datasetid)
- [description](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#description)
- [id](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#id)
- [itemId](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#itemid)
- [label](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#label)
- [labelSuggestions](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#labelsuggestions)
- [metadata](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#metadata)
- [snapshots](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#snapshots)
- [type](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#type)
- [updatedAt](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#updatedat)
- [updatedBy](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#updatedby)

### Methods

- [toJSON](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#tojson)

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

### annotationId

• `Optional` **annotationId**: `string`

The annotation ID of the annotation.

___

### attributes

• **attributes**: `string`[]

The attributes of the annotation.

___

### clientId

• **clientId**: `string`

The client ID of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[clientId](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#clientid)

___

### coordinates

• `Optional` **coordinates**: `any`

The coordinates of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[coordinates](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#coordinates)

___

### createdAt

• **createdAt**: `IDate`

The creation date of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[createdAt](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#createdat)

___

### creator

• **creator**: `string`

The creator of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[creator](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#creator)

___

### data

• `Optional` **data**: `T`

The data of the annotation.

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the annotation belongs to.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[datasetId](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#datasetid)

___

### description

• `Optional` **description**: `string`

The description of the annotation.

___

### id

• **id**: `string`

The ID of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[id](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#id)

___

### itemId

• **itemId**: `string`

The item ID of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[itemId](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#itemid)

___

### label

• **label**: `string`

The label of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[label](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#label)

___

### labelSuggestions

• **labelSuggestions**: `Object`

The label suggestions for the annotation.

#### Index signature

▪ [p: `string`]: `number`

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[labelSuggestions](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#labelsuggestions)

___

### metadata

• **metadata**: `any`

The metadata of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[metadata](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#metadata)

___

### snapshots

• **snapshots**: `SnapshotService`<`T`\>

The snapshots of the annotation.

___

### type

• **type**: `string`

The type of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[type](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#type)

___

### updatedAt

• **updatedAt**: `IDate`

The last update date of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[updatedAt](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#updatedat)

___

### updatedBy

• **updatedBy**: `string`

The last updater of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md).[updatedBy](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#updatedby)

## Methods

### toJSON

▸ **toJSON**(): `Object`

Returns the annotation as a JSON object.

#### Returns

`Object`

| Name | Type |
| :------ | :------ |
| `attributes` | `string`[] |
| `clientId` | `string` |
| `coordinates` | `any` |
| `createdAt` | `IDate` |
| `creator` | `string` |
| `data` | `T` |
| `datasetId` | `string` |
| `description` | `string` |
| `id` | `string` |
| `itemId` | `string` |
| `label` | `string` |
| `labelColor` | `string` |
| `labelSuggestions` | { `[p: string]`: `number`;  } |
| `metadata` | `any` |
| `type` | `string` |
| `updatedAt` | `IDate` |
| `updatedBy` | `string` |
