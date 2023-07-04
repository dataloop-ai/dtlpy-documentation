def func1():
    """
    ## Offline model training, logging metrics in Dataloop

    Models can be trained offline (i.e. locally, without connecting the model to the platform) with only model metrics being uploaded to the Dataloop platform for versioning and comparisons.  This tutorial will walk you through how to upload metrics from model training via the SDK.

    The Dataloop entities required are:
     - package
     - codebase reference
     - model (with a valid dataset ID)

    ### Create Dataloop Entities
    First you need to create a dummy package, a dummy codebase reference, and a model with a valid dataset ID. The code below shows how to do this, and remember to replace <project_name> and <dataset_id> with the appropriate strings to reference your project and dataset.

    """


def func2():
    """
    Now that you’ve created the necessary Dataloop entities, metrics can be uploaded to the platform with `model.add_log_samples` function.

    Here is an example uploading some dummy training data:

    """


def func3():
    """
    Metrics plots will appear under the “metrics” tab of your chosen model. The above code example will look like this:

    ![Screenshot of model metrics plot](../../../assets/images/model_management/tutorial_model_metrics.png)

    Once you’ve uploaded multiple model metrics, you can compare them by checking all the relevant boxes on the left that you would like to compare.

    ### List Metrics
    You can list the metrics just like any other entity in the platform - using `list` (and optional dl.Filters):

    """
