# Class: Annotations

[dl.repositories](./index.md).Annotations

Annotations repository.

The Annotation class allows you to manage the annotations of data items.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Annotations`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_annotations.Annotations.md#constructor)

### Methods

- [create](appLib_SDKDrivers_xFrameDriver_annotations.Annotations.md#create)
- [crudReq](appLib_SDKDrivers_xFrameDriver_annotations.Annotations.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_annotations.Annotations.md#crudreqsync)
- [delete](appLib_SDKDrivers_xFrameDriver_annotations.Annotations.md#delete)
- [get](appLib_SDKDrivers_xFrameDriver_annotations.Annotations.md#get)
- [logs](appLib_SDKDrivers_xFrameDriver_annotations.Annotations.md#logs)
- [query](appLib_SDKDrivers_xFrameDriver_annotations.Annotations.md#query)
- [update](appLib_SDKDrivers_xFrameDriver_annotations.Annotations.md#update)

## Constructors

### constructor

• **new Annotations**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)
.[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### create

▸ **create**(`payload`): `Promise`<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)>

Creates a new annotation.

**`Example`**

```ts
// creates a new annotation of type classification under the label "Person"
const classAnnotation = await dl.annotations.create({
    type: "class",
    itemId: "itemId-123",
    label: "Person",
    description: "This is a person classification,
})
```

**`Example`**

```ts
const data = {
    box: [
        {
            x: 0,
            y: 0,
            z: 0,
        },
        {
            x: 0,
            y: 0,
            z: 0,
        },
    ],
    note: { messages: [] },
}

// creates a new annotation of type note under the label "Notes"
const noteAnnotation = await dl.annotations.create({
    type: "note",
    itemId: "itemId-123",
    label: "Notes",
    data
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Partial`<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)> | The payload containing the data of the new annotation. |

#### Returns

`Promise`<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)>

- A promise that resolves to the created annotation.

#### Implementation of

IBundle.create

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

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)
.[crudReq](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#crudreq)

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

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)
.[crudReqSync](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#crudreqsync)

___

### delete

▸ **delete**(`clientId`): `Promise`<`void`>

Deletes a specific annotation by its client id.

**`Example`**

```ts
await dl.annotations.delete('annotation-clientId-2')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `clientId` | `string` | The client id of the annotation to delete. |

#### Returns

`Promise`<`void`>

- A promise that resolves when the annotation has been deleted.

#### Implementation of

IBundle.delete

___

### get

▸ **get**(`clientId`): `Promise`<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)>

Retrieves a specific annotation by its client id.

**`Example`**

```ts
const annotation = await dl.annotations.get('clientId-123')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `clientId` | `string` | The client id of the annotation to retrieve. |

#### Returns

`Promise`<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)>

- A promise that resolves to the annotation with the specified client id.

#### Implementation of

IBundle.get

___

### logs

▸ **
logs**(`payload?`): `Promise`<[`SDKAnnotationLogs`](../modules/sdkApi_interfaces_entities_iAnnotation.md#sdkannotationlogs)>

Retrieves all annotation CRUD logs by itemId and datasetId.
If not provided, the active dataset and item will be used.

**`Example`**

```ts
const logs = await dl.annotations.logs({
    itemId: 'item-1',
    datasetId: 'dataset-1'
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload?` | `Object` | An optional payload containing the `itemId` and `datasetId` of the annotation. |
| `payload.datasetId` | `string` | The `datasetId` of the annotation. |
| `payload.itemId` | `string` | The `itemId` of the annotation. |

#### Returns

`Promise`<[`SDKAnnotationLogs`](../modules/sdkApi_interfaces_entities_iAnnotation.md#sdkannotationlogs)>

- A promise that resolves to the logs of the annotations.

#### Implementation of

IBundle.logs

___

### query

▸ **
query**(`payload?`): `Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)>>

Lists all annotations by filter.

**`Example`**

```ts
const pagedResponse = await dl.annotations.query()
const annotations = pagedResponse.items
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload?` | `Object` | The query containing the filter. |
| `payload.filter` | `DQL`<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)> | - |

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)>>

- A promise that resolves to a paged response with the queried annotations.

___

### update

▸ **update**(`payload`): `Promise`<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)>

Updates an existing annotation.

**`Example`**

```ts
const annotation = await dl.annotations.get('clientId-123')
if (annotation) {
    annotation.description = "New description"
}
const updatedAnnotation = await dl.annotations.update(annotation)
console.log(updatedAnnotation.description) // "New description"
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Partial`<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)> | The payload containing the updated data of the annotation. |

#### Returns

`Promise`<[`SDKAnnotation`](sdkApi_interfaces_entities_iAnnotation.SDKAnnotation.md)>

- A promise that resolves to the updated annotation.
