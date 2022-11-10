import behave
import os
from docs_build.tutorials_templates.data_management.manage_datasets.scripts import Scripts


@behave.when(u'I prepared test manage datasets "{section_name}"')
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
    context.scripts.project1 = context.project
    context.scripts.dataset_name1 = 'manage datasets dataset-section1'


def section2_prepare(context):
    context.scripts.project_name2 = context.project.name
    # context.scripts.driver2 = '' #TODO: Solve Driver security issues
    context.scripts.dataset_name2 = 'manage datasets dataset-section2'


def section3_prepare(context):
    context.scripts.project3 = context.project
    context.scripts.dataset_id3 = context.dataset.id


def section4_prepare(context):
    context.scripts.dataset4 = context.dataset


def section5_prepare(context):
    context.dataset.items.upload(local_path=os.path.join(os.environ['DATALOOP_TEST_ASSETS'], "images/hamster.jpg"),
                                 local_annotations_path=os.path.join(os.environ['DATALOOP_TEST_ASSETS'], "images/hamster.json"),
                                 remote_path='/images/hamster.jpg')
    context.second_dataset = context.project.datasets.create(dataset_name='manage datasets dataset2-section5')

    context.scripts.source_project_name5 = context.project.name
    context.scripts.source_dataset_name5 = context.dataset.name
    context.scripts.source_folder5 = '/images'
    context.scripts.destination_project_name5 = context.project.name
    context.scripts.destination_dataset_name5 = context.second_dataset.name
    context.scripts.destination_folder5 = '/transferred_images'


@behave.then(u'I run test manage datasets "{section_name}"')
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

    print('Hio')