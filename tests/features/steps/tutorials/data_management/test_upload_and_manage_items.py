import behave
import os
from docs_build.tutorials_templates.data_management.upload_and_manage_items.scripts import Scripts


@behave.when(u'I prepared test upload and manage items "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': section1_prepare,
        'section2': section2_prepare,
        'section3': section3_prepare,
        'section4': section4_prepare,
        'section5': section5_prepare,
    }

    context.scripts = Scripts()
    sections_list[section_name](context)


def section1_prepare(context):
    context.scripts.project_name1 = context.project.name
    context.scripts.dataset_name1 = context.dataset.name

    context.local_path_items = []
    for i in range(3):
        context.local_path_items.append(os.path.join(os.environ['DATALOOP_TEST_ASSETS'],
                                                     'sample_datasets/FruitImage/items/train/apple_{}.jpg'.format(i+1)))

    context.scripts.local_path_item1 = context.local_path_items[0]
    context.scripts.local_path_item2 = context.local_path_items[1]
    context.scripts.local_path_item3 = context.local_path_items[2]
    context.scripts.remote_path1 = '/FruitImage'


def section2_prepare(context):
    context.scripts.project_name2 = context.project.name
    context.scripts.dataset_name2 = context.dataset.name
    context.scripts.local_path2 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'],
                                               'sample_datasets/FruitImage/items/train/apple_4.jpg')
    context.scripts.remote_path2 = '/FruitImage'


def section3_prepare(context):
    context.scripts.project3 = context.project
    context.scripts.dataset_name3 = context.dataset.name
    context.scripts.file_name3 = 'flower.jpg'


def section4_prepare(context):
    context.scripts.item4 = context.item


def section5_prepare(context):
    context.scripts.dataset_id5 = context.dataset.id
    ''' First item and info attached: '''
    context.scripts.first_local_path5 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'],
                                                     'sample_datasets/FruitImage/items/train/apple_1.jpg')
    context.scripts.first_local_annotations_path5 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'],
                                                                 'sample_datasets/FruitImage/json/train/apple_1.json')
    ''' Second item and info attached: '''
    context.scripts.second_local_path5 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'],
                                                      'sample_datasets/FruitImage/items/train/apple_2.jpg')
    context.scripts.second_local_annotations_path5 = os.path.join(os.environ['DATALOOP_TEST_ASSETS'],
                                                                  'sample_datasets/FruitImage/json/train/apple_2.json')


@behave.then(u'I run test upload and manage items "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': context.scripts.section1,
        'section2': context.scripts.section2,
        'section3': context.scripts.section3,
        'section4': context.scripts.section4,
        'section5': context.scripts.section5,
    }

    try:
        sections_list[section_name]()

    except Exception as e:
        assert False, "Failed to run example : {}".format(e)



