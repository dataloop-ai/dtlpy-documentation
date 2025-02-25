# Class: FrameAgent

## Hierarchy

- `EventEmitter`

  ↳ **`FrameAgent`**

  ↳↳ [`PeerAgent`](PeerAgent.md)

## Table of contents

### Properties

- [id](FrameAgent.md#id)
- [remote](FrameAgent.md#remote)

### Constructors

- [constructor](FrameAgent.md#constructor)

### Methods

- [send](FrameAgent.md#send)
- [sendSync](FrameAgent.md#sendsync)
- [createPeer](FrameAgent.md#createpeer)
- [loadPeer](FrameAgent.md#loadpeer)
- [removePeer](FrameAgent.md#removepeer)
- [destroy](FrameAgent.md#destroy)

## Properties

### id

• **id**: `string`

___

### remote

• **remote**: `boolean` = `false`

## Constructors

### constructor

• **new FrameAgent**(`win?`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `win?` | `Window` |

#### Overrides

EventEmitter.constructor

## Methods

### send

▸ **send**(`data`, `peerId?`): `void`

#### Parameters

| Name | Type | Default value |
| :------ | :------ | :------ |
| `data` | `any` | `undefined` |
| `peerId` | `string` | `null` |

#### Returns

`void`

___

### sendSync

▸ **sendSync**(`data`, `options?`): `Promise`<`unknown`\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `any` |
| `options` | `Object` |
| `options.timeout?` | `number` |
| `options.peerId?` | `string` |

#### Returns

`Promise`<`unknown`\>

___

### createPeer

▸ **createPeer**(`onDataCallback?`): `Promise`<[`PeerAgent`](PeerAgent.md)\>

#### Parameters

| Name | Type |
| :------ | :------ |
| `onDataCallback?` | `Function` |

#### Returns

`Promise`<[`PeerAgent`](PeerAgent.md)\>

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

___

### removePeer

▸ **removePeer**(`peerId`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `peerId` | `string` |

#### Returns

`void`

___

### destroy

▸ **destroy**(`peerId?`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `peerId?` | `string` |

#### Returns

`void`
