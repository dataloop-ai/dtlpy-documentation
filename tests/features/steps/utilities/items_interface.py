import behave


@behave.given('I prepared an item of type "{item_type}"')
def step_impl(context, item_type):
    item_types_list = {
        "image": "../../../../assets/images/hamster.jpg"
    }
    try:
        context.item = context.dataset.items.upload(local_path=item_types_list[item_type])[0]
    except Exception as e:
        context.item = context.dataset.items.list()[0]


@behave.given('I prepared an item with annotations of type "{item_type}"')
def step_impl(context, item_type):
    item_types_list = {
        "image": ["../../../../assets/images/hamster.jpg", "../../../../assets/images/hamster.json"]
    }
    try:
        context.item = context.dataset.items.upload(local_path=item_types_list[item_type][0],
                                                    local_annotations_path=item_types_list[item_type][1])[0]
    except Exception as e:
        context.item = context.dataset.items.list()[0]


@behave.given('I delete the prepared item')
def step_impl(context):
    context.item.delete()
