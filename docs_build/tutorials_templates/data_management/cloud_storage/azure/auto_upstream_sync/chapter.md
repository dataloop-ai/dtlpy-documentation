## Dataset Binding with Azure  
  
We will create an Azure Function App to continuously sync a blob with Dataloop's dataset  
  
If you want to catch events from the Azure blob and update the Dataloop Dataset you need to set up a blob function.  
The function will catch the blob storage events and will reflect them into the Dataloop Platform.  
  
If you are familiar with [Azure Function App](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python), you can just use our integration function below.  
  
We assume you already have an Azure account with resource group and storage account. If you don't, follow the [Azure docs](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create) and create them.  
  
### Create the Blob Function  
1. Create a Container in the created Storage account  
   * Public access level -> Container OR Blob  
NOTE: This container should be used as the external storage for the Dataloop dataset.  
2. Go back to Function App and click Create -> to create a new function  
   * Choose Subscription  
   * Choose your Resource Group  
   * Choose Function Name  
   * Publish -> Code  
   * Runtime stack -> Python  
   * Version -> 3.10 >= Version >= 3.7  
   NOTE: when choosing python 3.7 please pay attention to the AOL warning  
   * Choose Region  
   * Use default values for all other options (OS and Plan ...)  
   * Press next and choose your Storage account  
   * Review and create  
  
### Deploy your function  
In VS code, flow the instructions in [azure docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python) to configure your environment and deploy the function:  
1. Configure your environment  
2. Sign in to Azure  
3. Create your local project  
   * On VS code go to Azure panel -> workspace (bottom left panel)-> create a function  
   * Choose the directory location for your project workspace and choose Select.  
    You should either create a new folder or choose an empty folder for the project workspace.  
    Don't choose a project folder that is already part of a workspace.  
   * In Select a template for your project's first function choose -> Azure Event Grid trigger  
   * Open the code file  
   * In the requirements.txt file -> add ```dtlpy```  
   * Replace the code on \_\_init\_\_.py file with the presented code snippet  
   NOTE: Make sure you **save** the file on Vs code - If not it **will not be deployed** to Azure  
  

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
4. Deploy the code to the function app you created - For more info take a look at [azure docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration#deploy-the-project-to-azure)  
5. In VS code go to view tab -> Command Palette -> Azure Functions: Upload Local Settings  
6. Go to the Function App -> Select your function -> Configuration (Under Settings section)  
       * Add the 4 secrets vars `DATASET_ID`, `DTLPY_USERNAME`, `DTLPY_PASSWORD`, `CONTAINER_NAME` (the container to add a trigger)  
    To populate the values for the vars: `DTLPY_USERNAME`, `DTLPY_PASSWORD` you'll need to create a **DataLoop Bot** on your Dataloop project using the following code:  

```python
import dtlpy as dl
dl.login()
project = dl.projects.get(project_name='project name')
bot = project.bots.create(name='serviceAccount', return_credentials=True)
print('username: ', bot.id)
print('password: ', bot.password)
```
7. Go to Function App -> Select your function -> Navigate in the sidebar to the functions tab and select your function ->  
Integration -> Select the trigger -> Create Event Grid subscription  
    * Event Schema -> Event Grid Schema  
    * Topic Types -> Storage Account (Blob & GPv2)  
    * Select your Subscription, Resource Group, Resource  
    * System Topic Name -> your Event Grid Topic (if you do not have one create it)  
    * Filter to Event Types -> Create and Delete  
    * Endpoint Type -> Function App (Azure function)  
    * Endpoint -> your function  
  
**NOTE:** It will take up to 5 minutes when you deploy using auto upstream  
  
  
**Done! Now your storage blob will be synced with the Dataloop dataset**  
