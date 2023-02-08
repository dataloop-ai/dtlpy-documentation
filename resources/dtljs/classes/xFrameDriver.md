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

- [agent](xFrameDriver.md#agent)
- [annotations](xFrameDriver.md#annotations)
- [attributes](xFrameDriver.md#attributes)
- [contributors](xFrameDriver.md#contributors)
- [datasets](xFrameDriver.md#datasets)
- [items](xFrameDriver.md#items)
- [labels](xFrameDriver.md#labels)
- [ontologies](xFrameDriver.md#ontologies)
- [projects](xFrameDriver.md#projects)
- [recipes](xFrameDriver.md#recipes)
- [settings](xFrameDriver.md#settings)
- [structures](xFrameDriver.md#structures)
- [tasks](xFrameDriver.md#tasks)

### Methods

- [init](xFrameDriver.md#init)

## Properties

### agent

• **agent**: `PeerAgent`

The application's agent.

___

### annotations

• **annotations**: [`Annotations`](./Annotations.md)

The Annotations repository.
It is used to access Annotation related CRUD methods.

___

### attributes

• **attributes**: `Attributes`

The Attributes repository.
It is used to access Attribute related CRUD methods.

___

### contributors

• **contributors**: [`Contributors`](Contributors.md)

The Contributors repository.
It is used to access Contributor related CRUD methods.

___

### datasets

• **datasets**: [`Datasets`](Datasets.md)

The Datasets repository.
It is used to access Dataset related CRUD methods.

___

### items

• **items**: [`Items`](Items.md)

The Items repository.
It is used to access Item related CRUD methods.

___

### labels

• **labels**: [`Labels`](Labels.md)

The Labels repository.
It is used to access Label related CRUD methods.

___

### ontologies

• **ontologies**: [`Ontologies`](Ontologies.md)

The Ontologies repository.
It is used to access Ontology related CRUD methods.

___

### projects

• **projects**: [`Projects`](Projects.md)

The Projects repository.
It is used to access Project related CRUD methods.

___

### recipes

• **recipes**: [`Recipes`](Recipes.md)

The Recipes repository.
It is used to access Recipe related CRUD methods.

___

### settings

• **settings**: [`AppSettings`](AppSettings.md)

The Settings repository.
It is used to access Settings related CRUD methods.

___

### structures

• **structures**: `Structures`

The Structures repository.
It is used to access Structure related CRUD methods.

___

### tasks

• **tasks**: [`Tasks`](Tasks.md)

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

