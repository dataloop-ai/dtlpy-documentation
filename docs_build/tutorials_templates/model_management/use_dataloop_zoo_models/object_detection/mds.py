def func1():
    """
    # Training an object detection model with YOLOv5
    In this tutorial we will use the YOLOv5 Model Adapter to train and inference on custom data.

    """


def func2():
    """
    ## Create the Package and pretrained model in your project
    We start by creating the entities in our project. The model codebase is in our public github.
    """


def func3():
    """
    ### Run the pretrained Model
    We will "build" to the model adapter to get the model code locally and then create an instance of the ModelAdapter class.
    After that, we load the pretrained model into the model adapter.
    """


def func4():
    """
    Get an item and predict with upload.
    You can also open the item in the platform to view and edit annotations easily.
    """


def func5():
    """
    ## Train on new dataset
    We will use a public fruits dataset. We create a project and a dataset and upload the data with 3 labels of fruit.
    NOTE: You might need to change the location of the items (should point to the root of the documentation repository)
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
    Now we have the package, model, and data ready. We are ready to train!
    """


def func9():
    """
    ## Save the model
    We will save the locally-trained model and upload the trained weights to the Item Bucket.
    This will ensure we have everything in the Dataloop platform and everyone can use our trained model.
    """


def func10():
    """
    We can also list our bucket's content, and add more files that are needed for loading/running the model
    """


def func11():
    """
    ## Predict with on newly trained model
    We will load our model and view the predictions for some items.
    """
