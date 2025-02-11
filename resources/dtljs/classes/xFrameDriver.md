# Class: xFrameDriver

This class represents the SDK driver used by external applications.
This class extends the EventEmitter and implements the JsSDK interface.

**`Implements`**

JsSDK

## Hierarchy

- `EventEmitter`

  ↳ **`xFrameDriver`**

## Implements

- [`JsSDK`](../interfaces/JsSDK.md)

## Table of contents

### Constructors

- [constructor](xFrameDriver.md#constructor)

### Properties

- [agent](xFrameDriver.md#agent)
- [projects](xFrameDriver.md#projects)
- [annotations](xFrameDriver.md#annotations)
- [items](xFrameDriver.md#items)
- [settings](xFrameDriver.md#settings)
- [recipes](xFrameDriver.md#recipes)
- [ontologies](xFrameDriver.md#ontologies)
- [labels](xFrameDriver.md#labels)
- [attributes](xFrameDriver.md#attributes)
- [structures](xFrameDriver.md#structures)
- [tasks](xFrameDriver.md#tasks)
- [contributors](xFrameDriver.md#contributors)
- [datasets](xFrameDriver.md#datasets)
- [executions](xFrameDriver.md#executions)
- [drivers](xFrameDriver.md#drivers)
- [integrations](xFrameDriver.md#integrations)
- [pipelines](xFrameDriver.md#pipelines)
- [navigator](xFrameDriver.md#navigator)

### Methods

- [init](xFrameDriver.md#init)
- [sendEvent](xFrameDriver.md#sendevent)

### Accessors

- [logger](xFrameDriver.md#logger)

## Constructors

### constructor

• **new xFrameDriver**()

#### Inherited from

EventEmitter.constructor

## Properties

### agent

• **agent**: [`PeerAgent`](PeerAgent.md)

The application's agent.

___

### projects

• **projects**: `Projects`

The Projects repository.
It is used to access Project related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[projects](../interfaces/JsSDK.md#projects)

___

### annotations

• **annotations**: `Annotations`

The Annotations repository.
It is used to access Annotation related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[annotations](../interfaces/JsSDK.md#annotations)

___

### items

• **items**: `Items`

The Items repository.
It is used to access Item related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[items](../interfaces/JsSDK.md#items)

___

### settings

• **settings**: [`AppSettings`](AppSettings.md)

The Settings repository.
It is used to access Settings related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[settings](../interfaces/JsSDK.md#settings)

___

### recipes

• **recipes**: `Recipes`

The Recipes repository.
It is used to access Recipe related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[recipes](../interfaces/JsSDK.md#recipes)

___

### ontologies

• **ontologies**: `Ontologies`

The Ontologies repository.
It is used to access Ontology related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[ontologies](../interfaces/JsSDK.md#ontologies)

___

### labels

• **labels**: `Labels`

The Labels repository.
It is used to access Label related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[labels](../interfaces/JsSDK.md#labels)

___

### attributes

• **attributes**: `Attributes`

The Attributes repository.
It is used to access Attribute related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[attributes](../interfaces/JsSDK.md#attributes)

___

### structures

• **structures**: `Structures`

The Structures repository.
It is used to access Structure related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[structures](../interfaces/JsSDK.md#structures)

___

### tasks

• **tasks**: `Tasks`

The Tasks repository.
It is used to access Task related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[tasks](../interfaces/JsSDK.md#tasks)

___

### contributors

• **contributors**: `Contributors`

The Contributors repository.
It is used to access Contributor related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[contributors](../interfaces/JsSDK.md#contributors)

___

### datasets

• **datasets**: `Datasets`

The Datasets repository.
It is used to access Dataset related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[datasets](../interfaces/JsSDK.md#datasets)

___

### executions

• **executions**: `Executions`

The Executions repository.
It is used to access Execution related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[executions](../interfaces/JsSDK.md#executions)

___

### drivers

• **drivers**: `Drivers`

The Drivers repository.
It is used to access Driver related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[drivers](../interfaces/JsSDK.md#drivers)

___

### integrations

• **integrations**: `Integrations`

The Integrations repository.
It is used to access Integration related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[integrations](../interfaces/JsSDK.md#integrations)

___

### pipelines

• **pipelines**: `Pipelines`

The Pipelines repository.
It is used to access Pipeline related CRUD methods.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[pipelines](../interfaces/JsSDK.md#pipelines)

___

### navigator

• **navigator**: [`SDKNavigator`](SDKNavigator.md)

The Navigator.
It is used to navigate to different routes within the platform.

#### Implementation of

[JsSDK](../interfaces/JsSDK.md).[navigator](../interfaces/JsSDK.md#navigator)

## Methods

### init

▸ **init**(): `Promise`<`void`\>

Initializes the xFrame SDK Driver with an agent and all the existing repositories.
Initializes agent events.

#### Returns

`Promise`<`void`\>

- A promise that resolves once the xFrameDriver instance has been initialized.

#### Implementation of

JsSDK.init

___

### sendEvent

▸ **sendEvent**(`data`): `void`

Sends an event from the app.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `data` | [`EventPayload`](../interfaces/EventPayload.md) | The event payload. |

#### Returns

`void`

## Accessors

### logger

• `get` **logger**(): `Logger`

Returns the logger object.

#### Returns

`Logger`
