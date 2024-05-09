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


def func3():
    project = dl.projects.get(project_name="<your-project-name>")
    dpk = dl.dpks.get(dpk_name='<app-name>')
    project.apps.install(dpk=dpk)


def func4():
    project = dl.projects.get(project_name="<your-project-name>")
    model = project.models.get("<model-name>")  # From the manifest's models.name
    artifact = model.artifacts.upload(filepath='/path/to/model_weights.pth')
    model.configuration['weights_filename'] = artifact.filename

    # to deploy the model
    model.deploy()


def func6():
    model = dl.models.get(model_id='<model_id>')
    item = dl.items.get(model_id='<item_id>')

    execution = model.predict(item_ids=[item.id])
    # wait for the execution to complete and get an updated execution
    execution.wait()
    execution = dl.executions.get(execution_id=execution.id)
    # print the most recent status
    print(execution.status[-1]['status'])
