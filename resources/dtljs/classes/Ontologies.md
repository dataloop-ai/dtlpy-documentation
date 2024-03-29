# Class: Ontologies

[repositories](./repositories.md).Ontologies

Ontologies repository --- *currently not supported*

The Ontology class allows the user to manage ontologies.

## Hierarchy

- [`Repository`](Repository.md)

  ↳ **`Ontologies`**

## Implements

- [`IBundle`](../interfaces/IBundle.md)<`APIOntologyV2`>

## Table of contents

### Constructors

- [constructor](Ontologies.md#constructor)

### Methods

- [create](Ontologies.md#create)
- [delete](Ontologies.md#delete)
- [get](Ontologies.md#get)
- [query](Ontologies.md#query)
- [update](Ontologies.md#update)

## Constructors

### constructor

• **new Ontologies**(`agent`)

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

▸ **create**(`payload`): `Promise`<`APIOntologyV2`>

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

`Promise`<`APIOntologyV2`>

- A promise that resolves to the created ontology.

___

### delete

▸ **delete**(`ontologyId`): `Promise`<`void`>

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

`Promise`<`void`>

- A promise that resolves when the ontology is deleted.

___

### get

▸ **get**(`ontologyId?`): `Promise`<`APIOntologyV2`>

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

`Promise`<`APIOntologyV2`>

- A promise that resolves to the retrieved ontology.

___

### query

▸ **query**(`payload?`
, `options?`): `Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<`APIOntologyV2`>>

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

`Promise`<[`IPagedResponse`](../interfaces/IPagedResponse.md)<`APIOntologyV2`>>

- A promise that resolves to the queried ontologies.

___

### update

▸ **update**(`payload`): `Promise`<`APIOntologyV2`>

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

`Promise`<`APIOntologyV2`>

- A promise that resolves to the updated ontology.
