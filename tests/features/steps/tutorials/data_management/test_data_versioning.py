import behave
from docs_build.tutorials_templates.data_management.data_versioning import scripts


@behave.when(u'I prepared test data versioning')
def step_impl(context):
    sections_list = {
        'section1': section1_prepare,
        'section2': section2_prepare,
    }
    section_name = context.table.rows.cells[0]

    context.scripts = scripts
    sections_list[section_name](context)


def section1_prepare(context):
    context.dataset = context.dl.datasets.get(dataset_name='data version dataset')
    context.dataset_id = context.dataset.id
    context.clone_name = context.dataset + '-clone'


def section2_prepare(context):
    context.dataset1 = context.dl.datasets.get(dataset_name='data version dataset')
    context.dataset2 = context.dl.datasets.get(dataset_name='data version dataset-clone')
    context.dataset2.recipe = context.dataset1.recipe
    context.dataset2.update()

    context.dataset_ids = [context.dataset1.id, context.dataset2.id]
    context.project_ids = [context.project.id, context.project.id]


@behave.then(u'I run test data versioning')
def step_impl(context):
    sections_list = {
        'section1': section1_run,
        'section2': section2_run,
    }
    section_name = context.table.rows.cells[0]

    try:
        sections_list[section_name](context)

    except Exception as e:
        assert False, "Failed to run example : {}".format(e)


def section1_run(context):
    context.scripts.section1(project=context.project, dataset_id=context.dataset_id, clone_name=context.clone_name)


def section2_run(context):
    context.scripts.section2(dataset_ids=context.dataset_ids, project_ids=context.project_ids, merge_name=context.merge_name)


@behave.then(u'I validate test data versioning')
def step_impl(context):
    sections_list = {
        'section1': section1_validate,
        'section2': section2_validate,
    }
    section_name = context.table.rows.cells[0]

    sections_list[section_name](context)


def section1_validate(context):
    clone_dataset = context.project.datasets.get(dataset_name=context.clone_name)
    assert context.item == clone_dataset.items.list[0]
    assert context.item.annotations.list == clone_dataset.items.list[0].annotations.list


def section2_validate(context):
    merge_dataset = context.project.datasets.get(dataset_name=context.merge_name)
    assert context.item == merge_dataset.items.list[0]
    assert context.item.annotations.list == merge_dataset.items.list[0].annotations.list
