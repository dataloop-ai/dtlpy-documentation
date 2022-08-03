import tensorflow as tf
import dtlpy as dl
import os
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from PIL import Image
import numpy as np


class ModelRunner(dl.BaseServiceRunner):
    def __init__(self):
        self.model = tf.keras.applications.InceptionV3(
            include_top=True,
            weights="imagenet",
            input_tensor=None,
            input_shape=None,
            pooling=None,
            classes=1000,
            classifier_activation="softmax",
        )

    def inference_and_upload(self, item: dl.Item):
        annotations = self.inference(item=item)
        item.annotations.upload(annotations=annotations)
        return item

    def inference(self, item: dl.Item):
        filepath = ''
        try:
            filepath = item.download(overwrite=True)
            image = np.asarray(Image.open(filepath).resize((299, 299), Image.BILINEAR))
            output = self.model.predict(preprocess_input(image)[None, ...])
            labels = decode_predictions(output)[0]
            label = labels[0][1]
            prob = labels[0][2]
            builder = item.annotations.builder()
            builder.add(annotation_definition=dl.Classification(label=label),
                        model_info={'name': 'inceptionv3',
                                    'confidence': '{:.2f}'.format(prob)})
        finally:
            if os.path.isfile(filepath):
                os.remove(filepath)
        return builder.to_json()['annotations']


def test():
    runner = ModelRunner()
    item = dl.items.get(item_id='62c67eef41c7db024a2d7198')
    runner.inference_and_upload(item)
