def func1():
    """
# Working with Dataloop SDK
These SDK documents contain everything you need to know about the Dataloop SDK. Information is laid out in the following way:
Entities- contains information about the various entities and their related functions/operations and data. For example for “Item” entities - Download, Update (e.g. update its metadata), or update its status in task.
Repositories- A collection of entities, which are usually queried (e.g. using a filter), or referred to (for example all Items in a Dataset entity). It allows performing bulk operations (for example Delete all items), or addressing each entity within the repository (for example every Item in an Items collection).
Pagination - We use pages instead of a list when we have an object that contains a lot of information. The page object divides a large list into pages (with a default of 1000 items) in order to save time when going over the entries. You can redefine the number of entries per page with the 'page_size' attribute.
When going over all entries in a page out of multiple pages, we use nested loops to first go to the pages and then go over the entities for each page.

Example 1 - populating pages with filter results and iterating through items.

"""


def func2():
    """
    Example 2 - A Page entity iterator also allows reverse iteration for cases in which you want to change items during the iteration:
    """


def func3():
    """
    Example 3 - If you want to iterate through all items within your filter, you can also do so without going through them page by page:
    """


def func4():
    """
    Example 4 -  Iterator of Annotations
    """