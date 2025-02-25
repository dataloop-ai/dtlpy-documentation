# Interface: IAnnotation

An interface representing an Annotation object, extending the IEntity interface.

**`Interface`**

IAnnotation

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IAnnotation`**

## Implemented by

- [`SDKAnnotation`](../classes/SDKAnnotation.md)

## Table of contents

### Properties

- [id](IAnnotation.md#id)
- [clientId](IAnnotation.md#clientid)
- [creator](IAnnotation.md#creator)
- [label](IAnnotation.md#label)
- [itemId](IAnnotation.md#itemid)
- [type](IAnnotation.md#type)
- [metadata](IAnnotation.md#metadata)
- [datasetId](IAnnotation.md#datasetid)
- [createdAt](IAnnotation.md#createdat)
- [updatedAt](IAnnotation.md#updatedat)
- [updatedBy](IAnnotation.md#updatedby)
- [coordinates](IAnnotation.md#coordinates)
- [labelSuggestions](IAnnotation.md#labelsuggestions)

## Properties

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Inherited from

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

#### Inherited from

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### label

• **label**: `string`

The label associated with the annotation.

___

### itemId

• **itemId**: `string`

The ID of the item the annotation is associated with.

___

### type

• **type**: `string`

The type of the annotation.

___

### metadata

• **metadata**: `any`

The metadata associated with the annotation.

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the annotation belongs to.

___

### createdAt

• **createdAt**: [`IDate`](../modules.md#idate)

The date and time the annotation was created.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### updatedAt

• **updatedAt**: [`IDate`](../modules.md#idate)

The date and time the annotation was last updated.

#### Overrides

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### updatedBy

• **updatedBy**: `string`

The user who last updated the annotation.

#### Overrides

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)

___

### coordinates

• `Optional` **coordinates**: `any`

The coordinates associated with the annotation.

___

### labelSuggestions

• **labelSuggestions**: `Object`

The label suggestions and their associated confidence scores.

#### Index signature

▪ [key: `string`]: `number`
