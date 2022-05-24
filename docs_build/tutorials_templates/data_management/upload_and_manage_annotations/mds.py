def section1():
    """

    # Upload & Manage Annotations

    """


def section2():
    """
    ## Upload User Metadata
    To upload annotations from JSON and include the user metadata, add the parameter local_annotation_path to the dataset.items.upload function, like so: 
    """


def section3():
    """
    ## Convert Annotations To COCO Format

    """


def section4():
    """
    ## Upload Entire Directory and their Corresponding  Dataloop JSON Annotations

    """


def section5():
    """
    ## Upload Annotations To Video Item
    Uploading annotations to video items needs to consider spanning between frames, and toggling visibility (occlusion). In this example, we will use the following CSV file.
    In this file there is a single 'person' box annotation that begins on frame number 20, disappears on frame number 41, reappears on frame number 51 and ends on frame number 90.

    [Video_annotations_example.CSV](https://cdn.document360.io/53f32fe9-1937-4652-8526-90c1bc78d3f8/Images/Documentation/video_annotation_example.csv)

    """


def section6():
    """
    # Set Attributes On Annotations
    
    You can set attributes on annotations in hte platform using the SDK. Since Dataloop deprecated a legacy attributes mechanism, attributes are refered to as '2.0' version and need to be set as such first.
    
    ## Free Text Attribute
    """


def section7():
    """
    ## Range Attributes (Slider in UI)

    """


def section8():
    """
    ## CheckBox Attribute (Multiple choice)
    """


def section9():
    """
    ## Radio Button Attribute (Single Choice)
    """


def section10():
    """
    ## Yes/No Attribute
    """


def section11():
    """
    # Show Annotations Over Image
    After uploading items and annotations with their metadata, you might want to see some of them and perform visual validation. 
    
    To see only the annotations, use the annotation type *show* option.

    """


def section12():
    """

    To see the item itself with all annotations, use the Annotations option.

    """


def section13():
    """

    # Download Data, Annotations & Metadata
    The item ID for a specific file can be found in the platform UI - Click BROWSE for a dataset, click on the selected file, and the file information will be displayed in the right-side panel. The item ID is detailed, and can be copied in a single click.

    ## Download Items and Annotations
    Download dataset items and annotations to your computer folder in two separate folders.
    See all annotation options [here](https://dataloop.ai/docs/sdk-download#annotation-options).


    """


def section14():
    """
    ## Multiple Annotation Options
    See all annotation options [here](https://dataloop.ai/docs/sdk-download#annotation-options).

    """


def section15():
    """

    ## Filter by Item and/or Annotation
    * **Items filter** - download filtered items based on multiple parameters, like their directory.
    You can also download items based on different filters. Learn all about item filters [here](https://dataloop.ai/docs/sdk-sort-filter).
    * **Annotation filter** - download filtered annotations based on multiple parameters like their label.
    You can also download items annotations based on different filters, learn all about annotation filters [here](https://dataloop.ai/docs/sdk-sort-filter-annotation).
    This example will download items and JSONS from a dog folder of the label 'dog'.


    """


def section16():
    """

    ## Filter by Annotations
    * **Annotation filter** - download filtered annotations based on multiple parameters like their label. You can also download items annotations based on different filters, learn all about annotation filters [here](https://dataloop.ai/docs/sdk-sort-filter-annotation).


    """


def section17():
    """

    ## Download Annotations in COCO Format

    * **Items filter** - download filtered items based on multiple parameters like their directory. You can also download items based on different filters, learn all about item filters [here](https://dataloop.ai/docs/sdk-sort-filter).
    * **Annotation filter** - download filtered annotations based on multiple parameters like their label. You can also download items annotations based on different filters, learn all about annotation filters [here](https://dataloop.ai/docs/sdk-sort-filter-annotation).
 
    This example will download COCO from a dog items folder of the label 'dog'.


    """
