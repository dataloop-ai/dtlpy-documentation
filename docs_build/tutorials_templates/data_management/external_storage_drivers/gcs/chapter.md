# Connecting Dataloop with Google Cloud Storage 🌉

Ever wondered how to connect your Google Cloud Storage (GCS) seamlessly with Dataloop? You're in the right place! Let's walk through the process step by step, from setting up your integration to automating your data sync.

## Choose Your Integration Adventure! 🎮

Before we dive into the technical stuff, let's pick the right integration path for your needs. We've got several exciting options:

### Cross Project Integration: The Team Player 🤝

Want to connect across different GCP projects? Here's your game plan:

1. 🪣 Create a Cloud Storage Bucket in your GCP kingdom
2. 👮‍♂️ Set up an IAM policy (your security badge)
3. 🔗 Create the integration and get your VIP pass (IAM user) from Dataloop

Ready to become a cross-project master? Check out our [detailed guide](https://docs.dataloop.ai/docs/cross-project-integration)!

### Private Key Integration: The Secret Agent 🕵️‍♂️

Need that extra layer of security? Here's your mission, should you choose to accept it:

1. 🪣 Create a Cloud Storage Bucket (your secure vault)
2. 👑 Create an IAM role (your security clearance)
3. 🤖 Create a Service Account (your trusted agent)
4. 🔑 Generate a Private Key (your secret decoder ring)

For the classified details, visit our [secret handbook](https://docs.dataloop.ai/docs/private-key-integration)!

## Step 1: Setting Up GCP Integration 🔗

Before we can start moving data around, we need to establish a secure connection between Dataloop and Google Cloud Platform. Let's set up the integration:

```python
import dtlpy as dl
import json

if dl.token_expired():
    dl.login()
organization = dl.organizations.get(organization_name=org_name)

# Read your GCP service account key JSON file
with open(r"C:\gcsfile.json", 'r') as f:
    gcs_json = json.load(f)
gcs_to_string = json.dumps(gcs_json)

# Create the integration
integration = organization.integrations.create(
    name='gcs-integration',
    integrations_type=dl.ExternalStorage.GCS,
    options={
        'key': '',
        'secret': '',
        'content': gcs_to_string
    }
)
```

To learn more about setting up integrations and required permissions, check out our [Dataloop documentation](https://docs.dataloop.ai/docs/storage-gcp).

## Step 2: Creating Your Storage Driver 🎯

Now that we have our integration set up, let's create a storage driver - think of it as your personal data concierge that connects your specific GCS bucket to Dataloop.

```python
import dtlpy as dl
project = dl.projects.get('<project_name>')
driver = project.drivers.create(
    name='driver_name',
    driver_type=dl.ExternalStorage.GCS,
    integration_id=integration.id,
    bucket_name='<bucket_name>',
    allow_external_delete=True,
    # Optional: If your path is gs://my-gcp-bucket/folder, use only 'folder'
    path="<folder_name>" 
)
```

Once your driver is ready, you can create a dataset:

```python
dataset = project.datasets.create(dataset_name=dataset_name, driver=driver)
# Sync the dataset
dataset.sync()
```

## Step 3: Syncing Your Data 🔄

### Manual Sync ⚡

Need to sync a specific item? You can use the same syntax as with other cloud providers:

```python
import dtlpy as dl
dl.login()
# Use the full item path in GCS context
item_path = 'external://' + '<Your_item_full_name>'
# Optional: specify a destination folder
remote_path = '/Test_Folder'
dataset = dl.datasets.get(dataset_id='your dataset id')
dataset.items.upload(local_path=item_path, remote_path=remote_path)
```

### Automatic Sync with Cloud Functions ✨

Want your Dataloop dataset to automatically stay in sync with your GCS bucket? Let's set up Google Cloud Functions!

#### Prerequisites 📋

1. A Google Cloud Platform (GCP) account ([Get started here](https://cloud.google.com/docs/get-started))
2. A GCS bucket created and ready to use
3. Basic familiarity with [Google Cloud Functions](https://cloud.google.com/functions) (optional)

#### Setting Up Your Cloud Functions 🛠️

You'll need to create two functions: one for file creation/updates and another for deletions.

![add_layer](../../../../../assets/bind_gcs/create_function.png)  
![add_layer](../../../../../assets/bind_gcs/settings.png)  

##### Function for Create/Update Events

1. Create Your Function:
   * Go to Cloud Functions and click "Create Function"
   * Basic settings:
     - Environment: 1st gen
     - Function name: Choose a name
     - Region: Select your preferred region

2. Configure the Trigger:
   * Trigger type: Cloud Storage
   * Event type: On (finalizing/creating) file in the selected bucket
   * Bucket: Choose your target bucket

3. Configure Runtime Settings:
   * Runtime: Python 3.7
   * Entry point: create_gcs
   * Add environment variables:
     - `DATASET_ID`
     - `DTLPY_USERNAME`
     - `DTLPY_PASSWORD`

4. Add Code:
   * Add to requirements.txt:
     ```
     dtlpy
     ```
   * Add this code to main.py:

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
    dataset = dl.datasets.get(
        dataset_id=dataset_id,
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

##### Function for Delete Events

Create a second function following the same steps, but with these differences:
* Event type: On (deleting) file in the selected bucket
* Entry point: delete_gcs
* Use this code:

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
    dataset = dl.datasets.get(
        dataset_id=dataset_id,
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

Need the bot credentials? Here's how to get them:

```python
import dtlpy as dl
dl.login()
project = dl.projects.get(project_name='project name')
bot = project.bots.create(name='serviceAccount', return_credentials=True)
print('🤖 Bot username:', bot.id)
print('🔑 Bot password:', bot.password)
```

## Need More Help? 🤔

For detailed GCP integration setup, check out our [comprehensive documentation](https://docs.dataloop.ai/docs/storage-gcp).

Happy data syncing! 🚀
