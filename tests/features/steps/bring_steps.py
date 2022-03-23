import os

# set var for assets
os.environ['DATALOOP_TEST_ASSETS'] = os.path.join(os.getcwd(), 'assets')

from tests.features.steps.utilities import platform_interface_steps

from tests.features.steps.annotations import test_download_one_by_one
from tests.features.steps.items import test_pdf_viewer_modality
from tests.features.steps.items import test_sdk_filter_by_status
from tests.features.steps.tasks import test_recipe_per_task
