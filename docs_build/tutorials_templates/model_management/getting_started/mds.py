def func1():
    """
    ## Getting Started

    This tutorial will help you get started with the basics of model management:
    * logging metrics only (aka “offline mode”)
    * using pretrained models from the Dataloop model zoo for inference and training

    ### Logging metrics
    To export metrics for tracking model performance, you need to create a dummy package (with a dummy codebase reference) and model (including a valid dataset ID). Remember to replace <project_name> and <dataset_id> with the appropriate strings to reference your project and dataset.

    """


def func2():
    """

    Once you’ve created these two entities, metrics can be sent to the platform with the `model.add_log_samples` command.
    Here is an example:
    """


def func3():
    """
    Metrics plots will appear under the “metrics” tab of your chosen model:
    ![Screenshot of model metrics plot](https://github.com/dataloop-ai/dtlpy-documentation/blob/model_mgmt_3/assets/images/model_management/metrics_example.png)

    ### Using pretrained models from the AI library

    The Dataloop AI library includes various architectures and pretrained models that can be used for inference or further training.

    To see available public models, filter all available packages:

    """


def func4():
    """
    Public models can be downloaded to be used on your machine for local training and inference, or can be trained and deployed on the cloud for integration into the Dataloop platform.

    ### Dataset Subsets
    Our public models use a train/validation split of the dataset for the training session. To avoid data leakage between training sessions and to make each training reproducible,
    we will determine the data subsets and save the split type to the dataset entity (using a DQL). Using DQL filters you can subset the data however you like.

    For example, if your dataset is split between folders, you can use this DQL:
    """


def func5():
    """

    This way, when the training starts, the sets will be downloaded using the DQL and any future training session on this dataset will have the same subsets of data.

    NOTE: In the future, this mechanism will be expanded using an item tagging system. This will allow more flexible data subsets and random data allocation.


    ### Training and inferencing models locally

    Download the codebase package and model you want to clone to your project.

    """


def func6():
    """
    To run the model, you need the model adapter for the train and inference methods.

    ### Deploying models in the cloud

    Get the package and model you want to clone to your project

    """


def func7():
    """
    If the model is not yet trained, train on a dataset with:
    `model.train()`

    Once the model is trained, you can deploy it. This call automatically creates a bot and service for the trained model.
    `model.deploy()`

    Now the model is deployed, you can create a UI slot to inference on individual data items on the platform, or call the model to inference in a FaaS.

    """
