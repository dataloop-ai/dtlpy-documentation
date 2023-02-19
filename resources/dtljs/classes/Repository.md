# Class: Repository

[repositories](./repositories.md).Repository

The Repository class is the base class for all repositories.

## Hierarchy

- **`Repository`**

  ↳ [`Annotations`](Annotations.md)

  ↳ [`AppSettings`](AppSettings.md)

  ↳ [`Contributors`](Contributors.md)

  ↳ [`Datasets`](Datasets.md)

  ↳ [`Executions`](Executions.md)

  ↳ [`Items`](Items.md)

  ↳ [`Labels`](Labels.md)

  ↳ [`Ontologies`](Ontologies.md)

  ↳ [`Projects`](Projects.md)

  ↳ [`Recipes`](Recipes.md)

  ↳ [`Tasks`](Tasks.md)

## Table of contents

### Constructors

- [constructor](Repository.md#constructor)

### Methods

- [crudReq](Repository.md#crudreq)
- [crudReqSync](Repository.md#crudreqsync)

## Constructors

### constructor

• **new Repository**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

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

___

### crudReqSync

▸ **crudReqSync**(`data`): `Promise`<`unknown`>

Sends a CRUD request to the xFrame.

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `any` |

#### Returns

`Promise`<`unknown`>
