# ⚙️ Service Configurations - Mastering FaaS Settings

Welcome to the world of FaaS service configurations! Think of service configurations as the control panel for your serverless functions. Let's explore how to fine-tune your services for optimal performance!

## 🎯 Managing Service Configurations

You can configure your services in two ways: through the DPK manifest file or directly on the deployed service.

### DPK Manifest Configuration

Define your service settings in the `dataloop.json` manifest:

```json
{
  "name": "my-package",
  "components": {
    "services": [
      {
        "name": "my-service",
        "runtime": {
          "podType": "regular-s",
          "concurrency": 10,
          "runnerImage": "python:3.9",
          "autoscaler": {
            "minReplicas": 0,
            "maxReplicas": 5,
            "queueLength": 10,
            "cooldownPeriod": 300
          }
        },
        "executionTimeout": 3600,
        "initParams": {
          "model_name": "resnet50"
        }
      }
    ]
  }
}
```

### Direct Service Updates

Modify configurations of deployed services:

```python
# Get an existing service
project = dl.projects.get('project-name')
service = project.services.get('service-name')

# Update runtime configuration
service.runtime.concurrency = 5
service.runtime.pod_type = dl.InstanceCatalog.REGULAR_M
service.update()

# Update autoscaler settings
service.runtime.autoscaler.min_replicas = 1
service.runtime.autoscaler.max_replicas = 10
service.runtime.autoscaler.queue_length = 20
service.update()

# Update execution timeout
service.execution_timeout = 7200  # 2 hours
service.update()

# Update service state
service.pause()  # Pause the service
service.resume()  # Resume the service
```

## 🔧 Advanced Runtime Settings

### Custom Resource Allocation

Need more power? Configure your compute resources:

```python
service = dl.services.get('service-name')
service.runtime = dl.KubernetesRuntime(
        pod_type=dl.InstanceCatalog.HIGHMEM_L,
        concurrency=4,
        runner_image='python:3.9',
        autoscaler=dl.KubernetesRabbitmqAutoscaler(
            min_replicas=1,
            max_replicas=10,
            queue_length=20
        )
    )
service.update()
```

### Instance Types

Choose the right compute power for your needs:

```python
# list all instance types
[e.value for e in dl.InstanceCatalog]
>> ['regular-xs',
 'regular-s',
 'regular-m',
 'regular-l',
 'highmem-xs',
 'highmem-s',
 'highmem-m',
 'highmem-l',
 'gpu-k80-s',
 'gpu-k80-m',
 'gpu-t4',
 'gpu-t4-m']
```

## Autoscaling Configuration

Dataloop supports two autoscaling methods for services. Each method aligns with different service types and workload patterns:


1. **Queue Length-Based Autoscaler** – scales services according to the number of pending executions in the service's queue.
2. **HTTP Request-Based Autoscaler (RPS)** - scales services based on incoming HTTP requests.


### Queue Length-Based Autoscaler

This autoscaler scales a service based on the length of its execution queue.

**Why**:
<br>

Each time an app service submits an execution—such as for a model run, data processing, or pipeline step—it’s added to a queue. The autoscaler tracks how many executions are waiting and adjusts the number of service replicas accordingly.


**When to Use**:
<br>

Use the queue length-based autoscaler when your service processes executions (e.g., models, pipelines, event-driven logic).

*Note*: By default, Dataloop services use this queue length-based autoscaler to scale dynamically based on the number of pending executions.


---

#### Set Up Autoscaler
To configure automatic scaling for your service based on execution queue length:




```python
# Define a queue length-based autoscaler
autoscaler = dl.KubernetesRabbitmqAutoscaler(
    min_replicas=0,            # Fully scale down when idle (cost-saving)
    max_replicas=5,            # Limits the number of concurrent replicas for the service
    queue_length=10,           # Scale up when queue exceeds 10 messages
    polling_interval=10,       # Check queue length every 10 seconds 
    cooldown_period=300        # Wait 5 minutes (300s) before scaling down after traffic drops
)

# Get the target service and assign runtime with autoscaler
service = project.services.get('auto-scaling-service')
service.runtime = dl.KubernetesRuntime(
    pod_type=dl.InstanceCatalog.REGULAR_S,  # Small pod type
    concurrency=2,                          # Each replica handles 2 executions in parallel
    autoscaler=autoscaler 
)

# Apply the configuration
service.update()
```

---

#### Autoscaling Strategies (Queue-Based)

You can fine-tune your autoscaling behavior depending on your operational priorities:

**Performance-Optimized Scaling**
<br>

This configuration is designed to respond quickly to sudden increases in workload by scaling aggressively. Suitable for latency-sensitive or time-critical operations.

*Use this strategy when*:
- You expect short, heavy bursts of tasks.
- Latency reduction is more important than cost.
- You want fast provisioning of compute resources.

