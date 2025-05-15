# Connecting Dataloop with Azure Blob Storage 🌉

Ever wondered how to connect your Azure Blob Storage seamlessly with Dataloop? You're in the right place! Let's walk through the process step by step, from setting up your integration to automating your data sync.

## Step 1: Setting Up Azure Integration 🔗

Before we can start moving data around, we need to establish a secure connection between Dataloop and Azure. Let's set up the integration:

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
organization = dl.organizations.get(organization_name='my-org')
organization.integrations.create(
    name='azure-integration',
    integrations_type=dl.ExternalStorage.AZUREBLOB,
    options={
        'key': 'my_key',
        'secret': 'my_secret',
        'clientId': 'my_clientId',
        'tenantId': 'my_tenantId'
    }
)
```

To learn more about setting up integrations and required permissions, check out our [Dataloop documentation](https://docs.dataloop.ai/docs/azure-cloud-storage).

## Step 2: Creating Your Storage Driver 🎯

Now that we have our integration set up, let's create a storage driver - think of it as your personal data concierge that connects your specific Azure container to Dataloop.

```python
import dtlpy as dl
project = dl.projects.get('project_name')
driver = project.drivers.create(
    name='driver_name',
    driver_type=dl.ExternalStorage.AZUREBLOB,
    integration_id='integration_id',
    bucket_name='container_name',  # In Azure, this is your container name
    allow_external_delete=True,
    path=""  # Optional: specify a path within the container
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

Need to sync a specific item? Here's your shortcut:

```python
import dtlpy as dl
dl.login()
# Use the full item path in Azure context
item_path = 'external://' + '<Your_item_full_name>'
# Optional: specify a destination folder
remote_path = '/Test_Folder'
dataset = dl.datasets.get(dataset_id='your dataset id')
dataset.items.upload(local_path=item_path, remote_path=remote_path)
```

### Automatic Sync with Azure Function ✨

Want your Dataloop dataset to automatically stay in sync with your Azure Blob container? Let's set up an Azure Function!

#### Prerequisites 📋

1. An Azure account with an active subscription
2. A resource group and storage account ([Create one if needed](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create))
3. Familiarity with [Azure Function App](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python) (optional)

#### Setting Up Your Azure Function 🛠️

1. Create a Container in your Storage Account:
   * Set Public access level to Container OR Blob
   * Note: This container will be your external storage for the Dataloop dataset

2. Create a new Function App:
   * Choose your Subscription and Resource Group
   * Pick a Function Name
   * Select:
     - Publish -> Code
     - Runtime stack -> Python (Version 3.7-3.10)
     - Region -> Your preferred region
     * Use defaults for OS and Plan
   * Link to your Storage account
   * Review and create

3. Deploy Your Function:
   * In VS Code:
     a. Configure your environment
     b. Sign in to Azure
     c. Create local project:
        - Go to Azure panel -> workspace -> create function
        - Choose directory location
        - Select Azure Event Grid trigger template
        - Add `dtlpy` to requirements.txt
        - Replace \_\_init\_\_.py with this code:

```python
import azure.functions as func
import os
os.environ["DATALOOP_PATH"] = "/tmp"
import dtlpy as dl

dataset_id = os.environ.get('DATASET_ID')
dtlpy_username = os.environ.get('DTLPY_USERNAME')
dtlpy_password = os.environ.get('DTLPY_PASSWORD')
container_name = os.environ.get('CONTAINER_NAME')

def main(event: func.EventGridEvent):
    url = event.get_json()['url']
    if container_name in url:
        dl.login_m2m(email=dtlpy_username, password=dtlpy_password)
        dataset = dl.datasets.get(dataset_id=dataset_id)
        driver_path = dl.drivers.get(driver_id=dataset.driver).path
        # remove th Container name from the path
        file_name_to_upload = url.split(container_name)[1]
        if driver_path == '/':
            driver_path = None
        if driver_path is not None and driver_path not in url:
            return
        if driver_path:
            if not driver_path.startswith("/"):
                driver_path = "/" + driver_path
            remote_path = file_name_to_upload.replace(driver_path, '')
        else:
            remote_path = file_name_to_upload
        if 'BlobCreated' in event.event_type:
            file_name = 'external:/' + file_name_to_upload
            dataset.items.upload(local_path=file_name, remote_path=os.path.dirname(remote_path))
        else:
            dataset.items.delete(filename=remote_path)
```

4. Configure Your Function:
   * Deploy the code ([Azure docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration#deploy-the-project-to-azure))
   * Upload local settings: View -> Command Palette -> "Azure Functions: Upload Local Settings"
   * Add environment variables:
     - `DATASET_ID`
     - `DTLPY_USERNAME`
     - `DTLPY_PASSWORD`
     - `CONTAINER_NAME`

Need those credentials? Here's how to get them:

```python
import dtlpy as dl
dl.login()
project = dl.projects.get(project_name='project name')
bot = project.bots.create(name='serviceAccount', return_credentials=True)
print('🤖 Bot username:', bot.id)
print('🔑 Bot password:', bot.password)
```

5. Set Up Event Grid Subscription:
   * Go to your function in Function App
   * Navigate to Integration -> Select trigger -> Create Event Grid subscription
   * Configure:
     - Event Schema -> Event Grid Schema
     - Topic Types -> Storage Account (Blob & GPv2)
     - Select your Subscription, Resource Group, Resource
     - System Topic Name -> your Event Grid Topic
     - Filter to Event Types -> Create and Delete
     - Endpoint Type -> Function App
     - Endpoint -> your function

**Note:** Allow up to 5 minutes for the automatic sync to become active.

## Need More Help? 🤔

For detailed Azure integration setup, check out our [comprehensive documentation](https://docs.dataloop.ai/docs/azure-cloud-storage).

Happy data syncing! 🚀
