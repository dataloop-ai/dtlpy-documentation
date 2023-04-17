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

```python
import dtlpy as dl
dl.login()
project = dl.projects.get(project_name='project name')
bot = project.bots.create(name='serviceAccount', return_credentials=True)
print('username: ', bot.id)
print('password: ', bot.password)
```
6. Code  
   * Runtimes: => python 3.7  
   * Entry point: Your function name from the code snippet (default `create_gcs`)  
   * In the requirements.txt file -> add `dtlpy`  
   * Copy the following code to the main.py file:  

```python
import os
os.environ["DATALOOP_PATH"] = "/tmp"
import dtlpy as dl
dataset_id = os.environ.get('DATASET_ID')
dtlpy_username = os.environ.get('DTLPY_USERNAME')
dtlpy_password = os.environ.get('DTLPY_PASSWORD')
def create_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    dl.login_m2m(email=dtlpy_username, password=dtlpy_password)
    dataset = dl.datasets.get(dataset_id=dataset_id,
                              fetch=False  # to avoid GET the dataset each time
                              )
    driver_path = dl.drivers.get(driver_id=dataset.driver).path
    remote_path = None
    if driver_path == '/':
        driver_path = None
    if driver_path is not None and driver_path not in file['name']:
        return
    if driver_path:
        remote_path = file['name'].replace(driver_path, '')
    file_name = 'external://' + file['name']
    dataset.items.upload(local_path=file_name, remote_path=remote_path)
```
* Click -> Deploy  
  
  
7. Add another function for delete actions  
   * Repeat the process  
   * Create another function for `delete` with `delete event` with the following code and the same settings  
   * Trigger -> Event type ->  On (deleting) file in the selected bucket  
   * Entry point: Your function name from the code snippet (default `delete_gcs`)  

```python
import os
os.environ["DATALOOP_PATH"] = "/tmp"
import dtlpy as dl
dataset_id = os.environ.get('DATASET_ID')
dtlpy_username = os.environ.get('DTLPY_USERNAME')
dtlpy_password = os.environ.get('DTLPY_PASSWORD')
def delete_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    dl.login_m2m(email=dtlpy_username, password=dtlpy_password)
    dataset = dl.datasets.get(dataset_id=dataset_id,
                              fetch=False  # to avoid GET the dataset each time
                              )
    driver_path = dl.drivers.get(driver_id=dataset.driver).path
    if driver_path == '/':
        driver_path = None
    if driver_path is not None and driver_path not in file['name']:
        return
    if driver_path:
        remote_path = file['name'].replace(driver_path, '')
    else:
        remote_path = file['name']
    dataset.items.delete(filename=remote_path)
```
### You're good to go!  
  
  
  
#### For pictures examples:  
  
![add_layer](../../../../assets/bind_gcs/create_function.png)  
![add_layer](../../../../assets/bind_gcs/settings.png)  
