# Class: Repository

[dl.repositories](./index.md).Repository

The Repository class is the base class for all repositories.

## Hierarchy

- **`Repository`**

  ↳ [`Annotations`](appLib_SDKDrivers_xFrameDriver_annotations.Annotations.md)

  ↳ [`AppSettings`](appLib_SDKDrivers_xFrameDriver_appSettings.AppSettings.md)

  ↳ [`Contributors`](appLib_SDKDrivers_xFrameDriver_contributors.Contributors.md)

  ↳ [`Datasets`](appLib_SDKDrivers_xFrameDriver_datasets.Datasets.md)

  ↳ [`Items`](appLib_SDKDrivers_xFrameDriver_items.Items.md)

  ↳ [`Labels`](appLib_SDKDrivers_xFrameDriver_labels.Labels.md)

  ↳ [`Ontologies`](appLib_SDKDrivers_xFrameDriver_ontologies.Ontologies.md)

  ↳ [`Projects`](appLib_SDKDrivers_xFrameDriver_projects.Projects.md)

  ↳ [`Recipes`](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md)

  ↳ [`Tasks`](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md)

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

### Methods

- [crudReq](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#crudreqsync)

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
