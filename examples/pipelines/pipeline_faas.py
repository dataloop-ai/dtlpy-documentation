import os
import time
import dtlpy as dl
import logging

logger = logging.getLogger(name=__name__)


class ServiceRunner(dl.BaseServiceRunner):
    """
    Package runner class
    """

    def __init__(self):
        print("start-init")

    def automate(self, item: dl.Item):
        item.metadata['system']['fromPipe'] = True
        item.update(system_metadata=True)
        return item
