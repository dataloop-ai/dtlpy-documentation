![LOGO](assets/logo.svg)  
[![Documentation Status](https://readthedocs.org/projects/dtlpy/badge/?version=latest)](https://sdk-docs.dataloop.ai/en/latest/?badge=latest)
[![pypi](https://img.shields.io/pypi/v/dtlpy.svg)](https://pypi.org/project/dtlpy/)
[![versions](https://img.shields.io/pypi/pyversions/dtlpy.svg)](https://github.com/dataloop-ai/dtlpy)
[![license](https://img.shields.io/github/license/dataloop-ai/dtlpy-documentation.svg)](https://github.com/dataloop-ai/dtlpy-documentation/blob/master/LICENSE)

# SDK Documentations and Tutorials for Dataloop's SDK

The following repository will gather Dataloop's SDK examples and best practices.

## Table of Content

1. [Installation](#installation)
1. [Tutorials](#tutorials)
1. [Code Examples](#code-examples)
1. [Other Resources](#resources)
1. [Contributions](#contributes)

## Installation

First, clone this repo:

```
git clone https://github.com/dataloop-ai/dtlpy-documentation.git
cd dtlpy-documentation
```

If you don't have python installed, download and install from [here](https://www.python.org/downloads/) (python<3.10).  
We recommend creating a python virtual environment:

```
pip3 install --upgrade virtualenv
virtualenv -p python3 venv
source venv/bin/activate

pip3 install -r requirements.txt
```

To run the tutorials, launch the Jupyter Notebook

```
jupyter notebook tutorials
```

## Tutorials

* Annotations image
  *  [Advance tutorials](tutorials/annotations_image/advance_tutorials/chapter.ipynb)
  *  [Bounding box and cuboid](tutorials/annotations_image/bounding_box_and_cuboid/chapter.ipynb)
  *  [Classification point and pose](tutorials/annotations_image/classification_point_and_pose/chapter.ipynb)
  *  [Ellipse and item description](tutorials/annotations_image/ellipse_and_item_description/chapter.ipynb)
  *  [Polygon and polyline](tutorials/annotations_image/polygon_and_polyline/chapter.ipynb)
  *  [Setup](tutorials/annotations_image/setup/chapter.ipynb)
* Annotations video
  *  [Video annotations](tutorials/annotations_video/video_annotations/chapter.ipynb)
* Data management
  *  [Connect cloud storage](tutorials/data_management/connect_cloud_storage/chapter.ipynb)
  *  [Data versioning](tutorials/data_management/data_versioning/chapter.ipynb)
  *  [Manage datasets](tutorials/data_management/manage_datasets/chapter.ipynb)
  *  [Modalities](tutorials/data_management/modalities/chapter.ipynb)
  * Sort and filter
    *  [Advanced sdk filters](tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.ipynb)
    *  [Annotation level](tutorials/data_management/sort_and_filter/annotation_level/chapter.ipynb)
    *  [Item level](tutorials/data_management/sort_and_filter/item_level/chapter.ipynb)
    *  [Pagination](tutorials/data_management/sort_and_filter/pagination/chapter.ipynb)
  *  [Upload and manage annotations](tutorials/data_management/upload_and_manage_annotations/chapter.ipynb)
  *  [Upload and manage data and metadata](tutorials/data_management/upload_and_manage_data_and_metadata/chapter.ipynb)
  *  [Working with metadata](tutorials/data_management/working_with_metadata/chapter.ipynb)
* Faas
  *  [Concept](tutorials/faas/concept/chapter.ipynb)
  *  [Introduction](tutorials/faas/introduction/chapter.ipynb)
  *  [Multiple functions](tutorials/faas/multiple_functions/chapter.ipynb)
  *  [Single function rgb to gray](tutorials/faas/single_function_rgb_to_gray/chapter.ipynb)
* Model management
  *  [Create new model](tutorials/model_management/create_new_model/chapter.ipynb)
  *  [Dataloop dataloader](tutorials/model_management/dataloop_dataloader/chapter.ipynb)
  *  [Introduction](tutorials/model_management/introduction/chapter.ipynb)
  * Use dataloop zoo models
    *  [Classification](tutorials/model_management/use_dataloop_zoo_models/classification/chapter.ipynb)
    *  [Object detection](tutorials/model_management/use_dataloop_zoo_models/object_detection/chapter.ipynb)
* Recipe and ontology
  *  [Concepts](tutorials/recipe_and_ontology/concepts/chapter.ipynb)
  *  [Ontology](tutorials/recipe_and_ontology/ontology/chapter.ipynb)
  *  [Recipe](tutorials/recipe_and_ontology/recipe/chapter.ipynb)
* Task workflows
  * Qa
    *  [Create a new qa task](tutorials/task_workflows/qa/create_a_new_qa_task/chapter.ipynb)
    * Qa assignment
      *  [Note annotation](tutorials/task_workflows/qa/qa_assignment/note_annotation/chapter.ipynb)
      *  [Qa on annotation level](tutorials/task_workflows/qa/qa_assignment/qa_on_annotation_level/chapter.ipynb)
      *  [Qa on item level](tutorials/task_workflows/qa/qa_assignment/qa_on_item_level/chapter.ipynb)
    *  [Redistributing and reassigning a qa task](tutorials/task_workflows/qa/redistributing_and_reassigning_a_qa_task/chapter.ipynb)
  * Tasks and assignments
    *  [Create a task](tutorials/task_workflows/tasks_and_assignments/create_a_task/chapter.ipynb)
    *  [Redistributing and reassigning a task](tutorials/task_workflows/tasks_and_assignments/redistributing_and_reassigning_a_task/chapter.ipynb)
    *  [Task assignment](tutorials/task_workflows/tasks_and_assignments/task_assignment/chapter.ipynb)

## Code Examples

* Annotations
  *  [Annotate items using model](examples/annotations/annotate_items_using_model.py)
  *  [Annotate video using model and tracker](examples/annotations/annotate_video_using_model_and_tracker.py)
  *  [Copy annotations](examples/annotations/copy_annotations.py)
  *  [Create annotations](examples/annotations/create_annotations.py)
  *  [Create video annotations](examples/annotations/create_video_annotations.py)
  *  [Delete annotations](examples/annotations/delete_annotations.py)
  *  [Download one by one](examples/annotations/download_one_by_one.py)
  *  [Play video annotation](examples/annotations/play_video_annotation.py)
  *  [Show item and mask](examples/annotations/show_item_and_mask.py)
  *  [Upload annotation to dataset](examples/annotations/upload_annotation_to_dataset.py)
* Converters
  *  [Annotations convert to voc](examples/converters/annotations_convert_to_voc.py)
  *  [Annotations convert to yolo](examples/converters/annotations_convert_to_yolo.py)
  *  [Converter](examples/converters/converter.py)
  *  [Convert annotation types](examples/converters/convert_annotation_types.py)
* Datasets
  *  [Add labels](examples/datasets/add_labels.py)
  *  [Copy folder](examples/datasets/copy_folder.py)
* Integrations
  * S3 lambda
    *  [Lambda function](examples/integrations/s3_lambda/lambda_function.py)
    *  [Sync dataset](examples/integrations/s3_lambda/sync_dataset.py)
* Items
  *  [Add metadata to item](examples/items/add_metadata_to_item.py)
  *  [Add pdf viewer modality](examples/items/add_pdf_viewer_modality.py)
  *  [Filter by task status](examples/items/filter_by_task_status.py)
  *  [Move item](examples/items/move_item.py)
* Pipelines
  *  [Create pipeline](examples/pipelines/create_pipeline.py)
* Reports
  *  [Create reports examples](examples/reports/create_reports_examples.py)
* Tasks
  *  [Recipe per task](examples/tasks/recipe_per_task.py)
* Uploads
  *  [Upload batch of items](examples/uploads/upload_batch_of_items.py)
  *  [Upload items and custom format annotations](examples/uploads/upload_items_and_custom_format_annotations.py)
  *  [Upload items with modalities](examples/uploads/upload_items_with_modalities.py)
  *  [Upload segmentation annotations from mask image](examples/uploads/upload_segmentation_annotations_from_mask_image.py)
  *  [Upload yolo format annotations](examples/uploads/upload_yolo_format_annotations.py)

## Resources

* [Dataloop Docs](https://dataloop.ai/docs)
* [SDK Cheat Sheet](https://dataloop.ai/docs/sdk-cheatsheet?highlight=cheat)
* [DTLPY source code](https://github.com/dataloop-ai/dtlpy)
* [Platform](https://console.dataloop.ai/)

## Contributes
