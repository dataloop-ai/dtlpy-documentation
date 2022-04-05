def section1():
    """
    To access the filters entity click <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.filters" target="_blank">here</a>.
    ### Filter Operators
    To understand more about filter operators please click <a href="https://dataloop.ai/docs/dql-operators" target="_blank">here</a>.

    When adding a filter, several operators are available for use:

    #### Equal
    eq -> equal
    (or dl.FiltersOperation.EQUAL)

    For example, filter items from a specific folder directory.
    """


def section2():
    """
    #### Not Equal
    ne -> not equal
    (or dl.FiltersOperation.NOT_EQUAL)

    In this example, you will get all items that do not have ONLY a 'cat' label.
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>
    This Operator is a better fit for filters of a single value because, for example, this filter will return items that have both 'cat' and 'dog' labels.
    View an example of a solution for the issue in the <a href="https://docs.dataloop.ai/docs/sdk-advanced-filter#full-examples" target="_blank">full example section</a> at the bottom of the page.</div>
    """


def section3():
    """
    #### Greater Than
    gt -> greater than
    (or dl.FiltersOperation.GREATER_THAN)

    You will get items with a greater height (in pixels) than the given value in this example.
    """


def section4():
    """
    #### Less Than
    lt -> less than
    (or dl.FiltersOperation.LESS_THAN)

    You will get items with a width (in pixels) less than the given value in this example.
    """


def section5():
    """
    #### In a List
    in -> is in a list (when using this expression, values should be a list).
    (or dl.FiltersOperation.IN)
    In this example, you will get items with dog OR cat labels.
    """


def section6():
    """
    ### SDK defaults
    Filters ignore SDK defaults like hidden items and directories or note annotations as issues.
    If you wish to change this behavior, you may do the following:
    """


def section7():
    """
    #### Hidden Items and Directories
    If you wish to only show hidden items & directories in your filters use this code:
    """


def section8():
    """
    ### Delete a Filter
    """


def section9():
    """
    ### Full Examples
    #### How to filter items that were created between specific dates?
    In this example, you will get all of the items that were created in 2018.
    """


def section10():
    """
    #### How to filter items that don't have a specific label?
    In this example, you will get all items that do not have a 'cat' label AT ALL.
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>
    This filter will NOT return items that have both 'cat' and 'dog' labels.</div>
    """

def section11():
    """
    #### Exist
    The filter param FILTERS_OPERATIONS_EXISTS checks if an attribute exists. The following example checks if there is an item with user metadata:
    """
