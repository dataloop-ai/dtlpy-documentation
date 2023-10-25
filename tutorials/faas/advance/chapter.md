# Advance Configurations  
## Service Runtime  

```python
package: dl.Package
service = package.deploy(
    service_name='my-service',
    runtime=dl.KubernetesRuntime(
        pod_type=dl.InstanceCatalog.REGULAR_S,
        concurrency=10,
        runner_image='python:3.9',  # optional - any custom docker image,
        autoscaler=dl.KubernetesRabbitmqAutoscaler(
            min_replicas=0,
            max_replicas=1,
            queue_length=10,
            cooldown_period=300,
            polling_interval=10
        )))
```
## Autoscaler  
When we have changing loads of work, we want the number of replicas of the service to scale up when there are many executions coming in, and scale down otherwise.  
To do so, we need to create an autoscaler:  

```python
autoscaler = dl.KubernetesRabbitmqAutoscaler(
    min_replicas=0,
    max_replicas=1,
    queue_length=10,
    # cooldown_period: define how long to wait before scaling down (reducing the number of replicas) in case the queue is below the queue_length.
    cooldown_period=300,
    # polling_interval (in seconds): this parameter defines how often the queue is being sampled to perform any action.
    polling_interval=10
)
```
## Using Secrets in a Function  
You can use organization integration secrets (key-value) as environment variable inside the function's env.  
First you'll need to add the integrations (UI only), then simply add the integrations' ids whe deploying the service:  

```python
package: dl.Package
package.services.deploy(name='with-integrations',
                        secrets=['integrationId'])
```
Inside the service you can access the values using os package:  

```python
import os
print(os.environ['INTEGRATION_NAME'])
```
## Progress and Context  
  
In any function you can add two more inputs: `progress` and `context`.  
  
For example:  
  
```python  
class ServiceRunner(dl.BaseServiceRunner):  
def detect(self, item: dl.Item, progress: dl.Progress, context: dl.Context):  
    progress.update(status='inProgress', progress=0,  
                    message='execution started')  
```  
Context is a class that saves all the relevant information for this run, e.g. `context.execution_id`, `context.service_id` and more.  
  
You can also use the `context.logger` to get a logger instance. Using this logger will help us save the logs in the correct way (log level) and will make it easier to filter them in the logs page.  
  
Use the python auto complete to check all the dl.Context options.  
  
  
Progress can be used to update the progress percent and change the status of each step:  
  
```python  
progress.update(progress=0,  message='execution started')  
progress.update(progress=80,  message='almost done')  
progress.update(progress=99,  message='one more sec...')  
progress.update(progress=100,  message='done')  
```  
  
