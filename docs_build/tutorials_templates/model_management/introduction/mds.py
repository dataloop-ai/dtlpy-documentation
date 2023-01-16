def func1():
    """
    # Model Management

    ## Quick Overview
    Dataloop's model management allows machine learning engineers to manage their research and production processes in one centralized place.

    Models are run using a combination of Packages, Datasets, and Artifacts.

    Model architectures are pushed to the cloud via Packages. Packages are bundles of code that contain the codebase required for the model to run. Datasets will include the images being used for training or inference, and they also indicate which images are included within a dataset subset (e.g. train/validation/test, or dividing your datset in other ways to achieve specific model training objectives).

    Models can come from ready-to-go packages of open source algorithms (e.g. ResNet, Yolo). Models can also be created from pre-trained models for fine-tuning or transfer learning.

    You can also upload your own models and compare model performance by viewing training metrics.

    All models can be integrated into the Dataloop platform, connected to the UI via buttons or slots, or added to pipelines.


    ## Introduction

    In this tutorial we will cover the required Dataloop entities to create, compare, restore, manage, and deploy model training sessions and trained models.

    ![Components of a Model](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/assets/images/model_management/model_diagram.png/)

    ### Package and Model Entities

    #### Package

    We will use the Package entity to save the architecture of the model (e.g Yolov5, Inception, SVM, etc.) and the model algorithm code.

    - In “online” mode (see “Model Comparison” below), Packages should include a Model Adapter to create the Dataloop API

    Model algorithms that are ready as-is to use can be found in the AI Library. All public packages listed in the AI Library are pretrained and include the model algorithm code and default configurations. Users can download the codebase of any packages pushed to the cloud.

    #### Model

    Using the Package (code), Dataset and Ontology (data and labels) and configuration (a dictionary) we can now create a Model.

    The Model contains the weights and any other artifacts needed to load the trained model and inference.

    A Model can also be cloned to be a starting point for a new model (for fine-tuning or transfer learning).

    ### Additional Package components

    Some users may want to further customize their models, such as uploading their own model weights or creating their own custom model. This can be achieved with Artifacts and a Model Adapter.

    #### Artifacts and Codebase

    Artifacts are any additional files necessary for a given model to run on the cloud. For example, if a user wanted to upload their own weights to create a pre-trained model, the weights file would be included as an Artifact. These artifacts can be uploaded via one of the following:

    1. local directory or path
    2. dl.Item
    3. Git repository
    4. other link

    #### The Model Adapter

    The Model Adapter is a python class that creates a single API between Dataloop's platform and your model. The Model Adapter class contains standardized methods that make it possible to integrate models into other parts of the Dataloop platform. Model Adapters allow the following model functions:
    1. train
    2. predict
    3. load/save model weights
    4. annotation conversion (if needed)

    ### Model comparison

    All models can be viewed in one place, and different model versions can be compared and evaluated with user-selected metrics.

    #### Offline vs online mode

    Model management can be used in two modes: offline (for local model training) or online (for integration into the Dataloop platform).

    In "offline" mode, users can run and train models on their local machine using local data, and can compare model configurations and metrics on the platform. “Offline” requires minimal platform integration, and can be used after dl.Package and dl.Model entities are created. This mode allows only visualizing metrics exported from the (local) model training session.

    In “offline” mode, code and weights are not saved anywhere in the Dataloop platform. Only model metrics are saved and viewable at a later time.

    ![An example of model metrics](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/assets/images/model_management/metrics_example.png/)

    In "online" mode, models can be trained to be deployed anywhere on the platform. For example, you can easily create a button interface to use your model to inference on a new data item and view it on the platform.

    To do this, you need to create a ModelAdapter class and implement the required functions to build the Dataloop API.

    “Online” mode also includes all the platform features mentioned above in “offline” mode.
    """
