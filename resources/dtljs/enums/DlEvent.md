# Enumeration: DlEvent

Events that are emitted from the host (platform) to the frame (SDK)

## Table of contents

### Enumeration Members

- [READY](DlEvent.md#ready)
- [THEME](DlEvent.md#theme)
- [VALIDATION\_RESULT](DlEvent.md#validation_result)
- [NODE\_CONFIG](DlEvent.md#node_config)
- [INVOKE\_PAYLOAD](DlEvent.md#invoke_payload)
- [EXECUTION\_STATUS](DlEvent.md#execution_status)
- [VIEWER\_SETTINGS](DlEvent.md#viewer_settings)
- [TOOL\_CONTROLS](DlEvent.md#tool_controls)
- [ACTIVE\_QUERY](DlEvent.md#active_query)
- [NAVIGATION](DlEvent.md#navigation)

## Enumeration Members

### READY

• **READY** = ``"ready"``

The frame is ready to receive messages

___

### THEME

• **THEME** = ``"theme"``

The theme of the platform has changed

___

### VALIDATION\_RESULT

• **VALIDATION\_RESULT** = ``"validationResult"``

The result of the validation script

___

### NODE\_CONFIG

• **NODE\_CONFIG** = ``"nodeConfig"``

The pipeline node configuration

___

### INVOKE\_PAYLOAD

• **INVOKE\_PAYLOAD** = ``"invokePayload"``

The payload sent during a toolbar invoke to a panel

___

### EXECUTION\_STATUS

• **EXECUTION\_STATUS** = ``"executionStatus"``

Execution status - fired on creation, success & failure events with execution details

___

### VIEWER\_SETTINGS

• **VIEWER\_SETTINGS** = ``"viewerSettings"``

Triggered when changes are made to the viewer settings within the top bar controls, providing an updated settings object as the payload.

___

### TOOL\_CONTROLS

• **TOOL\_CONTROLS** = ``"toolControls"``

Triggered when changes are made to the tool controls in the left bar, providing an updated settings object as the payload.

___

### ACTIVE\_QUERY

• **ACTIVE\_QUERY** = ``"activeQuery"``

Triggered when the active query has changed

___

### NAVIGATION

• **NAVIGATION** = ``"navigation"``

Triggered on navigation events
