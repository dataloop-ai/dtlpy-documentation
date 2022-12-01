import behave
import os
from docs_build.tutorials_templates.data_management.upload_and_manage_annotations.scripts import Scripts


@behave.when(u'I prepared test upload and manage annotations "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        "section1": section1_prepare,
        "section2": section2_prepare,
        "section3": section3_prepare,
        "section4": section4_prepare,
        "section5": section5_prepare,
        "section5a": section5a_prepare,
        "section5b": section5b_prepare,
        "section6": section6_prepare,
        "section7": section7_prepare,
        "section8": section8_prepare,
        "section9": section9_prepare,
        "section10": section10_prepare,
        "section11": section11_prepare,
        "section12": section12_prepare,
        "section13": section13_prepare,
        "section14": section14_prepare,
        "section15": section15_prepare,
        "section16": section16_prepare,
        "section17": section17_prepare,
        "section18": section18_prepare,
        "section19": section19_prepare,
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


def section4_prepare(context):
    context.scripts.dataset4 = context.dataset
    context.scripts.local_items_path4 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], "sample_datasets/FruitImage/items/train/apple_3.jpg")
    context.scripts.local_annotations_path4 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], "sample_datasets/FruitImage/json/train/apple_3.json")


def section5_prepare(context):
    context.scripts.csv_file_path5 = ''
    context.scripts.dataset5 = context.dataset.id
    context.scripts.item_id5 = context.item.id


def section5a_prepare(context):
    assert True


def section5b_prepare(context):
    assert True


def section6_prepare(context):
    assert True


def section7_prepare(context):
    assert True


def section8_prepare(context):
    assert True


def section9_prepare(context):
    assert True


def section10_prepare(context):
    assert True


def section11_prepare(context):
    assert True


def section12_prepare(context):
    assert True


def section13_prepare(context):
    assert True


def section14_prepare(context):
    assert True


def section15_prepare(context):
    assert True


def section16_prepare(context):
    assert True


def section17_prepare(context):
    assert True


def section18_prepare(context):
    assert True


def section19_prepare(context):
    assert True


@behave.then(u'I run test upload and manage annotations "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': context.scripts.section1,
        'section2': context.scripts.section2,
        'section3': context.scripts.section3,
        'section4': context.scripts.section4,
        'section5': context.scripts.section5,
        'section5a': context.scripts.section5a,
        'section5b': context.scripts.section5b,
        'section6': context.scripts.section6,
        'section7': context.scripts.section7,
        'section8': context.scripts.section8,
        'section9': context.scripts.section9,
        'section10': context.scripts.section10,
        'section11': context.scripts.section11,
        'section12': context.scripts.section12,
        'section13': context.scripts.section13,
        'section14': context.scripts.section14,
        'section15': context.scripts.section15,
        'section16': context.scripts.section16,
        'section17': context.scripts.section17,
        'section18': context.scripts.section18,
        'section19': context.scripts.section19,
    }

    try:
        sections_list[section_name]()

    except Exception as e:
        assert False, "Failed to run example : {}".format(e)
