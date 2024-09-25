# Class: AppSettings

[appLib/SDKDrivers/xFrameDriver/appSettings](../modules/appLib_SDKDrivers_xFrameDriver_appSettings.md).AppSettings

Settings repository.

The Settings class allows you to manage the settings of the app.

**`Implements`**

IBundle<iAppSettings>

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`AppSettings`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<`iAppSettings`\>

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

### get

▸ **get**(`setting?`): `Promise`<`iAppSettings`\>

Retrieves the settings of your app.

**`Example`**

```ts
const generalSettings = await dl.settings.get()
const { theme, currentUser } = generalSettings
```

**`Example`**

```ts
const setting = await dl.settings.get('userSettingName')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `setting?` | `string` | The name of the user setting to retrieve. |

#### Returns

`Promise`<`iAppSettings`\>

- A promise that resolves to the settings of the app.

#### Implementation of

IBundle.get
