# Class: CrudMessage<T\>

## Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

## Table of contents

### Properties

- [data](CrudMessage.md#data)
- [crud](CrudMessage.md#crud)
- [scope](CrudMessage.md#scope)

### Constructors

- [constructor](CrudMessage.md#constructor)

## Properties

### data

• **data**: `T`

___

### crud

• **crud**: [`CrudType`](../enums/CrudType.md) \| [`CrudEvent`](../enums/CrudEvent.md)

___

### scope

• **scope**: [`AppMessageScope`](../enums/AppMessageScope.md)

## Constructors

### constructor

• **new CrudMessage**<`T`\>(`init?`)

#### Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

#### Parameters

| Name | Type |
| :------ | :------ |
| `init?` | `Partial`<[`CrudMessage`](CrudMessage.md)<`any`\>\> |
