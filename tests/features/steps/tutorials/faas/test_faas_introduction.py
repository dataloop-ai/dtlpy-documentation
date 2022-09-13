import behave
from docs_build.tutorials_templates.faas.introduction.scripts import Scripts


@behave.when(u'I prepared test faas introduction')
def step_impl(context):
    try:
        """
        Instantiate class object
        """
        context.scripts = Scripts()
        try:
            """ Try to get the project before running the test
             If true - Delete the project
             If false - Continue to next step"""
            context.scripts.func3(dl=context.dl)
            context.scripts.project.delete(True, True)
        except Exception as e:
            assert e.status_code == '404', "Failed to delete project {}".format(context.scripts.project)

    except Exception as e:
        assert False, "Failed to run preparation : {}".format(e)


@behave.then(u'I run test faas introduction')
def step_impl(context):
    try:

        context.scripts.func2(dl=context.dl)
        context.project = context.scripts.project
        context.scripts.func3(dl=context.dl)
        context.scripts.func4(project=context.project)
        context.item = context.scripts.item

    except Exception as e:
        assert False, "Failed to run example : {}".format(e)


@behave.then(u'I validate test faas introduction')
def step_impl(context):
    assert type(context.project) == context.dl.Project, "context.project is a dl.Project type."
    assert len(context.project.datasets.list()) == 2, "Project missing datasets and contain only {}".format([dataset.name for dataset in context.project.datasets.list()])
    assert context.project.datasets.list()[1].items_count == 1, "Item failed to upload to the dataset"
