def section1():
    """
    # Segmentation
    ## Init Segmentation
    Each annotation init receives the coordinates for the specific type, label, and optional attributes. A binary mask should be exactly the same dimensions as the image item, with 0 for background and 1 for the annotation.


    """


def section2():
    """
    ## Create a Semantic Segmentation Annotation


    """


def section3():
    """
    ## Convert Mask to Polygon
    The Dataloop SDK includes a function to convert a semantic mask to a polygon annotation, which is often easier to edit and work with in the UI.
    The following example filters for items with semantic mask annotations, and converts them into Polygon annotations.

    """


def section4():
    """
    ## Convert Polygon to Mask
    The Dataloop SDK also includes a function to convert a Polygon annotation into semantic mask annotation.
    The following example filters for items with Polygon annotations, and converts them into semantic mask annotations.
    This script uses module CV2, please make sure it is installed.



    """


def section5():
    """
    ## Create Semantic Segmentation from Image Mask and Upload
    The following script creates a semantic mask based on RGB colors of an image item and upload them to the Dataloop platform
    Please notice that directory paths look different in OS and Linux and does not require "r" at the beginning
    Make sure to use install OpenCV package to version 3.4.8.x with the script
    **pip install opencv-python == 3 .4.8.latest**


    """


def section6():
    """
    ## Create Semantic Segmentation annotations from an Instance Mask
    The following script creates semantic segmentation annotations based on the given instance mask and
    the instance map, and then upload them to the Dataloop platform.
    Please notice that the instance map should be ordered by the mask values.

    """
