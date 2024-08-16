def func1():
    """
    # FaaS Example: Auto-Annotate / Pre-Annotate Service
    This tutorials demonstrates creating and deploying a service that pre-annotates an items before manual annotation work is performed, as part of active-learning process.

    ## Service Code
    Your code can perform any action you need toe execute as part of pre-annotating items for example:
    - Access a remote server/API to retrieve annotations
    - Run your algorithm or ML model as a service in Dataloop FaaS

    In this example we use a simple face detection algorithm that uses Cv2 and Caffe model

    """


def func2():
    """
    ## Define the module
    In this example, we load the model in the init method, which runs only once at deployment time, saving us time bu not loading on each execution/
    This can inputs are attributes that we want the service to include for its entire lifetime. In this case, it's the model and weights files we want the service to use and the confidence limit for accepting detections.

    """


def func3():
    """
    ## Model and weights files
    The function uses 2 files containing the model and its weights for inference. We need to have these files at the same folder as the entry point.
    To get these files please download them here.
    https://storage.googleapis.com/dtlpy/model_assets/faas-tutorial/model_weights.zip

    ## Package Requirements
    Our package's codebase uses 2 Python libraries that are not standard ones. Therefore, we need to make sure they are pre-installed before running the entry point. One way to do so is to use a custom Docker Image (information on this process can be found here. The other way is to add a requirements.txt file to the package codebase. To do so, simply add the following requirements.txt file in the same folder of the entry point (main.py):
    https://docs.dataloop.ai/docs/service-runtime#customimage
    """


def func4():
    """
    ## Push the Package
    Make sure you have the following files in one directory:
    - main.py
    - requirements.txt
    - res10_300x300_ssd_iter_140000.caffemodel
    - deploy.prototxt.txt

    Run this to push your package:
    """


def func5():
    """
    ## Deploy The  Service
    The package is now ready to be deployed as a service in the Dataloop Platform.
    Whenever executed, your package will run as a service on default instance type. Review the service configuration to configure it to your needs, for example
    - Change instance-type to use stronger instances with more memory, CPU and GPU
    - Increase auto-scaling to handle larger loads
    - Increase timeouts to allow longer execution time


    """


def func6():
    """
    ## Trigger the Service
    Once the service is deployed, we can create a trigger to run it automatically when a certain event occurs.
    In our example we trigger the face-detection service whenever an item is uploaded to the platform.
    Consider using other triggers or different ways to run you service:
    - Add the services to a FaaS-node in a pipeline, before annotation tasks
    - Use DQL trigger to run only on specific datasets, or in specific tasks
    - Run the service when an item is updated
    """


def func7():
    """
    ## Uploading Model Weights as Artifacts
    Large data files such as ML model weights can be too big to include in a package. These and other large files can be uploaded as artifact.

    """
