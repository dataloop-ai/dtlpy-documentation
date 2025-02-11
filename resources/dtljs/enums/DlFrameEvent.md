# Enumeration: DlFrameEvent

Events that are emitted from the frame (SDK) to the host (platform)

## Table of contents

### Enumeration Members

- [UPDATE\_NODE\_CONFIG](DlFrameEvent.md#update_node_config)
- [TOGGLE\_ACTION\_LOCK](DlFrameEvent.md#toggle_action_lock)
- [CLOSE\_DIALOG](DlFrameEvent.md#close_dialog)
- [REDO](DlFrameEvent.md#redo)
- [UNDO](DlFrameEvent.md#undo)
- [TOAST\_MESSAGE](DlFrameEvent.md#toast_message)
- [INVOKE\_PANEL](DlFrameEvent.md#invoke_panel)
- [SET\_HEIGHT](DlFrameEvent.md#set_height)
- [UPDATE\_TIME\_SERVICE\_SETTINGS](DlFrameEvent.md#update_time_service_settings)
- [UPDATE\_VIEWER\_SETTINGS](DlFrameEvent.md#update_viewer_settings)
- [CLIPBOARD\_WRITE](DlFrameEvent.md#clipboard_write)
- [REFRESH\_DATA](DlFrameEvent.md#refresh_data)

## Enumeration Members

### UPDATE\_NODE\_CONFIG

• **UPDATE\_NODE\_CONFIG** = ``"updateNodeConfig"``

Updates the node configuration

___

### TOGGLE\_ACTION\_LOCK

• **TOGGLE\_ACTION\_LOCK** = ``"toggleActionLock"``

Toggles the action lock

___

### CLOSE\_DIALOG

• **CLOSE\_DIALOG** = ``"app:closeDialog"``

Closes dialog slot

___

### REDO

• **REDO** = ``"redo"``

Redo action

___

### UNDO

• **UNDO** = ``"undo"``

Undo action

___

### TOAST\_MESSAGE

• **TOAST\_MESSAGE** = ``"app:toastMessage"``

Toast message (info, warning, error, success)

___

### INVOKE\_PANEL

• **INVOKE\_PANEL** = ``"invokePanel"``

Invokes another panel from the app

___

### SET\_HEIGHT

• **SET\_HEIGHT** = ``"app:setHeight"``

Sets iframe height

___

### UPDATE\_TIME\_SERVICE\_SETTINGS

• **UPDATE\_TIME\_SERVICE\_SETTINGS** = ``"app:updateTimeServiceSettings"``

Sets time service settings (payload: SDKTimeServiceSettings)

___

### UPDATE\_VIEWER\_SETTINGS

• **UPDATE\_VIEWER\_SETTINGS** = ``"app:updateViewerSettings"``

Sets the settings values of the top bar controls based on the values provided by the app.

___

### CLIPBOARD\_WRITE

• **CLIPBOARD\_WRITE** = ``"app:clipboardWrite"``

Copy to clipboard

___

### REFRESH\_DATA

• **REFRESH\_DATA** = ``"app:refreshData"``

Refresh page data
