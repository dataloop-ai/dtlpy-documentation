# Class: xFrameDriver

[main](../index.md).xFrameDriver

This class represents the SDK driver used by external applications.
This class extends the EventEmitter and implements the JsSDK interface.

## Hierarchy

- `EventEmitter`

  ↳ **`xFrameDriver`**

## Implements

- `JsSDK`

## Table of contents

### Properties

- [agent](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#agent)
- [annotations](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#annotations)
- [attributes](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#attributes)
- [contributors](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#contributors)
- [datasets](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#datasets)
- [items](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#items)
- [labels](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#labels)
- [ontologies](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#ontologies)
- [projects](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#projects)
- [recipes](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#recipes)
- [settings](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#settings)
- [structures](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#structures)
- [tasks](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#tasks)

### Methods

- [init](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#init)
- [listenerCount](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#listenercount)

## Properties

### agent

• **agent**: `PeerAgent`

The application's agent.

___

### annotations

• **annotations**: [`Annotations`](appLib_SDKDrivers_xFrameDriver_annotations.Annotations.md)

The Annotations repository.
It is used to access Annotation related CRUD methods.

___

### attributes

• **attributes**: `Attributes`

The Attributes repository.
It is used to access Attribute related CRUD methods.

___

### contributors

• **contributors**: [`Contributors`](appLib_SDKDrivers_xFrameDriver_contributors.Contributors.md)

The Contributors repository.
It is used to access Contributor related CRUD methods.

___

### datasets

• **datasets**: [`Datasets`](appLib_SDKDrivers_xFrameDriver_datasets.Datasets.md)

The Datasets repository.
It is used to access Dataset related CRUD methods.

___

### items

• **items**: [`Items`](appLib_SDKDrivers_xFrameDriver_items.Items.md)

The Items repository.
It is used to access Item related CRUD methods.

___

### labels

• **labels**: [`Labels`](appLib_SDKDrivers_xFrameDriver_labels.Labels.md)

The Labels repository.
It is used to access Label related CRUD methods.

___

### ontologies

• **ontologies**: [`Ontologies`](appLib_SDKDrivers_xFrameDriver_ontologies.Ontologies.md)

The Ontologies repository.
It is used to access Ontology related CRUD methods.

___

### projects

• **projects**: [`Projects`](appLib_SDKDrivers_xFrameDriver_projects.Projects.md)

The Projects repository.
It is used to access Project related CRUD methods.

___

### recipes

• **recipes**: [`Recipes`](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md)

The Recipes repository.
It is used to access Recipe related CRUD methods.

___

### settings

• **settings**: [`AppSettings`](appLib_SDKDrivers_xFrameDriver_appSettings.AppSettings.md)

The Settings repository.
It is used to access Settings related CRUD methods.

___

### structures

• **structures**: `Structures`

The Structures repository.
It is used to access Structure related CRUD methods.

___

### tasks

• **tasks**: [`Tasks`](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md)

The Tasks repository.
It is used to access Task related CRUD methods.

## Methods

### init

▸ **init**(): `Promise`<`void`>

Initializes the xFrame SDK Driver with an agent and all the existing repositories.
Initializes agent events.

#### Returns

`Promise`<`void`>

- A promise that resolves once the xFrameDriver instance has been initialized.

___

### listenerCount

▸ `Static` **listenerCount**(`emitter`, `event`): `number`

**`Deprecated`**

since v4.0.0

#### Parameters

| Name | Type |
| :------ | :------ |
| `emitter` | `EventEmitter` |
| `event` | `string` \| `symbol` |

#### Returns

`number`

#### Inherited from

EventEmitter.listenerCount
