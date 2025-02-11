# Interface: JsSDK

The JsSDK is the base interface for the SDK.

**`Interface`**

JsSDK

## Implemented by

- [`DlMockDriver`](../classes/DlMockDriver.md)
- [`xFrameDriver`](../classes/xFrameDriver.md)

## Table of contents

### Properties

- [init](JsSDK.md#init)
- [on](JsSDK.md#on)
- [once](JsSDK.md#once)
- [off](JsSDK.md#off)
- [projects](JsSDK.md#projects)
- [annotations](JsSDK.md#annotations)
- [items](JsSDK.md#items)
- [settings](JsSDK.md#settings)
- [recipes](JsSDK.md#recipes)
- [ontologies](JsSDK.md#ontologies)
- [labels](JsSDK.md#labels)
- [attributes](JsSDK.md#attributes)
- [structures](JsSDK.md#structures)
- [datasets](JsSDK.md#datasets)
- [tasks](JsSDK.md#tasks)
- [contributors](JsSDK.md#contributors)
- [executions](JsSDK.md#executions)
- [drivers](JsSDK.md#drivers)
- [integrations](JsSDK.md#integrations)
- [pipelines](JsSDK.md#pipelines)
- [navigator](JsSDK.md#navigator)

## Properties

### init

• `Optional` **init**: (...`args`: `any`[]) => `void`

#### Type declaration

▸ (`...args`): `void`

##### Parameters

| Name | Type |
| :------ | :------ |
| `...args` | `any`[] |

##### Returns

`void`

___

### on

• `Optional` **on**: (`e`: `string`, `handler`: (...`args`: `any`[]) => `void`) => `void`

#### Type declaration

▸ (`e`, `handler`): `void`

##### Parameters

| Name | Type |
| :------ | :------ |
| `e` | `string` |
| `handler` | (...`args`: `any`[]) => `void` |

##### Returns

`void`

___

### once

• `Optional` **once**: (`e`: `string`, `handler`: (...`args`: `any`[]) => `void`) => `void`

#### Type declaration

▸ (`e`, `handler`): `void`

##### Parameters

| Name | Type |
| :------ | :------ |
| `e` | `string` |
| `handler` | (...`args`: `any`[]) => `void` |

##### Returns

`void`

___

### off

• `Optional` **off**: (`e`: `string`, `handler`: (...`args`: `any`[]) => `void`) => `void`

#### Type declaration

▸ (`e`, `handler`): `void`

##### Parameters

| Name | Type |
| :------ | :------ |
| `e` | `string` |
| `handler` | (...`args`: `any`[]) => `void` |

##### Returns

`void`

___

### projects

• `Optional` **projects**: [`IBundle`](IBundle.md)<[`SDKProject`](../classes/SDKProject.md)\>

___

### annotations

• `Optional` **annotations**: [`IBundle`](IBundle.md)<[`SDKAnnotation`](../classes/SDKAnnotation.md)<`any`\>\>

___

### items

• `Optional` **items**: [`IBundle`](IBundle.md)<[`SDKItem`](../classes/SDKItem.md)\>

___

### settings

• `Optional` **settings**: [`IBundle`](IBundle.md)<[`iAppSettings`](iAppSettings.md)\>

___

### recipes

• `Optional` **recipes**: [`IBundle`](IBundle.md)<[`APIRecipeV2`](../classes/APIRecipeV2.md)\>

___

### ontologies

• `Optional` **ontologies**: [`IBundle`](IBundle.md)<[`APIOntologyV2`](../classes/APIOntologyV2.md)\>

___

### labels

• `Optional` **labels**: [`IBundle`](IBundle.md)<[`APILabelTreeNodeV2`](../classes/APILabelTreeNodeV2.md) \| [`SDKLabelTreeNode`](../classes/SDKLabelTreeNode.md)\>

___

### attributes

• `Optional` **attributes**: [`IBundle`](IBundle.md)<[`APIAttributeSectionV2`](../classes/APIAttributeSectionV2.md)\>

___

### structures

• `Optional` **structures**: [`IBundle`](IBundle.md)<[`APIStructureV2`](../classes/APIStructureV2.md)\>

___

### datasets

• `Optional` **datasets**: [`IBundle`](IBundle.md)<[`SDKDataset`](../classes/SDKDataset.md)\>

___

### tasks

• `Optional` **tasks**: [`IBundle`](IBundle.md)<[`SDKTask`](../classes/SDKTask.md)\>

___

### contributors

• `Optional` **contributors**: [`IBundle`](IBundle.md)<[`SDKContributor`](../classes/SDKContributor.md)\>

___

### executions

• `Optional` **executions**: [`IBundle`](IBundle.md)<[`SDKExecution`](../classes/SDKExecution.md)\>

___

### drivers

• `Optional` **drivers**: [`IBundle`](IBundle.md)<[`SDKDriver`](../classes/SDKDriver.md)\>

___

### integrations

• `Optional` **integrations**: [`IBundle`](IBundle.md)<[`SDKIntegration`](../classes/SDKIntegration.md)\>

___

### pipelines

• `Optional` **pipelines**: [`IBundle`](IBundle.md)<[`SDKPipeline`](../classes/SDKPipeline.md)\>

___

### navigator

• `Optional` **navigator**: [`IAppNavigator`](IAppNavigator.md)
