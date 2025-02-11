# Dataloop JS SDK - v0.0.93

## Table of contents

### README.md

- [README.md](README.md)

### App Debug

- [App Debug](apps/debug/index.md)

### Interfaces

- [DlMockData](interfaces/DlMockData.md)
- [iAppSettings](interfaces/iAppSettings.md)
- [IAppNavigator](interfaces/IAppNavigator.md)
- [EventPayload](interfaces/EventPayload.md)
- [IAgentMessageSource](interfaces/IAgentMessageSource.md)
- [IAgentMessage](interfaces/IAgentMessage.md)
- [DlNavigationOptions](interfaces/DlNavigationOptions.md)
- [JsSDK](interfaces/JsSDK.md)
- [IBundle](interfaces/IBundle.md)
- [ISupportedSlots](interfaces/ISupportedSlots.md)
- [IResource](interfaces/IResource.md)
- [IConditions](interfaces/IConditions.md)
- [IPanelConfig](interfaces/IPanelConfig.md)
- [IInvoke](interfaces/IInvoke.md)
- [ToolbarInvoke](interfaces/ToolbarInvoke.md)
- [IToolbarBase](interfaces/IToolbarBase.md)
- [IToolbarConfig](interfaces/IToolbarConfig.md)
- [IPipelineNode](interfaces/IPipelineNode.md)
- [IComputeConfigs](interfaces/IComputeConfigs.md)
- [IFunction](interfaces/IFunction.md)
- [IModuleConfig](interfaces/IModuleConfig.md)
- [IComponents](interfaces/IComponents.md)
- [IAppSettings](interfaces/IAppSettings-1.md)
- [ICrumbConfig](interfaces/ICrumbConfig.md)
- [ISidePanelConfig](interfaces/ISidePanelConfig.md)
- [IRoute](interfaces/IRoute.md)
- [SlotConfig](interfaces/SlotConfig.md)
- [IEntity](interfaces/IEntity.md)
- [IAccount](interfaces/IAccount.md)
- [IAnnotation](interfaces/IAnnotation.md)
- [AnnotationMetaData](interfaces/AnnotationMetaData.md)
- [SystemAnnotationMetaData](interfaces/SystemAnnotationMetaData.md)
- [AnnotationChanges](interfaces/AnnotationChanges.md)
- [IAttributeSection](interfaces/IAttributeSection.md)
- [IAttributeInstruction](interfaces/IAttributeInstruction.md)
- [CreateAttributePayloadV2](interfaces/CreateAttributePayloadV2.md)
- [UpdateAttributePayloadV2](interfaces/UpdateAttributePayloadV2.md)
- [IAttributeRange](interfaces/IAttributeRange.md)
- [IAttributeHierarchy](interfaces/IAttributeHierarchy.md)
- [IDataset](interfaces/IDataset.md)
- [IDriver](interfaces/IDriver.md)
- [IExecution](interfaces/IExecution.md)
- [SDKExecutionPayload](interfaces/SDKExecutionPayload.md)
- [IGroup](interfaces/IGroup.md)
- [IIntegration](interfaces/IIntegration.md)
- [IItem](interfaces/IItem.md)
- [ILabel](interfaces/ILabel.md)
- [ILabelDisplayData](interfaces/ILabelDisplayData.md)
- [ILabelDisplayImage](interfaces/ILabelDisplayImage.md)
- [ILabelScope](interfaces/ILabelScope.md)
- [ILabelTreeNode](interfaces/ILabelTreeNode.md)
- [CreateLabelPayloadV2](interfaces/CreateLabelPayloadV2.md)
- [UpdateLabelNodePayloadV2](interfaces/UpdateLabelNodePayloadV2.md)
- [ISDKLabelTreeNode](interfaces/ISDKLabelTreeNode.md)
- [IOntology](interfaces/IOntology.md)
- [OntologyQueryV2](interfaces/OntologyQueryV2.md)
- [CreateOntologyPayloadV2](interfaces/CreateOntologyPayloadV2.md)
- [UpdateOntologyPayloadV2](interfaces/UpdateOntologyPayloadV2.md)
- [IOrg](interfaces/IOrg.md)
- [IPipeline](interfaces/IPipeline.md)
- [IProject](interfaces/IProject.md)
- [IPagedResponse](interfaces/IPagedResponse.md)
- [IQueryOptions](interfaces/IQueryOptions.md)
- [IRecipeMetaData](interfaces/IRecipeMetaData.md)
- [IRecipeOntology](interfaces/IRecipeOntology.md)
- [IRecipe](interfaces/IRecipe.md)
- [IToolOptions](interfaces/IToolOptions.md)
- [RecipePayloadV2](interfaces/RecipePayloadV2.md)
- [RecipesQueryV2](interfaces/RecipesQueryV2.md)
- [PartialRecipePayloadV2](interfaces/PartialRecipePayloadV2.md)
- [IStructure](interfaces/IStructure.md)
- [CreateStructurePayloadV2](interfaces/CreateStructurePayloadV2.md)
- [UpdateStructurePayloadV2](interfaces/UpdateStructurePayloadV2.md)
- [ITask](interfaces/ITask.md)
- [SDKUpdateTaskAssigneesPayload](interfaces/SDKUpdateTaskAssigneesPayload.md)
- [IUser](interfaces/IUser.md)
- [IContributor](interfaces/IContributor.md)
- [IAnnotationSnapshot](interfaces/IAnnotationSnapshot.md)
- [SDKTimeServiceSettings](interfaces/SDKTimeServiceSettings.md)

