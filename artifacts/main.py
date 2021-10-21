import os

import dtlpy as dl
import logging
from external_file import print_external

logger = logging.getLogger(name=__name__)


class ServiceRunner(dl.BaseServiceRunner):
    """
    Package runner class
    """

    def __init__(self, weight_path=None):
        self.package = dl.packages.get(package_name='artifacts-example')
        print('This print is from the init of the service.')
        logger.warning('We can also use logger for different debug levels')
        # this to download the file to the package
        if weight_path is None:
            weight_path = r'external_file.py'
        if not os.path.isfile(weight_path):
            self.package.artifacts.download(artifact_name=weight_path,
                                            local_path=os.path.join(os.getcwd(), weight_path))

    def run(self, item):
        """
        This is the main function for this FaaS
        :param item: dl.Item
        :return:
        """
        print_external()
        print('This is a print from an execution that runs on the item: {}'.format(item.name))
