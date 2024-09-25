# Enumeration: DlEvent

[appLib/SDKDrivers/xFrameDriver/events](../modules/appLib_SDKDrivers_xFrameDriver_events.md).DlEvent

Events that are emitted from the host (platform) to the frame (SDK)

## Table of contents

### Enumeration Members

- [ACTIVE\_QUERY](appLib_SDKDrivers_xFrameDriver_events.DlEvent.md#active_query)
- [EXECUTION\_STATUS](appLib_SDKDrivers_xFrameDriver_events.DlEvent.md#execution_status)
- [INVOKE\_PAYLOAD](appLib_SDKDrivers_xFrameDriver_events.DlEvent.md#invoke_payload)
- [NAVIGATION](appLib_SDKDrivers_xFrameDriver_events.DlEvent.md#navigation)
- [NODE\_CONFIG](appLib_SDKDrivers_xFrameDriver_events.DlEvent.md#node_config)
- [READY](appLib_SDKDrivers_xFrameDriver_events.DlEvent.md#ready)
- [THEME](appLib_SDKDrivers_xFrameDriver_events.DlEvent.md#theme)
- [TOOL\_CONTROLS](appLib_SDKDrivers_xFrameDriver_events.DlEvent.md#tool_controls)
- [VALIDATION\_RESULT](appLib_SDKDrivers_xFrameDriver_events.DlEvent.md#validation_result)
- [VIEWER\_SETTINGS](appLib_SDKDrivers_xFrameDriver_events.DlEvent.md#viewer_settings)

## Enumeration Members

### ACTIVE\_QUERY

• **ACTIVE\_QUERY** = ``"activeQuery"``

Triggered when the active query has changed

___

### EXECUTION\_STATUS

• **EXECUTION\_STATUS** = ``"executionStatus"``

Execution status - fired on creation, success & failure events with execution details

___

### INVOKE\_PAYLOAD

• **INVOKE\_PAYLOAD** = ``"invokePayload"``

The payload sent during a toolbar invoke to a panel

___

### NAVIGATION

• **NAVIGATION** = ``"navigation"``

Triggered on navigation events

___

### NODE\_CONFIG

• **NODE\_CONFIG** = ``"nodeConfig"``

The pipeline node configuration

___

### READY

• **READY** = ``"ready"``

The frame is ready to receive messages

___

### THEME

• **THEME** = ``"theme"``

The theme of the platform has changed

___

### TOOL\_CONTROLS

• **TOOL\_CONTROLS** = ``"toolControls"``

Triggered when changes are made to the tool controls in the left bar, providing an updated settings object as the payload.

___

### VALIDATION\_RESULT

• **VALIDATION\_RESULT** = ``"validationResult"``

The result of the validation script

___

### VIEWER\_SETTINGS

• **VIEWER\_SETTINGS** = ``"viewerSettings"``

Triggered when changes are made to the viewer settings within the top bar controls, providing an updated settings object as the payload.
