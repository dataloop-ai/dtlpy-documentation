# Functions as a Service (FaaS): Your Serverless Toolkit 🚀

Learn how to create, deploy, and manage serverless functions in Dataloop - your key to automating workflows and extending platform capabilities.

## Project Setup ⚙️

### Dataloop login

> ```python
> import dtlpy as dl
> from dotenv import load_dotenv
> import os
>
> # Load environment variables from .env file
> load_dotenv(override=True)
>
> # Access your API key securely
> api_key = os.getenv('DTLPY_API_KEY')
>
> # Initialize Dataloop with the API key
> dl.login_api_key(api_key=api_key)
> ```

### Project and Dataset setup

> ```python
> # Set your project and dataset names
> project_name = "onboarding-project"
> dataset_name = "onboarding-dataset"
>
> try:
>     # Try to get existing project
>     project = dl.projects.get(project_name=project_name)
>     print(f"Project '{project_name}' already exists")
> except Exception:
>     project = dl.projects.create(project_name=project_name)
>     # Create project if it doesn't exist
>     print(f"Created project '{project_name}'")
>
> try:
>     # Try to get existing dataset
>     dataset = project.datasets.get(dataset_name=dataset_name)
>     print(f"Dataset '{dataset_name}' already exists")
>
> except Exception:
>     # Create dataset if it doesn't exist
>     dataset = project.datasets.create(dataset_name=dataset_name)
>     print(f"Created dataset '{dataset_name}'")
> ```

## Getting Started with FaaS 🌟

### Quick deploy from a function

> ```python
> import dtlpy as dl
>
> def hello_world(item: dl.Item) -> dl.Item:
>     print(f'Hello World - Item name: {item.name}')
>     print(f'Hello World -Item id: {item.id}')
>     return item
>
> app_name = 'hello-world-app'
> # Creates and deploys a service from a plain Python function.
> service = dl.Service.from_function(
>     func=hello_world,
>     name=app_name,
>     project=project,
>     client_api=dl.client_api
> )
> ```

> ```python
> app = project.apps.get(app_name=app_name)
> app.print()
>
> # Open your project in dataloop platform and navigate to the marketplace and choose the Applications tab
> # Look for your new installed app, hard refresh < CRTL + SHIFT + R > if you can find it
> project.open_in_web()
> ```

> ```python
> # A new service was deployed
> service.open_in_web()
> ```
>Congratulations, you just created your first service 🎉

