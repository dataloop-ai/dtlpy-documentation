## Create Your own Model and Snapshot  
  
We will create a dummy model adapter in order to build our model and snapshot entities  
NOTE: This is an example for a torch model adapter. This example will NOT run as-is. For working examples please refer to our models on github <add links>  
  
The following class inherits from the dl.BaseModelAdapter, which have all the Dataloop methods for interacting with the Model and Snapshot  
There are four methods that are model-related that the creator must implement for the adapter to have the API with Dataloop  

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
  
Now we can create our Model entity with an Item codebase.  

```python
project = dl.projects.get('MyProject')
codebase: dl.ItemCodebase = project.codebases.pack(directory='/path/to/codebase')
model = project.models.create(model_name='first-git-model',
                              description='Example from model creation tutorial',
                              output_type=dl.AnnotationType.CLASSIFICATION,
                              tags=['torch', 'inception', 'classification'],
                              codebase=codebase,
                              entry_point='dataloop_adapter.py',
                              )
```
For creating a Model with a Git code, simply change the codebase to be a Git one:  
  

```python
project = dl.projects.get('MyProject')
codebase: dl.GitCodebase = dl.GitCodebase(git_url='github.com/mygit', git_tag='v25.6.93')
model = project.models.create(model_name='first-model',
                              description='Example from model creation tutorial',
                              output_type=dl.AnnotationType.CLASSIFICATION,
                              tags=['torch', 'inception', 'classification'],
                              codebase=codebase,
                              entry_point='dataloop_adapter.py',
                              )
```
Creating a local snapshot:  

```python
bucket = dl.buckets.create(dl.BucketType.ITEM)
bucket.upload('/path/to/weights')
snapshot = model.snapshots.create(snapshot_name='tutorial-snapshot',
                                  description='first snapshot we uploaded',
                                  tags=['pretrained', 'tutorial'],
                                  dataset_id=None,
                                  configuration={'weights_filename': 'model.pth'
                                                 },
                                  project_id=model.project.id,
                                  bucket=bucket,
                                  labels=['car', 'fish', 'pizza']
                                  )
```
Building to model adapter and calling one of the adapter's methods:  
  

```python
adapter = model.build()
adapter.load_from_snapshot(snapshot=snapshot)
adapter.train()
```
