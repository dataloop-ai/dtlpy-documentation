import behave
from examples.items.sdk_filter_by_status import filter_by_status
import random


@behave.when(u'I prepared test sdk filter by status "{status}"')
def step_impl(context, status):
    try:
        # Update creator email to project creator
        context.creator = context.project.creator
        # Create task
        context.task = context.dataset.tasks.create(task_name='task-{}'.format(context.num), assignee_ids=[context.creator])
        context.status_dict = {"approved": 0, "completed": 0, "discard": 0}
        # Set status and box annotation to items
        pages = context.task.get_items()
        for page in pages:
            for item in page:
                rand = random.randrange(0, 2)
                if rand == 0:
                    item_status = 'completed'
                else:
                    item_status = 'discard'

                annotation = context.dl.Annotation.new(annotation_definition=context.dl.Box(top=10, left=10, bottom=100,
                                                                                            right=100, label='box'),
                                                       item=item)
                context.annotation = annotation.upload()
                item.update_status(status=item_status, task_id=context.task.id)
                context.status_dict[item_status] = context.status_dict[item_status] + 1
        # Save the task id
        context.task_id = context.task.id

        # Create qa task if status approved
        if status == 'approved':
            context.qa_task = context.task.create_qa_task(due_date=None, assignee_ids=[context.creator])
            for page in context.qa_task.get_items():
                for item in page:
                    item.update_status(status=status, task_id=context.qa_task.id)
                    context.status_dict[status] = context.status_dict[status] + 1

            context.task_id = context.qa_task.id

    except Exception as e:
        assert False, "Failed to run preparation : {}".format(e)


@behave.then(u'I run test sdk filter by status "{status}"')
def step_impl(context, status):
    try:
        context.pages = filter_by_status(project_name=context.project.name, dataset_name=context.dataset.name, task_id=context.task_id, status=[status], email=context.creator,
                                         greater_than=context.timestamp[0], less_than=context.timestamp[1])
    except Exception as e:
        assert False, "Failed to run example : {}".format(e)


@behave.then(u'I validate test sdk filter by status "{status}"')
def step_impl(context, status):
    assert context.status_dict[status] == context.pages.items_count, \
        "Filters are wrong expected {} , got {}".format(context.status_dict[status], context.pages.items_count)
