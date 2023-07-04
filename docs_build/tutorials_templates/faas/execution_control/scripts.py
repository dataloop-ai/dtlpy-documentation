import dtlpy as dl


class Scripts:

    def func1(self):
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

    def func2(self):
        execution.terminate()

    def func3(self):
        service.execution_timeout = 60  # 1 minute

    def func4(self):
        service.on_reset = 'failed'
        service.on_reset = 'rerun'
        # The service must be updated after changing these attributes
        service.update()

    def func5(self):
        execution = dl.executions.get(execution_id='')
        execution = execution.wait()
        print(f"Execution is done with status: {execution.latest_status['status']!r}, duration: {execution.duration:.2f}[s]")
