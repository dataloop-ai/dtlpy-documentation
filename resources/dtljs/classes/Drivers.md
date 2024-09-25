# Class: Drivers

[appLib/SDKDrivers/xFrameDriver/drivers](../modules/appLib_SDKDrivers_xFrameDriver_drivers.md).Drivers

Drivers repository.

The Drivers class allows the user to manage drivers and their properties.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Drivers`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<[`SDKDriver`](sdkApi_interfaces_entities_iDriver.SDKDriver.md)\>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_drivers.Drivers.md#constructor)

### Methods

- [crudReq](appLib_SDKDrivers_xFrameDriver_drivers.Drivers.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_drivers.Drivers.md#crudreqsync)
- [query](appLib_SDKDrivers_xFrameDriver_drivers.Drivers.md#query)

## Constructors

### constructor

• **new Drivers**(`agent`)

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

___

### query

▸ **query**(): `Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<[`SDKDriver`](sdkApi_interfaces_entities_iDriver.SDKDriver.md)\>\>

Lists all the drivers in the active project.

**`Example`**

```ts
const pagedResponse = await dl.drivers.query()
const drivers = pagedResponse.items
```

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<[`SDKDriver`](sdkApi_interfaces_entities_iDriver.SDKDriver.md)\>\>

- A promise that resolves to a paged response with the listed drivers.

#### Implementation of

IBundle.query
