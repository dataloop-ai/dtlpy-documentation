import behave
import os
from docs_build.tutorials_templates.data_management.working_with_metadata.scripts import Scripts


@behave.when(u'I prepared test working with metadata "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        "section1": section1_prepare,
        "section2": section2_prepare,
        "section3": section3_prepare,
        "section4": section4_prepare,
        "section5": section5_prepare,
        "section6": section6_prepare,
        "section7": section7_prepare,
        "section8": section8_prepare,
        "section9": section9_prepare,
        "section10": section10_prepare,
        "section11": section11_prepare,
        # "section12": section12_prepare, NO PREPARE REQUIRED
        # "section13": section13_prepare, DONE FROM section12
        # "section14": section14_prepare, DONE FROM section13
        "section15": section15_prepare,
    }

    if section_name == "section12":
        return  # NO PREPARE NEEDED

    context.scripts = Scripts()
    sections_list[section_name](context)


def section1_prepare(context):
    context.scripts.dataset_name1 = context.dataset.name
    context.scripts.project_name1 = context.project.name


def section2_prepare(context):
    context.scripts.item2 = context.item
    context.scripts.annotation2 = context.item.annotations.list()[0]


def section3_prepare(context):
    context.scripts.item3 = context.item
    context.scripts.annotation3 = context.item.annotations.list()[0]


def section4_prepare(context):
    context.scripts.item4 = context.item
    context.scripts.annotation4 = context.item.annotations.list()[0]


def section5_prepare(context):
    context.scripts.item5 = context.item
    context.scripts.annotation5 = context.item.annotations.list()[0]


def section6_prepare(context):
    context.scripts.item6 = context.item
    context.scripts.annotation6 = context.item.annotations.list()[0]


def section7_prepare(context):
    context.scripts.item7 = context.item
    context.scripts.annotation7 = context.item.annotations.list()[0]


def section8_prepare(context):
    item_path = "sample_datasets/FruitImage/items/train/apple_1.jpg"
    full_path = context.dataset.items.upload(local_path=os.path.join(os.environ['DATALOOP_TEST_ASSETS'], item_path))

    context.scripts.dataset8 = context.dataset
    context.scripts.local_path8 = full_path
    context.scripts.item_id8 = context.item.id
    ### In progress


def section9_prepare(context):
    context.scripts.annotation9 = context.item.annotations.list()[0]


def section10_prepare(context):
    context.scripts.dataset_name10 = context.dataset.name
    context.scripts.project_name10 = context.project.name


def section11_prepare(context):
    item_path = "sample_datasets/FruitImage/items/train/apple_2.jpg"
    full_path = context.dataset.items.upload(local_path=os.path.join(os.environ['DATALOOP_TEST_ASSETS'], item_path))

    context.scripts.dataset11 = context.dataset
    context.scripts.local_path11 = full_path
    context.scripts.item_id11 = context.item.id
    ### In progress


def section15_prepare(context):
    item_path = "sample_datasets/FruitImage/items/train/apple_3.jpg"
    full_path = context.dataset.items.upload(local_path=os.path.join(os.environ['DATALOOP_TEST_ASSETS'], item_path))

    context.scripts.dataset11 = context.dataset
    context.scripts.local_path11 = full_path
    context.scripts.item_id11 = context.item.id
    ### In progress


@behave.then(u'I run test working with metadata "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': context.scripts.section1,
        'section2': context.scripts.section2,
        'section3': context.scripts.section3,
        'section4': context.scripts.section4,
        'section5': context.scripts.section5,
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
    }

    try:
        sections_list[section_name]()

    except Exception as e:
        assert False, "Failed to run example : {}".format(e)

    if section_name == 'section12':
        try:
            sections_list['section13']()
        except Exception as e:
            assert False, "Failed to run example : {}".format(e)

        try:
            context.scripts.dataset14 = context.dataset
            sections_list['section14']()
        except Exception as e:
            assert False, "Failed to run example : {}".format(e)
