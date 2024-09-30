def section1():
    """
    # Upload & Manage Annotations
    """


def section2():
    """
    ## Upload User Metadata
    To upload annotations from JSON and include the user metadata, add the parameter local_annotation_path to the dataset.items.upload function, like so: 
    """


def section2a():
    """
    ## Upload with Task and Recipe Context

    Annotation can be uploaded or edited with a context. The Recipe, Task and Assignment IDs can be add to the system metadata:
    """


def section3():
    """
    ## Convert and Upload annotations from COCO/YOLO/VOC format to Dataloop

    To convert and upload annotations from COCO/YOLO/VOC format to Dataloop format:
    1. Download the following git repository: [dtlpy-converters](https://github.com/dataloop-ai-apps/dtlpy-converters).
    2. Update and run the following script:
    """


def section4():
    """
    ## Upload Entire Directory and their Corresponding Dataloop JSON Annotations
    """


def section5():
    """
    ## Upload Annotations To Video Item
    Uploading annotations to video items needs to consider spanning between frames, and toggling visibility (occlusion). In this example, we will use the following CSV file.
    In this file there is a single 'person' box annotation that begins on frame number 20, disappears on frame number 41, reappears on frame number 51 and ends on frame number 90.

    [Video_annotations_example.CSV](https://cdn.document360.io/53f32fe9-1937-4652-8526-90c1bc78d3f8/Images/Documentation/video_annotation_example.csv)
    """


def section5a():
    """
    ## Upload Annotations In VTT Format
    The Dataloop builder support VTT files, for uploading Web Text Tracks for video transcription.
    """


def section5b():
    """
    ## Upload Audio Annotation to an Audio File
    """


def section6():
    """
    ## Set Attributes On Annotations
    
    You can set attributes on annotations in hte platform using the SDK. Since Dataloop deprecated a legacy attributes mechanism, attributes are refered to as '2.0' version and need to be set as such first.
    
    ### Free Text Attribute
    """


def section7():
    """
    ### Range Attributes (Slider in UI)
    """


def section8():
    """
    ### CheckBox Attribute (Multiple choice)
    """


def section9():
    """
    ### Radio Button Attribute (Single Choice)
    """


def section10():
    """
    ### Yes/No Attribute
    """


def section11():
    """
    ## Show Annotations Over Image
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
    To list the download annotation option use `dl.ViewAnnotationOptions`:
    1. JSON: Download json files with the Dataloop annotation format.
    2. MASK: Save a PNG image file with the RGB annotation drawn.
    3. INSTANCE: Saves a PNG with the annotation label ID as the pixel value.
    4. ANNOTATION_ON_IMAGE: Saves a PNG with the annotation drawn on top of the image.
    5. VTT: Save `subtitle` annotation type in a VTT format.
    6. OBJECT_ID: Save a PNG with the object ID as the pixel value.
    """


def section14():
    """
    NOTE: The annotation option can also be a list to download multiple options:
    """


def section15():
    """
    ## Filter by Item and/or Annotation
    * **Items filter** - download filtered items based on multiple parameters, like their directory.
    You can also download items based on different filters. Learn all about item filters [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/item_level/chapter.md/).
    * **Annotation filter** - download filtered annotations based on multiple parameters like their label.
    You can also download items annotations based on different filters, learn all about annotation filters [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/annotation_level/chapter.md/).
    This example will download items and JSONS from a dog folder of the label 'dog'.
    """


def section16():
    """
    ## Filter by Annotations
    * **Annotation filter** - download filtered annotations based on multiple parameters like their label. You can also download items annotations based on different filters, learn all about annotation filters [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/annotation_level/chapter.md/).
    """


def section17():
    """
    ## Download Annotations in COCO/YOLO/VOC Format

    * **Items filter** - download filtered items based on multiple parameters like their directory. You can also download items based on different filters, learn all about item filters [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/item_level/chapter.md/).
    * **Annotation filter** - download filtered annotations based on multiple parameters like their label. You can also download items annotations based on different filters, learn all about annotation filters [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/annotation_level/chapter.md/).
 
    This example will download COCO from a dog items folder of the label 'dog' (edit the script to change to YOLO/VOC).
    """


def section18():
    """
    ## Exporting Files with File Extension as Part of the Filename

    Files can be exported from a dataset with their file extension as part of the exported filename. The export_version param in dataset.download can be set to ExportVersion.V1 or ExportVersion.V2 to avoid duplication of files with different extensions. This allows items with the same filename and different extensions in the dataset to be saved as different items.
    * **Old functionality (V1)** – abc.jpg → annotations are saved as abc.png and the JSON is saved as abc.json 
    * **New functionality (V2)** – abc.jpg → annotations are saved as abc.jpg.png and JSON is saved as abc.jpg.json
    """


def section19():
    """
    ## Download NdArray with Numpy

    - only images that have .jpg or .png formats are supported
    - save_localy=False - means it returns a buffer
    - to_array - means it returns the buffer as an array
    """


def section20():
    """
    ## Download Json and open it without saving it to disk

    - only for .json files
    - save_localy=False means it returns a buffer
    """
