## Create your own model  
  
You can use your own model to use on the platform by creating Package and Model entities, and then use a model adapter to create an API with Dataloop.  
  
In this tutorial you will learn how to create a basic model adapter to be able to inference on platform items.  
  
### Create a model adapter  
  
In the example code below, the adapter is defined in a script saved as `adapter.py`. The SimpleModelAdapter class inherits from `dl.BaseModelAdapter`, which contains all the Dataloop methods required to interact with the Package and Model, as well as some some internal wrapper functions that make it easier to use Dataloop entities (e.g. `predict_items`, `predict_datasets`).  
  
The minimum required functions to implement for a model to inference are `load` and `predict`.  
  
`load` is supposed to implement loading the model (e.g. from any weights.pth). The `load` takes a local path as input.  
  
In the `dl.BaseModelAdapter` we have a `load_from_model` wrapper which will download the model artifacts locally and call the custom `load` with the path containing all the files.  
  
`predict` is where the model will do its inference, and the predict function expects a preprocessed batch (e.g. ndarray for images), and returns a list of dl.AnnotationCollection entities.  
  
The wrapper for `predict` is `predict_items`, which takes a list of items from the platform and prepares everything for predicting. It uses the `prepare_item_func` to preprocess items into the a batch and calles the custom `predict`. After the prediction, it takes the ouput and uploads it to each item.  
  
NOTE: You can edit the preprocess function by simply override the `prepare_item_func` method. For example, to pass the items as-is you can just return the inputed item.  
  
in `adapter.py`, add the following model adapter:  

```python
import dtlpy as dl
import torch
import os
@dl.Package.decorators.module(name='model-adapter',
                              description='Model Adapter for my model',
                              init_inputs={'model_entity': dl.Model})
class SimpleModelAdapter(dl.BaseModelAdapter):
    def load(self, local_path, **kwargs):
        print('loading a model')
        self.model = torch.load(os.path.join(local_path, 'model.pth'))
    def predict(self, batch, **kwargs):
        print('predicting batch of size: {}'.format(len(batch)))
        preds = self.model(batch)
        batch_annotations = list()
        for i_img, predicted_class in enumerate(preds):  # annotations per image
            image_annotations = dl.AnnotationCollection()
            # in this example, we will assume preds is a label for a classification model
            image_annotations.add(annotation_definition=dl.Classification(label=predicted_class),
                                  model_info={'name': self.model_name})
            batch_annotations.append(image_annotations)
        return batch_annotations
```
Please see an example [here](https://github.com/dataloop-ai-apps/torch-models/blob/main/resnet_adapter.py) (for PyTroch's Resnet) in Github of a working model adapter and see how to construct Annotation Collections.  
  
### Push the package  
  
To create our Package entity, we first need to retrieve the metadata and indicate where the entry point to the package is within the codebase.  
  

```python
import dtlpy as dl
from model_adapter import SimpleModelAdapter
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name')
metadata = dl.Package.get_ml_metadata(cls=SimpleModelAdapter,
                                      default_configuration={},
                                      output_type=dl.AnnotationType.CLASSIFICATION
                                      )
module = dl.PackageModule.from_entry_point(entry_point='model_adapter.py')
```
Then we can push the package and all its components to the cloud.  
  
Service configs help define the dl.Service that will be created when deploying/training the model.  
  
To change the service configurations, see the documentation on [service types](https://dataloop.ai/docs/service-runtime).  
  

```python
package = project.packages.push(package_name='My-Package',
                                src_path=os.getcwd(),
                                package_type='ml',
                                # codebase=codebase,
                                modules=[module],
                                service_config={
                                    'runtime': dl.KubernetesRuntime(pod_type=dl.INSTANCE_CATALOG_GPU_K80_S,
                                                                    autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                                                        min_replicas=0,
                                                                        max_replicas=1),
                                                                    concurrency=1).to_json()},
                                metadata=metadata)
```
### Create the model and upload artifacts  
  
Now you can create a model and upload pretrained model weights with an Artifact Item.  
Here, the weights will be uploaded as an Item Artifact connected to the model.  
You can upload any weights file here and use the artifact filename to update the `weights_filename` field in the model configuration.  
  
  

```python
model = package.models.create(model_name='tutorial-model',
                              description='first model we are uploading',
                              tags=['pretrained', 'tutorial'],
                              dataset_id=None,
                              configuration={},
                              project_id=package.project.id,
                              labels=['car', 'fish', 'pizza']
                              )
artifact = model.artifacts.upload(filepath='/path/to/model_weights.pth')
model.configuration['weights_filename'] = artifact.filename
```
To deploy a model we'll also update the status:  
  

```python
model.status = 'trained'
model.update()
model.deploy()
```
## Checking that your model works  
  
NOTE: The deployed service must be up and ready in order to run the predictions (including in the test tab). You can check the status of the deployed service in the services page.  
  
### Via the UI  
  
You should now be able to see the model in the “Deployed” tab. After clicking on your model, you should see a “Test” tab where you can drag and drop an image, click “Test” and see the results of your model prediction.  
  
If you get timeouts or error predicting, check that the service is up and is functioning as expected.  
  
![Screenshot of deployed model test tab](../../../assets/images/model_management/test_tab.png)  
  
### Via the SDK  
  
To test whether your function was successfully uploaded and deployed onto the platform, you can use the `model.predict()` function to predict on a list of item IDs.  
The function will return an Execution entity, which you can use to check the status of the prediction execution.  
Once the execution is completed, the annotation will be uploaded to each item.  

```python
model = dl.models.get(model_id='<model_id>')
item = dl.items.get(model_id='<item_id>')
execution = model.predict(item_ids=[item.id])
# wait for the execution to complete and get an updated execution
execution.wait()
execution = dl.executions.get(execution_id=execution.id)
# print the most recent status
print(execution.status[-1]['status'])
```
  
If you encounter errors, you will need to look at the logs to see where the error occurred.  Go to "Model Management", under the "Deployed" tab, click on the number in the "Executions" column for the appropriate model, and then click on the "Execution" log icon on the right side of the screen (the paper icon). Here you can see the output of the cloud machine. You can also access this page via the "Application Hub", under "Executions".  
