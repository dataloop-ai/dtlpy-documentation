import os

import dtlpy as dl
import logging

logger = logging.getLogger(name=__name__)


class ServiceRunner(dl.BaseServiceRunner):
    """
    Package runner class
    """

    def __init__(self, artifact_filename=None):
        """
        In this init we will download the artifact to be used later in any function execution
        :param artifact_filename:
        """
        self.package = dl.packages.get(package_name='artifacts-package')

        if artifact_filename is None:
            artifact_filename = r'monkey-612x612.zip'
        full_weight_path = os.path.join(os.getcwd(), artifact_filename)
        # this to download the file from the package
        if not os.path.isfile(full_weight_path):
            # here the file still not exist
            print("external_file dose not exist")
            # here we download it
            self.package.artifacts.download(artifact_name=artifact_filename,
                                            local_path=full_weight_path)
        #  here the file is exist
        if os.path.isfile(full_weight_path):
            print("external_file exists")

    def run(self):
        """
        This is the main function for this FaaS
        :return:
        """
        print('listing local files:')
        print(os.listdir(os.getcwd()))
        print('The artifact zip is now in our local folder')
