# Class: Drivers

[repositories](./repositories.md).Drivers

Drivers repository.

The Drivers class allows the user to manage drivers and their properties.

## Hierarchy

- [`Repository`](Repository.md)

  ↳ **`Drivers`**

## Implements

- [`IBundle`](../interfaces/IBundle.md)<[`SDKDriver`](SDKDriver.md)>

## Table of contents

### Constructors

- [constructor](Drivers.md#constructor)

### Methods

- [query](Drivers.md#query)

## Constructors

### constructor

• **new Drivers**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](Repository.md)
.[constructor](Repository.md#constructor)

## Methods

### query

▸ **query**(): `Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKDriver`](SDKDriver.md)>>

Lists all the drivers in the active project.

**`Example`**

```ts
const pagedResponse = await dl.drivers.query()
const drivers = pagedResponse.items
```

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKDriver`](SDKDriver.md)>>

- A promise that resolves to a paged response with the listed drivers.
