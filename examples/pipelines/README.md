# Example of a simple pipeline

## Description

This example will include a simple pipeline flow generation from the SDK and json template.

The example have the following files:

* [Create & Deploy new pipeline ](create_pipeline.py) - example entry point file (i.e main)
* [Pipeline template](pipeline_template.json) - the basic template scheme

To run the example, you will need to create a project and a dataset and change the `project_name` and `dataset_name` to those you want to use.

```
project_name = 'My Project'  
dataset_name = 'My Dataset'
```

For this example, we will create service (you can use any existing service), and of-course the pipeline in your project.
If you want to use existing service, set the name in the function, otherwise, you can continue

```
service_name = 'existing-service-name'
```

## Pipeline

Our pipeline will be consisted of the following components:  
* A 'code-block' FaaS - that you can change its code from the UI.
* '*automate*' FaaS - that will be triggered on any new item created in the dataset. 
* A Task - will be generated upon the first item in the pipeline. 

Once an item was created, the pipeline would trigger, the code block will be called with the item, it will set `item.metadata['user']['first'] = 'Hello''`, the item will assigned to your user, enter the task/assignment item, upon pressing 'Done' a complete event will be triggered, and the item will continue to the automate function that will add `item.metadata['user']['first'] = 'World''` and exit the pipeline.

![Alt text](../../assets/pipeline_example.png)
