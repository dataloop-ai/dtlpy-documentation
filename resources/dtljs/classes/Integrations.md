# Class: Integrations

[appLib/SDKDrivers/xFrameDriver/integrations](../modules/appLib_SDKDrivers_xFrameDriver_integrations.md).Integrations

Integrations repository.

The Integrations class allows the user to manage integrations and their properties.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Integrations`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<`SDKIntegration`\>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_integrations.Integrations.md#constructor)

### Methods

- [crudReq](appLib_SDKDrivers_xFrameDriver_integrations.Integrations.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_integrations.Integrations.md#crudreqsync)
- [query](appLib_SDKDrivers_xFrameDriver_integrations.Integrations.md#query)

## Constructors

### constructor

• **new Integrations**(`agent`)

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

▸ **query**(): `Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<`SDKIntegration`\>\>

Lists all the integrations in the active org.

**`Example`**

```ts
const pagedResponse = await dl.integrations.query()
const integrations = pagedResponse.items
```

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<`SDKIntegration`\>\>

- A promise that resolves to a paged response with the listed integrations.

#### Implementation of

IBundle.query
