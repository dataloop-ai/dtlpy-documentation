import behave
import dtlpy as dl


@behave.when(u"I Prepare Annotated Item")
def step_impl(context):
    project: dl.Project = context.dl.project.create()
    dataset = project.create()
    item = dataset.items.upload()
