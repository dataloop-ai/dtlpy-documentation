def section1():
    """
    ## Pagination
    ### Pages
    We use pages instead of a list when we have an object that contains a lot of information.
    
    The page object divides a large list into pages (with a default of 1000 items) in order to save time when going over the items.
    
    It is the same as we display it in the annotation platform, see example <a href="https://dataloop.ai/docs/organize-dataset#datastructuredisplay" target="_blank">here</a>.</div>

    You can redefine the number of items on a page with the page_size attribute.
    When we go over the items we use nested loops to first go to the pages and then go over the items for each page.

    ### Iterator of Items
    You can create a generator of items with different filters.

    """


def section2():
    """
    A Page entity iterator also allows reverse iteration for cases in which you want to change items during the iteration:

    """


def section3():
    """
    If you want to iterate through all items within your filter, you can also do so without going through them page by page:

    """


def section4():
    """
    If you are planning to do some process on each item, it's faster to use multi-threads (or multi-process) for parallel computation.
    The following uses ThreadPoolExecutor with 32 workers to process parallel batches of 32 items:

    """


def section5():
    """
    Lets compare the runtime to see that now the process is faster:

    """


def section6():
    """
    Visualizing the progress with tqdm progress bar:
    """

def section7():
    """
    ### Set page_size
    The following example sets the page_size to 50:
    """
