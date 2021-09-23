import logging
import dtlpy as dl

logger = logging.getLogger(name=__name__)


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

    def item_to_json(self, item: dl.Item, progress=None):
        """
        Write your main package service here

        :param progress: Use this to update the progress of your package
        :return:
        """
        logger.info("Received item filename: {}".format(item.filename))
        return {'this': item.id}

    def json_to_item(self, json_obj):
        logger.info("Received item object: {}".format(json_obj))
        item = dl.items.get(item_id=json_obj['this'])
        return item
