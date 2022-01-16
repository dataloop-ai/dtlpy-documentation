import dtlpy as dl
import numpy as np
import logging
import cv2

logger = logging.getLogger(name=__name__)


class ImageProcess(dl.BaseServiceRunner):
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
        logger.info('Converting RGB to gray, item: {}'.format(item.filename))
        gray_item = item.dataset.items.upload(local_path=gray,
                                              remote_path='/gray' + item.dir,
                                              remote_name=item.filename)
        # Add modality
        logger.info('Adding modality to original item. Gray item: {}'.format(gray_item.filename))
        item.modalities.create(name='gray',
                               ref=gray_item.id)
        item.update(system_metadata=True)

    @staticmethod
    def clahe_equalization(item: dl.Item):
        """
        Function to perform histogram equalization (CLAHE)
        Will add a modality to the original item
        Based on opencv https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
        :param item: dl.Item to convert
        :return: None
        """
        buffer = item.download(save_locally=False)
        bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
        # create a CLAHE object (Arguments are optional).
        logger.info('Preforming equalization on LAB, item: {}'.format(item.filename))
        lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
        lab_planes = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        lab_planes[0] = clahe.apply(lab_planes[0])
        lab = cv2.merge(lab_planes)
        bgr_equalized = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
        bgr_equalized_item = item.dataset.items.upload(local_path=bgr_equalized,
                                                       remote_path='/equ' + item.dir,
                                                       remote_name=item.filename)
        # Add modality
        logger.info('Adding modality to original item. Equalized item: {}'.format(bgr_equalized_item.filename))
        item.modalities.create(name='equ',
                               ref=bgr_equalized_item.id)
        item.update(system_metadata=True)
