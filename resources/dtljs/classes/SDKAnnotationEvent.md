# Class: SDKAnnotationEvent

Represents an annotation event.

## Table of contents

### Properties

- [id](SDKAnnotationEvent.md#id)
- [annotationId](SDKAnnotationEvent.md#annotationid)
- [user](SDKAnnotationEvent.md#user)
- [timestamp](SDKAnnotationEvent.md#timestamp)
- [changes](SDKAnnotationEvent.md#changes)
- [deleted](SDKAnnotationEvent.md#deleted)

### Constructors

- [constructor](SDKAnnotationEvent.md#constructor)

## Properties

### id

• **id**: `string`

___

### annotationId

• **annotationId**: `string`

___

### user

• **user**: `string`

___

### timestamp

• **timestamp**: `Date`

___

### changes

• `Optional` **changes**: [`AnnotationChanges`](../interfaces/AnnotationChanges.md)

___

### deleted

• `Optional` **deleted**: `boolean` \| ``"discarded"``

## Constructors

### constructor

• **new SDKAnnotationEvent**(`event`)

Creates an instance of SDKAnnotationEvent.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `event` | `Partial`<[`SDKAnnotationEvent`](SDKAnnotationEvent.md)\> | The event data to initialize the SDKAnnotationEvent object with. |
