# Class: SDKAnnotation

[dl.entities](./index.md).SDKAnnotation

Represents an annotation instance within the SDK.

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
- [type](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#type)
- [updatedAt](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#updatedat)
- [updatedBy](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md#updatedby)

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

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md)
.[id](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#id)

___

### itemId

• **itemId**: `string`

The item ID of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md)
.[itemId](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#itemid)

___

### label

• **label**: `string`

The label of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md)
.[label](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#label)

___

### labelSuggestions

• **labelSuggestions**: `Object`

The label suggestions for the annotation.

#### Index signature

▪ [p: `string`]: `number`

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md)
.[labelSuggestions](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#labelsuggestions)

___

### metadata

• **metadata**: `any`

The metadata of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md)
.[metadata](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#metadata)

___

### type

• **type**: `string`

The type of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md)
.[type](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#type)

___

### updatedAt

• **updatedAt**: `IDate`

The last update date of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md)
.[updatedAt](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#updatedat)

___

### updatedBy

• **updatedBy**: `string`

The last updater of the annotation.

#### Implementation of

[IAnnotation](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md)
.[updatedBy](../interfaces/sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#updatedby)
