import behave


@behave.given('I prepared a project by the name of "{project_name}"')
def step_impl(context, project_name):
    try:
        context.project = context.dl.projects.create(project_name=project_name)
    except Exception as e:
        assert 'name already used by another project. Try using a different project name' in e.args[1]
        context.project = context.dl.projects.get(project_name=project_name)


@behave.given('I delete the prepared project')
def step_impl(context):
    try:
        context.project.delete(True, True)
    except Exception as e:
        assert 'You are not authorized to perform the specified action' in e.args[1]
