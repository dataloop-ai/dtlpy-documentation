import behave
from docs_build.tutorials_templates.data_management.data_versioning.scripts import Scripts


@behave.when(u'I prepared test data versioning "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': section1_prepare,
        'section2': section2_prepare,
    }

    context.scripts = Scripts()
    sections_list[section_name](context)


def section1_prepare(context):
    context.scripts.project = context.project
    context.scripts.dataset = context.dataset
    context.scripts.clone_name = context.dataset.name + '-clone'


def section2_prepare(context):
    context.scripts.project = context.project
    context.scripts.dataset = context.dataset
    context.scripts.dataset_clone = context.project.datasets.get(dataset_name=context.dataset.name + '-clone')
    context.scripts.merge_name = context.dataset.name + '-merge'


@behave.then(u'I run test data versioning "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': section1_run,
        'section2': section2_run,
    }

    try:
        sections_list[section_name](context)

    except Exception as e:
        assert False, "Failed to run example : {}".format(e)


def section1_run(context):
    context.scripts.section1()


def section2_run(context):
    context.scripts.section2()


@behave.then(u'I validate test data versioning "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': section1_validate,
        'section2': section2_validate,
    }

    sections_list[section_name](context)


def section1_validate(context):
    clone_dataset = context.project.datasets.get(dataset_name=context.dataset.name + '-clone')
    clone_item = clone_dataset.items.get(filepath=context.item.filename)
    assert context.item.annotations_count == clone_item.annotations_count


def section2_validate(context):
    merge_dataset = context.project.datasets.get(dataset_name=context.dataset.name + '-merge')
    merge_item = merge_dataset.items.get(filepath=context.item.filename)
    assert context.item.annotations_count == merge_item.annotations_count
