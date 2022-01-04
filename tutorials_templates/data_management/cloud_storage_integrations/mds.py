def section1():
    """
    # Connect Cloud Storage


    If you already have your data managed and organized on a cloud storage service, such as GCS/S3/Azure, you may want to
    utilize that with Dataloop, and not upload the binaries and create duplicates.

    ## Cloud Storage Integration

    Access & Permissions Creating an integration with GCS/S2/Azure cloud requires adding a key/secret with the following
    permissions:

    List (Mandatory) - allowing Dataloop to list all of the items in the storage. Get (Mandatory) - get the items and
    perform pre-process functionalities like thumbnails, item info etc. Put / Write (Mandatory) - lets you upload your items
    directly to the external storage from the Dataloop platform. Delete - lets you delete your items directly from the
    external storage using the Dataloop platform.

    ## Create Integration With GCS

    ### Creating an integration GCS requires having JSON file with GCS configuration
    """


def section2():
    """
    ### Create Integration With S3
    """


def section3():
    """
    ### Create Integration With Azure
    """


def section4():
    """
    ## Storage Driver

    Once you have an integration, you can set up a driver, which adds a specific bucket (and optionally with a specific
    path/folder) as a storage resource.

    ## Create Drivers in the Platform (browser)
    """
