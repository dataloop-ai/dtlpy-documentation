def func1():
    """
    # Training an object detection model with YOLOv5
    In this tutorial we will download a public model from the AI library to inference and train on custom data locally.
    Here we will use a YOLOv5 model.

    Start by installing the following packages if you don't have them installed already. The model adapter will use them later.
    torch
    torchvision
    imgaug
    scikit-image<0.18
    """


def func2():
    """
    ## Create the Package and pretrained model in your project
        First, we create the Model entity for our project. You can view the public models in the public Dataloop Github.
    You can view all publicly available models by using a Filter. Here we will use a YOLOv5 model pretrained on the COCO dataset.

    """


def func3():
    """
    ### Run the pretrained Model
    We will "build" to the model adapter to get the model code locally and then create an instance of the ModelAdapter class.
    After that, we load the pretrained model into the model adapter.
    """


def func4():
    """
    ### Predict on an item
    Now we can get an item and inference on it with the predict method and upload the annotations. If you would like to see the item and predictions, you can open the item on the platform and edit it directly there.
    """


def func5():
    """
    ## Train on new dataset
    We will use a public fruits dataset. We create a project and a dataset and upload the data with 3 labels of fruit.
    NOTE: You might need to change the location of the items, which currently points to the root of the documentation repository. If you downloaded the dtlpy documentation repo locally, this should work as-is.
    """


def func6():
    """
    Now we'll run the "prepare_dataset" method. This will clone and freeze the dataset (so that we'll be able to reproduce the training and keep a snapshot of the data).
    The cloned dataset will be split into subsets (using DQL or percentage). In this example, we'll use a 80/20 train validation split.
    After that we clone the pretrained model to have a starting point for the fine-tuning.
    The model's configuration will determine some runtime configurations, for instance, we will train for only 2 epochs.
    """


def func7():
    """
    We'll load the new un-trained model to the adapter and prepare the training local dataset
    """


def func8():
    """
    ## Start the training
    The package, model, and data are now prepared. We are ready to train!
    """


def func9():
    """
    ## Save the model
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
