import behave
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
    # context.scripts.driver2 = '' #TODO: Create Driver
    context.scripts.dataset_name2 = 'manage datasets dataset-section2'


def section3_prepare(context):
    context.scripts.project3 = context.project
    context.scripts.dataset_id3 = context.dataset.id


def section4_prepare(context):
    context.scripts.project = context.project
    context.scripts.dataset = context.dataset
    context.scripts.clone_name = context.dataset.name + '-clone'


def section5_prepare(context):
    context.scripts.project = context.project
    context.scripts.dataset = context.dataset
    context.scripts.clone_name = context.dataset.name + '-clone'


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
