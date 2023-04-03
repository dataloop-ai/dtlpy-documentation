# Interface: SDKExecutionPayload

[interfaces](./index.md).SDKExecutionPayload

The payload for creating an execution.

**`Interface`**

SDKExecutionPayload

## Table of contents

### Properties

- [async](SDKExecutionPayload.md#async)
- [caption](SDKExecutionPayload.md#caption)
- [functionName](SDKExecutionPayload.md#functionname)
- [input](SDKExecutionPayload.md#input)
- [notification](SDKExecutionPayload.md#notification)
- [projectId](SDKExecutionPayload.md#projectid)
- [serviceName](SDKExecutionPayload.md#servicename)
- [successMessage](SDKExecutionPayload.md#successmessage)
- [title](SDKExecutionPayload.md#title)

## Properties

### async

• `Optional` **async**: `boolean`

If true, wait for the execution to finish on the platform

___

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

### title

• `Optional` **title**: `string`

The notification's title
