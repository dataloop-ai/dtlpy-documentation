import dtlpy as dl


class Scripts:
    def func1(self):
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

    def func2(self):
        # Update package with the slot
        package.slots = slots
        package = package.update()

        # Update service with the new package version
        service.package_revision = package.version
        service.update()

    def func3(self):
        package.services.activate_slots(service=service,
                                        project_id=project.id,
                                        slots=slots)

    def func4(self):
        service.pause()

