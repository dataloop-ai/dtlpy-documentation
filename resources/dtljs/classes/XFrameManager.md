# Class: XFrameManager

## Hierarchy

- `EventEmitter`

  ↳ **`XFrameManager`**

## Table of contents

### Properties

- [onDataCallback](XFrameManager.md#ondatacallback)

### Constructors

- [constructor](XFrameManager.md#constructor)

### Accessors

- [logger](XFrameManager.md#logger)
- [hostAgent](XFrameManager.md#hostagent)
- [guestAgents](XFrameManager.md#guestagents)

### Methods

- [createFrameByUrl](XFrameManager.md#createframebyurl)
- [createGuest](XFrameManager.md#createguest)
- [registerGuest](XFrameManager.md#registerguest)
- [removeGuest](XFrameManager.md#removeguest)

## Properties

### onDataCallback

• **onDataCallback**: `Function`

## Constructors

### constructor

• **new XFrameManager**(`hostWindow?`, `onDataCallback?`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `hostWindow?` | `Window` |
| `onDataCallback?` | `Function` |

#### Overrides

EventEmitter.constructor

## Accessors

### logger

• `get` **logger**(): `Logger`

#### Returns

`Logger`

___

### hostAgent

• `get` **hostAgent**(): [`FrameAgent`](FrameAgent.md)

#### Returns

[`FrameAgent`](FrameAgent.md)

___

### guestAgents

• `get` **guestAgents**(): [`FrameAgent`](FrameAgent.md)[]

#### Returns

[`FrameAgent`](FrameAgent.md)[]

## Methods

### createFrameByUrl

▸ **createFrameByUrl**(`url`): `Promise`<[`PeerAgent`](PeerAgent.md)\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `url` | `string` |

#### Returns

`Promise`<[`PeerAgent`](PeerAgent.md)\>

___

### createGuest

▸ **createGuest**(): `Promise`<[`PeerAgent`](PeerAgent.md)\>

#### Returns

`Promise`<[`PeerAgent`](PeerAgent.md)\>

___

### registerGuest

▸ **registerGuest**(`guestWindow`, `peerId?`): `Promise`<[`PeerAgent`](PeerAgent.md)\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `guestWindow` | `Window` |
| `peerId?` | `string` |

#### Returns

`Promise`<[`PeerAgent`](PeerAgent.md)\>

___

### removeGuest

▸ **removeGuest**(`peerId`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `peerId` | `string` |

#### Returns

`void`
