def func1():
    """
    # Model Management

    ## Introduction
    Dataloop's model management gives machine learning engineers the ability to manage their research and production processes.

    In this tutorial we will cover the Dataloop entities required to create, compare, restore, manage, and deploy training sessions and trained models.

    The Model Management module separates between model code, model parameters, and the dataset used for training.
    This allows for fully reproducible model training in the future.

    Model code can be imported from ready-to-go model algorithms available in the AI Library, or uploaded from a bucket/other external codebase.
    All existing user models can be viewed in one place, and models can be compared and evaluated with user-selected metrics.

    Pre-trained models can be created directly with the trained model weights, without any training information (come as-is).

    Models can be evaluated with new data, and individual data items and their predictions can be explored directly within the Model Management page.

    Model management can be used in two modes:
    online (for integration into the Dataloop platform), and offline (for local machine use only).

    In "online" mode, models can be easily trained and deployed anywhere on the platform,
    once the user creates a ModelAdapter class and implements some functions to build an API between Dataloop and the model.
    This includes all the platform features mentioned above.

    In "offline" mode, users can run and train models on their local machine using local data, and can compare model
    configurations and metrics on the platform, once a dl.Package and a dl.Model entity are created on the platform.
    This includes only the visualizations of the metrics exported from the (local) model training session.
    In this mode, code and weights are *not* saved anywhere in the Dataloop platform.

    ### Package and Model Entities

    #### Package

    We use the Package entity to save the code of the algorithm, the architecture of the model, e.g Yolov5, Inception, SVM, etc.
    - In "online" mode it should contain the Model Adapter to create a Dataloop API


    #### Model

    Using the Package (code), Dataset and Ontology (data and labels) and configuration (a dictionary) we can create a Model.
    The Model contains the weights and any other artifacts needed to load the trained model and inference.
    A model can be cloned to create a new model, to become a starting point for fine-tuning and transfer learning.

    #### Artifacts and Codebase
    1. local
    2. item
    3. git
    4. link

    ### The Model Adapter

    The Model Adapter is a python class to create a single API between Dataloop's platform and your model.

    1. train
    2. predict
    3. load/save model weights
    4. annotation conversion if needed

    We enable two modes of work:
    In "offline" mode, everything is local. You don't need to upload any code or weights to the platform, resulting in minimal platform integration.
    For example, you cannot use the Model Management components in a pipeline, and you cannot easily create a button interface with your model's inference.
    In "online" mode, after you build an Adapter, our platform can interact with your trained model. You will then be able to connect buttons and slots inside the platform and use it directly in pipelines.
    """
