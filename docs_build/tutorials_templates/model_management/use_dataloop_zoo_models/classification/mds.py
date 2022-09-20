def func1():
    """
    # Training a classification model with ResNet
    In this tutorial we will use a publicly available model from the AI library to inference and train on custom data.
    Here we will use a ResNet50 model.

    Start by installing the following packages if you don't have them installed already. The model adapter will use them later.

    torch
    torchvision
    imgaug
    scikit-image<0.18

    """


def func2():
    """
    ## Create the Package and pretrained Model in your project

    First, we create the Model entity for our project. You can view the public models in the public Dataloop Github.
    You can view all publicly available models by using a Filter. Here we will use a ResNet50 model pretrained on the ImageNET dataset.
    """


def func3():
    """
    ### Run a pretrained model

    We will "build" a model adapter to get the package code locally and create an instance of the ModelAdapter class.
    Then we will load the pretrained model into the model adapter.
    """


def func4():
    """
    ### Predict on an item
    Now you can get an item and inference on it with the predict method and then upload the annotations.
    If you would like to see the item and predictions, you can open the item on the platform and edit there.
    """


def func5():
    """
    ## Train on new dataset
    Here we will use a public dataset of sheep faces. We create a project and a dataset and upload the data with 4 labels of sheep.
    NOTE: You might need to change the location of the items, which currently points to the root of the documentation repository. If you downloaded the documentation repo to your local machine, this should work as-is.
    """


def func6():
    """
    Now we'll run the "prepare_dataset" method. This will clone and freeze the dataset so that we'll be able to reproduce the training with and keep the snapshot of the data.
    The cloned dataset will be split into subsets, either filtered using DQL or as percentages. In this example, we'll use an 80/20 train validation split.
    After partitioning the data, we will clone the pretrained model to have a starting point for the fine-tuning.
    The model's configuration will determine some runtime configurations, such as number of epochs. In this tutorial we will train for only 2 epochs.
    """


def func7():
    """
    We'll load the new, un-trained model into the adapter and prepare the training local dataset.
    """


def func8():
    """
    ## Start the training
    The package, model, and data are now prepared. We are ready to train!
    """


def func9():
    """
    ## Save the Model
    We will save the locally-trained model and upload the trained weights to the Item Artifact.
    This will ensure that everything is in the Dataloop platform and other developers can use our trained model.
    """


def func10():
    """
    We can also list all Artifacts associated with this Package, and add more files that are needed to load or run the model.
    """


def func11():
    """
    ## Predict on our newly trained model
    With everything in place, we will load our model and view the item's prediction.
    """
