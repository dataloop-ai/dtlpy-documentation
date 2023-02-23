def section1():
    """
    ## Dataset Binding with Google Cloud Storage

    We will create a GCP cloud function to continuously sync a bucket with Dataloop's Dataset

    If you want to catch events from the GCS bucket and update the Dataloop Dataset you need to set up a Cloud function.
    The function will catch the GCS bucket events and will reflect them into the Dataloop Platform.

    If you are familiar with [GCP Cloud Functions](https://cloud.google.com/functions), you can just use our integration function below.

    We assume you already have a GCP account. If you don't, follow the [GCP docs](https://cloud.google.com/docs/get-started) and create it.

    ### Create the Cloud Function
    1. Create a GCS bucket

        NOTE: This bucket should be used as the external storage for the Dataloop dataset.

    2. Go to Cloud Functions and click Create Function -> to create a new function
    3. Basic
       * Environment -> 1st gen Subscription
       * Choose Function Name
       * Choose the function region
    4. Trigger
       * Trigger type -> Cloud Storage
       * Event type ->  On (finalizing/creating) file in the selected bucket
       * Bucket -> Choose the bucket you would like allow auto sync with Dataloop
       * Click Save
    5. Runtime, build, connections and security settings
       * Choose the Runtime tab
       * Runtime environment variable -> Add variable
       * Add the 3 environment variables `DATASET_ID`, `DTLPY_USERNAME` and `DTLPY_PASSWORD`
         * To populate the values for the vars: `DTLPY_USERNAME`, `DTLPY_PASSWORD` you'll need to create a **DataLoop Bot** on your Dataloop project using the following code:
        * The output:
          * username -> `DTLPY_USERNAME`
          * password -> `DTLPY_PASSWORD`
        * After adding all environment variables -> Next
    """


def section2():
    """
    6. Code
       * Runtimes: => python 3.7
       * Entry point: Your function name from the code snippet (default `create_gcs`)
       * In the requirements.txt file -> add `dtlpy`
       * Copy the following code to the main.py file:
    """


def section3():
    """
    * Click -> Deploy


    7. Add another function for delete actions
       * Repeat the process
       * Create another function for `delete` with `delete event` with the following code and the same settings
       * Trigger -> Event type ->  On (deleting) file in the selected bucket
       * Entry point: Your function name from the code snippet (default `delete_gcs`)
    """


def section4():
    """
    ### You're good to go!



    #### For pictures examples:

    ![add_layer](../../../../assets/bind_gcs/create_function.png)
    ![add_layer](../../../../assets/bind_gcs/settings.png)
    """
