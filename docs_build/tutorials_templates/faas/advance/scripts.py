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

    def func5(self):
        class ServiceRunner(dl.BaseServiceRunner):
            def detect(self, item: dl.Item):
                # Do some work
                foo = 0
                self.kill_event()
                # Do some more work
                bar = 1
                self.kill_event()
                # Sleep for a while
                import time
                time.sleep(1)
                # And... done!
                return

    def func6(self):
        execution.terminate()

    def func7(self):
        service.execution_timeout = 60  # 1 minute

    def func8(self):
        service.on_reset = 'failed'
        service.on_reset = 'rerun'
        # The service must be updated after changing these attributes
        service.update()

    def func9(self):
        package: dl.Package
        package.services.deploy(name='with-integrations',
                                secrets=['integrationId'])

    def func10(self):
        import os
        print(os.environ['INTEGRATION_NAME'])
