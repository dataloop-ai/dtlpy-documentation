import behave
from docs_build.tutorials_templates.data_management.upload_and_manage_annotations.scripts import Scripts


@behave.when(u'I prepared test upload and manage annotations "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        "section1": section1_prepare
    }

    context.scripts = Scripts()
    sections_list[section_name](context)


def section1_prepare(context):
    context.scripts.item_id1 = context.item.id
    context.scripts.annotation_id1 = context.item.annotations.list()[0].id


@behave.then(u'I run test upload and manage annotations "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': context.scripts.section1,
    }

    try:
        sections_list[section_name]()

    except Exception as e:
        assert False, "Failed to run example : {}".format(e)
