import behave
from tutorials_templates.faas.single_function_rgb_to_gray.scripts import Scripts
import random


@behave.when(u'I prepared test single function')
def step_impl(context):
    try:
        """
        Instantiate class object
        """
        context.scripts = Scripts()

    except Exception as e:
        assert False, "Failed to run preparation : {}".format(e)


@behave.then(u'I run test single function')
def step_impl(context):
    try:
        context.scripts.func1()
        context.rgb2gray = context.scripts.rgb2gray
        context.scripts.func2(dl=context.dl, rgb2gray=context.rgb2gray)
        context.service = context.scripts.service
        context.scripts.func4(project=context.project, service=context.service, item=context.item)
        context.execution = context.scripts.execution

    except Exception as e:
        assert False, "Failed to run example : {}".format(e)


@behave.then(u'I validate test single function')
def step_impl(context):
    assert type(context.project) == context.dl.Project, "context.project is not a dl.Project type."
    assert context.execution.latest_status['status'] == "success", "Execution Failed {}".format(context.execution.latest_status)
