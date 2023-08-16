def func1():
    """
    # Training a classification model with ResNet
    In this tutorial we will download a public model from the AI library to inference and train on custom data locally.
    Here we will use a ResNet50 model.

    Start by installing the following packages if you don't have them installed already. The model adapter will use them later.
    torch
    torchvision
    imgaug
    scikit-image<0.18

    Then, import the modules required for the scripts in this tutorial.
    """


def func2():
    """
    ## Clone the Public Model Into Your Project

    First, we'll clone the Model entity to our project. You can view the public models in the public Dataloop Github.
    You can view all publicly available models by using a Filter. Here we will use a ResNet50 model pretrained on the ImageNET dataset.
    """


def func3():
    """
    ### Run a pretrained model
    We will then "build" a model adapter to get the package code locally and create an instance of the ModelAdapter class. Then we will load the pretrained model and weights into the model adapter.
    """


def func4():
    """
    ### Predict on an item
    Now we can get an item and inference on it with the predict method and upload the annotations. If you would like to see the item and predictions, you can view it locally or you can open the item on the platform and edit it directly there.
    """


def func5():
    """
    ## Train on new dataset
    Here we will use a public dataset of sheep faces. We create a project and a dataset and upload the data with 4 labels of sheep.
    NOTE: You might need to change the location of the items, which currently points to the root of the documentation repository. If you downloaded the dtlpy documentation repo locally, this should work as is.
    """


def func6():
    """
    Now we'll run the "prepare_dataset" method. This will clone and freeze the dataset so that we'll be able to reproduce the training with the same copy of the data. The cloned dataset will be split into subsets, either filtered using DQL or as percentages. In this example, we'll use an 80/20 train validation split.

    """


def func7():
    """
    After partitioning and cloning the data, we will clone the pretrained model to have a starting point for the fine-tuning. We create an artifact where we can save the model weights. We will also indicate the model's configuration will determine some runtime configurations, such as number of epochs. In this tutorial we will train for only 2 epochs.
    """


def func8():
    """
    We'll load the new, untrained model into the adapter and prepare the local dataset to be used for training.
    """


def func9():
    """
    ## Start the training
    The package, model, and data are now prepared. We are ready to train!
    """


def func10():
    """
    ## Save the Model
    We will save the locally-trained model and upload the trained weights to the Artifact Item. This ensures that everything is on the Dataloop platform and allows other developers to use our trained model.
    """


def func11():
    """
    We can also list all Artifacts associated with this Package, and add more files that are needed to load or run the model.
    """


def func12():
    """
    ## Predict on our newly trained model
    With everything in place, we will load our model and view an item's prediction.
    """
