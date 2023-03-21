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
