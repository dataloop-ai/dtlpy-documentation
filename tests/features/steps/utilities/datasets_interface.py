import behave


@behave.given('I prepared a dataset by the name of "{dataset_name}"')
def step_impl(context, dataset_name):
    try:
        context.dataset = context.project.datasets.create(dataset_name=dataset_name)
    except Exception as e:
        context.dataset = context.project.datasets.get(dataset_name=dataset_name)


@behave.given('I delete the prepared dataset')
def step_impl(context):
    context.dataset.delete()
