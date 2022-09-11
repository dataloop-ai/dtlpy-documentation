## Create your own Package and Model  
  
You can use your own model on the platform by creating package and model entities, and using a model adapter to create an API with Dataloop.  
  
The first thing a model adapter does is create a model adapter class. The example here inherits from dl.BaseModelAdapter, which contains all the Dataloop methods required to interact with the Package and Model. You must implement these methods in the model adapter class in order for them to work: load, save, train, predict.  

```python
import dtlpy as dl
import torch
import os
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
  
To create our Package entity, we first need to pack our package code to a dl.ItemCodebase.  

```python
project = dl.projects.get('MyProject')
codebase: dl.ItemCodebase = project.codebases.pack(directory='/path/to/codebase')
package = project.packages.push(package_name='first-custom-model',
                                description='Example from model creation tutorial',
                                output_type=dl.AnnotationType.CLASSIFICATION,
                                tags=['torch', 'inception', 'classification'],
                                codebase=codebase,
                                entry_point='dataloop_adapter.py',
                                )
```
If you’re creating a Package with code from Git, change the codebase type to be dl.GitCodebase.  
  

```python
codebase: dl.GitCodebase = dl.GitCodebase(git_url='github.com/mygit', git_tag='v25.6.93')
```
Now you can create a model and upload pretrained model weights with dl.Artifacts.  

```python
artifact = project.artifacts.upload(filepath='/path/to/weights')
model = package.models.create(model_name='tutorial-model',
                                  description='first model we uploaded',
                                  tags=['pretrained', 'tutorial'],
                                  dataset_id=None,
                                  configuration={'weights_filename': 'model.pth'
                                                 },
                                  # project_id=package.project.id,
                                  model_artifacts=[artifact],
                                  labels=['car', 'fish', 'pizza']
                                  )
```
Finally, build to the model adapter and call one of the adapter’s methods to see that your custom model works.  

```python
adapter = package.build()
adapter.model = model
# adapter.load_from_model(model=model)
adapter.train()
```
