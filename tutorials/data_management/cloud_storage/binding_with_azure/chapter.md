## Dataset Binding with Azure  
  
We will create an Azure Function App to continuously sync a blob with Dataloop's dataset  
  
If you want to catch events from the Azure blob and update the Dataloop Dataset you need to set up a blob function.  
The function will catch the blob storage events and will reflect them into the Dataloop Platform.  
  
If you are familiar with [Azure Function App](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python), you can just use our integration function below.  
  
We assume you already have an Azure account with resource group and storage account. If you don't, follow the [Azure docs](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create) and create them.  
  
### Create the Blob Function  
1. Create a Container in the created Storage account  
   * Public access level -> Container OR Blob  
NOTE this container should be used as the external storage for the Dataloop dataset.  
2. Go back to Resource group and click Create -> Function App  
   * Choose Subscription, your Resource group, Name and Region  
   * Publish -> Code  
   * Runtime stack -> Python  
   * Version -> <=3.7  
   * press next and choose your Storage account  
  
In VScode, flow the instructions in [azure docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python) to configure your environment and deploy the function:  
1. Configure your environment  
2. Sign in to Azure  
3. Create your local project  
   * in Select a template for your project's first function choose -> Azure Event Grid trigger  
   * open the code file  
   * add dtlpy to the requirements.txt file  
   * add a function code to \_\_init\_\_.py file  
  

```python
import azure.functions as func
import dtlpy as dl
import os
os.environ["DATALOOP_PATH"] = "/tmp"
dataset_id = os.environ.get('DATASET_ID')
dtlpy_username = os.environ.get('DTLPY_USERNAME')
dtlpy_password = os.environ.get('DTLPY_PASSWORD')
container_name = os.environ.get('CONTAINER_NAME')
def main(event: func.EventGridEvent):
    url = event.get_json()['url']
    if container_name in url:
        dl.login_m2m(email=dtlpy_username, password=dtlpy_password)
        dataset = dl.datasets.get(dataset_id=dataset_id,
                                  fetch=False  # to avoid GET the dataset each time
                                  )
        # remove th Container name from the path
        file_name = url.split(container_name)[1]
        if 'BlobCreated' in event.event_type:
            file_name = 'external:/' + file_name
            dataset.items.upload(local_path=file_name)
        else:
            dataset.items.delete(filename=file_name)
```
4. Deploy the code to the function app you created.  
5. In VS code go to view tab -> Command Palette -> Azure Functions: Upload Local Settings  
6. Go to the Function App -> Select your function -> Configuration (Under Settings section)  
       * add the 4 secrets vars DATASET_ID, DTLPY_USERNAME, DTLPY_PASSWORD, CONTAINER_NAME (your container that want to trigger it)  
7. Go to Function App -> select your function -> go to Functions tag and select your function -> Integration ->  
    select the trigger -> Create Event Grid subscription  
    * Event Schema -> Event Grid Schema  
    * Topic Types -> Storage Account (Blob & GPv2)  
    * select your Subscription, Resource Group, Resource  
    * System Topic Name -> your Event Grid Topic (if you do not have one create it)  
    * Filter to Event Types -> Create and Delete  
    * Endpoint Type -> Function App  
    * Endpoint -> your function  
  
**Done! Now your storage blob will be synced with the Dataloop dataset**  
