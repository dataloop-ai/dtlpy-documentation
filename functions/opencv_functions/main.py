import dtlpy as dl
import numpy as np
import logging
import cv2

logger = logging.getLogger(name=__name__)


class ServiceRunner(dl.BaseServiceRunner):
    """
    A collection of opencv function to run on Dataloop items

    """

    @staticmethod
    def rgb2gray(item: dl.Item):
        """
        Function to convert RGB image to GRAY
        Will also add a modality to the original item

        :param item: dl.Item to convert
        :return: None
        """
        buffer = item.download(save_locally=False)
        bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
        gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        bgr_equalized_item = item.dataset.items.upload(local_path=gray,
                                                       remote_path='/gray' + item.dir,
                                                       remote_name=item.filename)
        # add modality
        item.modalities.create(name='gray',
                               ref=bgr_equalized_item.id)
        item.update(system_metadata=True)

    @staticmethod
    def clahe_equalization(item: dl.Item):
        """
        Improve the contrast of the item using CLAHE (Contrast Limited Adaptive Histogram Equalization)
        https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
        Creates an overlay modality of the output on the original item

        :param item: dl.Item
        :return:
        """
        buffer = item.download(save_locally=False)
        bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
        lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        l = clahe.apply(l)
        lab = cv2.merge((l, a, b))
        bgr_equalized = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
        bgr_equalized_item = item.dataset.items.upload(local_path=bgr_equalized,
                                                       remote_path='/equalized' + item.dir,
                                                       remote_name=item.filename)
        # add modality
        item.modalities.create(name='equalized',
                               ref=bgr_equalized_item.id)
        item.update(system_metadata=True)
