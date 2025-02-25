# Interface: IDriver

An interface representing a driver configuration object.

**`Interface`**

IDriver

## Hierarchy

- [`IEntity`](IEntity.md)

  ↳ **`IDriver`**

## Implemented by

- [`SDKDriver`](../classes/SDKDriver.md)

## Table of contents

### Properties

- [clientId](IDriver.md#clientid)
- [updatedAt](IDriver.md#updatedat)
- [updatedBy](IDriver.md#updatedby)
- [type](IDriver.md#type)
- [creator](IDriver.md#creator)
- [id](IDriver.md#id)
- [createdAt](IDriver.md#createdat)
- [name](IDriver.md#name)
- [integrationId](IDriver.md#integrationid)
- [integrationType](IDriver.md#integrationtype)
- [metadata](IDriver.md#metadata)
- [allowExternalDelete](IDriver.md#allowexternaldelete)
- [allowExternalModification](IDriver.md#allowexternalmodification)
- [region](IDriver.md#region)
- [bucketName](IDriver.md#bucketname)
- [path](IDriver.md#path)
- [storageClass](IDriver.md#storageclass)
- [bucket](IDriver.md#bucket)
- [containerName](IDriver.md#containername)

## Properties

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### updatedAt

• `Optional` **updatedAt**: [`IDate`](../modules.md#idate)

The date and time when the Entity was last updated.

#### Inherited from

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)

___

### type

• **type**: `string`

The driver type.

___

### creator

• **creator**: `string`

The driver creator.

#### Overrides

[IEntity](IEntity.md).[creator](IEntity.md#creator)

___

### id

• **id**: `string`

The driver ID.

#### Overrides

[IEntity](IEntity.md).[id](IEntity.md#id)

___

### createdAt

• **createdAt**: `string`

The creation date.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

___

### name

• **name**: `string`

The driver name.

___

### integrationId

• **integrationId**: `string`

The integration ID.

___

### integrationType

• `Optional` **integrationType**: `string`

The integration type.

___

### metadata

• **metadata**: `any`

The driver metadata.

___

### allowExternalDelete

• **allowExternalDelete**: `boolean`

Indicates if the driver allows external delete.

___

### allowExternalModification

• **allowExternalModification**: `boolean`

Indicates if the driver allows external modification.

___

### region

• `Optional` **region**: `string`

The region.

___

### bucketName

• `Optional` **bucketName**: `string`

The bucket name.

___

### path

• `Optional` **path**: `string`

The path.

___

### storageClass

• `Optional` **storageClass**: `string`

The storage class.

___

### bucket

• `Optional` **bucket**: `string`

The bucket.

___

### containerName

• `Optional` **containerName**: `string`

The container name.
