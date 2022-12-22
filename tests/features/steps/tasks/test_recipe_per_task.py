import behave
import os
from examples.tasks.recipe_per_task import create_multiple_tasks
import random
import time


@behave.when(u'I run recipe per task example')
def step_impl(context):
    try:
        create_multiple_tasks()
    except Exception as e:
        assert False, "Failed to run example : {}".format(e)


@behave.then(u'I prepared recipe per task example on project "{project_name}" with dataset "{dataset_name}"')
def step_impl(context, project_name, dataset_name):
    try:
        context.project = context.dl.projects.get(project_name=project_name)
        context.to_delete_projects_ids.append(context.project.id)
        context.feature.dataloop_feature_project = context.project
        time.sleep(5)
        context.dataset = context.project.datasets.get(dataset_name=dataset_name)
        context.feature.dataloop_feature_dataset = context.dataset
        time.sleep(5)

        context.project.add_member(email='annotator1@dataloop.ai', role=context.dl.MemberRole.ANNOTATOR)
        context.project.add_member(email='annotator2@dataloop.ai', role=context.dl.MemberRole.ANNOTATOR)

        # Upload 10 items
        filepath = "images/hamster.jpg"
        filepath = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], filepath)

        filename = 'file'
        counter = 0
        while counter < 10:
            uploaded_filename = filename + str(counter) + '.jpg'
            import io
            with open(filepath, 'rb') as f:
                buffer = io.BytesIO(f.read())
                buffer.name = uploaded_filename
            context.dataset.items.upload(
                local_path=buffer,
                remote_path=None
            )
            counter += 1
        context.all_tasks = context.project.tasks.list()
        for task in context.all_tasks:
            task.add_items(
                items=context.dataset.items.list().items,
                assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'])

    except Exception as e:
        assert False, "Failed to run preparation : {}".format(e)


@behave.then(u'I validate recipe per task example')
def step_impl(context):
    assert len(context.all_tasks) == 3, "Failed to create 3 tasks"
    assert context.all_tasks[0].recipe_id == context.project.recipes.list()[0][1].id, \
        "Wrong recipe id in task: {}".format(context.all_tasks[0].name)
    assert context.all_tasks[1].recipe_id == context.project.recipes.list()[0][2].id, \
        "Wrong recipe id in task: {}".format(context.all_tasks[1].name)
    assert context.all_tasks[2].recipe_id == context.project.recipes.list()[0][3].id, \
        "Wrong recipe id in task: {}".format(context.all_tasks[2].name)
