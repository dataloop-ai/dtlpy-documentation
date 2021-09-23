import dtlpy as dl
import numpy as np
from assets.keras_yolo3_master.yolo import YOLO
from PIL import Image

dl.setenv('rc')

model = YOLO()
project = dl.projects.get('COCO')
dataset2 = project.datasets.get('demo')
dataset1 = project.datasets.get('version')
item = dataset1.items.upload(local_path=r'E:\Datasets\COCO\2017\images\val2017\000000000785.jpg')
##########################
# Clone to other dataset #
##########################
assert isinstance(item, dl.Item)
cloned = item.clone(dst_dataset_id=dataset2.id, remote_filepath='/cloned/{}'.format(item.name))

##################
# Inference both #
##################

image = Image.open(item.download())
output, out_boxes, out_scores, out_classes = model.detect_image(image)

builder = item.annotations.builder()
for i_box, box in enumerate(out_boxes):
    top = int(out_boxes[i_box][0])
    left = int(out_boxes[i_box][1])
    bottom = int(out_boxes[i_box][2])
    right = int(out_boxes[i_box][3])
    builder.add(annotation_definition=dl.Box(left=left,
                                             top=top,
                                             right=right,
                                             bottom=bottom,
                                             label=model.class_names[out_classes[i_box]],
                                             attributes=[float(out_scores[i_box])]),
                metadata={'user': {'model': {'name': 'YOLOv3',
                                             'confidence': float(out_scores[i_box])}}})
item.annotations.upload(builder)


def run_flip():
    flipped = np.fliplr(np.asarray(image))
    output, out_boxes, out_scores, out_classes = model.detect_image(Image.fromarray(flipped))
    builder = item.annotations.builder()
    for i_box, box in enumerate(out_boxes):
        top = int(out_boxes[i_box][0])
        left = item.width - int(out_boxes[i_box][3])
        bottom = int(out_boxes[i_box][2])
        right = item.width - int(out_boxes[i_box][1])
        builder.add(annotation_definition=dl.Box(left=left,
                                                 top=top,
                                                 right=right,
                                                 bottom=bottom,
                                                 label=model.class_names[out_classes[i_box]],
                                                 attributes=[float(out_scores[i_box])]),
                    metadata={'user': {'model': {'name': 'YOLOv3_flipped',
                                                 'confidence': float(out_scores[i_box])}}})
    item.annotations.upload(builder)
