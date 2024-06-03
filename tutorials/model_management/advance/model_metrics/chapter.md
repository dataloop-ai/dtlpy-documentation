## Logging metrics in Dataloop  
  
This tutorial will walk you through how to upload metrics from model training via the SDK.  
  
NOTE: The models in our marketplace already using and uploading metrics.  
  
The Dataloop entities required are:  
 - dl.Package  
 - dl.Model (with a valid dataset ID)  
  
### Create Dataloop Entities  
First we'll create a dummy package and a model with a valid dataset ID. The code below shows how to do this, and remember to replace <project_name> and <dataset_id> with the appropriate strings to reference your project and dataset.  
  

```python
import dtlpy as dl
import os
project = dl.projects.get(project_name='<project-name>')
package = project.packages.push(package_name='dummy-model-package',
                                src_path=os.getcwd(),
                                modules=[])
model = package.models.create(model_name='My Model',
                              description='model for offline model logging',
                              dataset_id='<dataset-id>',
                              labels=[])
```
Now that you’ve created the necessary Dataloop entities, metrics can be uploaded to the platform with `model.metrics.create` and `dl.PlotSample`.  
  
Here is an example uploading some dummy training data:  
  

```python
epoch = np.linspace(0, 9, 10)
epoch_metric = np.linspace(0, 9, 10)
for x_metric, y_metric in zip(epoch, epoch_metric):
    model.metrics.create(samples=dl.PlotSample(figure='tutorial plot',
                                               legend='some metric',
                                               x=x_metric,
                                               y=y_metric),
                         dataset_id=model.dataset_id)
```
Metrics plots will appear under the “metrics” tab of your chosen model. The above code example will look like this:  
  
![Screenshot of model metrics plot](../../../../assets/images/model_management/tutorial_model_metrics.png)  
  
Once you’ve uploaded multiple model metrics, you can compare them by checking all the relevant boxes on the left that you would like to compare.  
  
### List Metrics  
You can list the metrics just like any other entity in the platform - using `list` (and optional dl.Filters):  
  

```python
samples = model.metrics.list()
for sample in samples.all():
    print(sample.x, sample.y)
# or retrieve it as a DataFrame
df = model.metrics.list().to_df()
```
