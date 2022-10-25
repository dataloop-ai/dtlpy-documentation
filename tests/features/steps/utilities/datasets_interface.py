import behave


@behave.given('I prepared a dataset by the name of "{dataset_name}"')
def step_impl(context, dataset_name):
    try:
        context.dataset = context.project.datasets.create(dataset_name=dataset_name)
    except Exception as e:
        assert 'Dataset with same name already exist in the specified project' in e.args[1]
        context.dataset = context.project.datasets.get(dataset_name=dataset_name)


@behave.given('I delete the prepared dataset')
def step_impl(context):
    try:
        context.dataset.delete()
    except Exception as e:
        assert 'You are not authorized to perform the specified action' in e.args[1]
