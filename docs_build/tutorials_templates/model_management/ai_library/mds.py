def func1():
    """
    ## Models from the AI Library

    Ready-to-use models are available in the Dataloop AI Library

    The AI library contains various algorithms and pretrained models that can be used for inference or fine-tuning via additional training on your custom datasets.

    This tutorial will cover how to use AI library models for:

    - predicting from pretrained models, and
    - fine-tuning training on a custom dataset.

    To see all available models in the AI Library, use a filter to view all available models with a "public" scope"

    """


def func2():
    """
    ### Predicting

    #### Clone and deploy a model

    First we'll create a new project and dataset, and upload a new item:

    """


def func3():
    """

    We'll get the public model clone it into the new project.

    Only models that are trained (i.e. model.status = 'trained') can be deployed. Models from the AI library can be deployed directly.

    Note: You can add any service configuration to override the default on the deployed service
    """


def func4():
    """

    #### Predict items

    Once a model is deployed, you can predict on items using the `model.predict()` function.
    The function returns an execution object that can be used to track whether the prediction execution was successful.
    If successful, the annotations will be uploaded to the item directly and can be viewed in the annotation studio.

    If you have just deployed the model, `get` the model again to get the updated model metadata that includes the deployment information.

    """


def func5():
    """

    ### Finetune on a custom dataset

    If you would like to customize the AI library model (for transfer-learning or fine-tuning), you can indicate the new dataset and labels you want to use for model training.

    """


def func6():
    """

    #### Define dataset subsets

    Our AI library models require a train/validation split of the dataset for the training session. To avoid data leakage between training sessions and to make each training reproducible, we will define the data subsets and save the split type to the dataset entity (using a DQL). Using DQL filters you can subset the data however you like.

    For example, if your dataset is split between folders, you can use this DQL to add metadata for all items in the dataset
    """


def func7():
    """
    This way, when the training starts, the sets will be downloaded using the DQL and any future training session on this dataset will have the same subsets of data.

    NOTE: In the future, this mechanism will be expanded to use a tagging system on items. This will allow more flexible data subsets and random data allocation.

    #### Train

    To train the model on your custom data, simply use the `model.train()` function and wait for the training to finish. You can monitor the training progress on the platform or via the python SDK. To see the updated model status, retrieve the model again from the platform.

    """


def func8():
    """
    #### Deploy the new model

    Once the model is trained, it can be deployed as a service. The `model.deploy()` function automatically creates a bot and service for the trained model.

    Once you have a model deployed, you can create a UI slot to inference on individual data items on the platform, or call the model to inference in a FaaS or pipelines.

    """
