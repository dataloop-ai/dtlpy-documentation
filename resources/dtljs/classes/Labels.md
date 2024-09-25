# Class: Labels

[appLib/SDKDrivers/xFrameDriver/labels](../modules/appLib_SDKDrivers_xFrameDriver_labels.md).Labels

Labels repository --- *currently not supported*

The Labels class allows the user to manage labels.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Labels`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<`SDKLabelTreeNode`\>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_labels.Labels.md#constructor)

### Methods

- [crudReq](appLib_SDKDrivers_xFrameDriver_labels.Labels.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_labels.Labels.md#crudreqsync)

## Constructors

### constructor

• **new Labels**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### crudReq

▸ **crudReq**(`data`): `void`

Sends a CRUD request to the xFrame.

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `any` |

#### Returns

`void`

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[crudReq](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#crudreq)

___

### crudReqSync

▸ **crudReqSync**(`data`, `options?`): `Promise`<`any`\>

Sends a CRUD request to the xFrame.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `data` | `any` | The data to send. |
| `options` | `Object` |  |
| `options.timeout?` | `number` | an option to set the timeout for the request. |

#### Returns

`Promise`<`any`\>

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[crudReqSync](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#crudreqsync)
