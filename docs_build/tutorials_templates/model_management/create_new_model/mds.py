def func1():
    """
    ## Create your own Package and Model

    You can use your own model on the platform by creating Package and Model entities, and then use a model adapter to create an API with Dataloop.

    The first thing a model adapter does is create a model adapter class. The example here inherits from dl.BaseModelAdapter, which contains all the Dataloop methods required to interact with the Package and Model. You must implement these methods in the model adapter class in order for them to work: load, save, train, predict.

     In this example, the adapter is defined in a script called "adapter_script.py" and is separate from the rest of the code on this page. This script will load a model from a saved model weights file in the root directory called 'model.pth'.

    """


def func2():
    """
    NOTE: The code above is an example for a torch model adapter. This example will NOT run if copied as-is. For working examples please refer to the examples in the Dataloop Github.

    To create our Package entity, we first need to pack our package code to a dl.ItemCodebase, retrieve the metadata, and indicate where the entry point to the package is. If you’re creating a Package with code from Git, change the codebase type to be dl.GitCodebase.

    """


def func3():
    """
    Then we can push the package and all its parts to the cloud. To change the computing configurations, see the Dataloop docs for the Instance Catalog.

    """


def func4():
    """
    Now you can create a model and upload pretrained model weights with an Artifact Item. Here, the Artfiact item is where the saved model weights are. You can upload any weights file here and name it according to the 'weights_filename' in the configuration.
    """


def func5():
    """
    Finally, build the model adapter and call one of the adapter’s methods to see that your custom model works. If you've entered a dataset_id when creating the model, you can also train the model on that dataset.
    """
