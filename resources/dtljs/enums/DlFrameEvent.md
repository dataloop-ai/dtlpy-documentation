# Enumeration: DlFrameEvent

[appLib/SDKDrivers/xFrameDriver/events](../modules/appLib_SDKDrivers_xFrameDriver_events.md).DlFrameEvent

Events that are emitted from the frame (SDK) to the host (platform)

## Table of contents

### Enumeration Members

- [CLIPBOARD\_WRITE](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#clipboard_write)
- [CLOSE\_DIALOG](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#close_dialog)
- [INVOKE\_PANEL](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#invoke_panel)
- [REDO](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#redo)
- [REFRESH\_DATA](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#refresh_data)
- [SET\_HEIGHT](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#set_height)
- [TOAST\_MESSAGE](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#toast_message)
- [TOGGLE\_ACTION\_LOCK](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#toggle_action_lock)
- [UNDO](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#undo)
- [UPDATE\_NODE\_CONFIG](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#update_node_config)
- [UPDATE\_TIME\_SERVICE\_SETTINGS](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#update_time_service_settings)
- [UPDATE\_VIEWER\_SETTINGS](appLib_SDKDrivers_xFrameDriver_events.DlFrameEvent.md#update_viewer_settings)

## Enumeration Members

### CLIPBOARD\_WRITE

• **CLIPBOARD\_WRITE** = ``"app:clipboardWrite"``

Copy to clipboard

___

### CLOSE\_DIALOG

• **CLOSE\_DIALOG** = ``"app:closeDialog"``

Closes dialog slot

___

### INVOKE\_PANEL

• **INVOKE\_PANEL** = ``"invokePanel"``

Invokes another panel from the app

___

### REDO

• **REDO** = ``"redo"``

Redo action

___

### REFRESH\_DATA

• **REFRESH\_DATA** = ``"app:refreshData"``

Refresh page data

___

### SET\_HEIGHT

• **SET\_HEIGHT** = ``"app:setHeight"``

Sets iframe height

___

### TOAST\_MESSAGE

• **TOAST\_MESSAGE** = ``"app:toastMessage"``

Toast message (info, warning, error, success)

___

### TOGGLE\_ACTION\_LOCK

• **TOGGLE\_ACTION\_LOCK** = ``"toggleActionLock"``

Toggles the action lock

___

### UNDO

• **UNDO** = ``"undo"``

Undo action

___

### UPDATE\_NODE\_CONFIG

• **UPDATE\_NODE\_CONFIG** = ``"updateNodeConfig"``

Updates the node configuration

___

### UPDATE\_TIME\_SERVICE\_SETTINGS

• **UPDATE\_TIME\_SERVICE\_SETTINGS** = ``"app:updateTimeServiceSettings"``

Sets time service settings (payload: SDKTimeServiceSettings)

___

### UPDATE\_VIEWER\_SETTINGS

• **UPDATE\_VIEWER\_SETTINGS** = ``"app:updateViewerSettings"``

Sets the settings values of the top bar controls based on the values provided by the app.
