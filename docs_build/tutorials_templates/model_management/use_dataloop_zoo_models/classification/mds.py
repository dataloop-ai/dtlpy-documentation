def func1():
    """
    # Training a classification model with ResNet
    In this tutorial we will use the Resnet Model Adapter to inference and train on custom data.
    If you don't have the following packages, you'll need to install. The Torch Model Adapter will use them later:
    torch
    torchvision
    imgaug
    scikit-image<0.18

    """


def func2():
    """
    ## Create the Model and Pretrained Snapshot in Your Project
    We start by creating the entities in our project. The model codebase is in our public github.
    """


def func3():
    """
    ### Run Pretrained Model
    We will "build" to model adapter to get the model code locally and the create an instance of the ModelAdapter class.
    After that, we load the pretrained snapshot into the model adapter.
    """


def func4():
    """
    Get an item and predict with upload.
    You can also open the item in the platform to view and edit annotations easily.
    """


def func5():
    """
    ## Train on new dataset
    We will use a public sheep face dataset. We create a project and a dataset and upload the data with 4 labels of sheep.
    NOTE: You might need to change the location of the items (should point to the root of the documentation repository)
    """


def func6():
    """
    Now we'll run the "prepare_dataset" method. This will clone and freeze the dataset (so that we'll be able to reproduce the training and keep a snapshot of the data).
    The cloned dataset will be split into subsets (using DQL or percentage). In this examples, we'll use a 80/20 train validation split.
    After that we clone the pretrained snapshot to have a starting point for the fine-tuning.
    The snapshot's configuration will determine some runtime configurations, for instance, we will train for only 2 epochs.
    """


def func7():
    """
    We'll load the new un-trained snapshot to the adapter and prepare the training local dataset
    """


def func8():
    """
    ## Start The Train
    Now We have the model, the snapshot, and the data ready. We are ready to train.
    """


def func9():
    """
    ## Save the Snapshot
    We will save the locally-trained snapshot and upload the trained weights to the Item Bucket.
    This will ensure we have everything in the Dataloop platform and everyone can use our trained snapshot.
    """


def func10():
    """
    We can also list our bucket's content, and add more files that are needed for loading/running the snapshot
    """


def func11():
    """
    ## Predict On Our New Trained Snapshot
    We will load our snapshot and visualize some items' predictions
    """
