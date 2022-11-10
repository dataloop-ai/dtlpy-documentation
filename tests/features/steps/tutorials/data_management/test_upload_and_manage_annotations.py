import behave
import os
from docs_build.tutorials_templates.data_management.upload_and_manage_annotations.scripts import Scripts


@behave.when(u'I prepared test upload and manage annotations "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        "section1": section1_prepare,
        "section2": section2_prepare,
        "section3": section3_prepare
    }

    context.scripts = Scripts()
    sections_list[section_name](context)


def section1_prepare(context):
    context.scripts.item_id1 = context.item.id
    context.scripts.annotation_id1 = context.item.annotations.list()[0].id


def section2_prepare(context):
    context.scripts.project_name2 = context.project.name
    context.scripts.dataset_name2 = context.dataset.name
    context.scripts.local_items_path2 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], "sample_datasets/FruitImage/items/train/apple_1.jpg")
    context.scripts.local_annotations_path2 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], "sample_datasets/FruitImage/json/train/apple_1.json")


def section3_prepare(context):
    context.scripts.dataset3 = context.dataset
    context.scripts.local_items_path3 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], "sample_datasets/FruitImage/items/train/apple_2.jpg")
    context.scripts.local_annotations_path3 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], "sample_datasets/FruitImage/json/train/apple_2.json")


@behave.then(u'I run test upload and manage annotations "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': context.scripts.section1,
        'section2': context.scripts.section2,
        'section3': context.scripts.section3,
    }

    try:
        sections_list[section_name]()

    except Exception as e:
        assert False, "Failed to run example : {}".format(e)
