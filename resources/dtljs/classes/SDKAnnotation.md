# Class: SDKAnnotation

[entities](./entities.md).SDKAnnotation

Represents an annotation instance within the SDK.

## Implements

- [`IAnnotation`](../interfaces/IAnnotation.md)

## Table of contents

### Constructors

- [constructor](SDKAnnotation.md#constructor)

### Properties

- [annotationId](SDKAnnotation.md#annotationid)
- [attributes](SDKAnnotation.md#attributes)
- [clientId](SDKAnnotation.md#clientid)
- [coordinates](SDKAnnotation.md#coordinates)
- [createdAt](SDKAnnotation.md#createdat)
- [creator](SDKAnnotation.md#creator)
- [data](SDKAnnotation.md#data)
- [datasetId](SDKAnnotation.md#datasetid)
- [description](SDKAnnotation.md#description)
- [id](SDKAnnotation.md#id)
- [itemId](SDKAnnotation.md#itemid)
- [label](SDKAnnotation.md#label)
- [labelSuggestions](SDKAnnotation.md#labelsuggestions)
- [metadata](SDKAnnotation.md#metadata)
- [type](SDKAnnotation.md#type)
- [updatedAt](SDKAnnotation.md#updatedat)
- [updatedBy](SDKAnnotation.md#updatedby)

## Constructors

### constructor

• **new SDKAnnotation**(`annotation`)

Creates an instance of SDKAnnotation.

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

___

### coordinates

• `Optional` **coordinates**: `any`

The coordinates of the annotation.

___

### createdAt

• **createdAt**: `IDate`

The creation date of the annotation.

___

### creator

• **creator**: `string`

The creator of the annotation.

___

### data

• `Optional` **data**: `any`

The data of the annotation.

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the annotation belongs to.

___

### description

• `Optional` **description**: `string`

The description of the annotation.

___

### id

• **id**: `string`

The ID of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md)
.[id](../interfaces/IAnnotation.md#id)

___

### itemId

• **itemId**: `string`

The item ID of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md)
.[itemId](../interfaces/IAnnotation.md#itemid)

___

### label

• **label**: `string`

The label of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md)
.[label](../interfaces/IAnnotation.md#label)

___

### labelSuggestions

• **labelSuggestions**: `Object`

The label suggestions for the annotation.

#### Index signature

▪ [p: `string`]: `number`

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md)
.[labelSuggestions](../interfaces/IAnnotation.md#labelsuggestions)

___

### metadata

• **metadata**: `any`

The metadata of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md)
.[metadata](../interfaces/IAnnotation.md#metadata)

___

### type

• **type**: `string`

The type of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md)
.[type](../interfaces/IAnnotation.md#type)

___

### updatedAt

• **updatedAt**: `IDate`

The last update date of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md)
.[updatedAt](../interfaces/IAnnotation.md#updatedat)

___

### updatedBy

• **updatedBy**: `string`

The last updater of the annotation.

#### Implementation of

[IAnnotation](../interfaces/IAnnotation.md)
.[updatedBy](../interfaces/IAnnotation.md#updatedby)
