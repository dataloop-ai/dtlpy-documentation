# Class: AgentMessage<T\>

## Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

## Implements

- [`IAgentMessage`](../interfaces/IAgentMessage.md)<`T`\>

## Table of contents

### Properties

- [type](AgentMessage.md#type)
- [data](AgentMessage.md#data)
- [source](AgentMessage.md#source)
- [timeout](AgentMessage.md#timeout)

### Constructors

- [constructor](AgentMessage.md#constructor)

## Properties

### type

• **type**: [`AgentMessageType`](../enums/AgentMessageType.md)

#### Implementation of

[IAgentMessage](../interfaces/IAgentMessage.md).[type](../interfaces/IAgentMessage.md#type)

___

### data

• **data**: `T`

#### Implementation of

[IAgentMessage](../interfaces/IAgentMessage.md).[data](../interfaces/IAgentMessage.md#data)

___

### source

• `Optional` **source**: [`IAgentMessageSource`](../interfaces/IAgentMessageSource.md)

#### Implementation of

[IAgentMessage](../interfaces/IAgentMessage.md).[source](../interfaces/IAgentMessage.md#source)

___

### timeout

• `Optional` **timeout**: `number`

#### Implementation of

[IAgentMessage](../interfaces/IAgentMessage.md).[timeout](../interfaces/IAgentMessage.md#timeout)

## Constructors

### constructor

• **new AgentMessage**<`T`\>(`message`)

#### Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

#### Parameters

| Name | Type |
| :------ | :------ |
| `message` | [`IAgentMessage`](../interfaces/IAgentMessage.md)<`any`\> |
