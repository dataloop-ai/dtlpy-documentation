def section1():
    """
    Modalities are multiple layers representing the same reality/scene. For example multiple sensors for the same image/object. In the Dataloop system there’s the main item, and other items relating to it are set as modality layers, saved in its metadata.
    ## Setup
    """


def section2():
    """
    ## Set a single modality
    In the following example, Item2 is defined as a modality for the main item, item1

    """


def section3():
    """
    ## Upload multiple modalities
    Start by creating a JSON layout for your items and save it as modalities_layout.json. Use item paths for files stored locally on your machine or URLs for linked items.
    We use the dictionary key for the main item, and value will be a list of the modalities (local or URL for each item):
    """


def section4():
    """
    Use the following code to upload items and set as modalities based on the JSON you created (or any other dictionary).
    We use a Threaded pool to upload and create the modalities faster

    """


def section5():
    """
    Run the main() function to start the run
    """
