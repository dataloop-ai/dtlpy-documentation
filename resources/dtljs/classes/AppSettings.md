# Class: AppSettings

[repositories](./repositories.md).AppSettings

Settings repository.

The Settings class allows you to manage the settings of the app.

## Hierarchy

- [`Repository`](Repository.md)

  ↳ **`AppSettings`**

## Implements

- [`IBundle`](../interfaces/IBundle.md)<`iAppSettings`>

## Table of contents

### Constructors

- [constructor](AppSettings.md#constructor)

### Methods

- [get](AppSettings.md#get)

## Constructors

### constructor

• **new AppSettings**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](Repository.md)
.[constructor](Repository.md#constructor)

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
