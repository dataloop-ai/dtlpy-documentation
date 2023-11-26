# Executions Control  
## Execution Termination  
Sometimes when we run long term executions, such as model training, we need the option to terminate the execution. This is facilitated using terminate at Checkpoint.  
To stop an execution set the code checkpoints to check if this execution received a termination and if it did, raise the Termination Exception.  
This allows you to save some work that was already done before terminating.  
For example:  

```python
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
```
Each time there is a "kill_event" the service runner checks to see if this execution received a termination request.  
To kill such execution we use  

```python
execution.terminate()
```
## Execution Timeout  
You can tell an execution to stop after a given number of seconds with the timeout parameter (the default time is 1 hour).  
In case a service reset, such as in timeout or service update, If there are running executions the service will wait for the execution timeout before resetting.  
The number have to be a natural number (int).  

```python
service.execution_timeout = 60  # 1 minute
```
You can decide what to do to executions that have experienced a timeout. There are 2 options of timeout handling:  
1. Mark execution as failed  
2. Retry  

```python
service.on_reset = 'failed'
service.on_reset = 'rerun'
# The service must be updated after changing these attributes
service.update()
```
## Monitoring Execution Completion  
  
With the SDK, you have the ability to monitor the progress of a single execution until it reaches either a `success` or `failed` status.  
Keep in mind that the local instance of dl.Execution does not automatically synchronize with the current status, requiring periodic polling to obtain the updated information.  
You can easily accomplish this by using the following commands:  
  

```python
execution = dl.executions.get(execution_id='')
execution = execution.wait()
print(f"Execution is done with status: {execution.latest_status['status']!r}, duration: {execution.duration:.2f}[s]")
```
The process will be suspended (with background polling) until there is a change in the execution status.  
  
## Rerun  
Using the `execution.rerun()` function you can trigger another run of the same execution (if it failed, or for any other reason).  
Note that this will overwrite the `latest_status` of the execution (but will keep everything on the execution status log)  
  

```python
execution = dl.executions.get(execution_id='')
execution = execution.rerun()
```
