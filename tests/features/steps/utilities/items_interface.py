import behave
import os

from tests.features.steps.utilities.platform_interface_steps import rebuild_path


@behave.given('I prepared an item of type "{item_type}"')
def step_impl(context, item_type):
    item_types_list = {
        "image": os.environ['DATALOOP_TEST_ASSETS'] + "/images/hamster.jpg"
    }
    local_path = rebuild_path(item_types_list[item_type])

    try:
        context.item = context.dataset.items.upload(local_path=local_path)[0]
    except Exception as e:
        context.item = context.dataset.items.list()[0]


@behave.given('I prepared an item with annotations of type "{item_type}"')
def step_impl(context, item_type):
    item_types_list = {
        "image": [os.environ['DATALOOP_TEST_ASSETS'] + "/images/hamster.jpg", os.environ['DATALOOP_TEST_ASSETS'] + "/images/hamster.json"]
    }

    local_path = rebuild_path(item_types_list[item_type][0])
    local_annotations_path = rebuild_path(item_types_list[item_type][1])

    try:

        context.item = context.dataset.items.upload(local_path=local_path,
                                                    local_annotations_path=local_annotations_path)[0]
    except Exception as e:
        context.item = context.dataset.items.list()[0]


@behave.given('I delete the prepared item')
def step_impl(context):
    context.item.delete()
