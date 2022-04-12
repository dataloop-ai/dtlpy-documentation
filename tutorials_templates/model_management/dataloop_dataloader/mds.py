def func1():
    """
    # Dataloop Dataloader
    A dl.Dataset image and annotation generator for training and for items visualization

    We can visualize the data with augmentation for debug and exploration.
    After that, we will use the Data Generator as an input to the training functions
    """


def func2():
    """
    ## Object Detection Examples
    We can visualize a random item from the dataset:
    """


def func3():
    """
    Or get the same item using it's index:
    """


def func4():
    """
    Adding augmentations using imgaug repository:
    """


def func5():
    """
    All of the Data Generator options (from the function docstring):

    :param dataset_entity: dl.Dataset entity
    :param annotation_type: dl.AnnotationType - type of annotation to load from the annotated dataset
    :param filters: dl.Filters - filtering entity to filter the dataset items
    :param data_path: Path to Dataloop annotations (root to "item" and "json").
    :param overwrite:
    :param label_to_id_map: dict - {label_string: id} dictionary
    :param transforms: Optional transform to be applied on a sample. list or torchvision.Transform
    :param num_workers:
    :param shuffle: Whether to shuffle the data (default: True) If set to False, sorts the data in alphanumeric order.
    :param seed: Optional random seed for shuffling and transformations.
    :param to_categorical: convert label id to categorical format
    :param class_balancing: if True - performing random over-sample with class ids as the target to balance training data
    :param return_originals: bool - If True, return ALSO images and annotations before transformations (for debug)
    :param ignore_empty: bool - If True, generator will NOT collect items without annotations


    The output of a single element is a dictionary holding all the relevant informtaion.
    the keys for the DataGen above are: ['image_filepath', 'item_id', 'box', 'class', 'labels', 'annotation_filepath', 'image', 'annotations', 'orig_image', 'orig_annotations']
    """


def func6():
    """
    We'll add the flag to return the origin items to understand better how the augmentations look like.
    Let's set the flag and we can plot:
    """


def func7():
    """
    ## Segmentation Examples
    First we'll load a semantic dataset and view some images and the output structure

    """


def func8():
    """
    Visualize original vs augmented image and annotations mask:
    """


def func9():
    """
    Converting to 3d one-hot to visualize the binary mask per label. We will plot only 8 label (there might be more on the item):
    """


def func10():
    """
    batch_size and collate_fn
    """


def func11():
    """
    label mapping and default background
    """
