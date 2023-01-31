def section1():
    """
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
    2. Go back to Function App and click create -> to create a new function
       * Choose Subscription
       * Choose your Resource group
       * Choose Function name
       * Publish -> Code
       * Runtime stack -> Python
       * Version -> 3.10>=Version>=3.7
       NOTE when choosing python 3.7 you need to pay attention to the warning
       * Choose Region
       *  Use default values for all other options (OS and Plan ...)
       * Press next and choose your Storage account
       * Review and create

    In VScode, flow the instructions in [azure docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python) to configure your environment and deploy the function:
    1. Configure your environment
    2. Sign in to Azure
    3. Create your local project
       * Choose the directory location for your project workspace and choose Select. You should either create a new folder or choose an empty folder for the project workspace. Don't choose a project folder that is already part of a workspace.
       * In Select a template for your project's first function choose -> Azure Event Grid trigger
       * Open the code file
       * In the requirements.txt file -> add dtlpy
       * Add a function code to \_\_init\_\_.py file
       NOTE Make sure you save the file at Vscode - if not it will not be deployed to Azure

    """


def section2():
    """
    4. Deploy the code to the function app you created [azure docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration#deploy-the-project-to-azure)
    5. In VS code go to view tab -> Command Palette -> Azure Functions: Upload Local Settings
    6. Go to the Function App -> Select your function -> Configuration (Under Settings section)
           * add the 4 secrets vars DATASET_ID, DTLPY_USERNAME, DTLPY_PASSWORD, CONTAINER_NAME (your container that want to trigger it)
                * for get the DTLPY_USERNAME, DTLPY_PASSWORD you need to create a bot to your project useing this code
    """


def section3():
    """
    7. Go to Function App -> select your function -> navigate in the sidebar to the functions tab and select your function -> Integration ->
        select the trigger -> Create Event Grid subscription
        * Event Schema -> Event Grid Schema
        * Topic Types -> Storage Account (Blob & GPv2)
        * select your Subscription, Resource Group, Resource
        * System Topic Name -> your Event Grid Topic (if you do not have one create it)
        * Filter to Event Types -> Create and Delete
        * Endpoint Type -> Function App (Azure function)
        * Endpoint -> your function
    Note It will take up to 5 min when you deploy using auto upstream

    **Done! Now your storage blob will be synced with the Dataloop dataset**
    """