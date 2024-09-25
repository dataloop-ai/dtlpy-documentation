# Interface: IDriver

[sdkApi/interfaces/entities/iDriver](../modules/sdkApi_interfaces_entities_iDriver.md).IDriver

An interface representing a driver configuration object.

**`Interface`**

IDriver

## Hierarchy

- [`IEntity`](sdkApi_interfaces_entities_base.IEntity.md)

  ↳ **`IDriver`**

## Implemented by

- [`SDKDriver`](../classes/sdkApi_interfaces_entities_iDriver.SDKDriver.md)

## Table of contents

### Properties

- [allowExternalDelete](sdkApi_interfaces_entities_iDriver.IDriver.md#allowexternaldelete)
- [allowExternalModification](sdkApi_interfaces_entities_iDriver.IDriver.md#allowexternalmodification)
- [bucket](sdkApi_interfaces_entities_iDriver.IDriver.md#bucket)
- [bucketName](sdkApi_interfaces_entities_iDriver.IDriver.md#bucketname)
- [clientId](sdkApi_interfaces_entities_iDriver.IDriver.md#clientid)
- [containerName](sdkApi_interfaces_entities_iDriver.IDriver.md#containername)
- [createdAt](sdkApi_interfaces_entities_iDriver.IDriver.md#createdat)
- [creator](sdkApi_interfaces_entities_iDriver.IDriver.md#creator)
- [id](sdkApi_interfaces_entities_iDriver.IDriver.md#id)
- [integrationId](sdkApi_interfaces_entities_iDriver.IDriver.md#integrationid)
- [integrationType](sdkApi_interfaces_entities_iDriver.IDriver.md#integrationtype)
- [metadata](sdkApi_interfaces_entities_iDriver.IDriver.md#metadata)
- [name](sdkApi_interfaces_entities_iDriver.IDriver.md#name)
- [path](sdkApi_interfaces_entities_iDriver.IDriver.md#path)
- [region](sdkApi_interfaces_entities_iDriver.IDriver.md#region)
- [storageClass](sdkApi_interfaces_entities_iDriver.IDriver.md#storageclass)
- [type](sdkApi_interfaces_entities_iDriver.IDriver.md#type)
- [updatedAt](sdkApi_interfaces_entities_iDriver.IDriver.md#updatedat)
- [updatedBy](sdkApi_interfaces_entities_iDriver.IDriver.md#updatedby)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[clientId](sdkApi_interfaces_entities_base.IEntity.md#clientid)

___

### containerName

• `Optional` **containerName**: `string`

The container name.

___

### createdAt

• **createdAt**: `string`

The creation date.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[createdAt](sdkApi_interfaces_entities_base.IEntity.md#createdat)

___

### creator

• **creator**: `string`

The driver creator.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[creator](sdkApi_interfaces_entities_base.IEntity.md#creator)

___

### id

• **id**: `string`

The driver ID.

#### Overrides

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[id](sdkApi_interfaces_entities_base.IEntity.md#id)

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

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedAt](sdkApi_interfaces_entities_base.IEntity.md#updatedat)

___

### updatedBy

• `Optional` **updatedBy**: `string`

The user who last updated the Entity.

#### Inherited from

[IEntity](sdkApi_interfaces_entities_base.IEntity.md).[updatedBy](sdkApi_interfaces_entities_base.IEntity.md#updatedby)
