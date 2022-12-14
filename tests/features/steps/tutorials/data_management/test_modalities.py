import behave
import os
import json
from docs_build.tutorials_templates.data_management.modalities.scripts import Scripts


@behave.when(u'I prepared test modalities "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        "section1": section1_prepare,
        "section2": section2_prepare,
        # "section3": section3_prepare, NOT RUNNABLE
        "section4": section4_prepare,
        # "section5": section5_prepare, PREPARED FROM section4
    }

    context.scripts = Scripts()
    sections_list[section_name](context)


def section1_prepare(context):
    context.scripts.project_name1 = context.project.name
    context.scripts.dataset_name1 = context.dataset.name


def section2_prepare(context):
    item1_path = "sample_datasets/FruitImage/items/train/apple_1.jpg"
    item2_path = "sample_datasets/FruitImage/items/train/apple_2.jpg"
    item1 = context.dataset.items.upload(local_path=os.path.join(os.environ['DATALOOP_TEST_ASSETS'], item1_path))
    item2 = context.dataset.items.upload(local_path=os.path.join(os.environ['DATALOOP_TEST_ASSETS'], item2_path))
    context.scripts.first_item_id2 = item1.id
    context.scripts.second_item_id2 = item2.id
    context.scripts.dataset2 = context.dataset


def section4_prepare(context):
    context.scripts.dataset4 = context.dataset

    modalities_json_path = "modalities/modalities_json.json"
    context.scripts.modalities_json4 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], modalities_json_path)


@behave.then(u'I run test modalities "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': context.scripts.section1,
        'section2': context.scripts.section2,
        # 'section3': context.scripts.section3, NOT RUNNABLE
        'section4': context.scripts.section4,
        'section5': context.scripts.section5,
    }

    try:
        sections_list[section_name]()

    except Exception as e:
        assert False, "Failed to run example : {}".format(e)

    if section_name == 'section4':
        sections_list['section5']()

