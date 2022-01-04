import os

import dtlpy as dl
import logging

logger = logging.getLogger(name=__name__)


class ServiceRunner(dl.BaseServiceRunner):
    """
    Package runner class
    """

    def __init__(self, weight_path=None):
        self.package = dl.packages.get(package_name='artifacts-package')

        if weight_path is None:
            weight_path = r'external_file.py'
        full_weight_path = os.path.join(os.getcwd(), weight_path)
        # this to download the file from the package
        if not os.path.isfile(full_weight_path):
            # here the file still not exist
            print("external_file dose not exist")
            # here we download it
            self.package.artifacts.download(artifact_name=weight_path,
                                            local_path=full_weight_path)
        #  here the file is exist
        if os.path.isfile(full_weight_path):
            print("external_file exists")

    def run(self, item):
        """
        This is the main function for this FaaS
        :param item: dl.Item
        :return:
        """
        from external_file import print_external
        print_external()
        print('This is a print from an execution that runs on the item: {}'.format(item.name))
