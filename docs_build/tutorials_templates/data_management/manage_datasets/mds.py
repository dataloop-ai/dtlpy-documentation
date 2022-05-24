def section1():
    """
    # Manage Datasets

    Datasets are buckets in the dataloop system that hold a collection of data items of any type, regardless of their
    storage location (on Dataloop storage or external cloud storage).

    ## Create Dataset

    You can create datasets within a project. There are no limits to the number of dataset a project can have, which
    correlates with data versioning where datasets can be cloned and merged.
    """


def section2():
    """
    ## Create Dataset With Cloud Storage Driver

    If you’ve created an integration and driver to your cloud storage, you can create a dataset connected to that driver. A
    single integration (for example: S3) can have multiple drivers (per bucket or even per folder), so you need to specify
    that.

    """


def section3():
    """

    ## Retrieve Datasets

    You can read all datasets that exist in a project, and then access the datasets by their ID (or name).

    """


def section4():
    """

    ## Create Directory

    A dataset can have multiple directories, allowing you to manage files by context, such as upload time, working batch,
    source, etc.
    """


def section5():
    """
    ## Hard-copy a Folder to Another Dataset

    You can create a clone of a folder into a new dataset, but if you want to actually move between datasets a folder with
    files that are stored in the Dataloop system, you’ll need to download the files and upload again to the destination dataset.

    """
