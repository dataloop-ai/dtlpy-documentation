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
    NOTE: This container should be used as the external storage for the Dataloop dataset.
    2. Go back to Function App and click create -> to create a new function
       * Choose Subscription
       * Choose your Resource group
       * Choose Function name
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

    """


def section2():
    """
    4. Deploy the code to the function app you created - For more info take a look at [azure docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration#deploy-the-project-to-azure)
    5. In VS code go to view tab -> Command Palette -> Azure Functions: Upload Local Settings
    6. Go to the Function App -> Select your function -> Configuration (Under Settings section)
           * Add the 4 secrets vars `DATASET_ID`, `DTLPY_USERNAME`, `DTLPY_PASSWORD`, `CONTAINER_NAME` (your container that want to trigger it)
                * To populate the values for the vars: `DTLPY_USERNAME`, `DTLPY_PASSWORD` you have 2 options:
                    * Option 1: Use your **registered** dataloop user and password
                    * Option 2: Create a **DataLoop Bot** on your project using this code - the bot will be used as the service account of the function


    If you choose option 2 follow these steps:
        1. Open your favorite IDE (Doesn't matter where)
        2. Open a new file
        3. Copy this code snippet and run it
        4. Use the printed values and populate the relevant vars
        NOTE: Make sure the project name is the same project where the desired upstream dataset is located

    """


def section3():
    """
    7. Go to Function App -> Select your function -> Navigate in the sidebar to the functions tab and select your function ->
    Integration -> Select the trigger -> Create Event Grid subscription
        * Event Schema -> Event Grid Schema
        * Topic Types -> Storage Account (Blob & GPv2)
        * Select your Subscription, Resource Group, Resource
        * System Topic Name -> your Event Grid Topic (if you do not have one create it)
        * Filter to Event Types -> Create and Delete
        * Endpoint Type -> Function App (Azure function)
        * Endpoint -> your function

    **NOTE:** It will take up to 5 mins when you deploy using auto upstream


    **Done! Now your storage blob will be synced with the Dataloop dataset**
    """