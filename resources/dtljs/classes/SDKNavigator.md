# Class: SDKNavigator

[appLib/SDKDrivers/xFrameDriver/navigator](../modules/appLib_SDKDrivers_xFrameDriver_navigator.md).SDKNavigator

SDKNavigator - The platform navigator.

The SDKNavigator class enables navigation to routes within the platform.

## Implements

- [`IAppNavigator`](../interfaces/appLib_SDKDrivers_xFrameDriver_navigator.IAppNavigator.md)

## Table of contents

### Constructors

- [constructor](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#constructor)

### Methods

- [applicationHub](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#applicationhub)
- [assignments](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#assignments)
- [auditLogs](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#auditlogs)
- [cloudStorage](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#cloudstorage)
- [custom](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#custom)
- [datasetBrowser](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#datasetbrowser)
- [datasets](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#datasets)
- [orgMembersAndGroups](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#orgmembersandgroups)
- [projectOverview](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#projectoverview)
- [projectTeam](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#projectteam)
- [projects](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#projects)
- [recipe](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#recipe)
- [recipes](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#recipes)
- [startline](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#startline)
- [studio](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#studio)
- [taskBrowser](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#taskbrowser)
- [tasks](appLib_SDKDrivers_xFrameDriver_navigator.SDKNavigator.md#tasks)

## Constructors

### constructor

• **new SDKNavigator**(`agent`)

Creates an instance of Navigator.

#### Parameters

| Name | Type |
| :------ | :------ |
| `agent` | `PeerAgent` |

## Methods

### applicationHub

▸ **applicationHub**(`options?`): `void`

Navigates to the application hub page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### assignments

▸ **assignments**(`options?`): `void`

Navigates to the active project's assignments page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### auditLogs

▸ **auditLogs**(`options?`): `void`

Navigates to the active organization's audit logs page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### cloudStorage

▸ **cloudStorage**(`options?`): `void`

Navigates to the active project's cloud storage page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### custom

▸ **custom**(`route`, `payload?`): `void`

Navigates to a custom route.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `route` | `string` | The route to navigate to. |
| `payload?` | `Object` | The navigation payload. |
| `payload.options?` | `DlNavigationOptions` | The navigation options. |
| `payload.params?` | `any` | The navigation params. |

#### Returns

`void`

___

### datasetBrowser

▸ **datasetBrowser**(`datasetId`, `options?`): `void`

Navigates to the dataset browser page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `datasetId` | `string` | The id of the dataset to navigate to. |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### datasets

▸ **datasets**(`options?`): `void`

Navigates to the datasets page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### orgMembersAndGroups

▸ **orgMembersAndGroups**(`options?`): `void`

Navigates to the active organization's members and groups page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### projectOverview

▸ **projectOverview**(`options?`): `void`

Navigates to the project overview page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### projectTeam

▸ **projectTeam**(`options?`): `void`

Navigates to the active project's team page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### projects

▸ **projects**(`options?`): `void`

Navigates to the projects page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### recipe

▸ **recipe**(`recipeId`, `options?`): `void`

Navigates to the active project's recipe page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `recipeId` | `string` | The id of the recipe to navigate to. |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### recipes

▸ **recipes**(`options?`): `void`

Navigates to the active project's recipes page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### startline

▸ **startline**(`payload`): `void`

Navigates to the startline page.

**`Example`**

```ts
dl.navigator.startline({ query: { tab: "Models" }, options: { newTab: true } })
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `payload` | `Object` | - |
| `payload.options?` | `DlNavigationOptions` | The navigation options. For example: { newTab: true } |
| `payload.query?` | `Dictionary` | The query parameters. For example: { tab: "Models" } |

#### Returns

`void`

___

### studio

▸ **studio**(`params`, `options?`): `void`

Navigates to the active project's dataset item page (the studio).

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `params` | `Object` | The navigation params. |
| `params.datasetId?` | `string` | The id of the dataset the item belongs to. When not provided, the active dataset is used. |
| `params.itemId` | `string` | The id of the item to navigate to. |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### taskBrowser

▸ **taskBrowser**(`taskId`, `options?`): `void`

Navigates to the active project's task browser page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `taskId` | `string` | The id of the task to navigate to. |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`

___

### tasks

▸ **tasks**(`options?`): `void`

Navigates to the active project's tasks page.

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `options?` | `DlNavigationOptions` | The navigation options. |

#### Returns

`void`
