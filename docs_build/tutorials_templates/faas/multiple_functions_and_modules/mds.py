def func1():
    """
    # Multiple Functions and Modules
    ## Multiple Functions
    ### Create and Deploy a Package of Several Functions
    First, login to the Dataloop platform:
    """


def func2():
    """
    Let’s define the project and dataset you will work with in this tutorial.
    To create a new project and dataset:
    """


def func3():
    """
    To use an existing project and dataset:
    """


def func4():
    """
    ### Write your code
    The following code consists of two image-manipulation methods: 
    * RGB to grayscale over an image
    * CLAHE Histogram Equalization over an image - Contrast Limited Adaptive Histogram Equalization (CLAHE) to equalize images
    
    To proceed with this tutorial, copy the following code and save it as a main.py file. 
    """


def func5():
    """
    ### Define the module
    Multiple functions may be defined in a single package under a “module” entity. This way you will be able to use a single codebase for various services.
    
    Here, we will create a module containing the two functions we discussed. The “main.py” file you downloaded is defined as the module entry point. Later, you will specify its directory file path.
    """


def func6():
    """
    ### Push the package
    When you deployed the service in the previous tutorial (“Single Function”), a module and a package were automatically generated. 

    Now we will explicitly create and push the module as a package in the Dataloop FaaS library (application hub). For that, please specify the source path (src_path) of the “main.py” file you downloaded, and then run the following code:
    """


def func7():
    """
    ### Deploy a service
    Now that the package is ready, it can be deployed to the Dataloop platform as a service.
    To create a service from a package, you need to define which module the service will serve. Notice that a service can only contain a single module. All the module functions will be automatically added to the service.

    Multiple services can be deployed from a single package. Each service can get its own configuration: a different module and settings (computing resources, triggers, UI slots, etc.).

    In our example, there is only one module in the package. Let’s deploy the service:
    """


def func8():
    """
    ### Trigger the service
    Once the service is up, we can configure a trigger to automatically run the service functions. When you bind a trigger to a function, that function will execute when the trigger fires. The trigger is defined by a given time pattern or by an event in the Dataloop system.

    Event based trigger is related to a combination of resource and action. A resource can be any entity in our system (item, dataset, annotation, etc.) and the associated action will define a change in the resource that will prompt the trigger (update, create, delete). You can only have one resource per trigger.


    The resource object that triggered the function will be passed as the function's parameter (input). 

    Let’s set a trigger in the event a new item is created:
    """


def func9():
    """
    In the defined filters we specified a dataset. Once a new item is uploaded (created) in this dataset, the CLAHE function will be executed for this item. You can also add filters to specify the item type (image, video, JSON, directory, etc.) or a certain format (jpeg, jpg, WebM, etc.).

    A separate trigger must be set for each function in your service.
    Now, we will define a trigger for the second function in the module rgb2gray. Each time an item is updated, invoke the rgb2gray function:
    """


def func10():
    """
    To trigger the function only once (only on the first item update), set TriggerExecutionMode.ONCE instead of TriggerExecutionMode.ALWAYS.

    ### Execute the function
    Now we can upload (“create”) an image to our dataset to trigger the service. The function clahe_equalization will be invoked:
    """


def func11():
    """
    Remote path is optional, images will go to the main directory by default.

    To see the original item, please click [here](https://raw.githubusercontent.com/dataloop-ai/dtlpy-documentation/main/assets/images/hamster.jpg/).
    
    ### Review the function's logs
    You can review the execution log history to check that your execution succeeded:
    """


def func12():
    """
    The transformed image will be saved in your dataset. 
    Once you see in the log that the execution succeeded, you may open the item to see its transformation:
    """


def func13():
    """
    ### Pause the service:
    We recommend pausing the service you created for this tutorial so it will not be triggered:
    """


def func14():
    """
    Congratulations! You have successfully created, deployed, and tested Dataloop functions!

    ## Multiple Modules
    You can define multiple different modules in a package. A typical use-case for multiple-modules is to have a single code base that can be used by a number of services (for different applications). For example, having a single YoloV4 codebase, but creating different modules for training, inference, etc.

    When creating a service from that package, you will need to define which module the service will serve (a service can only serve a single module with all its functions). For example, to push a 2 module package, you will need to have 2 entry points, one for each module, and this is how you define the modules:

    """


def func15():
    """
    Create the package with your modules
    """


def func16():
    """
    You will pass these modules as a param to packages.push()
    After that, when you deploy the package, you will need to specify the module name:
    Note: A service can only implement one module.

    """
