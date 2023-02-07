# Class: Annotations

[repositories](./repositories.md).Annotations

Annotations repository.

The Annotation class allows you to manage the annotations of data items.

## Hierarchy

- [`Repository`](./Repository.md)

  ↳ **`Annotations`**

## Implements

- [`IBundle`](../interfaces/IBundle.md)<[`SDKAnnotation`](./SDKAnnotation.md)>

## Table of contents

### Constructors

- [constructor](Annotations.md#constructor)

### Methods

- [create](Annotations.md#create)
- [delete](Annotations.md#delete)
- [get](Annotations.md#get)
- [logs](Annotations.md#logs)
- [query](Annotations.md#query)
- [update](Annotations.md#update)

## Constructors

### constructor

• **new Annotations**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](Repository.md)
.[constructor](Repository.md#constructor)

## Methods

### create

▸ **create**(`payload`): `Promise`<[`SDKAnnotation`](SDKAnnotation.md)>

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
| `payload` | `Partial`<[`SDKAnnotation`](SDKAnnotation.md)> | The payload containing the data of the new annotation. |

#### Returns

`Promise`<[`SDKAnnotation`](SDKAnnotation.md)>

- A promise that resolves to the created annotation.

#### Implementation of

IBundle.create

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

▸ **get**(`clientId`): `Promise`<[`SDKAnnotation`](SDKAnnotation.md)>

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

`Promise`<[`SDKAnnotation`](SDKAnnotation.md)>

- A promise that resolves to the annotation with the specified client id.

#### Implementation of

IBundle.get

___

### logs

▸ **logs**(`payload?`): `Promise`<`SDKAnnotationLogs`>

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

`Promise`<`SDKAnnotationLogs`>

- A promise that resolves to the logs of the annotations.

#### Implementation of

IBundle.logs

___

### query

▸ **query**(`payload?`): `Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKAnnotation`](SDKAnnotation.md)>>

Lists all annotations by filter.

**`Example`**
-
```ts
const pagedResponse = await dl.annotations.query()
const annotations = pagedResponse.items
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload?` | `Object` | The query containing the filter. |
| `payload.filter` | `DQL`<[`SDKAnnotation`](SDKAnnotation.md)> | - |

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<[`SDKAnnotation`](SDKAnnotation.md)>>

- A promise that resolves to a paged response with the queried annotations.

___

### update

▸ **update**(`payload`): `Promise`<[`SDKAnnotation`](SDKAnnotation.md)>

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
| `payload` | `Partial`<[`SDKAnnotation`](SDKAnnotation.md)> | The payload containing the updated data of the annotation. |

#### Returns

`Promise`<[`SDKAnnotation`](SDKAnnotation.md)>

- A promise that resolves to the updated annotation.
