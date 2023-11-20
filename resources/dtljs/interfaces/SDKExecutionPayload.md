# Interface: SDKExecutionPayload

[interfaces](./index.md).SDKExecutionPayload

The payload for creating an execution.

**`Interface`**

SDKExecutionPayload

## Table of contents

### Properties

- [sync](SDKExecutionPayload.md#sync)
- [caption](SDKExecutionPayload.md#caption)
- [functionName](SDKExecutionPayload.md#functionname)
- [input](SDKExecutionPayload.md#input)
- [notification](SDKExecutionPayload.md#notification)
- [projectId](SDKExecutionPayload.md#projectid)
- [serviceName](SDKExecutionPayload.md#servicename)
- [successMessage](SDKExecutionPayload.md#successmessage)
- [title](SDKExecutionPayload.md#title)

## Properties

### sync

• `Optional` **sync**: `boolean`

Enabled by default, this feature ensures that the platform subscribes to changes and monitors the execution's status, consequently triggering events for execution status updates.

To track these changes from an application, you can subscribe to the `DlEvent.EXECUTION_STATUS` event.

```typescript
await dl.on(DlEvent.EXECUTION_STATUS, (payload: { execution: SDKExecution, status: 'created' | 'success' | 'failed' }) => {
    console.log(`Execution ${payload.execution.id} status: ${payload.status}`)
    console.log(`Execution output`, payload.execution.output)
})
```

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
