import behave


@behave.given('I prepared a project by the name of "{project_name}"')
def step_impl(context, project_name):
    try:
        context.project = context.dl.projects.create(project_name=project_name)
    except Exception as e:
        context.project = context.dl.projects.get(project_name=project_name)


@behave.given('I delete the prepared project')
def step_impl(context):
    context.project.delete()