>For more service info see: [Services Documentation](https://docs.dataloop.ai/docs/services?highlight=services)


> ```python
> # Let's see the service details
> service.print()
> project.services.list().print()
> ```

> ```
> # The service is deployed but not running automatically. It's a function waiting to be triggered.
> # To execute it manually on a specific item:
> service.print()
> item_id='item_id'
> execution = service.execute(
>     function_name='hello_world',
>     item_id=item_id
> )
> ```

> ```python
> # Look for your service executions
> # Explore the service execution logs and search for the output of your "Hello World" function.
> service.open_in_web()
> ```

## DPK Manifest

A DPK (Dataloop Package)is a self-contained package 

### 1. Basic Function Creation (DPK manifest)

For triggers, multiple functions, or custom runtime, use a DPK manifest. Define your class:

Copy the following code to hello_world.py module

> ```python
> import dtlpy as dl
>
> class HelloWorld(dl.BaseServiceRunner):
>     def hello_world(self, item: dl.Item):
>         """A simple function that prints item details"""
>         print(f'this is my first function Item name: {item.name}')
>         print(f'this is my first function Item id: {item.id}')
>         return item
> ```

Create the DPK manifest file (dataloop.json):

> ```json
> {
>   "name": "hello-world",
>   "version": "1.0.0",
>   "description": "A simple function that prints item details",
>   "components": {
>     "modules": [
>       {
>         "name": "hello-world",
>         "entryPoint": "hello_world.py",
>         "className": "HelloWorld",
>         "functions": [
>           {
>             "name": "hello_world",
>             "input": [
>               {
>                 "name": "item",
>                 "type": "Item"
>               }
>             ]
>           }
>         ]
>       }
>     ]
>   }
> }
> ```

Push the package to the platform:

> ```python
> dpk = project.dpks.publish()
> ```

> ```python
> dpk.print()
> project.dpks.list().print()
> ```

### 2. Service Configuration

Add the service configuration to the DPK manifest file (dataloop.json):

> ```json
> {
>   "name": "hello-world",
>   "version": "1.0.1",
>   "description": "A simple function that prints item details",
>   "components": {
>     "modules": [
>       {
>         "name": "hello-world",
>         "entryPoint": "hello_world.py",
>         "className": "HelloWorld",
>         "functions": [
>           {
>             "name": "hello_world",
>             "input": [
>               {
>                 "name": "item",
>                 "type": "Item"
>               }
>             ]
>           }
>         ]
>       }
>     ],
>     "services": [
>       {
>         "name": "hello-world-srv",
>         "moduleName": "hello-world",
>         "runtime": {
>           "podType": "regular-m",
>           "concurrency": 10,
>           "runnerImage": "python:3.10",
>           "autoscaler": {
>             "type": "rabbitmq",
>             "minReplicas": 0,
>             "maxReplicas": 2,
>             "queueLength": 100
>           }
>         }
>       }
>     ]
>   }
> }
> ```

Install the application:

> ```python
> dpk.print()
> ```

> ```python
> # republish the updated dpk
> dpk = project.dpks.publish()
>
> # The app.install() call:
> # - Creates the app from the DPK
> # - Reads the services section from the manifest
> # - Automatically deploys the service with the specified runtime config
> app = project.apps.install(dpk)
> ```

> ```python
> # List all apps in the project
> app.print()
> project.apps.list().print()
> project.services.list().print()
> ```

## Function Types and Triggers 🎯

### 1. Item Functions

> ```python
> def process_single_item(item: dl.Item):
>     """Function that processes a single item"""
>     # Add metadata
>     item.metadata['processed'] = True
>     item.metadata['processor'] = 'faas'
>     item.update()
>
>     # Add annotation
>     builder = item.annotations.builder()
>     builder.add(dl.Classification(label='processed'))
>     item.annotations.upload(builder)
>
>     return item
> ```

### 2. Dataset Functions

> ```python
> def dataset_stats(dataset: dl.Dataset):
>     """Calculate dataset statistics"""
>     stats = {
>         'total_items': dataset.items_count,
>         'annotations_count': 0,
>         'file_types': {}
>     }
>
>     # Collect detailed stats
>     for item in dataset.items.list().all():
>         # Count annotations
>         stats['annotations_count'] += len(item.annotations.list())
>
>         # Track file types
>         file_type = item.filename.split('.')[-1]
>         stats['file_types'][file_type] = stats['file_types'].get(file_type, 0) + 1
>
>     return stats
> ```

### 3. Trigger Functions

Add trigger to the DPK manifest file under components (dataloop.json) amd bump the dpk version:

> ```json
> "components": {
>   "triggers": [
>     {
>       "name": "run-on-item-created",
>       "active": true,
>       "type": "Event",
>       "namespace": "services.hello-world-srv",
>       "spec": {
>         "filter": {
>           "$and": [
>             {
>               "$or": [
>                 {
>                   "metadata.system.mimetype": "image/*"
>                 },
>                 {
>                   "metadata.system.mimetype": "text/*"
>                 }
>               ]
>             },
>             {
>               "hidden": false
>             },
>             {
>               "type": "file"
>             }
>           ]
>         },
>         "executionMode": "Always",
>         "resource": "Item",
>         "actions": [
>           "Created"
>         ],
>         "input": {},
>         "operation": {
>           "type": "function",
>           "functionName": "hello_world"
>         }
>       }
>     }
>   ]
> }
> ```

## Function Management 📋

### 1. Execution Management

> ```python
> dpk = project.dpks.publish()
> app.dpk_version = dpk.version
> app.update()
> ```

> ```python
> project.services.list().print()
> ```

> ```python
> service = project.services.get(service_name='service_name')
> service.print()
> ```

> ```python
> # show service triggers
> triggers = service.triggers.list()
> triggers.print()
> ```

upload image to dataset and see that is being executed by the service trigger

> ```python
> # Execute function
> execution = service.execute(
>     function_name="hello_world",
>     item_id=item_id,
>     project_id=project.id
> )
>
> # Wait for execution to complete
> execution = execution.wait()
>
> # Get results
> if execution.latest_status['status'] == 'success':
>     results = execution.output
> else:
>     error = execution.latest_status['message']
> ```

> ```python
> # List all services
> services = project.services.list()
>
> # Get service logs
> logs = service.log(follow=False, view=True)
> print(logs)
>
> # Update service
> service.runtime.pod_type = dl.InstanceCatalog.REGULAR_M
> service.runtime.concurrency = 20
> service.update()
>
> # Stop service
> service.pause()
>
> # Resume service
> service.resume()
> ```

