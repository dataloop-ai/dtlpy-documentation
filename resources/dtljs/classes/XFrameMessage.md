# Class: XFrameMessage

## Table of contents

### Properties

- [id](XFrameMessage.md#id)
- [xFrame](XFrameMessage.md#xframe)
- [responseId](XFrameMessage.md#responseid)
- [error](XFrameMessage.md#error)
- [message](XFrameMessage.md#message)
- [type](XFrameMessage.md#type)
- [resolve](XFrameMessage.md#resolve)
- [reject](XFrameMessage.md#reject)
- [sync](XFrameMessage.md#sync)
- [data](XFrameMessage.md#data)
- [sentTime](XFrameMessage.md#senttime)
- [timeout](XFrameMessage.md#timeout)
- [channelId](XFrameMessage.md#channelid)

### Constructors

- [constructor](XFrameMessage.md#constructor)

### Methods

- [fromJson](XFrameMessage.md#fromjson)

## Properties

### id

• **id**: `string`

___

### xFrame

• **xFrame**: `boolean` = `true`

___

### responseId

• **responseId**: `string`

___

### error

• **error**: `string`

___

### message

• **message**: `string`

___

### type

• **type**: [`XFrameMessageType`](../enums/XFrameMessageType.md)

___

### resolve

• **resolve**: `any`

___

### reject

• **reject**: `any`

___

### sync

• **sync**: `boolean`

___

### data

• **data**: `any`

___

### sentTime

• **sentTime**: `number` = `null`

___

### timeout

• **timeout**: `number` = `1800`

___

### channelId

• **channelId**: `string`

## Constructors

### constructor

• **new XFrameMessage**(`init?`)

#### Parameters

| Name | Type |
| :------ | :------ |
| `init?` | `Partial`<[`XFrameMessage`](XFrameMessage.md)\> |

## Methods

### fromJson

▸ `Static` **fromJson**(`data`): `void`

#### Parameters

| Name | Type |
| :------ | :------ |
| `data` | `Partial`<[`XFrameMessage`](XFrameMessage.md)\> |

#### Returns

`void`
