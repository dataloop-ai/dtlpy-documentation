import time

import behave
import json
import os
from examples.annotations.download_one_by_one import example
import tempfile


@behave.when(u'I prepared download one by one example')
def step_impl(context):
    try:
        context.dataset = context.project.datasets.create(dataset_name='my-dataset-{}'.format(str(context.num)))
        context.new_path = '/folder_a/folder_b'
        if context.new_path not in context.dataset.directory_tree.dir_names:
            context.dataset.items.make_dir(directory=context.new_path)

        context.items_filepath = [
            os.path.join(os.environ['DATALOOP_TEST_ASSETS'], 'sample_datasets/FruitImage/items/test/apple_77.jpg'),
            os.path.join(os.environ['DATALOOP_TEST_ASSETS'], 'sample_datasets/FruitImage/items/test/apple_78.jpg'),
            os.path.join(os.environ['DATALOOP_TEST_ASSETS'], 'sample_datasets/FruitImage/items/test/apple_79.jpg')]

        # Upload items
        context.item_1 = context.dataset.items.upload(local_path=context.items_filepath[0], remote_path='/')
        context.item_2 = context.dataset.items.upload(local_path=context.items_filepath[1], remote_path='/folder_a')
        context.item_3 = context.dataset.items.upload(local_path=context.items_filepath[2], remote_path=context.new_path)

        # Wait for image-preprocess to finish
        time.sleep(10)

        # Upload annotations
        context.annotations_file_path = os.path.join(os.environ['DATALOOP_TEST_ASSETS'],
                                                     'sample_datasets/FruitImage/json/test/apple_77.json')
        with open(context.annotations_file_path, "r") as f:
            context.annotations = json.load(f)["annotations"]
        context.item_1.annotations.upload(context.annotations)

        context.annotations_file_path = os.path.join(os.environ['DATALOOP_TEST_ASSETS'],
                                                     'sample_datasets/FruitImage/json/test/apple_78.json')
        with open(context.annotations_file_path, "r") as f:
            context.annotations = json.load(f)["annotations"]
        context.item_2.annotations.upload(context.annotations)

        context.annotations_file_path = os.path.join(os.environ['DATALOOP_TEST_ASSETS'],
                                                     'sample_datasets/FruitImage/json/test/apple_79.json')
        with open(context.annotations_file_path, "r") as f:
            context.annotations = json.load(f)["annotations"]
        context.item_3.annotations.upload(context.annotations)

        # Create temp directory
        temp_dir = tempfile.TemporaryDirectory()
        context.root_path = temp_dir.name
        context.to_delete_test_assets_dir.append(temp_dir)
        # Wait for on-create to success

    except Exception as e:
        assert "Failed to run preparation : {}".format(e)


@behave.then(u'I run download one by one example')
def step_impl(context):
    try:
        example(context.dataset.id, context.root_path)
    except Exception as e:
        assert "Failed to run example : {}".format(e)


@behave.then(u'I validate download one by one example')
def step_impl(context):

    assert not len(os.listdir(context.root_path)) == 0, 'no files nd in {}'.format(context.root_path)
    try:
        with open(os.path.join(context.root_path, 'apple_77.json'), "r") as f:
            context.annotations = json.load(f)["annotations"]
    except Exception as e:
        assert False, "File not found\n{}".format(e)

    assert len(context.item_1.annotations.list()) == len(context.annotations), "Missing annotations in file apple_77.json"

    try:
        with open(os.path.join(context.root_path, 'folder_a/apple_78.json'), "r") as f:
            context.annotations = json.load(f)["annotations"]
    except Exception as e:
        assert False, "File not found\n{}".format(e)

    assert len(context.item_2.annotations.list()) == len(context.annotations), "Missing annotations in file apple_78.json"

    try:
        with open(os.path.join(context.root_path, context.new_path[1:], 'apple_79.json'), "r") as f:
            context.annotations = json.load(f)["annotations"]
    except Exception as e:
        assert False, "File not found\n{}".format(e)

    assert len(context.item_3.annotations.list()) == len(context.annotations), "Missing annotations in file apple_79.json"
