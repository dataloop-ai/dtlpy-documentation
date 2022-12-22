import os

# set var for assets
os.environ['DATALOOP_TEST_ASSETS'] = os.path.join(os.getcwd(), 'assets')

from tests.features.steps.utilities import platform_interface_steps
from tests.features.steps.utilities import items_interface

from tests.features.steps.annotations import test_download_one_by_one
from tests.features.steps.items import test_pdf_viewer_modality
from tests.features.steps.items import test_sdk_filter_by_status
from tests.features.steps.tasks import test_recipe_per_task
from tests.features.steps.tutorials.faas import test_faas_introduction
from tests.features.steps.tutorials.faas import test_faas_single_function
from tests.features.steps.tutorials.data_management import test_upload_and_manage_items
from tests.features.steps.tutorials.data_management import test_modalities
from tests.features.steps.utilities import items_interface
from tests.features.steps.tutorials.data_management import test_working_with_metadata
