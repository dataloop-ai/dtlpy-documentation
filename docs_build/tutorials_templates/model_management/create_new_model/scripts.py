import dtlpy as dl


def func1():
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


def func2():
    project = dl.projects.get('MyProject')
    codebase: dl.ItemCodebase = project.codebases.pack(directory='/path/to/codebase')
    package = project.packages.push(package_name='first-custom-model',
                                    description='Example from model creation tutorial',
                                    output_type=dl.AnnotationType.CLASSIFICATION,
                                    tags=['torch', 'inception', 'classification'],
                                    codebase=codebase,
                                    entry_point='dataloop_adapter.py',
                                    )


def func3():
    codebase: dl.GitCodebase = dl.GitCodebase(git_url='github.com/mygit', git_tag='v25.6.93')

def func4():
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


def func5():
    adapter = package.build()
    adapter.model = model
    # adapter.load_from_model(model=model)
    adapter.train()
