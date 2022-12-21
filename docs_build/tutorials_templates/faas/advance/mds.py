def func1():
    """
    # UI Slots
    ## Define a UI slot in the platform
    UI slots can be created for any function, making it possible to invoke the function through a button click.
    Binding functions to UI slots will enable you to manually trigger them on selected items, annotations, or tasks.

    Dataloop currently supports the following UI slots:
    1. Item as a resource:
        1. Dataset Browser
        2. Annotation Studio
    2. Annotation as a resource:
        1. Annotation Studio
    3. Task as a resource:
        1. Tasks browser

    Let’s define a UI button for the “RGB to Gray” function.
    For that, we should create a slot entity in the SDK, that can be later activated from the UI to quickly invoke functions.

    In this case, the input for the RGB function is an item, so the slot resource should be item as well (i.e. SlotDisplayScopeResource.ITEM).
    As a result, the function will be accessible in the annotations studio under "Applications" dropdown:

    """


def func2():
    """
    Once the function finishes executing, you can decide what the function outputs. Currently, 3 Post-Action outputs are available for UI slots:
    1. SlotPostActionType.DOWNLOAD - Download the output, available only for item output.
    2. SlotPostActionType.DRAW_ANNOTATION - Available only for annotation output. Draw the annotation on the item.
    3. SlotPostActionType.NO_ACTION - Take no further actions

    Additionally, you can use filters to specify which items in are eligible to be used in app (e.g. filtered by item type, item format, etc.).

    ## Update the Package and Service with the Slot

    Now you can update your package and service with the new slot you added:

    """


def func3():
    """
    ## Activate the UI slot

    To make the UI slot visible to users in the platform, you need to activate the slots:

    """


def func4():
    """
    Notice that clicking on the UI slot button will trigger the service only if it is active.

    Pause the service:
    We recommend pausing the service you created for this tutorial so it will not be triggered:

    """


def func5():
    """
    Congratulations! You have successfully created, deployed, and tested Dataloop functions!

    # Executions Control
    ## Execution Termination
    Sometimes when we run long term executions, such as model training, we need the option to terminate the execution. This is facilitated using terminate at Checkpoint.
    To stop an execution set the code checkpoints to check if this execution received a termination and if it did, raise the Termination Exception.
    This allows you to save some work that was already done before terminating.
    For example:
    """


def func6():
    """
    Each time there is a "kill_event" the service runner checks to see if this execution received a termination request.
    To kill such execution we use
    """


def func7():
    """
    ## Execution Timeout
    You can tell an execution to stop after a given number of seconds with the timeout parameter (the default time is 1 hour).
    In case a service reset, such as in timeout or service update, If there are running executions the service will wait for the execution timeout before resetting.
    The number have to be a natural number (int).
    """


def func8():
    """
    You can decide what to do to executions that have experienced a timeout. There are 2 options of timeout handling:
    1. Mark execution as failed
    2. Retry
    """


def func9():
    """
    # Using Secrets in a Function
    You can use organization integration secrets (key-value) as environment variable inside the function's env.
    First you'll need to add the integrations (UI only), then simply add the integrations' ids whe deploying the service:
    """


def func10():
    """
    Inside the service you can access the values using os package:
    """