### Classes

- [DlMockDriver](classes/DlMockDriver.md)
- [AppSettings](classes/AppSettings.md)
- [xFrameDriver](classes/xFrameDriver.md)
- [SDKNavigator](classes/SDKNavigator.md)
- [GuestApp](classes/GuestApp.md)
- [XFrameManager](classes/XFrameManager.md)
- [CrudMessage](classes/CrudMessage.md)
- [FrameAgent](classes/FrameAgent.md)
- [PeerAgent](classes/PeerAgent.md)
- [AgentMessage](classes/AgentMessage.md)
- [DlNavigationMessage](classes/DlNavigationMessage.md)
- [XFrameMessage](classes/XFrameMessage.md)
- [XFrameMessageError](classes/XFrameMessageError.md)
- [SDKAccount](classes/SDKAccount.md)
- [SDKAnnotation](classes/SDKAnnotation.md)
- [SDKAnnotationEvent](classes/SDKAnnotationEvent.md)
- [SDKAttributeInstruction](classes/SDKAttributeInstruction.md)
- [APIAttributeSectionV2](classes/APIAttributeSectionV2.md)
- [SDKDataset](classes/SDKDataset.md)
- [SDKDriver](classes/SDKDriver.md)
- [SDKExecution](classes/SDKExecution.md)
- [SDKFunctionExecution](classes/SDKFunctionExecution.md)
- [SDKGroup](classes/SDKGroup.md)
- [SDKIntegration](classes/SDKIntegration.md)
- [SDKItem](classes/SDKItem.md)
- [APILabelV2](classes/APILabelV2.md)
- [APILabelTreeNodeV2](classes/APILabelTreeNodeV2.md)
- [SDKLabel](classes/SDKLabel.md)
- [SDKLabelTreeNode](classes/SDKLabelTreeNode.md)
- [APIOntologyV2](classes/APIOntologyV2.md)
- [SDKOrg](classes/SDKOrg.md)
- [SDKPipeline](classes/SDKPipeline.md)
- [SDKProject](classes/SDKProject.md)
- [APIRecipeV2](classes/APIRecipeV2.md)
- [APIStructureV2](classes/APIStructureV2.md)
- [SDKTask](classes/SDKTask.md)
- [SDKUser](classes/SDKUser.md)
- [SDKContributor](classes/SDKContributor.md)
- [SDKAnnotationSnapshot](classes/SDKAnnotationSnapshot.md)
- [SnapshotService](classes/SnapshotService.md)

### Type Aliases

