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
    import dtlpy as dl
    from adapter_script import SimpleModelAdapter

    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name')

    codebase = project.codebases.pack(directory='<path to local dir>')
    # codebase: dl.GitCodebase = dl.GitCodebase(git_url='github.com/mygit', git_tag='v25.6.93')
    metadata = dl.Package.get_ml_metadata(cls=SimpleModelAdapter,  # it's fine to do this
                                          default_configuration={'weights_filename': 'model.pth',
                                                                 'input_size': 256},
                                          output_type=dl.AnnotationType.CLASSIFICATION
                                          )
    module = dl.PackageModule.from_entry_point(entry_point='adapter_script.py')


def func3():
    package = project.packages.push(package_name='My-Package',
                                    src_path=os.getcwd(),
                                    package_type='ml',
                                    codebase=codebase,
                                    modules=[module],
                                    is_global=False,
                                    service_config={
                                        'runtime': dl.KubernetesRuntime(pod_type=dl.INSTANCE_CATALOG_GPU_K80_S,
                                                                        runner_image='gcr.io/viewo-g/modelmgmt/resnet:0.0.6',
                                                                        autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                                                            min_replicas=0,
                                                                            max_replicas=1),
                                                                        concurrency=1).to_json()},
                                    metadata=metadata)


def func4():
    artifact = dl.LocalArtifact(filepath='<path to weights>')
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


def func5():
    adapter = package.build()
    adapter.model = model
    # adapter.load_from_model(model=model)
    adapter.train()
