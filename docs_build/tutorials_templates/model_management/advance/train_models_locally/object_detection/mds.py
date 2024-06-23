def func1():
    """
    # Training an Object Detection Model with YOLOv8
    In this tutorial we will download a public model from the marketplace to inference and train on custom data locally.
    Here we will use a YOLOv8 model.

    Create a venv and install the requirements for the yolov8 package [here](https://github.com/dataloop-ai-apps/yolov8/blob/master/requirements.txt/)
    Then, import the modules required for the scripts in this tutorial.
    """


def func2():
    """
    ## Create a Project and a Dataset
    We will use a public fruits dataset. We create a project and a dataset and upload the data with 3 labels of fruit.
    NOTE: You might need to change the location of the items, which currently points to the root of the documentation repository. If you downloaded the dtlpy documentation repo locally, this should work as-is.

    """


def func3():
    """
    Now we'll add the train and validation sets to the dataset metadata:
    """


def func4():
    """
    ## Clone the Public Model Into Your Project
    We'll get and clone the public yolo pretrained model (you can view the public models in the public Dataloop Github).
    You can view all publicly available models by using a Filter. Here we will use a YOLOv8 model pretrained on the COCO dataset.

    """


def func5():
    """
    ## Train on Your Dataset
    We'll load the new, untrained model into the adapter and prepare the local dataset to be used for training.
    """


def func6():
    """
    ## Start the Training
    The package, model, and data are now prepared. We are ready to train!
    """


def func7():
    """
    We can list all Artifacts associated with this Package, and add more files that are needed to load or run the model.
    """


def func8():
    """
    ## Predict Your Newly Trained Model
    With everything in place, we will load our model and view an item's prediction.
    """