<br> 

```python
# Performance-optimized: aggressive scaling for burst workloads
burst_autoscaler = dl.KubernetesRabbitmqAutoscaler(
    min_replicas=1,       # Keep at least 1 replica running at all times
    max_replicas=20,      # Allow the system to scale up to 20 replicas
    queue_length=5,       # Trigger scaling when there are more than 5 items in the queue
    polling_interval=5,   # Check queue status every 5 seconds for fast reaction
    cooldown_period=60    # Scale down quickly after 60 seconds of inactivity
)
```


**Cost-Optimized Scaling**
<br>

This configuration aims to reduce compute costs by tolerating higher queue sizes while delaying scale-down events. Ideal for workloads that can afford slower processing.


*Use this strategy when*:
- Budget and resource efficiency is a top priority.
- You have non-urgent workloads that tolerate queuing delays.
- You're processing tasks in bulk with moderate urgency.

<br>

```python
# Cost-optimized: slower scaling with conservative thresholds
efficient_autoscaler = dl.KubernetesRabbitmqAutoscaler(
    min_replicas=0,         # Scale down to zero when idle to save cost
    max_replicas=3,         # Limit to 3 replicas to cap resource usage
    queue_length=15,        # Only scale up when queue exceeds 15 messages
    polling_interval=30,    # Check queue status every 30 seconds (less overhead)
    cooldown_period=600     # Wait 10 minutes before scaling down (avoids flapping)
)
```

### HTTP Request-Based Autoscaler

The RPS autoscaler tracks the rate of incoming HTTP requests over a defined time window and adjusts scale based on real-time user interaction.

**Why**: 
<br> 

For UI-based services that do not produce executions, such as annotation studio panels, scaling based on queue length is not relevant. 
In these cases, autoscaling is driven by HTTP request rate instead.


**When to Use**:
<br> 

Services that serve UI components or panels, such as Annotation Studio panels.

---

#### Set Up Autoscaler

To configure automatic scaling for your service based on HTTP requests:


```python
# Define an HTTP request-based autoscaler
autoscaler = dl.KubernetesRPSAutoscaler(
    type='rps',                # Activate HTTP request-based autoscaler (mandatory)
    min_replicas=0,            # Fully scale down when idle (cost-saving)
    max_replicas=5,            # Limits the number of concurrent replicas for the service
    threshold=100,             # Scale up if more than 100 HTTP requests occur in the sliding window
    rate_seconds=30,            # Sliding time window in which the request count is evaluated
    polling_interval=10,       # Check request count every 10 seconds
    cooldown_period=3600      # Wait 60 minutes (3600s) before scaling down after traffic drops
)

# Get the target service and assign runtime with autoscaler
service = project.services.get('auto-scaling-service')
service.runtime = dl.KubernetesRuntime(
    pod_type=dl.InstanceCatalog.REGULAR_XS,  # Extra small pod type
    autoscaler=autoscaler
)

# Apply the configuration
service.update()
```


**Step-by-Step Runtime Flow**
<br>

1. **Panel Activation** - A user opens a panel in the UI.

2. **Request Routing** - The panel triggers HTTP requests to the service. These are monitored by the autoscaler (`"type": "rps"`).

3. **Autoscaler Monitors Usage** - Every 10 seconds (`polling_interval`), the autoscaler counts HTTP requests over the last 30 seconds (`rate_seconds`). If requests > 100 (`threshold`), the service scales up (adding additional replicas).

4. **Scaling Behavior** - The service can scale from 0 to 5 replicas (`min_replicas` to `max_replicas`), based on traffic. After traffic drops, it waits 3600 seconds before scaling down (`cooldown_period`).


---

#### Autoscaling Strategies (Requests-Based)

You can fine-tune your autoscaling behavior depending on your operational priorities:

**Performance-Optimized Scaling**
<br>

This configuration prioritizes quick responsiveness, ideal for services that must scale immediately when users interact with the UI.

```python
# Performance-optimized: aggressive scaling for burst workloads
burst_autoscaler = dl.KubernetesRPSAutoscaler(
  type='rps',              # Enables HTTP request-based autoscaling (mandatory)
  min_replicas=1,           # Always keep one replica running for faster first response
  max_replicas=5,           # Allow scaling up to 5 replicas under high traffic
  threshold=50,            # If more than 50 requests are received in the rate window, scale up
  rate_seconds=15,          # Count requests within the last 15 seconds
  polling_interval=10,      # Check request count every 10 seconds (high frequency)
  cooldown_period=3600      # Wait 3600 seconds of inactivity before scaling down to 1
)
```


**Cost-Optimized Scaling**
<br> 

This configuration minimizes resource usage by scaling conservatively. It's ideal when responsiveness is less critical.

