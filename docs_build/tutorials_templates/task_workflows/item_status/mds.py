def func1():
    """
    ## Item Status
    To flag for finishing work on an item in a task, the worker assigns a status to the item.
    The Dataloop system has default statuses, as well as the option to add custom statuses
    Default statuses for annotation tasks: COMPLETE and DISCARD
    Default statuses for QA tasks: APPROVE and DISCARD

    ### 1. Set status on an item in task
    """


def func2():
    """
    ### 2. Set status on multiple items
    #### 1. using dataset and filter (this way recommended of the items is not in the same task and items that include in only one task)
   """


def func3():
    """
    #### 2. use task entity (this way recommended for items in the same task)
   """


def func4():
    """
    ### 3. Clear status from an item (no-status)
    Clearing a status from an item will make it available again for work in the respective task, and the worker (annotator)
    will see the item in the assignment (either QA or annotations).
    """


def func5():
    """
    ### 4. Add task statuses
    """


def func6():
    """
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>
    Changing the statuses in the task doesn't change the status on any items that already received a status.
    """
