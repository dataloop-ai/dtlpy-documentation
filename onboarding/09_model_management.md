## Model management
The Model-Management module in Dataloop provides a comprehensive solution for managing the entire lifecycle of your models. With this module, you have the flexibility to either use pre-existing public model architectures or connect and utilize your own custom models.

You can train different versions of your models using data items and their annotations, experiment with various hyper-parameters to find the best configuration, and evaluate your models by inferencing over datasets. The module also allows you to compare the training and evaluation metrics of your models, review false-positive and false-negative instances, and make informed decisions based on the results.

Once you have trained and evaluated your models, you can deploy them as a service within Dataloop applications. This enables you to run your models at scale and make them available to a wider audience. Additionally, the Model-Management module provides the tools to build continuous learning pipelines, where your models can continuously learn and improve over time.

### Why use Dataloop's model management feature?

Dataloop's model management feature enables machine learning engineers to centralize their research and production processes. The models are executed using Packages, Datasets, and Artifacts. The code required to run the model is contained in Packages and pushed to the cloud. The Datasets hold the images used for training or inference and define which images belong to each subset, such as train/validation/test. Models can be obtained from ready-to-use open source algorithms or created from pre-trained models for further fine-tuning or transfer learning. Additionally, one can upload their own models and evaluate performance by viewing training metrics. All models can be incorporated into the Dataloop platform and integrated into the UI through buttons or slots or added to pipelines.

The Model Comparison feature in the Dataloop platform enables users to view and compare different versions of models all in one place. This can be done by selecting user-specified metrics to evaluate the models.

The Model Management system in the platform can work in two ways: "offline" mode and "online" mode.

* In the **offline mode**, users can train and run models locally using their own data and compare the configurations and metrics of different models on the platform. This mode does not require extensive platform integration and can be used after creating dl.Package and dl.Model entities. However, it is limited to visualizing metrics that have been exported from the local model training sessions only. The code and weights of the models are not saved in the Dataloop platform, but the metrics can be viewed at a later time.

* On the other hand, the **online mode** allows users to train models that can be deployed anywhere within the platform. For instance, users can create a button interface to use their model for inferencing on new data and view the results on the platform. To use this mode, users must create a ModelAdapter class and implement the required functions to access the Dataloop API. This mode includes all the features available in the "offline" mode.

### Model Management in Dataloop's Python SDK

Model management is also available both in the UI web version of Dataloop and in the Python SDK version.

You can find more about how to use models in our [redocly documentetaion on Model Management](https://dlportal-demo.redoc.ly/tutorials/model_management/) or [our Python SDK-focused documentation](https://sdk-docs.dataloop.ai/en/latest/tutorials.html#model-management).

Additionally, here are some code snippets that may be useful:
1. Clone a model;
```python
import dtlpy as dl

package = dl.packages.get(package_name='resnet')
pretrained_model = package.models.get(model_name='pretrained-resnet50')

model = pretrained_model.clone(model_name='my pretrained',
                               description='pretrained cloned in to my project',
                               project_id="$PROJECT_ID")
```
2. Deploy a model;
```python
import dtlpy as dl

package = dl.packages.get(package_name='resnet')
model = package.models.get(model_name='pretrained-resnet')

dataset = dl.datasets.get(dataset_id='datasetId')

model.evaluate(dataset=dataset)
```
3. Evaluate a model;
```python
import dtlpy as dl

package = dl.packages.get(package_name='resnet')
pretrained_model = package.models.get(model_name='pretrained-resnet')

model = pretrained_model.clone(model_name='my first exp',
                               description='with higher lr',
                               project_id="projectId")

model.train()
```
4. Train a model;
```python
import dtlpy as dl

package = dl.packages.get(package_name='resnet')
pretrained_model = package.models.get(model_name='pretrained-resnet')

model = pretrained_model.clone(model_name='my first exp',
                               description='with higher lr',
                               project_id="projectId")

model.train()
```

The next chapter of this onboarding will show you what the next steps are in learning more about Dataloop's Python SDK. It will provide additional resources and redirect you to more advanced tutorials and exercices.
