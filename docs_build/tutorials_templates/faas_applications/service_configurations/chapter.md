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

## 📈 Autoscaling Configuration

Dataloop supports two primary autoscaling mechanisms:

1. **Queue Length-Based Autoscaler (RabbitMQ – default)**  
2. **HTTP Request-Based Autoscaler (RPS – for UI services)**  

These mechanisms help ensure that services dynamically scale based on demand, optimizing both performance and cost.



### Queue Length-Based Autoscaler (RabbitMQ)

Scales based on execution queue size (RabbitMQ), ideal for backend task processing.

**Why**

Backend services that run execution jobs (like training models, data processing) generate tasks that are queued. Scaling based on queue size ensures that the system can handle surges in task load without manual intervention.

**When to Use**

- Services that produce executions (e.g., pipelines, triggers)
- Asynchronous and batch processing workloads
- Background operations needing FIFO processing

---

#### Basic Python Example – Queue-Based Autoscaler

```python
# Define a basic RabbitMQ-based autoscaler
autoscaler = dl.KubernetesRabbitmqAutoscaler(
    min_replicas=0,            # Fully scale down when idle
    max_replicas=5,            # Allow up to 5 pods
    queue_length=10,           # Scale up when queue exceeds 10 messages
    cooldown_period=300,       # Wait 5 minutes (300s) before scaling down
    polling_interval=10        # Check queue every 10 seconds
)

# Get the target service and assign runtime with autoscaler
service = project.services.get('auto-scaling-service')
service.runtime = dl.KubernetesRuntime(
    pod_type=dl.InstanceCatalog.REGULAR_M,  # Medium pod type
    concurrency=2,                           # Each pod handles 2 executions in parallel
    autoscaler=autoscaler
)

# Apply the configuration
service.update()
```

---

#### Queue-Based Strategies

Dataloop allows fine-tuning of RabbitMQ autoscalers depending on your operational priorities:

- Use performance-optimized strategies when you expect sudden workload bursts and want fast responsiveness.
- Use cost-optimized strategies when minimizing resource usage is more important than rapid scaling.

**Performance-Optimized Scaling (Burst Handling)**

This configuration is designed to respond quickly to sudden increases in task load by scaling aggressively. Suitable for latency-sensitive or time-critical operations.

**Use this strategy when**:

- You expect short, heavy bursts of tasks.
- Latency reduction is more important than cost.
- You want fast provisioning of compute resources.


```python
# Performance-optimized: aggressive scaling for burst workloads
burst_autoscaler = dl.KubernetesRabbitmqAutoscaler(
    min_replicas=1,       # Keep at least 1 replica running at all times
    max_replicas=20,      # Allow the system to scale up to 20 replicas
    queue_length=5,       # Trigger scaling when there are more than 5 items in the queue
    cooldown_period=60,   # Scale down quickly after 60 seconds of inactivity
    polling_interval=5    # Check queue status every 5 seconds for fast reaction
)

```

**Cost-Optimized Scaling (Slow Reaction, Fewer Resources)**

This configuration aims to reduce infrastructure costs by tolerating higher queue sizes and delaying scale-down events. Ideal for workloads that can afford slower processing.

**Use this strategy when**:

- Budget and resource efficiency is a top priority.
- You have non-urgent workloads that tolerate queuing delays.
- You're processing tasks in bulk with moderate urgency.


```python
# Cost-optimized: slower scaling with conservative thresholds
efficient_autoscaler = dl.KubernetesRabbitmqAutoscaler(
    min_replicas=0,         # Scale down to zero when idle to save cost
    max_replicas=3,         # Limit to 3 replicas to cap resource usage
    queue_length=15,        # Only scale up when queue exceeds 15 messages
    cooldown_period=600,    # Wait 10 minutes before scaling down (avoids flapping)
    polling_interval=30     # Check queue status every 30 seconds (less overhead)
)

```

### HTTP Request-Based Autoscaler (RPS)

The HTTP Request-Based Autoscaler, also known as RPS autoscaler, is a mechanism designed to scale services based on the rate of incoming HTTP requests over a defined time window.

**Why**: Some services (especially UI-based like Studio panels) rely solely on user interaction via HTTP. These services do not enqueue executions, so queue-based scaling is ineffective.

This autoscaler is essential for services that:

- Serve UI components or panels, such as Dataloop Studio tools.
- Are stateless, i.e., they do not produce execution jobs or message queues.
- Need to dynamically respond to user interaction, scaling up during active usage and scaling down when idle.

**When to Use**:
- Frontend/UI services (e.g., annotation tools, panel-based apps)
- Stateless services without execution tasks
- When responsiveness is critical during user interaction

#### Example - RPS Autoscaler

This is a full example of how the RPS autoscaler is embedded in a DPK service definition for a panel-based UI service.

