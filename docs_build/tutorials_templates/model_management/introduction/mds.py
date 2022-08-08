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

    The dataset used to train the model is cloned and stored in the model params. This allows data versioning within the model managment.

    Models can be evaluated with new data, and individual data items and their predictions can be explored directly within the Model Management page.

    Model management can be used in two modes:
    online (for integration into the Dataloop platform), and offline (for local machine use only).

    In "online" mode, models can be easily trained and deployed anywhere on the platform,
    once the user creates a ModelAdapter class and implements some functions to build an API between Dataloop and the model.
    This includes all the platform features mentioned above.

    In "offline" mode, users can run and train models on their local machine using local data, and can compare model
    configurations and metrics on the platform, once a dl.Model and a dl.Snapshot entity are created on the platform.
    This includes only the visualizations of the metrics exported from the (local) model training session.
    In this mode, code and weights are not saved anywhere in the Dataloop platform.

    ### Model and Snapshot entities

    #### Model

    The model entity is basically the algorithm, the architecture of the model, e.g Yolov5, Inception, SVM, etc.
    - In online it should contain the Model Adapter to create a Dataloop API


    #### Snapshot

    Using the Model (architecture), Dataset and Ontology (data and labels) and configuration (a dictionary) we can create a Snapshot of a training process.
    The Snapshot contains the weights and any other artifact needed to load the trained model

    a snapshot can be used as a parent to another snapshot - to start for that point (fine-tune and transfer learning)

    #### Buckets and Codebase
    1. local
    2. item
    3. git
    4. GCS

    ### The Model Adapter

    The Model Adapter is a python class to create a single API between Dataloop's platform and your Model

    1. Train
    2. Predict
    3. load/save model weights
    4. annotation conversion if needed

    We enable two modes of work:
    in Offline mode, everything is local, you don't have to upload any model code or any weights to platform, which causes the platform integration to be minimal.
    For example, you cannot use the Model Management components in a pipeline, can easily create a button interface with your model's inference and more.
    In Online mode - once you build an Adapter, our platform can interact with your model and trained snapshots and you can connect buttons and slots inside the platform to create, train, inference etc and connect the model and any train snapshot to the UI or to add to a pipeline
    """
