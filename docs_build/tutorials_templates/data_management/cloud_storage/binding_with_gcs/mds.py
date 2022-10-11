def section1():
    """
    ## Dataset Binding with Google Cloud Storage

    We will create a GCS cloud function to continuously sync a bucket with Dataloop's Dataset

    If you want to catch events from the GCS bucket and update the Dataloop Dataset you need to set up a Cloud function.
    The function will catch the GCS bucket events and will reflect them into the Dataloop Platform.

    ### Create the cloud function
    1. Create a cloud function for create event (must add the environment variables DATASET_ID, DTLPY_USERNAME and DTLPY_PASSWORD)
    ![add_layer](../../../../assets/bind_gcs/create_function.png)
    ![add_layer](../../../../assets/bind_gcs/settings.png)

    2. add dtlpy to the requirements.txt
    3. Copy the following code to the main file:
    """


def section2():
    """
    4. create another function for delete with delete event with this code
    """


def section3():
    """
    Deploy and you're good to go! 
    """
