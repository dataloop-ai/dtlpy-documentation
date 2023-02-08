# Interface: IAnnotation

[interfaces](./index.md).IAnnotation

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

- [clientId](IAnnotation.md#clientid)
- [coordinates](IAnnotation.md#coordinates)
- [createdAt](IAnnotation.md#createdat)
- [creator](IAnnotation.md#creator)
- [datasetId](IAnnotation.md#datasetid)
- [id](IAnnotation.md#id)
- [itemId](IAnnotation.md#itemid)
- [label](IAnnotation.md#label)
- [labelSuggestions](IAnnotation.md#labelsuggestions)
- [metadata](IAnnotation.md#metadata)
- [type](IAnnotation.md#type)
- [updatedAt](IAnnotation.md#updatedat)
- [updatedBy](IAnnotation.md#updatedby)

## Properties

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### coordinates

• `Optional` **coordinates**: `any`

The coordinates associated with the annotation.

___

### createdAt

• **createdAt**: `IDate`

The date and time the annotation was created.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

#### Inherited from

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the annotation belongs to.

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Inherited from

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### itemId

• **itemId**: `string`

The ID of the item the annotation is associated with.

___

### label

• **label**: `string`

The label associated with the annotation.

___

### labelSuggestions

• **labelSuggestions**: `Object`

The label suggestions and their associated confidence scores.

#### Index signature

▪ [key: `string`]: `number`

___

### metadata

• **metadata**: `any`

The metadata associated with the annotation.

___

### type

• **type**: `string`

The type of the annotation.

___

### updatedAt

• **updatedAt**: `IDate`

The date and time the annotation was last updated.

#### Overrides

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### updatedBy

• **updatedBy**: `string`

The user who last updated the annotation.

#### Overrides

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)