```json
"services": [
  {
    "name": "studio-panel-service",	 // Unique name for the service instance. This is referenced internally by Dataloop.
    "panelNames": ["floatingPanel"],    // Binds this service to UI panels. Requests originating from this panel will be handled by this service.
    "runtime": {
      "podType": "regular-xs",          // Defines the pod’s resource profile. regular-xs is typically used for lightweight, UI-focused services
      "autoscaler": {
        "type": "rps",                  // Mandatory field to activate HTTP request-based autoscaling
        "minReplicas": 0,              // Service can scale down to zero when not in use (cost-saving)
        "maxReplicas": 5,              // Limits the number of concurrent pods for the service (resource control).
        "threshold": 100,              // If more than 100 HTTP requests occur in the sliding window, scaling is triggered.
        "rateSeconds": 30,             // Sliding time window in which request count is evaluated.
        "pollingInterval": 10,         // How often (in seconds) to evaluate request counts and trigger scaling decisions
        "cooldownPeriod": "3600"       // Wait time (in seconds) after traffic drops before scaling down. Prevents premature de-scaling.
      }
    }
  }
]
```

**Step-by-Step Runtime Flow**

1. **Panel Activation**  
   A user opens a panel defined in the UI.  
   - Panel name: `"floatingPanel"`  
   - It is listed under `panelNames`, linking it to the service.  

2. **Request Routing**  
   - As the panel loads or interacts with backend APIs, it triggers **HTTP requests** to this specific service..  
   - These requests are tracked by the autoscaler, as the service is using `"type": "rps"`.  

3. **Autoscaler Monitors Usage**  
   - Every **10 seconds** (`pollingInterval`), the autoscaler checks HTTP request count over the last **30 seconds** (`rateSeconds`).  
   - If **requests > 100** (`threshold`), the system scales up by adding additional pods (replicas).

4. **Scaling Behavior**  
   - **`minReplicas: 0`** enables full scale-down when idle, so if no one is using the panel, it can fully scale down to save resources.
   - **`maxReplicas: 5`** limits the number of replicas, meaning even under high traffic, the service won’t consume more than 5 pods. 
   - After usage drops, autoscaler waits **3600 seconds (1 hour)** before scaling down (`cooldownPeriod`).

5. **System State**  
   - Dataloop schedules pod lifecycles automatically.  
   - Users get responsive services when needed and low-cost operation when idle.

#### RPS-Based Strategies

**Performance-Optimized (Responsive) – RPS Configuration**

This configuration prioritizes quick responsiveness, ideal for services that must scale immediately when users interact with the UI.

```json
"autoscaler": {
  "type": "rps",               // Mandatory: enables HTTP request-based autoscaling
  "minReplicas": 1,            // Always keep one replica running for faster first response
  "maxReplicas": 10,           // Allow scaling up to 10 replicas under high traffic
  "threshold": 50,             // If more than 50 requests are received in the rate window, scale up
  "rateSeconds": 15,           // Count requests within the last 15 seconds
  "pollingInterval": 5,        // Check request count every 5 seconds (high frequency)
  "cooldownPeriod": "60"       // Wait 60 seconds of no traffic before scaling down
}

```

**Cost-Optimized (Efficient) – RPS Configuration**

This configuration minimizes resource usage by scaling conservatively. It's ideal when responsiveness is less critical.

```json
"autoscaler": {
  "type": "rps",               // Required to activate RPS-based autoscaling
  "minReplicas": 0,            // Allow full scale-down to zero when idle
  "maxReplicas": 3,            // Constrain max resource usage to 3 pods
  "threshold": 100,            // Only scale when at least 100 requests arrive in the time window
  "rateSeconds": 30,           // Use a longer 30-second window to count requests
  "pollingInterval": 20,       // Check traffic every 20 seconds (less frequent)
  "cooldownPeriod": "3600"     // Wait 1 hour of inactivity before scaling down to zero
}

```

#### Best Practices for RPS Autoscaler

- Use `minReplicas: 0` and `cooldownPeriod` ≥ `3600s` for efficient panel lifecycle.
- Tie UI panels via `panelNames` correctly to ensure scaling is service-aware.
- Match `threshold` and `rateSeconds` based on expected user behavior.

### Summary: When to Use Each Autoscaler

| Feature                    | Queue-Based (RabbitMQ)         | HTTP-Based (RPS)             |
|---------------------------|----------------------------------|-------------------------------|
| Type                      | Default                         | Explicit `"rps"`              |
| Use Case                  | Background executions            | UI traffic (e.g., Studio)     |
| Trigger                   | Queue length                    | HTTP request count            |
| Configuration Simplicity  | Simple                          | More detailed setup           |
| Scale to Zero             | Supported via `minReplicas: 0`  | Supported via `minReplicas: 0`|
| Sample Strategy           | Concurrency + polling            | Request threshold + cooldown  |

___

## 🔐 Security and Environment

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