```python
# Cost-optimized: conservative scaling for resource efficiency
efficient_autoscaler = dl.KubernetesRPSAutoscaler(
  type='rps',              # Enables HTTP request-based autoscaling (mandatory)
  min_replicas=0,           # Allow full scale-down to zero when idle
  max_replicas=5,           # Allow scaling up to 5 replicas under high traffic
  threshold=100,           # Only scale when at least 100 requests arrive in the time window
  rate_seconds=30,          # Use a longer 30-second window to count requests
  polling_interval=20,      # Check traffic every 20 seconds (less frequent)
  cooldown_period=3600      # Wait 3600 seconds of inactivity before scaling down to 0
)
```


___

# 🔐 Security and Environment

### Working with Secrets

To add integrations and secrets to your organization, check out [this guide](https://developers.dataloop.ai/tutorials/data_management/integrations_and_secrets/chapter#creating-key-value-secrets-).

Integrations can be added to the manifest or to the service directly.

In the manifest:

```json
"components": {
    "modules": [
        // map a module to an integration in the DPK
        {"integrations": ["api_key"]}
    ],
    "integrations": [
        // add an integration to the DPK
        {
            "env": "API_KEY", // the environment variable name inside the FaaS function
            "key": "api_key", // the key name of the integration in the DPK
            "value": "integration-id", // the integration/secret id
            "type": "key_value", // the type of the integration
            "description": "API key for OpenAI platform", // the description of the integration
        }
    ]
}
```

Securely manage sensitive information:

```python
# Deploy service with secrets
service = project.services.get('secure-service')
service.integrations = [{
        "env": "API_KEY",
        "value": "integration-id",
        "type": "key_value",
        "description": "API key for OpenAI platform",
    },
    {
        "env": "DB_PASSWORD",
        "value": "integration-id",
        "type": "key_value",
        "description": "API key for OpenAI platform",
    }
]
service.update()

# Access secrets in your function
def secure_function(item: dl.Item):
    import os
    api_key = os.environ['API_KEY']
    db_password = os.environ['DB_PASSWORD']
    # Your secure code here
```

## 📊 Monitoring and Logging

### Progress Tracking

Monitor function execution progress:

```python
def process_item(item: dl.Item, progress: dl.Progress):
    # Initial status
    progress.update(status='started', progress=0)

    # Update progress during execution
    progress.update(
        status='processing',
        progress=50,
        message='Halfway there!'
    )

    # Final update
    progress.update(
        status='completed',
        progress=100,
        message='Successfully processed item'
    )
```

### Context Management

Access execution context for better monitoring:

```python
def advanced_function(item: dl.Item, context: dl.Context):
    # Get execution details
    execution_id = context.execution_id
    service_id = context.service_id

    # Use context logger
    context.logger.info(f'Processing item: {item.id}')
    context.logger.debug('Detailed debug information')

    # Add custom metrics
    context.add_metric('processing_time', 1.23)
    context.add_metric('confidence_score', 0.95)
```

Context will also provide more information about the execution, such as the trigger id, task id, and more (when relevant).

```python
# Get the trigger id
trigger_id = context.trigger_id

# Get the task id
task_id = context.task_id
```

## Share Custom Applications Between Projects

You can reuse an installed application across multiple projects by sharing its service—no need to reinstall or duplicate it.

### Benefits

- Save time and resources by avoiding repeated setups.
- Ensure consistency with the same version and configuration.
- Simplify updates—apply changes once, and all projects benefit.
- Optimize costs by centralizing the service.

When you install an application (e.g., Annotation Studio, Function App, Model), the system creates a service entry in CloudOps → Services. Sharing this service lets other projects access the same application without redeployment.  

### Requirements

To use an application from another project:

- **Same Organization** – The application’s service must belong to the same organization as your current project.
- **Service Bot Membership** – The application’s service bot (from the original project) must be added as a member of your current project.
- **User Access** – You must be a member of the original project where the application is hosted.

Read [Dataloop documentation](https://docs.dataloop.ai/docs/services#share-custom-applications-across-projects) for sharing your custom application.

## 💡 Pro Tips & Best Practices

### Resource Optimization

- Start with smaller instance types and scale up as needed
- Use autoscaling to handle variable workloads
- Monitor resource usage to optimize configurations

### Performance Tuning

- Adjust concurrency based on function resource usage
- Set appropriate timeouts for your workload
- Use efficient instance types for your specific needs

### Security Best Practices

- Always use secrets for sensitive information
- Implement proper error handling
- Regular audit of service configurations

### Monitoring Guidelines

- Implement comprehensive logging
- Use progress updates for long-running functions
- Monitor autoscaling behavior

Need help? Check out our other tutorials or reach out to our support team. Happy configuring! ⚡️
