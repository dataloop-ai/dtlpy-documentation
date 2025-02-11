# Interface: SDKExecutionPayload

The payload for creating an execution

**`Interface`**

SDKExecutionPayload

## Table of contents

### Properties

- [serviceName](SDKExecutionPayload.md#servicename)
- [input](SDKExecutionPayload.md#input)
- [functionName](SDKExecutionPayload.md#functionname)
- [sync](SDKExecutionPayload.md#sync)
- [projectId](SDKExecutionPayload.md#projectid)
- [notification](SDKExecutionPayload.md#notification)
- [title](SDKExecutionPayload.md#title)
- [caption](SDKExecutionPayload.md#caption)
- [successMessage](SDKExecutionPayload.md#successmessage)
- [onSuccessEvent](SDKExecutionPayload.md#onsuccessevent)
- [onFailureEvent](SDKExecutionPayload.md#onfailureevent)

## Properties

### serviceName

• **serviceName**: `string`

The name of the service

___

### input

• **input**: `Dictionary`

The function's inputs as a dictionary

___

### functionName

• **functionName**: `string`

The name of the function

___

### sync

• `Optional` **sync**: `boolean`

Enabled by default, this feature ensures that the platform subscribes to changes and monitors the execution's status, consequently triggering events for execution status updates.
To track these changes from an application, you can subscribe to the `DlEvent.EXECUTION_STATUS` event.

___

### projectId

• `Optional` **projectId**: `string`

The project id

___

### notification

• `Optional` **notification**: `boolean`

Add a notification to the execution

___

### title

• `Optional` **title**: `string`

The notification title

___

### caption

• `Optional` **caption**: `string`

The notification caption

___

### successMessage

• `Optional` **successMessage**: `string`

A success toast message string

___

### onSuccessEvent

• `Optional` **onSuccessEvent**: [`EventPayload`](EventPayload.md)

An event to be triggered on execution success

___

### onFailureEvent

• `Optional` **onFailureEvent**: [`EventPayload`](EventPayload.md)

An event to be triggered on execution failure
