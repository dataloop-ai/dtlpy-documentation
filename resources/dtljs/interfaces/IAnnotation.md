# Interface: IAnnotation

[sdkApi/interfaces/entities/iAnnotation](../modules/sdkApi_interfaces_entities_iAnnotation.md).IAnnotation

An interface representing an Annotation object, extending the IEntity interface.

**`Interface`**

IAnnotation

## Hierarchy

- [`IEntity`](sdkApi_interfaces_entities_base.IEntity.md)

  ↳ **`IAnnotation`**

## Implemented by

- [`SDKAnnotation`](../classes/sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)

## Table of contents

### Properties

- [clientId](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#clientid)
- [coordinates](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#coordinates)
- [createdAt](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#createdat)
- [creator](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#creator)
- [datasetId](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#datasetid)
- [id](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#id)
- [itemId](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#itemid)
- [label](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#label)
- [labelSuggestions](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#labelsuggestions)
- [metadata](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#metadata)
- [type](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#type)
- [updatedAt](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#updatedat)
- [updatedBy](sdkApi_interfaces_entities_iAnnotation.IAnnotation.md#updatedby)

## Properties

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[clientId](sdkApi_interfaces_entities_base.IEntity.md#clientid)

___

### coordinates

• `Optional` **coordinates**: `any`

The coordinates associated with the annotation.

___

### createdAt

• **createdAt**: `IDate`

The date and time the annotation was created.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[createdAt](sdkApi_interfaces_entities_base.IEntity.md#createdat)

___

### creator

• `Optional` **creator**: `string`

The creator of the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[creator](sdkApi_interfaces_entities_base.IEntity.md#creator)

___

### datasetId

• **datasetId**: `string`

The ID of the dataset the annotation belongs to.

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[id](sdkApi_interfaces_entities_base.IEntity.md#id)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedAt](sdkApi_interfaces_entities_base.IEntity.md#updatedat)

___

### updatedBy

• **updatedBy**: `string`

The user who last updated the annotation.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedBy](sdkApi_interfaces_entities_base.IEntity.md#updatedby)
