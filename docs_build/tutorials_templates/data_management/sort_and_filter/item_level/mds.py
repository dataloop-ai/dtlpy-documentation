def section1():
    """
    To access the filters entity click <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.filters" target="_blank">here</a>.
    # The Dataloop Query Language - DQL
    Using The <a href="https://docs.dataloop.ai/docs/api-dql" target="_blank">Dataloop Query Language</a>, you may navigate through massive amounts of data.

    You can *filter*, *sort*, and *update* your metadata with it.

    ## Filters
    Using filters, you can filter items and get a generator of the filtered items. The filters entity is used to build such filters.

    ### Filters - Field & Value
    Filter your items or annotations using the parameters in the JSON code that represent its data within our system.
    Access your item/annotation JSON using `to_json()`.
    #### Field
    Field refers to the attributes you filter by.
    
    For example, "dir" would be used if you wish to filter items by their folder/directory.

    #### Value
    Value refers to the input by which you want to filter.
    For example, `/new_folder` can be the directory/folder name where the items you wish to filter are located.
    ### Sort - Field & Value
    #### Field
    Field refers to the field you sort your items/annotations list by.
    For example, if you sort by filename, you will get the item list sorted in alphabetical order by filename.
    See the full list of the available fields <a href="https://docs.dataloop.ai/docs/api-dql" target="_blank">here</a>.
    #### Value
    Value refers to the list order direction. Either ascending or descending.

    ## Filter Items
    Filter items by the item's JSON fields.
    In this example, you will get all annotated items in a dataset sorted by the filename.
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>
    See all of the items iterator options on the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/pagination/chapter.md#iterator-of-items" target="_blank">Iterator of Items</a> page.</div>

    """


def section2():
    """
    ## Filter Items by the Items' Annotations
    <code>add_join</code> - filter items by the items' annotations JSON fields. For example, filter only items with 'box' annotations.
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>
    See all of the items iterator options on the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/pagination/chapter.md#iterator-of-items" target="_blank">Iterator of Items</a> page.</div>

    """


def section3():
    """
    ## Filters Method - "Or" and "And"
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Filters Operators</b><br>
    For more advanced filters operators visit the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.md" target="_blank">Advanced SDK Filters</a> page.</div>
    
    ### And
    If you wish to filter annotations with the "and" logical operator, you can do so by specifying which filters will be checked with "and".
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>
    AND is the default value and can be used without specifying the method.</b></div>
    In this example, you will get a list of annotated items with <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/working_with_metadata/chapter.md" target="_blank">user metadata</a> of the field "is_automated" and value True.

    """


def section4():
    """
    ### Or
    If you wish to filter annotations with the "or" logical operator, you can do so by specifying which filters will be checked with "or".
    In this example, you will get a list of items that are either on "folder1" or "folder2" directories.

    """


def section5():
    """
    ## Update User Metadata of Filtered Items
    <b>Update Filtered Items</b> - The `update_value` must be a dictionary.
    The dictionary will only update user metadata.
    Understand more about user metadata [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/working_with_metadata/chapter.md).
    In this example, you will update/add user metadata (with the field "BlackDogs" and value True), to items in a specific folder 'dogs' with an attribute 'black'.

    """


def section6():
    """
    ## Delete Filtered Items 
    In this example, you will delete items that were created on 30/8/2020 at 8:17 AM.

    """


def section7():
    """
    ## Item Filtering Fields 
    ### More Filter Options
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;">
    Use a dot to access parameters within curly brackets.
    For example use field='metadata.system.originalname' to filter by the item's original name.</div>

    """


def section8():
    """
    ## Full Examples
    ### How to filter items by their annotations label?

    """


def section9():
    """
    ### How to filter items by completed and approved status?
    """


def section10():
    """
    ### How to filter items by completed status (with items who are approved as well)?
    """


def section11():
    """
    ### How to filter items by only completed status?
    """


def section12():
    """
    ### How to filter unassigned items?
    """


def section13():
    """
    ### How to filter items by a specific folder?
    """


def section14():
    """
    ### Get all items named foo.bar
    """


def section15():
    """
    ### Sort files of size 0-5 MB by name, in ascending order
    """


def section16():
    """
    ### Sort with multiple fields: Sort Items by labels ascending and createdAt descending
    """


def section17():
    """
    ## Advanced Filtering Operators
    Explore advanced filtering options on <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.md/" target="_blank">this page</a>.

    ## Response to DQL Query
    A typical response to a DQL query will look like the following:
    """

def section18():
    """
    ## Using Custom DQL Filter
    If you have a DQL JSON copied from the platform you can create an SDK Filter directly with it using the `custom_filter` attribute:
    """

def section19():
    """
    ## Open a Filter in the UI
    You can open a filter in the platform UI using the `open_in_web` method:
    """