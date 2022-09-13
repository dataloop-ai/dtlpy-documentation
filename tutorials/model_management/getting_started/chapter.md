## Getting Started  
  
This tutorial will help you get started with the basics of model management:  
* logging metrics only (aka “offline mode”)  
* using pretrained models from the Dataloop model zoo for inference and training  
  
### Logging metrics  
To export metrics for tracking model performance, you need to create a dummy package (with a dummy codebase reference) and model (including a valid dataset ID). Remember to replace <project_name> and <dataset_id> with the appropriate strings to reference your project and dataset.  
  

```python
import dtlpy as dl
import os
project = dl.projects.get(project_name='My Project')
package = project.packages.push(package_name='dummy-model-package',
                                codebase=dl.entities.LocalCodebase(os.getcwd()),
                                modules=[])
model = package.models.create(model_name='My Model',
                              description='model for offline model logging',
                              dataset_id='My Dataset',
                              labels=[])
```
  
Once you’ve created these two entities, metrics can be sent to the platform with the `model.add_log_samples` command.  
Here is an example:  

```python
for x_metric, y_metric in zip(some_metric):
    model.add_log_samples(samples=dl.LogSample(figure='test metrics',
                                               legend='metric1',
                                               x=x_metric,
                                               y=y_metric),
                          dataset_id=model.dataset_id)
```
Metrics plots will appear under the “metrics” tab of your chosen model:  
ADD IMAgE  
  
### Using pretrained models from the AI library  
  
The Dataloop AI library includes various architectures and pretrained models that can be used for inference or further training.  
  
To see available public models, filter all available packages:  
  

```python
filters = dl.Filters(resource=dl.FiltersResource.PACKAGE, use_defaults=False)
filters.add(field='scope', values='public')
dl.packages.list(filters=filters).print()
```
Public models can be downloaded to be used on your machine for local training and inference, or can be trained and deployed on the cloud for integration into the Dataloop platform.  
  
### Training and inferencing models locally  
Download the codebase package and model you want to clone to your project  [[ maybe a screenshot of the AI Library screen, and copying the id? or the SDK list ]]  
  

```python
global_yolo_package = dl.packages.get(package_id="package_id")
global_yolo_model = global_yolo_package.models.get(model_id="model_id")
model = project.models.clone(from_model=global_yolo_model,
                             model_name='yolov5_remote',
                             project_id=project.id)
```
To run the model, you need the adapter for the training and inference methods.  
  
### Deploying models in the cloud  
  
Get the package and model you want to clone to your project  
  

```python
global_yolo_model = global_yolo_package.models.get(model_id="model_id")
model = dl.models.clone(from_model=global_yolo_model,
                        model_name='yolov5_remote',
                        project_id=project.id)
```
If the model is not yet trained, train on a dataset with:  
`model.train()`  
  
Once the model is trained, you can deploy it. This call automatically creates a bot and service for the trained model.  
`model.deploy()`  
  
Now the model is deployed, you can create a UI slot to inference on individual data items on the platform, or call the model to inference in a FaaS.  
  
