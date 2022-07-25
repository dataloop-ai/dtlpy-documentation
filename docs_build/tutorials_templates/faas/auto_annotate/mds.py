def func1():
    """
    ## Step-by-step: Setting up auto-annotation model
    This tutorial explains step-by-step how to upload your model to the Dataloop platform and use it for auto annotate any item

    ### Your Model
    Following this example you can use your own model, or the sample one presented below.
    It uses CV2 and Caffe for basic face detection.
    """


def func2():
    """
    ### Define the module
    In this example, we load the model in the init method.
    This method runs only once at deployment time. This can save us time by avoiding to load the model at each execution.
    The init inputs are attributes that we want the service to include for its entire lifetime.
    In this case, it's the model and weights files we want the service to use and the confidence limit of which to accept detections.

    """


def func3():
    """
    ### Weights File

    The function uses 2 files that hold the model and weight to run the detection.
    We need to have these files at the same folder as the entry point.
    To get these files please download them here.
    """

def func4():
    """
    ### Package Requirements

    Our package's codebase uses 2 Python libraries that are not standard libraries.
    Therefore, we need to make sure they are pre-installed before running the entry point.
    One way to do so is to use a custom Docker Image (information on this process can be found here.
    The other way is to add a requirements.txt file to the package codebase.
    To do so, simply add the following requirements.txt file in the same folder of the entry point (main.py):
    """

def func5():
    """
    ### Push The Package
    Now we have all our files in one place:
    - main.py
    - requirements.txt
    - res10_300x300_ssd_iter_140000.caffemodel
    - deploy.prototxt.txt

    Time to push the package:

    """

def func6():
    """
    ### Deploy A Service
    The package is now ready to be deployed to the Dataloop Platform.
    The runtime argument here is the service configuration. Concurrency=1 means that only one execution can run at a time (no parallel executions).

    """


def func7():
    """
    ### Trigger The Service
    Setting a trigger of ITEM.CREATED will set the service to run on any new item uploaded to the project.
    Additional triggers provide more options to trigger the service on various system events.

    """

def func7():
    """
    ### Model Weights As Artifacts
    When working with AI, we have the package with the model code on one hand and the weight file (the results of training the model) on the other hand.
    The model needs to load the weight file to be able to identify the data.
    When writing FaaS (Function as a Service), we create a package with our code. Since the weight file can be very large, we do not want to push such a large file into the package; therefore, we use data objects called artifacts.
    See this example how to upload model weights as artifacts.

    """
