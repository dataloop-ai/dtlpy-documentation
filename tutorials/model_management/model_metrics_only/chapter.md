## Offline model training, online metrics logging  
  
Models can be trained offline with only model metrics being uploaded to the Dataloop platform.  
  
The Dataloop entities required are:  
 - package  
 - codebase reference  
 - model (with a valid dataset ID)  
  
### Logging metrics  
To log metrics for tracking model performance, you need to create a dummy package (with a dummy codebase reference) and model (including a valid dataset ID). Remember to replace <project_name> and <dataset_id> with the appropriate strings to reference your project and dataset.  
  

```python
import dtlpy as dl
import os
project = dl.projects.get(project_name='<project_id>')
package = project.packages.push(package_name='dummy-model-package',
                                codebase=dl.entities.LocalCodebase(os.getcwd()),
                                modules=[])
model = package.models.create(model_name='My Model',
                              description='model for offline model logging',
                              dataset_id='<dataset_id>',
                              labels=[])
```
Now that you’ve created the necessary Dataloop entities, metrics can be uploaded to the platform with `model.add_log_samples` function.  
  
Here is an example uploading some dummy training data:  
  

```python
epoch = np.linspace(0, 9, 10)
epoch_metric = np.linspace(0, 9, 10)
for x_metric, y_metric in zip(epoch, epoch_metric):
    model.add_log_samples(samples=dl.LogSample(figure='tutorial plot',
                                               legend='some metric',
                                               x=x_metric,
                                               y=y_metric),
                          dataset_id=model.dataset_id)
```
Metrics plots will appear under the “metrics” tab of your chosen model, and will look something like this:  
![Screenshot of model metrics plot](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/assets/images/model_management/metrics_example.png/)  
  
