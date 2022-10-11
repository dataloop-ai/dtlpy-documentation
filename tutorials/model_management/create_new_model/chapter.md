## Create your own Package and Model  
  
You can use your own model on the platform by creating Package and Model entities, and then use a model adapter to create an API with Dataloop.  
  
The first thing a model adapter does is create a model adapter class. The example here inherits from dl.BaseModelAdapter, which contains all the Dataloop methods required to interact with the Package and Model. You must implement these methods in the model adapter class in order for them to work: load, save, train, predict.  
  
 In this example, the adapter is defined in a script called "adapter_script.py" and is separate from the rest of the code on this page. This script will load a model from a saved model weights file in the root directory called 'model.pth'.  
  

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
    def save(self, local_path, **kwargs):
        print('saving a model to {}'.format(local_path))
        torch.save(self.model, os.path.join(local_path, 'model.pth'))
    def train(self, data_path, output_path, **kwargs):
        print('running a training session')
    def predict(self, batch, **kwargs):
        print('predicting batch of size: {}'.format(len(batch)))
        preds = self.model(batch)
        return preds
```
NOTE: The code above is an example for a torch model adapter. This example will NOT run if copied as-is. For working examples please refer to the examples in the Dataloop Github.  
  
To create our Package entity, we first need to pack our package code to a dl.ItemCodebase, retrieve the metadata, and indicate where the entry point to the package is. If you’re creating a Package with code from Git, change the codebase type to be dl.GitCodebase.  
  

```python
import dtlpy as dl
from adapter_script import SimpleModelAdapter
project = dl.projects.get(project_name='<project_name>')
dataset = project.datasets.get(dataset_name='<dataset_name')
codebase = project.codebases.pack(directory='<path to local dir>')
# codebase: dl.GitCodebase = dl.GitCodebase(git_url='github.com/mygit', git_tag='v25.6.93')
metadata = dl.Package.get_ml_metadata(cls=SimpleModelAdapter,
                                      default_configuration={'weights_filename': 'model.pth',
                                                             'input_size': 256},
                                      output_type=dl.AnnotationType.CLASSIFICATION
                                      )
module = dl.PackageModule.from_entry_point(entry_point='adapter_script.py')
```
Then we can push the package and all its parts to the cloud. To change the computing configurations, see the Dataloop docs for the Instance Catalog.  
  

```python
package = project.packages.push(package_name='My-Package',
                                src_path=os.getcwd(),
                                package_type='ml',
                                codebase=codebase,
                                modules=[module],
                                is_global=False,
                                service_config={
                                    'runtime': dl.KubernetesRuntime(pod_type=dl.INSTANCE_CATALOG_GPU_K80_S,
                                                                    autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                                                        min_replicas=0,
                                                                        max_replicas=1),
                                                                    concurrency=1).to_json()},
                                metadata=metadata)
```
Now you can create a model and upload pretrained model weights with an Artifact Item. Here, the Artfiact item is where the saved model weights are. You can upload any weights file here and name it according to the 'weights_filename' in the configuration.  

```python
artifact = dl.LocalArtifact(local_path='<path to weights>')
model = package.models.create(model_name='tutorial-model',
                              description='first model we are uploading',
                              tags=['pretrained', 'tutorial'],
                              dataset_id=None,
                              configuration={'weights_filename': 'model.pth'
                                             },
                              project_id=package.project.id,
                              model_artifacts=[artifact],
                              labels=['car', 'fish', 'pizza']
                              )
```
Finally, build the model adapter and call one of the adapter’s methods to see that your custom model works. If you've entered a dataset_id when creating the model, you can also train the model on that dataset.  

```python
adapter = package.build()
adapter.load_from_model(model_entity=model)
```
