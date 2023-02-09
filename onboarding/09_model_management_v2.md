## Model management

Dataloop [Model Management](https://github.com/dataloop-ai/dtlpy-documentation/blob/model_mgmt/tutorials/model_management/introduction/chapter.md) helps you manage your machine learning models.

Models on the Dataloop platform are a specific type of FAAS, and changes in deploying or configurations result in different versions of models that can be compared.
Models require components and parts that can be changed, and these changes can be tracked and replicated in Model Management.

**The main concepts of Model Management:**

- [Package](https://dataloop.ai/docs/faas-package)
- [Service](https://dataloop.ai/docs/service-runtime)
- [Model](https://github.com/dataloop-ai/dtlpy-documentation/blob/glossary/docs_build/glossary/glossary.md#model-entity)
- [Artifact](https://github.com/dataloop-ai/dtlpy-documentation/blob/glossary/docs_build/glossary/glossary.md#artifacts-entity)


### **Example uses for model management:**

#### Logging metrics for model training

Models trained offline or online can connect to the model metrics. See [this tutorial](https://github.com/dataloop-ai/dtlpy-documentation/blob/model_mgmt/tutorials/model_management/model_metrics_only/chapter.md) for how to upload metrics functionality on the platform.

#### Copying or customizing model from the AI Library

The Dataloop AI Library contains pre-trained models that can be used directly for predicting on items, or further trained to customize on your dataset. See [this tutorial](https://github.com/dataloop-ai/dtlpy-documentation/blob/model_mgmt/tutorials/model_management/use_public_models/chapter.md) for how to copy or customize a public model on the platform.

#### Building custom models

If you have your own model you can build a model adapter to integrate it into the platform. See [this tutorial](https://github.com/dataloop-ai/dtlpy-documentation/blob/model_mgmt/tutorials/model_management/create_new_model/chapter.md) for a basic example.


### **Advanced exercises for using models:**

1. Clone and deploy a pre-trained model
2. Upload an image and predict on it (in the deployed models "test" tab)
3. Create your own model adapter for a pre-trained model, and upload to Model Management
4. Upload an image and predict on it (in the deployed models "test" tab)

