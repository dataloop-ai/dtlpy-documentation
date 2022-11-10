import behave
import os


@behave.given('There is an item of type "{item_type}"')
def step_impl(context, item_type):
    item_types_list = {
        "image": "images/hamster.jpg"
    }
    local_path = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], item_types_list[item_type])

    try:
        context.item = context.dataset.items.upload(local_path=local_path)[0]
    except Exception as e:
        context.item = context.dataset.items.list()[0][0]


@behave.given('There is an item with annotations of type "{item_type}"')
def step_impl(context, item_type):
    item_types_list = {
        "image": ["images/hamster.jpg", "images/hamster.json"]
    }

    local_path = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], item_types_list[item_type][0])
    local_annotations_path = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], item_types_list[item_type][1])

    try:
        context.item = context.dataset.items.upload(local_path=local_path,
                                                    local_annotations_path=local_annotations_path)[0]
    except Exception as e:
        context.item = context.dataset.items.list()[0][0]


@behave.given('I delete the item')
def step_impl(context):
    context.item.delete()