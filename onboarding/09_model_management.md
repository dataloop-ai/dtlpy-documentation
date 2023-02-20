## Model management
The Model-Management module in Dataloop provides a comprehensive solution for managing the entire lifecycle of your models. With this module, you have the flexibility to either use pre-existing public model architectures or connect and utilize your own custom models.

You can train different versions of your models using data items and their annotations, experiment with various hyper-parameters to find the best configuration, and evaluate your models by inferencing over datasets. The module also allows you to compare the training and evaluation metrics of your models, review false-positive and false-negative instances, and make informed decisions based on the results.

Once you have trained and evaluated your models, you can deploy them as a service within Dataloop applications. This enables you to run your models at scale and make them available to a wider audience. Additionally, the Model-Management module provides the tools to build continuous learning pipelines, where your models can continuously learn and improve over time.

### Why use Dataloop's model management feature?

Dataloop's model management feature enables machine learning engineers to centralize their research and production processes. The models are executed using Packages, Datasets, and Artifacts, and served with Services. The code required to run the model is contained in Packages and pushed to the cloud. The Datasets hold the images used for training or inference and define which images belong to each subset, such as train/validation/test. Artifacts are large files that are required for the deployment of a package, such as pre-trained model weights. Models can be obtained from ready-to-use open source algorithms or created from pre-trained models for further fine-tuning or transfer learning. Additionally, you can upload your own models and evaluate performance by viewing training metrics. All models can be incorporated into the Dataloop platform and integrated into the UI through buttons or slots or added to pipelines.

The Model Comparison feature in the Dataloop platform enables users to view and compare different versions of models all in one place. This can be done by selecting user-specified metrics to evaluate the models.

The Model Management system in the platform can work in two ways: "offline" mode and "online" mode.

* In the **offline mode**, users can train and run models locally using their own data and compare the configurations and metrics of different models on the platform. This mode does not require extensive platform integration and can be used after creating dl.Package and dl.Model entities. However, it is limited to visualizing metrics that have been exported from the local model training sessions only. The code and weights of the models are not saved in the Dataloop platform, but the metrics can be viewed at a later time.

* On the other hand, the **online mode** allows users to train models that can be deployed anywhere within the platform. For instance, users can create a button interface to use their model for inferencing on new data and view the results on the platform. To use this mode, users must create a ModelAdapter class and implement the required functions to access the Dataloop API. This mode includes all the features available in the "offline" mode.

### Model Management in SDK

Model management is also available both in the UI web version of Dataloop and in the SDK version.

You can find more about how to use models in our [redocly documentation on Model Management](https://dlportal-demo.redoc.ly/tutorials/model_management/) or [our SDK-focused documentation](https://sdk-docs.dataloop.ai/en/latest/tutorials.html#model-management).

Additionally, here are some code snippets that may be useful:
1. Log metrics:
```python
import dtlpy as dl
import os

project = dl.projects.get(project_id='$PROJECT_ID')
package = project.packages.push(package_name='dummy-model-package',
                                codebase=dl.entities.LocalCodebase(os.getcwd()),
                                modules=[])
model = package.models.create(model_name='My Model',
                              description='model for offline model logging',
                              dataset_id='$DATASET_ID',
                              labels=[])

epoch = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
epoch_metric = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x_metric, y_metric in zip(epoch, epoch_metric):
    model.add_log_samples(samples=dl.LogSample(figure='tutorial plot',
                                               legend='some metric',
                                               x=x_metric,
                                               y=y_metric),
                          dataset_id=model.dataset_id)
```
2. Deploy a pre-trained model:
```python
import dtlpy as dl

# list all publicly available models
filters = dl.Filters(resource=dl.FiltersResource.MODEL, use_defaults=False)
filters.add(field='scope', values='public')
dl.models.list(filters=filters).print()

project = dl.projects.get(project_id='$PROJECT_ID')
public_model = dl.models.get(model_id='$PUBLIC_MODEL_ID')
model = project.models.clone(from_model=public_model,
                             model_name='My cloned model',
                             project_id=project.id)
model.deploy()

```
3. Train a model:
```python
import dtlpy as dl

project = dl.projects.get(project_id='$PROJECT_ID')
dataset = dl.datasets.get(dataset_id='$DATASET_ID')
labels = list(dataset.labels_flat_dict.keys())

public_model = dl.models.get(model_id='$PUBLIC_MODEL_ID')
custom_model = dl.models.clone(from_model=public_model,
                               model_name='My custom-trained model',
                               dataset=dataset,
                               project_id=project.id,
                               labels=labels)

custom_model.train()
custom_model = dl.models.get(model_id=custom_model.id)
print(custom_model.status)
```
4. Predict with a deployed model:
```python
import dtlpy as dl

project = dl.projects.get(project_id='$PROJECT_ID')
model = project.models.get(model_name='My cloned model')

model.predict(item_ids=['$ITEM_ID'])
```

The next chapter of this onboarding will show you what the next steps are in learning more about Dataloop's SDK. It will provide additional resources and redirect you to more advanced tutorials and exercices.