- [CreatePayload](modules.md#createpayload)
- [CreateBulkPayload](modules.md#createbulkpayload)
- [ReadPayload](modules.md#readpayload)
- [UpdatePayload](modules.md#updatepayload)
- [UpdateBulkPayload](modules.md#updatebulkpayload)
- [DeletePayload](modules.md#deletepayload)
- [DeleteBulkPayload](modules.md#deletebulkpayload)
- [QueryPayload](modules.md#querypayload)
- [StreamPayload](modules.md#streampayload)
- [FetchPayload](modules.md#fetchpayload)
- [ClonePayload](modules.md#clonepayload)
- [LogsPayload](modules.md#logspayload)
- [SetStatusPayload](modules.md#setstatuspayload)
- [DoesLabelHaveAttributesPayload](modules.md#doeslabelhaveattributespayload)
- [CalcLabelsHaveAttributesPayload](modules.md#calclabelshaveattributespayload)
- [MissingRequiredAttributePayload](modules.md#missingrequiredattributepayload)
- [ResourceHandler](modules.md#resourcehandler)
- [ResourceInstance](modules.md#resourceinstance)
- [IDate](modules.md#idate)
- [SDKAnnotationLogs](modules.md#sdkannotationlogs)

### Enumerations

- [ThemeType](enums/ThemeType.md)
- [DlEvent](enums/DlEvent.md)
- [DlFrameEvent](enums/DlFrameEvent.md)
- [DlAnnotationFrameEvent](enums/DlAnnotationFrameEvent.md)
- [DlAnnotationEvent](enums/DlAnnotationEvent.md)
- [DlItemEvent](enums/DlItemEvent.md)
- [DlItemFrameEvent](enums/DlItemFrameEvent.md)
- [AgentState](enums/AgentState.md)
- [AgentMessageType](enums/AgentMessageType.md)
- [DlRoute](enums/DlRoute.md)
- [AppMessageScope](enums/AppMessageScope.md)
- [CrudType](enums/CrudType.md)
- [CrudEvent](enums/CrudEvent.md)
- [XFrameMessageType](enums/XFrameMessageType.md)
- [InvokeType](enums/InvokeType.md)
- [CustomNodeScope](enums/CustomNodeScope.md)

### Functions

- [initializeFrameDriver](modules.md#initializeframedriver)

## Type Aliases

### CreatePayload

Ƭ **CreatePayload**<`T`\>: `any`

#### Type parameters

| Name |
| :------ |
| `T` |

___

### CreateBulkPayload

Ƭ **CreateBulkPayload**<`T`\>: `any`[]

#### Type parameters

| Name |
| :------ |
| `T` |

___

### ReadPayload

Ƭ **ReadPayload**<`T`\>: `string` \| `Partial`<`T`\>

#### Type parameters

| Name |
| :------ |
| `T` |

___

### UpdatePayload

Ƭ **UpdatePayload**<`T`\>: `Partial`<`T`\>

#### Type parameters

| Name |
| :------ |
| `T` |

___

### UpdateBulkPayload

Ƭ **UpdateBulkPayload**<`T`\>: `Partial`<`T`\>[]

#### Type parameters

| Name |
| :------ |
| `T` |

___

### DeletePayload

Ƭ **DeletePayload**<`T`\>: `string` \| `Partial`<`T`\>

#### Type parameters

| Name |
| :------ |
| `T` |

___

### DeleteBulkPayload

Ƭ **DeleteBulkPayload**<`T`\>: `string`[]

#### Type parameters

| Name |
| :------ |
| `T` |

___

### QueryPayload

Ƭ **QueryPayload**<`T`\>: `any`

#### Type parameters

| Name |
| :------ |
| `T` |

___

### StreamPayload

Ƭ **StreamPayload**<`T`\>: `any`

#### Type parameters

| Name |
| :------ |
| `T` |

___

### FetchPayload

Ƭ **FetchPayload**<`T`\>: `string`

#### Type parameters

| Name |
| :------ |
| `T` |

___

### ClonePayload

Ƭ **ClonePayload**<`T`\>: `string`

#### Type parameters

| Name |
| :------ |
| `T` |

___

### LogsPayload

Ƭ **LogsPayload**<`T`\>: `Partial`<`T`\>

#### Type parameters

| Name |
| :------ |
| `T` |

___

### SetStatusPayload

Ƭ **SetStatusPayload**<`T`\>: `any`

#### Type parameters

| Name |
| :------ |
| `T` |

___

### DoesLabelHaveAttributesPayload

Ƭ **DoesLabelHaveAttributesPayload**<`T`\>: `any`

#### Type parameters

| Name |
| :------ |
| `T` |

___

### CalcLabelsHaveAttributesPayload

Ƭ **CalcLabelsHaveAttributesPayload**<`T`\>: `any`

#### Type parameters

| Name |
| :------ |
| `T` |

___

### MissingRequiredAttributePayload

Ƭ **MissingRequiredAttributePayload**<`T`\>: `string`

#### Type parameters

| Name |
| :------ |
| `T` |

___

### ResourceHandler

Ƭ **ResourceHandler**<`T`\>: `Object`

#### Type parameters

| Name | Type |
| :------ | :------ |
| `T` | `any` |

#### Type declaration

| Name | Type |
| :------ | :------ |
| `read?` | `ResponseResolver`<[`ReadPayload`](modules.md#readpayload)<`T`\>, `T` \| `undefined`\> |
| `getByName?` | `ResponseResolver`<`string`, `T` \| `undefined`\> |
| `countByQuery?` | `ResponseResolver`<[`QueryPayload`](modules.md#querypayload)<`T`\>, `number`\> |
| `create?` | `ResponseResolver`<[`CreatePayload`](modules.md#createpayload)<`T`\>, `T` \| `T`[]\> |
| `createBulk?` | `ResponseResolver`<[`CreateBulkPayload`](modules.md#createbulkpayload)<`T`\>, `T`[]\> |
| `update?` | `ResponseResolver`<[`UpdatePayload`](modules.md#updatepayload)<`T`\>, `T`\> |
| `updateBulk?` | `ResponseResolver`<[`UpdateBulkPayload`](modules.md#updatebulkpayload)<`T`\>, `T`[]\> |
| `delete?` | `ResponseResolver`<[`DeletePayload`](modules.md#deletepayload)<`T`\>, `string` \| `undefined`\> |
| `deleteBulk?` | `ResponseResolver`<[`DeleteBulkPayload`](modules.md#deletebulkpayload)<`T`\>, `void`\> |
| `query?` | `ResponseResolver`<[`QueryPayload`](modules.md#querypayload)<`T`\>, [`IPagedResponse`](interfaces/IPagedResponse.md)<`T`\>\> |
| `stream?` | `ResponseResolver`<[`StreamPayload`](modules.md#streampayload)<`T`\>, `string`\> |
| `fetch?` | `ResponseResolver`<[`FetchPayload`](modules.md#fetchpayload)<`T`\>, `any`\> |
| `clone?` | `ResponseResolver`<[`ClonePayload`](modules.md#clonepayload)<`T`\>, `T`\> |
| `logs?` | `ResponseResolver`<[`LogsPayload`](modules.md#logspayload)<`T`\>, `any`\> |
| `setStatus?` | `ResponseResolver`<[`CrudMessage`](classes/CrudMessage.md)<[`SetStatusPayload`](modules.md#setstatuspayload)<`T`\>\>, `void`\> |
| `doesLabelHaveAttributes?` | `ResponseResolver`<[`DoesLabelHaveAttributesPayload`](modules.md#doeslabelhaveattributespayload)<`T`\>, `boolean`\> |
| `calcLabelsHaveAttributes?` | `ResponseResolver`<[`CalcLabelsHaveAttributesPayload`](modules.md#calclabelshaveattributespayload)<`T`\>, `void`\> |
| `missingRequiredAttribute?` | `ResponseResolver`<[`MissingRequiredAttributePayload`](modules.md#missingrequiredattributepayload)<`T`\>, `boolean`\> |
| `getLabelAttributes?` | `ResponseResolver`<`string`, `any`\> |
| `updateAssignees?` | `ResponseResolver`<[`SDKUpdateTaskAssigneesPayload`](interfaces/SDKUpdateTaskAssigneesPayload.md), `T`\> |

___

### ResourceInstance

Ƭ **ResourceInstance**: [`SDKProject`](classes/SDKProject.md) \| [`SDKDataset`](classes/SDKDataset.md) \| [`SDKItem`](classes/SDKItem.md) \| [`SDKAnnotation`](classes/SDKAnnotation.md) \| [`APIRecipeV2`](classes/APIRecipeV2.md) \| [`APIOntologyV2`](classes/APIOntologyV2.md)

___

### IDate

Ƭ **IDate**: `Date` \| `number` \| `string`

___

### SDKAnnotationLogs

Ƭ **SDKAnnotationLogs**: `Object`

Represents a collection of annotation events.

#### Index signature

▪ [annotationId: `string`]: [`SDKAnnotationEvent`](classes/SDKAnnotationEvent.md)[]

## Functions

### initializeFrameDriver

▸ **initializeFrameDriver**(): `Promise`<`void`\>

#### Returns

`Promise`<`void`\>
