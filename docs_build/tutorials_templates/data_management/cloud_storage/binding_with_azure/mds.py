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
    2. Go back to Resource group and click Create -> Function App
       * Choose Subscription, your Resource group, Name and Region
       * Publish -> Code
       * Runtime stack -> Python
       * Version -> <=3.7

    In VScode, flow the instructions in [azure docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python) to configure your environment and deploy the function:
    1. Configure your environment
    2. Sign in to Azure
    3. Create your local project
       * in Select a template for your project's first function choose -> Azure Blob Storage trigger
       * in Storage account select your Storage account
       * in Resource group select your Resource group
       * Set the 'Create new Azure Blob Storage trigger' to your container name (used in the Dataloop platform)
        ![add_layer](../../../../assets/bind_azure/trigger_dataset.png)
       * open the code file
       * add dtlpy to the requirements.txt file
       * add **"disabled": false** to the function.json file
       * add a function code to \_\_init\_\_.py file

    """


def section2():
    """
    4. Deploy the code to the function app you created.
    5. In VS code go to view tab -> Command Palette -> Azure Functions: Upload Local Settings
    6. go to the Function App -> Select your function -> Configuration (Under Settings section)
           * add the 3 secrets vars DATASET_ID, DTLPY_USERNAME, DTLPY_PASSWORD

    **Done! Now your storage blob will be sync with the Dataloop dataset**
    """
