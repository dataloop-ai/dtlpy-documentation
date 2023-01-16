def func1():
    """
    ## Offline model training, online metrics logging

    Models can be trained offline with only model metrics being uploaded to the Dataloop platform.

    The Dataloop entities required are:
     - package
     - codebase reference
     - model (with a valid dataset ID)

    ### Logging metrics
    To log metrics for tracking model performance, you need to create a dummy package (with a dummy codebase reference) and model (including a valid dataset ID). Remember to replace <project_name> and <dataset_id> with the appropriate strings to reference your project and dataset.

    """


def func2():
    """
    Now that you’ve created the necessary Dataloop entities, metrics can be uploaded to the platform with `model.add_log_samples` function.

    Here is an example uploading some dummy training data:

    """


def func3():
    """
    Metrics plots will appear under the “metrics” tab of your chosen model, and will look something like this:
    ![Screenshot of model metrics plot](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/assets/images/model_management/metrics_example.png/)

    """