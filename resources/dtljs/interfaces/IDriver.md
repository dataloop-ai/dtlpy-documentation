# Interface: IDriver

[interfaces](./index.md).IDriver

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

- [allowExternalDelete](IDriver.md#allowexternaldelete)
- [allowExternalModification](IDriver.md#allowexternalmodification)
- [bucket](IDriver.md#bucket)
- [bucketName](IDriver.md#bucketname)
- [clientId](IDriver.md#clientid)
- [containerName](IDriver.md#containername)
- [createdAt](IDriver.md#createdat)
- [creator](IDriver.md#creator)
- [id](IDriver.md#id)
- [integrationId](IDriver.md#integrationid)
- [integrationType](IDriver.md#integrationtype)
- [metadata](IDriver.md#metadata)
- [name](IDriver.md#name)
- [path](IDriver.md#path)
- [region](IDriver.md#region)
- [storageClass](IDriver.md#storageclass)
- [type](IDriver.md#type)
- [updatedAt](IDriver.md#updatedat)
- [updatedBy](IDriver.md#updatedby)

## Properties

### allowExternalDelete

• **allowExternalDelete**: `boolean`

Indicates if the driver allows external delete.

___

### allowExternalModification

• **allowExternalModification**: `boolean`

Indicates if the driver allows external modification.

___

### bucket

• `Optional` **bucket**: `string`

The bucket.

___

### bucketName

• `Optional` **bucketName**: `string`

The bucket name.

___

### clientId

• `Optional` **clientId**: `string`

A local identifier for the Entity, unique within the client.

#### Inherited from

[IEntity](IEntity.md).[clientId](IEntity.md#clientid)

___

### containerName

• `Optional` **containerName**: `string`

The container name.

___

### createdAt

• **createdAt**: `string`

The creation date.

#### Overrides

[IEntity](IEntity.md).[createdAt](IEntity.md#createdat)

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

### name

• **name**: `string`

The driver name.

___

### path

• `Optional` **path**: `string`

The path.

___

### region

• `Optional` **region**: `string`

The region.

___

### storageClass

• `Optional` **storageClass**: `string`

The storage class.

___

### type

• **type**: `string`

The driver type.

___

### updatedAt

• `Optional` **updatedAt**: `IDate`

The date and time when the Entity was last updated.

#### Inherited from

[IEntity](IEntity.md).[updatedAt](IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](IEntity.md).[updatedBy](IEntity.md#updatedby)
