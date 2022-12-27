# Adding anntoation to item

In this simple function, we will add a classification annotation to an incoming item

* Note: be sure to change the project name to your own working project

## Create the package
Notice that in this directory, we have our `main.py` file which contained the code for this package.  
The package code is the content of this directory.

First we'll need to import the SDK

```python
import dtlpy as dl
```

Let's define the project and package name:

```python
package_name = "add-classification"
project_name = "my-project"
project = dl.projects.get(project_name=project_name)
```

Now we need to define the modules and function that we will use in this package:

```python
modules = [dl.PackageModule(
    name=package_name,
    entry_point='main.py',
    functions=[
        dl.PackageFunction(
            name='add_classification',
            inputs=[
                dl.FunctionIO(name='item', type=dl.PackageInputType.ITEM),
            ],
            outputs=[
                dl.FunctionIO(name='items', type=dl.PackageInputType.ITEMS)
            ],
            description='adds a classification to the item'
        )
    ]
)]
```

Add now we can push the package to the Dataloop platform

```python
package = project.packages.push(package_name=package_name,
                                modules=modules,
                                src_path='./functions/add_annotation_to_item')
print('New Package has been deployed')
```

## Deploying the Service

After pushing the code, we need to create the service to actually run it.  
We'll define the autoscaling (so it will not cost us when there's nothing to run)

```python
runtime = dl.KubernetesRuntime(autoscaler=dl.KubernetesRabbitmqAutoscaler(min_replicas=0,
                                                                          max_replicas=1,
                                                                          queue_length=10))

service = package.services.deploy(service_name=package.name,
                                  module_name=package.name,
                                  runtime=runtime)
```

And now we have the service up and running!

## Trigger Events

Finally, we can add the trigger on the `uploading items` event.  
We will do it with a filter (DQL) so that only items in `/incoming` directly will be sent to our function. 

```python
filters = dl.Filters()
filters.add(field='datasetId', values='dataset id')
filters.add(field='dir', values='/incoming')

trigger = service.triggers.create(
    name='add-classification',
    function_name='add_classification',
    resource=dl.TriggerResource.ITEM,
    actions=[dl.TriggerAction.CREATED],
    filters=filters
)

```

## Summary
We have successfully created a Package (our code), Service (the cloud machine) and the Trigger (events) so that every  
item uploaded to our dataset will automatically get a classification annotation!

