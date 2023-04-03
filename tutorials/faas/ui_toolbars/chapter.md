# UI Toolbars  
## Define a UI slot in the platform  
UI slots can be created for any function, making it possible to invoke the function through a button click.  
Binding functions to UI slots will enable you to manually trigger them on selected items, annotations, or tasks.  
  
Dataloop currently supports the following UI slots:  
1. Item as a resource:  
    1. Dataset Browser  
    2. Annotation Studio  
2. Annotation as a resource:  
    1. Annotation Studio  
3. Task as a resource:  
    1. Tasks browser  
  
Let’s define a UI button for the “RGB to Gray” function.  
For that, we should create a slot entity in the SDK, that can be later activated from the UI to quickly invoke functions.  
  
In this case, the input for the RGB function is an item, so the slot resource should be item as well (i.e. SlotDisplayScopeResource.ITEM).  
As a result, the function will be accessible in the annotations studio under "Applications" dropdown:  
  

```python
import dtlpy as dl
slots = [
    dl.PackageSlot(module_name='image-processing',
                   function_name='rgb2gray',
                   display_name='RGB2GRAY',
                   post_action=dl.SlotPostAction(type=dl.SlotPostActionType.NO_ACTION),
                   display_scopes=[
                       dl.SlotDisplayScope(
                           resource=dl.SlotDisplayScopeResource.ITEM,
                           panel=dl.UiBindingPanel.ALL,
                           filters={})])
]
```
Once the function finishes executing, you can decide what the function outputs. Currently, 3 Post-Action outputs are available for UI slots:  
1. SlotPostActionType.DOWNLOAD - Download the output, available only for item output.  
2. SlotPostActionType.DRAW_ANNOTATION - Available only for annotation output. Draw the annotation on the item.  
3. SlotPostActionType.NO_ACTION - Take no further actions  
  
Additionally, you can use filters to specify which items in are eligible to be used in app (e.g. filtered by item type, item format, etc.).  
  
## Update the Package and Service with the Slot  
  
Now you can update your package and service with the new slot you added:  
  

```python
# Update package with the slot
package.slots = slots
package = package.update()
# Update service with the new package version
service.package_revision = package.version
service.update()
```
## Activate the UI slot  
  
To make the UI slot visible to users in the platform, you need to activate the slots:  
  

```python
package.services.activate_slots(service=service,
                                project_id=project.id,
                                slots=slots)
```
Notice that clicking on the UI slot button will trigger the service only if it is active.  
  
Pause the service:  
We recommend pausing the service you created for this tutorial so it will not be triggered:  
  

```python
service.pause()
```
Congratulations! You have successfully created, deployed, and tested Dataloop functions!  
