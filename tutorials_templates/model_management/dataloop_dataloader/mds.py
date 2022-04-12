def func1():
    """
    # Dataloop Dataloader
    A dl.Dataset image and annotation generator for training and for items visualization

    We can visualize the data with augmentation for debugging and exploration.
    After that, we will use the Data Generator as an input to the training functions.
    """


def func2():
    """
    ## Object Detection Examples
    We can visualize a random item from the dataset:
    """


def func3():
    """
    Or get the same item using its index:
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


    The output of a single element is a dictionary holding all the relevant information.
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
    Converting to 3d one-hot encoding to visualize the binary mask per label. We will plot only 8 labels (there might be more on the item):
    """


def func10():
    """
    ## Setting a Label Map
    One of the inputs to the DatasetGenerator is 'label_to_id_map'. This variable can be used to change the label mapping for the annotations
    and allow using the dataset ontology in a greater variety of cases.
    For example, you can map multiple labels so a single id or add a default value for all the unlabeled pixels in segmentation annotations.
    This is what the annotation looks like without any mapping:
    """


def func11():
    """
    Now, we'll map both the 'eye' label and the background to 2 and the 'fur' to 1:
    """


def func12():
    """
    ## Batch size and batch_size and collate_fn
    If batch_size is not None, the returned structure will be a list with batch_size data items.
    Setting a collate function will convert the returned structure to a tensor of any kind.
    The default collate will convert everything to ndarrays. We also have tensorflow and torch collate to convert to the corresponding tensors.
    """
