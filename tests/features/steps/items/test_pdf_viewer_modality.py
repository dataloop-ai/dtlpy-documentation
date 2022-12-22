import behave
import os
from examples.items.add_pdf_viewer_modality import example
import random


@behave.when(u'I prepared pdf viewer modality example on "{filepath}"')
def step_impl(context, filepath):
    try:
        num = random.randint(10000, 100000)
        # Create dataset
        context.dataset = context.project.datasets.create(dataset_name='my-dataset-{}'.format(str(num)))
        # Get item filepath
        context.item_filepath = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], filepath)

        context.pdf_file_path = os.path.join(os.environ['DATALOOP_TEST_ASSETS'], 'images/lorem-ipsum.pdf')

    except Exception as e:
        assert False, "Failed to run preparation : {}".format(e)


@behave.then(u'I run pdf viewer modality example')
def step_impl(context):
    try:
        example(context.project.name, context.dataset.name, context.item_filepath, context.pdf_file_path)
    except Exception as e:
        assert "Failed to run example : {}".format(e)


@behave.then(u'I validate pdf viewer modality example')
def step_impl(context):
    assert context.dataset.items.list().items_count == 2
    filters = context.dl.Filters(field="metadata.system.mimetype", values="*image*")
    for page in context.dataset.items.list(filters=filters):
        for item in page:
            assert 'modalities' in item.metadata['system'], "Item has no modalities"
