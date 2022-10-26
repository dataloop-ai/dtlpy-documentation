import behave
from docs_build.tutorials_templates.data_management.data_versioning import scripts


@behave.when(u'I prepared test data versioning "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': section1_prepare,
        'section2': section2_prepare,
    }

    context.scripts = scripts
    sections_list[section_name](context)


def section1_prepare(context):
    context.dataset_id = context.dataset.id
    context.clone_name = context.dataset.name + '-clone'


def section2_prepare(context):
    context.dataset1 = context.project.datasets.get(dataset_name=context.dataset.name)
    context.dataset2 = context.project.datasets.get(dataset_name=context.dataset.name + '-clone')
    context.dataset_ids = [context.dataset1.id, context.dataset2.id]
    context.project_ids = [context.project.id, context.project.id]
    context.merge_name = context.dataset.name + '-merge'


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
    context.scripts.section1(project=context.project, dataset_id=context.dataset_id, clone_name=context.clone_name)


def section2_run(context):
    context.scripts.section2(dataset_ids=context.dataset_ids, project_ids=context.project_ids, merge_name=context.merge_name)


@behave.then(u'I validate test data versioning "{section_name}"')
def step_impl(context, section_name):
    sections_list = {
        'section1': section1_validate,
        'section2': section2_validate,
    }

    sections_list[section_name](context)


def section1_validate(context):
    clone_dataset = context.project.datasets.get(dataset_name=context.clone_name)
    clone_item = clone_dataset.items.get(filepath=context.item.filename)
    assert context.item.annotations_count == clone_item.annotations_count


def section2_validate(context):
    merge_dataset = context.project.datasets.get(dataset_name=context.merge_name)
    merge_item = merge_dataset.items.get(filepath=context.item.filename)
    assert context.item.annotations_count == merge_item.annotations_count
