def section1():
    """
    # Cloud Storage
    ## External Storage Dataset

    If you already have your data managed and organized on a cloud storage service, such as GCS/S3/Azure, you may want to
    utilize that with Dataloop, and not upload the binaries and create duplicates.

    ### Cloud Storage Integration

    Access & Permissions - Creating an integration with GCS/S2/Azure cloud requires adding a key/secret with the following
    permissions:

    List (Mandatory) - allowing Dataloop to list all of the items in the storage.
    Get (Mandatory) - get the items and perform pre-process functionalities like thumbnails, item info etc.
    Put / Write (Mandatory) - lets you upload your items
    directly to the external storage from the Dataloop platform.
    Delete - lets you delete your items directly from the external storage using the Dataloop platform.

    ### Create Integration With GCS

    ### Creating an integration GCS requires having JSON file with GCS configuration.
    """


def section2():
    """
    ### Create Integration With S3
    """


def section3():
    """
    ### Create Integration With Azure
    """


def section4():
    """
    ### Storage Driver

    Once you have an integration, you can set up a driver, which adds a specific bucket (and optionally with a specific
    path/folder) as a storage resource.

    ### Create Drivers in the Platform (browser)
    """


def section5():
    """
    Once the integration and drivers are ready, you can create a Dataloop Datsaset and sync all the data:
    """


def section6():
    """
    ## Create an AWS Lambda to Continuously Sync a Bucket with Dataloop's Dataset

    If you want to catch events from the AWS bucket and update the Dataloop Dataset you need to set up a Lambda.
    The Lambda will catch the AWS bucket events and will reflect them into the Dataloop Platform.

    We have prepared an environment zip file with our SDK for python3.8 so you don't need to create anything else to use dtlpy in the lambda.

    NOTE: For any other custom use (e.g other python version or more packages) try creating your own layer (We used [this](https://www.geeksforgeeks.org/how-to-install-python-packages-for-aws-lambda-layers) tutorial and the python:3.8 docker image).

    ### Create the Lambda
    1. Create a new Lambda
    2. The default timeout is 3[s] so we'll need to change to 1[m]:
        Configuration → General configuration → Edit → Timeout
    3. Copy the following code:
    """


def section7():
    """
    ### Add a Layer to the Lambda
    We have created an AWS Layer with the Dataloop SDK ready. Click [here](https://storage.googleapis.com/dtlpy/aws-python3.8-lambda-layer/layer.zip) to download the zip file.
    Because the layer's size is larger than 50MB you cannot use it directly (AWS restrictions), but need to upload it to a bucket first.
    Once uploaded, create a new layer for the dtlpy env:
    1. Go to the layers screen and "click Add Layer".
    ![add_layer](../../../assets/aws-lambda-screenshots/create_layer.png)
    2. Choose a name (dtlpy-env).
    3. Use the link to the bucket layer.zip.
    4. Select the env (x86_64, python3.8).
    5. Click "Create" and the bottom on the page.

    Go back to your lambda and add the layer:
    1. Select the "Add Layer".
    ![add_layer](../../../assets/aws-lambda-screenshots/add_layer.png)
    2. Choose "Custom layer" and select the Layer you've added and the version.
    3. click "Add" at the bottom.

    ### Create the Bucket Events
    Go to the bucket you are using, and create the event:
    1. Go to Properties → Event notifications → Create event notification
    1. Choose a name for the Event
    1. For Event types choose: All object create events, All object delete events
    1. Destination - Lambda function → Choose from your Lambda functions → choose the function you build → SAVE

    Deploy and you're good to go!
    """
