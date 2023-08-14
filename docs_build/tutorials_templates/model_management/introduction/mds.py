def func1():
    """
    # Model Management

    ## Quick overview
    Dataloop's model management centralizes model research and production processes for machine learning engineers in one place.

    Models can be installed from pre-trained open source model architectures (e.g.ResNet, YOLO). These models can also be fine-tuned on custom datasets on the Dataloop platform.

    You can also upload your own models or and compare model performance through the model metrics interface.


    ## Introduction

    In this tutorial we will cover the required Dataloop entities to create, compare, restore, manage, and deploy model training sessions and trained models.

    <img src="../../../assets/images/model_management/model_diagram.jpg" alt="drawing" width="600" height="300"/>

    ### Package and Model Entities

    #### Package

    We will use the Package entity to save the architecture of the model (e.g Yolov8, Inception, SVM, etc.) and any other function and modules.

    - Packages should include a Model Adapter to create the Dataloop API

    Models that are ready as-is to use can be found in the AI Library. All models listed in the AI Library are pretrained and include the model architecture code and default configurations.

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

    #### The Model adapter

    The model adapter is a python class that creates a single API between Dataloop's platform and your model. The ModelAdapter class contains standardized methods that make it possible to integrate models into other parts of the Dataloop platform. Model adapters allow the following model functions:
    1. train
    2. predict
    3. load/save model weights
    4. annotation conversion (if needed)

    ### Model comparison

    All models can be viewed in one place, and different model versions can be compared and evaluated with user-selected metrics.

    ![An example of model metrics](../../../assets/images/model_management/metrics_example.png)

    """
