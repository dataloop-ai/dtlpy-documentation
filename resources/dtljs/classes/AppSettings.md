# Class: AppSettings

Settings repository.

The Settings class allows you to manage the settings of the app.

**`Implements`**

IBundle<iAppSettings>

## Hierarchy

- `Repository`

  ↳ **`AppSettings`**

## Implements

- [`IBundle`](../interfaces/IBundle.md)<[`iAppSettings`](../interfaces/iAppSettings.md)\>

## Table of contents

### Methods

- [get](AppSettings.md#get)
- [crudReqSync](AppSettings.md#crudreqsync)
- [crudReq](AppSettings.md#crudreq)

### Constructors

- [constructor](AppSettings.md#constructor)

## Methods

### get

▸ **get**(`setting?`): `Promise`<[`iAppSettings`](../interfaces/iAppSettings.md)\>

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

`Promise`<[`iAppSettings`](../interfaces/iAppSettings.md)\>

- A promise that resolves to the settings of the app.

#### Implementation of

IBundle.get

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

Repository.crudReqSync

___

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

Repository.crudReq

## Constructors

### constructor

• **new AppSettings**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | [`PeerAgent`](PeerAgent.md) |

#### Inherited from

Repository.constructor
