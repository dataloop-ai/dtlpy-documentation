def section1():
    """
    To access the filters entity click <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.filters" target="_blank">here</a>.
    ## The Dataloop Query Language - DQL
    Using The <a href="https://docs.dataloop.ai/docs/api-dql" target="_blank">Dataloop Query Language</a>, you may navigate through massive amounts of data.

    You can *filter*, *sort*, and *update* your metadata with it.

    ### Filters
    Using filters, you can filter items and get a generator of the filtered items. The filters entity is used to build such filters.

    #### Filters - Field & Value
    Filter your items or annotations using the parameters in the JSON code that represent its data within our system.
    Access your item/annotation JSON using <code>to_json()</code>.
    ##### Field
    Field refers to the attributes you filter by.
    
    For example, "dir" would be used if you wish to filter items by their folder/directory.

    ##### Value
    Value refers to the input by which you want to filter.
    For example, "/new_folder" can be the directory/folder name where the items you wish to filter are located.
    #### Sort - Field & Value
    ##### Field
    Field refers to the field you sort your items/annotations list by.
    For example, if you sort by filename, you will get the item list sorted in alphabetical order by filename.
    See the full list of the available fields <a href="https://docs.dataloop.ai/docs/api-dql" target="_blank">here</a>.
    ##### Value
    Value refers to the list order direction. Either ascending or descending.

    ### Filter Annotations
    Filter annotations by the annotations' JSON fields.
    In this example, you will get all of the note annotations in the dataset sorted by the label.

    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>

    See all of the items iterator options on the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/pagination/chapter.md#iterator-of-items" target="_blank">Iterator of Items</a> page.</div>

    """


def section2():
    """

    ### Filter Annotations by the Annotations' Item
    <code>add_join</code> - filter Annotations by the annotations' items' JSON fields. For example, filter only box annotations from image items.
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>
    See all of the items iterator options on the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/pagination/chapter.md#iterator-of-items" target="_blank">Iterator of Items</a> page.</div>

    """


def section3():
    """
    ### Filters Method - "Or" and "And"
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Filters Operators</b><br>
    For more advanced filters operators visit the <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.md" target="_blank">Advanced SDK Filters</a> page.</div>
    
    #### And
    If you wish to filter annotations with the "and" logical operator, you can do so by specifying which filters will be checked with "and".
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>
    AND is the default value and can be used without specifying the method.</b></div>
    In this example, you will get a list of annotations in the dataset of the type <b>box</b> and label <b>car</b>.

    """


def section4():
    """
    #### Or
    If you wish to filter annotations with the "or" logical operator, you can do so by specifying which filters will be checked with "or".
    In this example, you will get a list of the dataset's annotations that are either a 'box' or a 'point' type.

    """


def section5():
    """
    ### Delete Filtered Items 
    In this example, you will delete annotations that were created on 30/8/2020 at 8:17 AM.

    """


def section6():
    """
    ### Annotation Filtering Fields
    #### More Filter Options
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;">
    Use a dot to access parameters within curly brackets.
    For example use field='metadata.system.status' to filter by the annotation's status.</div>

    """


def section7():
    """
    ### Full Examples
    #### How to filter annotations by their label?

    """


def section8():
    """
    ### Advanced Filtering Operators
    Explore advanced filtering options on <a href="https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.md" target="_blank">this page</a>.

    """
