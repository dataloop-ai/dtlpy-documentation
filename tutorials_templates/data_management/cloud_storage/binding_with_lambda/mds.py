def section1():
    """
    # Create an AWS Lambda to Continuously Sync a Bucket with Dataloop's Dataset

    If you want to catch events from the AWS bucket and update the Dataloop Dataset you need to set up a Lambda.
    The Lambda will catch the AWS bucket events and will reflect them into the Dataloop Platform.

    We created the environment zip file with our SDK for python3.8. For other version or more packages try creating your own layer.
    (We used (this)[https://www.geeksforgeeks.org/how-to-install-python-packages-for-aws-lambda-layers] tutorial and the python:3.8 docker image)

    # Create the Lambda

    Create a new Lambda and copy the following code:

    """


def section2():
    """
    ## Add a Layer to the Lambda
    We have created an AWS Layer with the Dataloop SDK ready.
    After creating the lambda, select the "Add Layer" and upload the zip file downloaded from (here)[https://storage.googleapis.com/dtlpy/aws-python3.8-lambda-layer/layer.zip]

    ## Create the Bucket Events
    Go to the bucket you are using, and create the event:
    1. Go to Properties → Event notifications → Create event notification
    1. Choose a name for the Event
    1. For Event types choose: All object create events, All object delete events
    1. Destination - Lambda function → Choose from your Lambda functions → choose the function you build → SAVE

    Deploy and you're good to go!
    """
