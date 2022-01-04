# Example of a simple pipeline

## Description

This example will include a simple pipeline flow generation from a json template.

The example have the following files:

* [Create & Deploy new pipeline ](creating_pipelines.py) - example entry point file (i.e main)
* [Pipeline template](pipeline_template.json) - the basic template scheme
* [FaaS definition](pipeline_faas.py) - a simple faas definition
* [Utility](utils.py) - a short utility (create service, create pipeline)

To run the example, you will need to change the `project_name` to a project you already created in dataloop platform.

`project_name = 'My Project'`

For this example, we will generate a dataset, recipe, package, service and of-course pipeline at your project, with the following names:

```
package_name = 'pipeline-faas-example-package'
dataset_name = 'pipeline-faas-example-dataset'
pipeline_name = 'pipeline-faas-example'
```

## Pipeline

Our pipeline will be consisted of the following components, '*automate*' FaaS - that will be triggerd on any new item created in the dataset, a Task - will be generated upon the first item in the pipline, and an arbitery FaaS - that you can change it's code from the UI.

Once an item was created, the pipeline would trigger, the automate function will be called with the item, it will set `item.metadata.system.fromPipe = True`, the item will assigned to your user, enter the task/assignment item, upon pressing 'Done' a complete event will be triggerd, and the item will trigger the arbitery function that will have the 'hello world' code - will set `item.metadata.user = {'Hello': 'World'}` and exit the pipeline.

![Alt text](../assets/pipeline_example.png)
