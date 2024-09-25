# Class: Ontologies

[appLib/SDKDrivers/xFrameDriver/ontologies](../modules/appLib_SDKDrivers_xFrameDriver_ontologies.md).Ontologies

Ontologies repository --- *currently not supported*

The Ontology class allows the user to manage ontologies.

## Hierarchy

- [`Repository`](appLib_SDKDrivers_xFrameDriver_repository.Repository.md)

  ↳ **`Ontologies`**

## Implements

- [`IBundle`](../interfaces/sdkApi_interfaces_bundles.IBundle.md)<`APIOntologyV2`\>

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_ontologies.Ontologies.md#constructor)

### Methods

- [create](appLib_SDKDrivers_xFrameDriver_ontologies.Ontologies.md#create)
- [crudReq](appLib_SDKDrivers_xFrameDriver_ontologies.Ontologies.md#crudreq)
- [crudReqSync](appLib_SDKDrivers_xFrameDriver_ontologies.Ontologies.md#crudreqsync)
- [delete](appLib_SDKDrivers_xFrameDriver_ontologies.Ontologies.md#delete)
- [get](appLib_SDKDrivers_xFrameDriver_ontologies.Ontologies.md#get)
- [query](appLib_SDKDrivers_xFrameDriver_ontologies.Ontologies.md#query)
- [update](appLib_SDKDrivers_xFrameDriver_ontologies.Ontologies.md#update)

## Constructors

### constructor

• **new Ontologies**(`agent`)

Creates an instance of Repository.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

#### Inherited from

[Repository](appLib_SDKDrivers_xFrameDriver_repository.Repository.md).[constructor](appLib_SDKDrivers_xFrameDriver_repository.Repository.md#constructor)

## Methods

### create

▸ **create**(`payload`): `Promise`<`APIOntologyV2`\>

Creates a new ontology.

**`Example`**

```ts
const ontology = await dl.ontologies.create({
    title: 'My ontology',
    projectIds: ['projectId']
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `CreateOntologyPayloadV2` | The payload of the ontology to be created. |

#### Returns

`Promise`<`APIOntologyV2`\>

- A promise that resolves to the created ontology.

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

### delete

▸ **delete**(`ontologyId`): `Promise`<`void`\>

Deletes an ontology.

**`Example`**

```ts
await dl.ontologies.delete('ontologyId')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ontologyId` | `string` | The id of the ontology to be deleted. |

#### Returns

`Promise`<`void`\>

- A promise that resolves when the ontology is deleted.

#### Implementation of

IBundle.delete

___

### get

▸ **get**(`ontologyId?`): `Promise`<`APIOntologyV2`\>

Retrieves an ontology.

If no ontology id is provided, the active ontology will be retrieved.

**`Example`**

```ts
const activeOntology = await dl.ontologies.get()
```

**`Example`**

```ts
const ontology = await dl.ontologies.get('ontologyId')
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `ontologyId?` | `string` | The id of the ontology to be retrieved. |

#### Returns

`Promise`<`APIOntologyV2`\>

- A promise that resolves to the retrieved ontology.

#### Implementation of

IBundle.get

___

### query

▸ **query**(`payload?`, `options?`): `Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<`APIOntologyV2`\>\>

Queries ontologies.

**`Example`**

```ts
const ontologies = await dl.ontologies.query({
   ids: ['ontologyId', 'ontologyId2']
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload?` | `OntologyQueryV2` | The payload of the query. |
| `options?` | `IQueryOptions` | The options of the query. |

#### Returns

`Promise`<[`IPagedResponse`](../interfaces/sdkApi_interfaces_entities_iQuery.IPagedResponse.md)<`APIOntologyV2`\>\>

- A promise that resolves to the queried ontologies.

#### Implementation of

IBundle.query

___

### update

▸ **update**(`payload`): `Promise`<`APIOntologyV2`\>

Retrieves a list of ontologies.

**`Example`**

```ts
const updatedOntology = await dl.ontologies.update({
   id: 'ontologyId',
   title: 'My updated ontology'
})
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `UpdateOntologyPayloadV2` | The payload of the ontology to be updated. |

#### Returns

`Promise`<`APIOntologyV2`\>

- A promise that resolves to the updated ontology.

#### Implementation of

IBundle.update
