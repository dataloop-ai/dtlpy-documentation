import behave
import os
from docs_build.tutorials_templates.data_management.modalities.scripts import Scripts


@behave.when(u'I prepared test modalities "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        "section1": section1_prepare,
        "section2": section2_prepare,
        # "section3": section3_prepare, NOT RUNNABLE
        "section4": section4_prepare,
        # "section5": section5_prepare, PREPARE FROM section4
    }

    context.scripts = Scripts()
    sections_list[section_name](context)


def section1_prepare(context):
    return True


def section2_prepare(context):
    return True


def section4_prepare(context):
    return True




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
