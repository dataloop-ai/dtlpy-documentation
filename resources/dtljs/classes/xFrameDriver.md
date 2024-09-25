# Class: xFrameDriver

[appLib/SDKDrivers/xFrameDriver](../modules/appLib_SDKDrivers_xFrameDriver.md).xFrameDriver

This class represents the SDK driver used by external applications.
This class extends the EventEmitter and implements the JsSDK interface.

**`Implements`**

JsSDK

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
- [drivers](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#drivers)
- [executions](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#executions)
- [integrations](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#integrations)
- [items](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#items)
- [labels](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#labels)
- [navigator](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#navigator)
- [ontologies](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#ontologies)
- [projects](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#projects)
- [recipes](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#recipes)
- [settings](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#settings)
- [structures](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#structures)
- [tasks](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#tasks)

### Accessors

- [logger](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#logger)

### Methods

- [init](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#init)
- [sendEvent](appLib_SDKDrivers_xFrameDriver.xFrameDriver.md#sendevent)
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

#### Implementation of

JsSDK.annotations

___

### attributes

• **attributes**: `Attributes`

The Attributes repository.
It is used to access Attribute related CRUD methods.

#### Implementation of

JsSDK.attributes

___

### contributors

• **contributors**: [`Contributors`](appLib_SDKDrivers_xFrameDriver_contributors.Contributors.md)

The Contributors repository.
It is used to access Contributor related CRUD methods.

#### Implementation of

JsSDK.contributors

___

### datasets

• **datasets**: [`Datasets`](appLib_SDKDrivers_xFrameDriver_datasets.Datasets.md)

The Datasets repository.
It is used to access Dataset related CRUD methods.

#### Implementation of

JsSDK.datasets

___

### drivers

• **drivers**: [`Drivers`](appLib_SDKDrivers_xFrameDriver_drivers.Drivers.md)

The Drivers repository.
It is used to access Driver related CRUD methods.

#### Implementation of

JsSDK.drivers

___

### executions

• **executions**: [`Executions`](appLib_SDKDrivers_xFrameDriver_executions.Executions.md)

The Executions repository.
It is used to access Execution related CRUD methods.

#### Implementation of

JsSDK.executions

___

### integrations

• **integrations**: [`Integrations`](appLib_SDKDrivers_xFrameDriver_integrations.Integrations.md)

The Integrations repository.
It is used to access Integration related CRUD methods.

#### Implementation of

JsSDK.integrations

___

### items

• **items**: [`Items`](appLib_SDKDrivers_xFrameDriver_items.Items.md)

The Items repository.
It is used to access Item related CRUD methods.

#### Implementation of

JsSDK.items

___

### labels

• **labels**: [`Labels`](appLib_SDKDrivers_xFrameDriver_labels.Labels.md)

The Labels repository.
It is used to access Label related CRUD methods.

#### Implementation of

JsSDK.labels

___

### navigator

• **navigator**: [`SDKNavigator`](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md)

The Navigator.
It is used to navigate to different routes within the platform.

#### Implementation of

JsSDK.navigator

___

### ontologies

• **ontologies**: [`Ontologies`](appLib_SDKDrivers_xFrameDriver_ontologies.Ontologies.md)

The Ontologies repository.
It is used to access Ontology related CRUD methods.

#### Implementation of

JsSDK.ontologies

___

### projects

• **projects**: [`Projects`](appLib_SDKDrivers_xFrameDriver_projects.Projects.md)

The Projects repository.
It is used to access Project related CRUD methods.

#### Implementation of

JsSDK.projects

___

### recipes

• **recipes**: [`Recipes`](appLib_SDKDrivers_xFrameDriver_recipes.Recipes.md)

The Recipes repository.
It is used to access Recipe related CRUD methods.

#### Implementation of

JsSDK.recipes

___

### settings

• **settings**: [`AppSettings`](appLib_SDKDrivers_xFrameDriver_appSettings.AppSettings.md)

The Settings repository.
It is used to access Settings related CRUD methods.

#### Implementation of

JsSDK.settings

___

### structures

• **structures**: `Structures`

The Structures repository.
It is used to access Structure related CRUD methods.

#### Implementation of

JsSDK.structures

___

### tasks

• **tasks**: [`Tasks`](appLib_SDKDrivers_xFrameDriver_tasks.Tasks.md)

The Tasks repository.
It is used to access Task related CRUD methods.

#### Implementation of

JsSDK.tasks

## Accessors

### logger

• `get` **logger**(): `Logger`

Returns the logger object.

#### Returns

`Logger`

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
| `data` | `EventPayload` | The event payload. |

#### Returns

`void`

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
