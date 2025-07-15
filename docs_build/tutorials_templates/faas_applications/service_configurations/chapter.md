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

### Basic Autoscaler

Set up automatic scaling based on queue length:

```python
autoscaler = dl.KubernetesRabbitmqAutoscaler(
    min_replicas=0,
    max_replicas=5,
    queue_length=10,
    cooldown_period=300,
    polling_interval=10
)

service = project.services.get('auto-scaling-service')
service.runtime = dl.KubernetesRuntime(
        pod_type=dl.InstanceCatalog.REGULAR_M,
        concurrency=2,
        autoscaler=autoscaler
    )
service.update()
```

### Advanced Autoscaling Strategies

Fine-tune your autoscaling behavior:

```python
# Aggressive scaling for burst workloads
burst_autoscaler = dl.KubernetesRabbitmqAutoscaler(
    min_replicas=1,
    max_replicas=20,
    queue_length=5,  # Scale up quickly
    cooldown_period=60,  # Scale down quickly
    polling_interval=5
)

# Cost-optimized scaling
efficient_autoscaler = dl.KubernetesRabbitmqAutoscaler(
    min_replicas=0,
    max_replicas=3,
    queue_length=15,  # More tolerance for queuing
    cooldown_period=600,  # Longer cooldown to prevent thrashing
    polling_interval=30
)
```

### Setting Up Autoscaling in Your DPK Definition

Autoscaling lets your Dataloop services automatically adjust resources based on real-time demand—saving costs and improving responsiveness. You can configure autoscaling directly in your DPK (Dataloop Package Kit) manifest under the `runtime.autoscaler` section of your service definition.

Supported Autoscaler Types
- `rps`: Scales based on HTTP request rate (requests per second). Ideal for UI panels and interactive services.
- `cpu`: Scales based on CPU usage.
- `ram`: Scales based on memory usage.

The RPS-based autoscaler is especially relevant for apps using served UI panels (e.g., Studio tools), where responsiveness is critical during user interaction, and efficient resource management is desired during idle times.

#### Example: RPS-Based Autoscaler

Here’s how to define an autoscaler that scales your service based on incoming HTTP requests:

```json
"runtime": {
  "podType": "regular-xs",
  "autoscaler": {
    "type": "rps",             // "cpu" or "ram" also supported
    "minReplicas": 0,          // Minimum number of running instances
    "maxReplicas": 1,          // Maximum number of instances when scaling
    "threshold": 10,           // Request threshold to trigger scaling
    "rateSeconds": 30,         // Time window to count requests
    "cooldownPeriod": "3600"   // Time to wait before scaling down (in seconds)
  }
}
```

**What it Actually Means**:

- threshold = 10: The service will scale up when it receives 10 or more requests in a given window.
- rateSeconds = 30: The window of time over which requests are counted is 30 seconds.
- cooldownPeriod = 3600: After the last request, the service will wait 3600 seconds (1 hour) before scaling down.

**Full DPK Example**:

```json
{
    "name": "your-rps",
    "displayName": "your RPS",
    "icon": "icon-dl-sdk-documentation",
    "components": {
        "panels": [
            {
                "name": "floatingPanel",
                "minRole": "annotator",
                "supportedSlots": [
                    {
                        "type": "floatingWindow",
                        "configuration": {
                            "layout": {
                                "width": 455,
                                "height": 340,
                                "resizable": true,
                                "backgroundColor": "dl-color-studio-panel",
                                "position": {
                 "x": 775,
                 "y": 55
             }
                            },
                            "route": [
                                "datasetItem"
                            ]
                        }
                    }
                ],
                "icon": "icon-dl-sdk-documentation",
                "metadata": {},
                "defaultSettings": {},
                "conditions": {
                    "resources": [
                        {
                            "entityType": "item",
                            "filter": {
                            }
                        }
                    ]
                }
            }
        ],
        "toolbars": [],
        "modules": [],
        "services": [
            {
                "name": "your-abc-floating",
                "panelNames": [
                    "floatingPanel"
                ],
                "initParams": {},
                "packageRevision": "latest",
                "runtime": {
                    "podType": "regular-xs",
                    "autoscaler": {
                        "type": "rps",
                        "minReplicas": 0,
                        "maxReplicas": 1,
                        "threshold": 10,
                        "rateSeconds": 30,
                        "cooldownPeriod": "3600"
                    }
                },
                "maxAttempts": 3
            }
        ],
        "triggers": [],
        "pipelines": [],
        "models": [],
        "snapshots": []
    }
}

```

#### Best Practices & Notes

- Use higher cooldown periods (e.g., 3600s or 1hr) for panel-based services to avoid excessive start/stop cycles, which can impact user experience.
- Ensure your panel name is correctly linked in the panelNames array of the service.
- This autoscaling setup optimizes cost and compute by dynamically starting/stopping resources based on actual user demand.

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
