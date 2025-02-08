# Functions as a Service (FaaS): Your Serverless Toolkit 🚀

Learn how to create, deploy, and manage serverless functions in Dataloop - your key to automating workflows and extending platform capabilities.

## Getting Started with FaaS 🌟

### 1. Basic Function Creation

```python
import dtlpy as dl

class HelloWorld(dl.BaseServiceConfig):
    def hello_world(self, item: dl.Item):
        """A simple function that prints item details"""
        print(f'Item name: {item.name}')
        print(f'Item id: {item.id}')
        return item

```

Create the DPK manifest file (`dataloop.json`):

```json
{
  "name": "hello-world",
  "version": "1.0.0",
  "description": "A simple function that prints item details",
  "components": {
    "modules": [
      {
        "name": "hello-world",
        "entrypoint": "hello_world.py",
        "className": "HelloWorld",
        "functions": [
          {
            "name": "hello_world",
            "inputs": [
              {
                "name": "item",
                "type": "item"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

Push the package to the platform:

```python
dpk = project.dpks.publish()
```

### 2. Service Configuration

Add the service configuration to the DPK manifest file (`dataloop.json`):

```json
{
  "name": "hello-world",
  "version": "1.0.0",
  "description": "A simple function that prints item details",
  "components": {
    "modules": [
      {
        "name": "hello-world",
        "entrypoint": "hello_world.py",
        "className": "HelloWorld",
        "functions": [
          {
            "name": "hello_world",
            "inputs": [
              {
                "name": "item",
                "type": "item"
              }
            ]
          }
        ]
      }
    ],
    "services": [
      {
        "name": "hello-world",
        "moduleName": "hello-world",
        "runtime": {
          "podType": "regular-m",
          "concurrency": 10,
          "runnerImage": "python:3.10",
          "autoscaler": {
            "type": "rabbitmq",
            "minReplicas": 0,
            "maxReplicas": 2,
            "queueLength": 100
          }
        }
      }
    ]
  }
}
```

Install the application:

```python
app = project.apps.install(dpk)
```

## Function Types and Triggers 🎯

### 1. Item Functions

```python
def process_single_item(item: dl.Item):
    """Function that processes a single item"""
    # Add metadata
    item.metadata['processed'] = True
    item.metadata['processor'] = 'faas'
    item.update()

    # Add annotation
    builder = item.annotations.builder()
    builder.add(dl.Classification(label='processed'))
    item.annotations.upload(builder)

    return item
```

### 2. Dataset Functions

```python
def dataset_stats(dataset: dl.Dataset):
    """Calculate dataset statistics"""
    stats = {
        'total_items': dataset.items_count,
        'annotations_count': 0,
        'file_types': {}
    }

    # Collect detailed stats
    for item in dataset.items.list().all():
        # Count annotations
        stats['annotations_count'] += len(item.annotations.list())
        # Track file types
        file_type = item.filename.split('.')[-1]
        stats['file_types'][file_type] = stats['file_types'].get(file_type, 0) + 1

    return stats
```

### 3. Trigger Functions

Add trigger to the DPK manifest file (`dataloop.json`):

```json
"components": {
    "triggers": [
        {
        "name": "run-on-item-created",
        "active": true,
        "type": "Event",
        "namespace": "services.hello-world",
        "spec": {
          "filter": {
            "$and": [
              {
                "$or": [
                  {
                    "metadata.system.mimetype": "image/*"
                  },
                  {
                    "metadata.system.mimetype": "text/*"
                  }
                ]
              },
              {
                "hidden": false
              },
              {
                "type": "file"
              }
            ]
          },
          "executionMode": "Always",
          "resource": "Item",
          "actions": [
            "Created"
          ],
          "input": {},
          "operation": {
            "type": "function",
            "functionName": "hello_world"
          }
        }
      }
    ]
}
```

## Function Management 📋

### 1. Execution Management

```python
# Execute function
execution = service.execute(
    function_name='process_item',
    item_id='item_id',
    project_id='project_id'
)
# Wait for execution to complete
execution = execution.wait()

# Get results
if execution.latest_status['status'] == 'success':
    results = execution.output
else:
    error = execution.latest_status['message']
```

### 2. Service Management

```python
# List all services
services = project.services.list()

# Get service logs
logs = service.logs(follow=True)
print(logs)

# Update service
service.update(
    runtime=dl.KubernetesRuntime(
        pod_type=dl.InstanceCatalog.REGULAR_M,  # Upgrade resources
        concurrency=20
    )
)

# Stop service
service.pause()

# Resume service
service.resume()
```

Ready to explore data versioning? Let's move on to the next chapter! 🚀
