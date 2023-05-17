def section1():
    """
    # Integrations

    If you already have your data managed and organized on a cloud storage service, such as S3, you may want to
    utilize that with Dataloop, and not upload the binaries and create duplicates.

    ### Amazon Web Services integration

    Access & Permissions - Creating an integration with AWS requires allowing dataloop specific permissions for accessing the resource

    To learn more about setting up integrations, please visit our [Dataloop documentation](https://dataloop.ai/docs/storage-s3)


    ### Create AWS Access-Key integration
    """

def section2():
    """
    ### Create AWS Cross Account integration

    Follow these steps:
    1. Create an S3 bucket on your AWS account
    2. Create an IAM policy on your AWS account
    3. Create the integration and get an IAM user from Dataloop
    To learn more about setting up integrations, please visit our [Dataloop documentation](https://dataloop.ai/docs/storage-s3)

    To create the integration and get the IAM user follow this code snippet
    """

def section3():
    """

    4. Create an IAM role that can access the bucket on your AWS account
    5. Add The IAM user to the trust relationship of the role
    To learn more about setting up integrations, please visit our [Dataloop documentation](https://dataloop.ai/docs/storage-s3)

    To update the integration and provide the IAM role ARN follow this code snippet
    """