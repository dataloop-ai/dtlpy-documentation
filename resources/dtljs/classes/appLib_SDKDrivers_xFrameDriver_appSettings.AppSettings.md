# Class: AppSettings

[dl.repositories](./index.md).AppSettings

Settings repository.

The Settings class allows you to manage the settings of the app.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`AppSettings`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<`iAppSettings`>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_appSettings.AppSettings.md#constructor)

### Methods

- [crudReq](appLib_SDKDrivers_xFrameDriver_appSettings.AppSettings.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_appSettings.AppSettings.md#crudreqsync)
- [get](appLib_SDKDrivers_xFrameDriver_appSettings.AppSettings.md#get)

## Constructors

### constructor

• **new AppSettings**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)
.[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### get

▸ **get**(): `Promise`<`iAppSettings`>

Retrieves the settings of your app.

**`Example`**

```ts
const settings = await dl.settings.get()
```

#### Returns

`Promise`<`iAppSettings`>

- A promise that resolves to the settings of the app.
