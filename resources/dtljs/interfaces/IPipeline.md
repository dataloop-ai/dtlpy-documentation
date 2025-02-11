# Interface: IPipeline

An interface representing a Pipeline object, extending the IEntity interface.

**`Interface`**

IPipeline

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IPipeline`**

## Implemented by

- [`SDKPipeline`](../classes/SDKPipeline.md)

## Table of contents

### Properties

- [clientId](IPipeline.md#clientid)
- [id](IPipeline.md#id)
- [name](IPipeline.md#name)
- [creator](IPipeline.md#creator)
- [createdAt](IPipeline.md#createdat)
- [updatedAt](IPipeline.md#updatedat)
- [orgId](IPipeline.md#orgid)
- [projectId](IPipeline.md#projectid)
- [startNodes](IPipeline.md#startnodes)
- [compositionId](IPipeline.md#compositionid)
- [description](IPipeline.md#description)
- [preview](IPipeline.md#preview)
- [nodes](IPipeline.md#nodes)
- [connections](IPipeline.md#connections)
- [templateKind](IPipeline.md#templatekind)
- [info](IPipeline.md#info)
- [status](IPipeline.md#status)
- [settings](IPipeline.md#settings)
- [variables](IPipeline.md#variables)
- [resetTimestamp](IPipeline.md#resettimestamp)
- [updatedBy](IPipeline.md#updatedby)
- [readonly](IPipeline.md#readonly)
- [active](IPipeline.md#active)

## Properties

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### id

• **id**: `string`

A globally unique identifier for the Entity.

#### Overrides

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### name

• **name**: `string`

___

### creator

• **creator**: `string`

The creator of the Entity.

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### createdAt

• **createdAt**: `Date`

The date and time when the Entity was created.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### updatedAt

• **updatedAt**: `Date`

The date and time when the Entity was last updated.

#### Overrides

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### orgId

• **orgId**: `string`

___

### projectId

• **projectId**: `string`

___

### startNodes

• `Optional` **startNodes**: `Dictionary`[]

___

### compositionId

• `Optional` **compositionId**: `string`

___

### description

• **description**: `string`

___

### preview

• **preview**: `string`

___

### nodes

• **nodes**: `Dictionary`[]

___

### connections

• **connections**: `Dictionary`[]

___

### templateKind

• `Optional` **templateKind**: `string`

___

### info

• `Optional` **info**: `Dictionary`

___

### status

• **status**: `string`

___

### settings

• `Optional` **settings**: `Dictionary`

___

### variables

• `Optional` **variables**: `Dictionary`[]

___

### resetTimestamp

• `Optional` **resetTimestamp**: `Date`

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Overrides

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)

___

### readonly

• `Optional` **readonly**: `boolean`

___

### active

• `Optional` **active**: `boolean`
