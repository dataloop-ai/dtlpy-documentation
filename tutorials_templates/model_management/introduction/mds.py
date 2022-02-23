def func1():
    """
    # Model Management

    ## Introduction
    Dataloop's Model Management is here to provide Machine Learning engineers the ability to manage their research and production process.

    We want to introduce Dataloop entities to create, manage, view, compare, restore, and deploy training sessions.

    Our Model Management gives a separation between Model code, weights and configuration, and the data.

    in Offline mode, there is no need to do any code integration with Dataloop - just create a model and snapshots entities and you can start managing your work on the platform create reproducible training:
    - same configurations and dataset to reproduce the training
    - view project/org models and snapshots in the platform
    - view training metrics and results
    - compare experiments
    NOTE: all functions from the codebase can be used in FaaS and pipelines only with custom functions! User must create a FaaS and expose those functions any way he’d like

    Online Mode:
    In the online mode, you can train and deploy your models easily anywhere on the platform.
    All you need to do is create a Model Adapter class and expose some functions to build an API between Dataloop and your model.
    After that, you can easily add model blocks to pipelines, add UI slots in the studio, one-button-training etc

    TODO: add more documentation in the Adapter function and maybe some example

    ### Model and Snapshot entities

    #### Model

    The model entity is basically the algorithm, the architecture of the model, e.g Yolov5, Inception, SVM, etc.
    - In online it should contain the Model Adapter to create a Dataloop API

    TODO: add the module attributes

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
