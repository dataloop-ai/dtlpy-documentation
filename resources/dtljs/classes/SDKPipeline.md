# Class: SDKPipeline

A class representing a Task object.

**`Implements`**

## Implements

- [`IPipeline`](../interfaces/IPipeline.md)

## Table of contents

### Properties

- [id](SDKPipeline.md#id)
- [name](SDKPipeline.md#name)
- [creator](SDKPipeline.md#creator)
- [createdAt](SDKPipeline.md#createdat)
- [updatedAt](SDKPipeline.md#updatedat)
- [orgId](SDKPipeline.md#orgid)
- [projectId](SDKPipeline.md#projectid)
- [startNodes](SDKPipeline.md#startnodes)
- [compositionId](SDKPipeline.md#compositionid)
- [description](SDKPipeline.md#description)
- [preview](SDKPipeline.md#preview)
- [nodes](SDKPipeline.md#nodes)
- [connections](SDKPipeline.md#connections)
- [templateKind](SDKPipeline.md#templatekind)
- [info](SDKPipeline.md#info)
- [status](SDKPipeline.md#status)
- [settings](SDKPipeline.md#settings)
- [variables](SDKPipeline.md#variables)
- [resetTimestamp](SDKPipeline.md#resettimestamp)
- [updatedBy](SDKPipeline.md#updatedby)
- [readonly](SDKPipeline.md#readonly)
- [active](SDKPipeline.md#active)

### Constructors

- [constructor](SDKPipeline.md#constructor)

## Properties

### id

• **id**: `string`

The unique identifier of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[id](../interfaces/IPipeline.md#id)

___

### name

• **name**: `string`

The name of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[name](../interfaces/IPipeline.md#name)

___

### creator

• **creator**: `string`

The creator of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[creator](../interfaces/IPipeline.md#creator)

___

### createdAt

• **createdAt**: `Date`

The date and time when the pipeline was created.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[createdAt](../interfaces/IPipeline.md#createdat)

___

### updatedAt

• **updatedAt**: `Date`

The date and time when the pipeline was last updated.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[updatedAt](../interfaces/IPipeline.md#updatedat)

___

### orgId

• **orgId**: `string`

The organization ID of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[orgId](../interfaces/IPipeline.md#orgid)

___

### projectId

• **projectId**: `string`

The project ID of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[projectId](../interfaces/IPipeline.md#projectid)

___

### startNodes

• `Optional` **startNodes**: `Dictionary`[]

The start nodes of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[startNodes](../interfaces/IPipeline.md#startnodes)

___

### compositionId

• `Optional` **compositionId**: `string`

The composition ID of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[compositionId](../interfaces/IPipeline.md#compositionid)

___

### description

• **description**: `string`

The description of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[description](../interfaces/IPipeline.md#description)

___

### preview

• **preview**: `string`

The preview of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[preview](../interfaces/IPipeline.md#preview)

___

### nodes

• **nodes**: `Dictionary`[]

The nodes of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[nodes](../interfaces/IPipeline.md#nodes)

___

### connections

• **connections**: `Dictionary`[]

The connections of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[connections](../interfaces/IPipeline.md#connections)

___

### templateKind

• `Optional` **templateKind**: `string`

The template kind of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[templateKind](../interfaces/IPipeline.md#templatekind)

___

### info

• `Optional` **info**: `Dictionary`

The info of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[info](../interfaces/IPipeline.md#info)

___

### status

• **status**: `string`

The status of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[status](../interfaces/IPipeline.md#status)

___

### settings

• `Optional` **settings**: `Dictionary`

The settings of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[settings](../interfaces/IPipeline.md#settings)

___

### variables

• `Optional` **variables**: `Dictionary`[]

The variables of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[variables](../interfaces/IPipeline.md#variables)

___

### resetTimestamp

• `Optional` **resetTimestamp**: `Date`

The reset timestamp of the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[resetTimestamp](../interfaces/IPipeline.md#resettimestamp)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the pipeline.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[updatedBy](../interfaces/IPipeline.md#updatedby)

___

### readonly

• `Optional` **readonly**: `boolean`

Whether the pipeline is readonly.

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[readonly](../interfaces/IPipeline.md#readonly)

___

### active

• `Optional` **active**: `boolean`

Whether the pipeline is active (running).

#### Implementation of

[IPipeline](../interfaces/IPipeline.md).[active](../interfaces/IPipeline.md#active)

## Constructors

### constructor

• **new SDKPipeline**(`pipeline`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `pipeline` | `any` |
