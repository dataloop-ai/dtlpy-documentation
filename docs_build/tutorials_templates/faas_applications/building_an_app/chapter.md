# 👋 Your First FaaS Application - Hello World!

Welcome to the world of serverless functions in Dataloop! In this tutorial, you'll learn how to create, package, and run your first function. Think of FaaS as your personal automation toolkit - it lets you extend Dataloop's capabilities with your own custom code.

# 📦 Creating Your First DPK (Dataloop Package)

## Step 1: Write Your Function
Let's start with a simple function that processes items:

```python
import dtlpy as dl

class HelloWorld(dl.BaseServiceConfig):
    def hello_world(self, item: dl.Item):
        """
        A simple function that prints and returns item details
        :param item: dl.Item to process
        :return: processed item
        """
        print(f'Processing item: {item.name}')
        print(f'Item ID: {item.id}')
        
        # Add a simple metadata flag
        item.metadata['processed'] = True
        item.update()
        
        return item
```

Save this code in a file named `hello_world.py`.

## Step 2: Create the DPK Manifest
Create a file named `dataloop.json` with your package configuration:

```json
{
  "name": "hello-world",
  "version": "1.0.0",
  "description": "My first Dataloop function",
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

# 🚀 Deploying Your Function

## Step 1: Initialize Dataloop
First, make sure you're logged in:

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
```

## Step 2: Get Your Project
```python
project = dl.projects.get(project_name='your-project-name')
```

## Step 3: Publish and Install
```python
# Publish your DPK
dpk = project.dpks.publish()

# Install the application
app = project.apps.install(dpk)

# Get the service
service = project.services.get('hello-world')
```

# 🎯 Running Your Function

## Manual Execution
Try your function on a specific item:

```python
# Get an item to process
dataset = project.datasets.get('your-dataset-name')
item = dataset.items.get(filepath='/path/to/item.jpg')

# Execute the function
execution = service.execute(
    function_name='hello_world',
    item_id=item.id,
    project_id=project.id
)

# Wait for completion and get results
execution.wait()
if execution.latest_status['status'] == 'success':
    processed_item = execution.output
    print(f'Successfully processed item: {processed_item.name}')
else:
    print(f'Execution failed: {execution.latest_status["message"]}')
```

## Add a Trigger (Optional)
Want your function to run automatically on new items? Add this to your `dataloop.json`:

```json
{
  "components": {
    "triggers": [
      {
        "name": "process-new-items",
        "active": true,
        "type": "Event",
        "namespace": "services.hello-world",
        "spec": {
          "filter": {
            "resource": "Item",
            "actions": ["Created"],
            "metadata.system.mimetype": "image/*"
          },
          "operation": {
            "type": "function",
            "functionName": "hello_world"
          }
        }
      }
    ]
  }
}
```

# 💡 Pro Tips

## Best Practices
- Keep your functions focused and single-purpose
- Use meaningful names for your DPK and functions
- Always handle errors gracefully
- Test locally before deploying

## Debugging
- Use print statements for basic debugging
- Check service logs for issues:
```python
logs = service.logs(follow=True)
print(logs)
```

## Service Management
```python
# Pause service when not needed
service.pause()

# Resume when ready to process
service.resume()

# Update configuration if needed
service.update(
    runtime=dl.KubernetesRuntime(
        pod_type=dl.InstanceCatalog.REGULAR_M,
        concurrency=20
    )
)
```

# 🔍 What's Next?

Now that you've created your first function, you can:
- Add more complex processing logic
- Implement different types of triggers
- Create functions that work with datasets
- Build multi-function applications

Need help? Check out our other tutorials or reach out to our support team. Happy coding! 🚀✨
