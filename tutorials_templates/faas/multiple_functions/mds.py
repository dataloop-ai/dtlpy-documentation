def func1():
    """
    # Create and Deploy a package of several functions

    ## Write your code
    The following code consists of two image-manipulation methods:
    1. RGB to grayscale over an image
    1. Histogram equalization over an image

    You can either download it as a Python file from here main.py or copy it from our Git repository

    """


def func2():
    """
    ## Define the module
    You can define multiple different modules in a package. One of the incentives is to have a single code base that can be used by a number of services (for different applications).

    When creating a service from that package, you will need to define which module the service will serve (a service can only serve a single module with all its functions)
    """


def func3():
    """
    ## Push the package
    Now we have all our files in one place and we can push the package:

    """


def func4():
    """
    ## Deploy a service
    The package is now ready to be deployed to the Dataloop Platform:
    """


def func5():
    """
    ## Trigger the service
    Once the service is up, we can configure a trigger to automatically run the image manipulation functions whenever a given criterion is met.
    Let’s set the following trigger: “an item is uploaded to the platform”

    """


def func6():
    """
    ## Execute the function
    Now we can upload an image to a dataset to trigger our service:
    """


def func7():
    """
    ## Review the function's logs
    We can also review the execution logs history:
    """


def func8():
    """
    ## Add a slot UI of the function to the UI platform

    Assigning a function to UI slots creates a button in the Dataloop platform, allowing users to quickly
    invoke the FaaS function when needed, in the dataset browser or studio.

    To define a slot that will be displayed in the image studio, let's run this:

    """


def func9():
    """
    Now we should update our package and service with the slot:
    """


def func10():
    """
    🎉 Success!
    You have successfully created, deployed, tested, and viewed logs of Dataloop Functions!

    """
