# Interface: SDKExecutionPayload

[sdkApi/interfaces/entities/iExecution](../modules/sdkApi_interfaces_entities_iExecution.md).SDKExecutionPayload

The payload for creating an execution

**`Interface`**

SDKExecutionPayload

## Table of contents

### Properties

- [caption](sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md#caption)
- [functionName](sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md#functionname)
- [input](sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md#input)
- [notification](sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md#notification)
- [onFailureEvent](sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md#onfailureevent)
- [onSuccessEvent](sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md#onsuccessevent)
- [projectId](sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md#projectid)
- [serviceName](sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md#servicename)
- [successMessage](sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md#successmessage)
- [sync](sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md#sync)
- [title](sdkApi_interfaces_entities_iExecution.SDKExecutionPayload.md#title)

## Properties

### caption

• `Optional` **caption**: `string`

The notification caption

___

### functionName

• **functionName**: `string`

The name of the function

___

### input

• **input**: `Dictionary`

The function's inputs as a dictionary

___

### notification

• `Optional` **notification**: `boolean`

Add a notification to the execution

___

### onFailureEvent

• `Optional` **onFailureEvent**: `EventPayload`

An event to be triggered on execution failure

___

### onSuccessEvent

• `Optional` **onSuccessEvent**: `EventPayload`

An event to be triggered on execution success

___

### projectId

• `Optional` **projectId**: `string`

The project id

___

### serviceName

• **serviceName**: `string`

The name of the service

___

### successMessage

• `Optional` **successMessage**: `string`

A success toast message string

___

### sync

• `Optional` **sync**: `boolean`

Enabled by default, this feature ensures that the platform subscribes to changes and monitors the execution's status, consequently triggering events for execution status updates.
To track these changes from an application, you can subscribe to the `DlEvent.EXECUTION_STATUS` event.

___

### title

• `Optional` **title**: `string`

The notification title
