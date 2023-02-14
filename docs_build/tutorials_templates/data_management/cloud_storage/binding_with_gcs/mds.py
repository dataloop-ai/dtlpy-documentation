def section1():
    """
    ## Dataset Binding with Google Cloud Storage

    We will create a GCS cloud function to continuously sync a bucket with Dataloop's Dataset

    If you want to catch events from the GCS bucket and update the Dataloop Dataset you need to set up a Cloud function.
    The function will catch the GCS bucket events and will reflect them into the Dataloop Platform.

    ### Create the cloud function
    1. Create a cloud function for create event (must add the environment variables DATASET_ID, DTLPY_USERNAME and DTLPY_PASSWORD)
        To populate the values for the vars: `DTLPY_USERNAME`, `DTLPY_PASSWORD` you'll need to create a **DataLoop Bot** on your Dataloop project using the following code:
    """


def section2():
    """
    ![add_layer](../../../../assets/bind_gcs/create_function.png)
    ![add_layer](../../../../assets/bind_gcs/settings.png)

    2. runtimes: =>python37, Entry point: create_gcs (your function name)
    3. Add dtlpy to the requirements.txt file
    4. Copy the following code to the main.py file:
    """


def section3():
    """
    4. create another function for delete with delete event with this code and the same settings
    """


def section4():
    """
    Deploy and you're good to go! 
    """
