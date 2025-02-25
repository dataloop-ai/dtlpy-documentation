# Class: PeerAgent

## Hierarchy

- [`FrameAgent`](FrameAgent.md)

  ↳ **`PeerAgent`**

## Table of contents

### Properties

- [id](PeerAgent.md#id)
- [remote](PeerAgent.md#remote)
- [channel](PeerAgent.md#channel)
- [onDataCallback](PeerAgent.md#ondatacallback)

### Methods

- [createPeer](PeerAgent.md#createpeer)
- [loadPeer](PeerAgent.md#loadpeer)
- [removePeer](PeerAgent.md#removepeer)
- [send](PeerAgent.md#send)
- [sendSync](PeerAgent.md#sendsync)
- [sendCode](PeerAgent.md#sendcode)
- [sendRPC](PeerAgent.md#sendrpc)
- [sendEvent](PeerAgent.md#sendevent)
- [navigate](PeerAgent.md#navigate)
- [connect](PeerAgent.md#connect)
- [destroy](PeerAgent.md#destroy)

### Constructors

- [constructor](PeerAgent.md#constructor)

### Accessors

- [isRegistered](PeerAgent.md#isregistered)

## Properties

### id

• **id**: `string`

#### Inherited from

[FrameAgent](FrameAgent.md).[id](FrameAgent.md#id)

___

### remote

• **remote**: `boolean` = `false`

#### Inherited from

[FrameAgent](FrameAgent.md).[remote](FrameAgent.md#remote)

___

### channel

• **channel**: `Channel`

___

### onDataCallback

• **onDataCallback**: `Function`

## Methods

### createPeer

▸ **createPeer**(`onDataCallback?`): `Promise`<[`PeerAgent`](PeerAgent.md)\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `onDataCallback?` | `Function` |

#### Returns

`Promise`<[`PeerAgent`](PeerAgent.md)\>

#### Inherited from

[FrameAgent](FrameAgent.md).[createPeer](FrameAgent.md#createpeer)

___

### loadPeer

▸ **loadPeer**(`peerId`, `peerWindow`): `Promise`<[`PeerAgent`](PeerAgent.md)\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `peerId` | `string` |
| `peerWindow` | `Window` |

#### Returns

`Promise`<[`PeerAgent`](PeerAgent.md)\>

#### Inherited from

[FrameAgent](FrameAgent.md).[loadPeer](FrameAgent.md#loadpeer)

___

### removePeer

▸ **removePeer**(`peerId`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `peerId` | `string` |

#### Returns

`void`

#### Inherited from

[FrameAgent](FrameAgent.md).[removePeer](FrameAgent.md#removepeer)

___

### send

▸ **send**(`data`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `any` |

#### Returns

`void`

#### Overrides

[FrameAgent](FrameAgent.md).[send](FrameAgent.md#send)

___

### sendSync

▸ **sendSync**(`data`, `options?`): `Promise`<`unknown`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `any` |
| `options` | `Object` |
| `options.timeout?` | `number` |

#### Returns

`Promise`<`unknown`\>

#### Overrides

[FrameAgent](FrameAgent.md).[sendSync](FrameAgent.md#sendsync)

___

### sendCode

▸ **sendCode**(`code`, `options?`): `Promise`<`unknown`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `code` | `string` |
| `options` | `Object` |
| `options.timeout?` | `number` |

#### Returns

`Promise`<`unknown`\>

___

### sendRPC

▸ **sendRPC**(`data`, `options?`): `Promise`<`unknown`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `RPCData` |
| `options` | `Object` |
| `options.timeout?` | `number` |

#### Returns

`Promise`<`unknown`\>

___

### sendEvent

▸ **sendEvent**(`data`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | [`EventPayload`](../interfaces/EventPayload.md) |

#### Returns

`void`

___

### navigate

▸ **navigate**(`data`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | [`DlNavigationMessage`](DlNavigationMessage.md) |

#### Returns

`void`

___

### connect

▸ **connect**(`win`): `Promise`<`void`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `win` | `Window` |

#### Returns

`Promise`<`void`\>

___

### destroy

▸ **destroy**(): `void`

#### Returns

`void`

#### Overrides

[FrameAgent](FrameAgent.md).[destroy](FrameAgent.md#destroy)

## Constructors

### constructor

• **new PeerAgent**(`localWin`, `onDataCallback?`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `localWin` | `Window` |
| `onDataCallback?` | `Function` |

#### Overrides

[FrameAgent](FrameAgent.md).[constructor](FrameAgent.md#constructor)

## Accessors

### isRegistered

• `get` **isRegistered**(): `boolean`

#### Returns

`boolean`
