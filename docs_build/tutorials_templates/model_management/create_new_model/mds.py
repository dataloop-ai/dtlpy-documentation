def func1():
    """
    ## Create your own model

    You can use your own model to use on the platform by creating Package and Model entities, and then use a model adapter to create an API with Dataloop.

    In this tutorial you will learn how to create a basic model adapter to be able to inference with a pretrained model and how to fine-tune a pretrained model with your custom dataset.


    ### Inference from a pre-trained model

    To use a pretrained model to inference on a new item, you will create a model adapter, push the package, upload the weights as an artifact, and create the model entity.


    #### Create a model adapter

    In the example code below, the adapter is defined in a script saved as "adapter_script.py". The SimpleModelAdapter class inherits from dl.BaseModelAdapter, which contains all the Dataloop methods required to interact with the Package and Model, as well as some helper functions that make it easier to use Dataloop entities (e.g. predict_items, predict_datasets).

    The minimum required functions to implement for a model to inference are _load_ and _predict_.

    “Load” will load a model from a saved model weights file.  If the model is instantiated with a model entity (as it is here), the load function is expected to input the local path for the weights file.

    If the weights file is a link, it can be uploaded as a LinkArtifact entity during model creation. If the file is saved locally, enter the appropriate name in the configurations (e.g. default_configuration=’weights_filename’ : ‘model.pth’). Helper functions in the BaseModelAdapter will download the weights file locally and load it based on the name listed here.

    “Predict” is where the model will do its inference, and the predict function expects input images as ndarrays, and returns a list of dl.AnnotationCollection entities.


    """


def func2():
    """
    Please see an example [here](https://github.com/dataloop-ai/yolov5/blob/master/dataloop/model_adapter.py) (for YOLOv5) in Github of a working model adapter and see how to construct Annotation Collections.

    #### Push the package

    To create our Package entity, we first need to retrieve the metadata and indicate where the entry point to the package is within the codebase. If you’re creating a Package with code from Git, change the codebase type to be dl.GitCodebase. If the code is somewhere other than the root directory, you can pack the codebase with project.codebases.pack(directory=’<path to local dir>’).

    """


def func3():
    """
    Then we can push the package and all its components to the cloud. To change the service configurations, see the documentation on [service types](https://dataloop.ai/docs/service-runtime).

    """


def func4():
    """
    #### Upload artifacts and create the model

      Now you can create a model and upload pretrained model weights with an Artifact Item. Here, the Artifact item will be uploaded with the file containing the model weights. You can upload any weights file here and use the artifact filename to update the ```weights_filename``` field in the model configuration.
  

    """


def func5():
    """
    To deploy a model, its status must be set to trained so you can deploy a model by updating the status to trained and then deploy it.

    """

def func6():
    """
    ### Checking that your model works

    #### Via the UI

    You should now be able to see the model in the “Deployed” tab. After clicking on your model, you should see a “Test” tab where you can drag and drop an image, click “Test” and see the results of your model prediction.

    ![Screenshot of deployed model test tab](../../../assets/images/model_management/test_tab.png)

    #### Via the SDK

    To test whether your function was successfully uploaded and deployed onto the platform, you can use the `model.predict()` function to predict on a list of item IDs. The function will return an Execution entity, which you can use to check the status of the prediction execution.

    """

def func7():
    """
    If you encounter errors, you will need to look at the logs to see where the error occurred.  Go to "Model Management", under the "Deployed" tab, click on the number in the "Executions" column for the appropriate model, and then click on the "Execution" log icon on the right side of the screen (the paper icon). Here you can see the output of the cloud machine. You can also access this page via the "Application Hub", under "Executions".
    """