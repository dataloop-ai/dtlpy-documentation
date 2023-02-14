import dtlpy as dl


def func1():
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


def func2():
    import dtlpy as dl
    from adapter_script import SimpleModelAdapter

    project = dl.projects.get(project_name='<project_name>')
    dataset = project.datasets.get(dataset_name='<dataset_name')

    # codebase = project.codebases.pack(directory='<path to local dir>')
    # codebase: dl.GitCodebase = dl.GitCodebase(git_url='github.com/mygit', git_tag='v25.6.93')
    metadata = dl.Package.get_ml_metadata(cls=SimpleModelAdapter,
                                          default_configuration={},
                                          output_type=dl.AnnotationType.CLASSIFICATION
                                          )
    module = dl.PackageModule.from_entry_point(entry_point='adapter_script.py')


def func3():
    package = project.packages.push(package_name='My-Package',
                                    src_path=os.getcwd(),
                                    package_type='ml',
                                    # codebase=codebase,
                                    modules=[module],
                                    is_global=False,
                                    service_config={
                                        'runtime': dl.KubernetesRuntime(pod_type=dl.INSTANCE_CATALOG_GPU_K80_S,
                                                                        autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                                                            min_replicas=0,
                                                                            max_replicas=1),
                                                                        concurrency=1).to_json()},
                                    metadata=metadata)


def func4():
    artifact = dl.LocalArtifact(local_path='<path to weights>')
    model = package.models.create(model_name='tutorial-model',
                                  description='first model we are uploading',
                                  tags=['pretrained', 'tutorial'],
                                  dataset_id=None,
                                  configuration={'weights_filename': '<weights filename and extension>'
                                                 },
                                  project_id=package.project.id,
                                  model_artifacts=[artifact],
                                  labels=['car', 'fish', 'pizza']
                                  )


def func5():
    model.status = 'trained'
    model.update()
    model.deploy()


def func6():
    model = dl.models.get(model_id='<model_id>')
    item = dl.items.get(model_id='<item_id>')

    execution = model.predict(item_ids=[item.id])
    # after a few seconds, update your execution from the cloud
    execution = dl.executions.get(execution_id=execution.id)
    # print the most recent status
    print(execution.status[-1]['status'])