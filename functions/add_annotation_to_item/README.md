# Adding anntoation to item

In this simple function, we will add a classification annotation to an incoming item

* Note: be sure to change the project name to your own working project

## Create the app and service

This directory contains `main.py` with the package code. Create a `dataloop.json` manifest in this directory with your module and service (e.g. name `add-classification`, function `add_classification`, runtime with autoscaler). Then:

```python
import os
import dtlpy as dl

project_name = "my-project"
project = dl.projects.get(project_name=project_name)

script_dir = os.path.dirname(os.path.abspath(__file__))
dpk = project.dpks.publish(
    manifest_filepath=os.path.join(script_dir, 'dataloop.json'),
    local_path=script_dir
)
app = project.apps.install(dpk=dpk)

service = project.services.get(service_name='add-classification')
```

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

