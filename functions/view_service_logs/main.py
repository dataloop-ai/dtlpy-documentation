import dtlpy as dl
import time
import logging

logger = logging.getLogger(name=__name__)
# logging.getLogger('dtlpy').setLevel(logging.WARN)
dl.verbose.logging_level = 'warning'


class ServiceRunner(dl.BaseServiceRunner):
    """
    Package runner class

    """

    def __init__(self, **kwargs):
        """
        Init package attributes here

        :param kwargs: config params
        :return:
        """

    def run(self, item, progress=None):
        """
        Write your main package service here

        :param progress: Use this to update the progress of your package
        :return:
        """
        # these lines can be removed
        for i in range(10):
            print(i)
            print(item.name)
            time.sleep(1)
