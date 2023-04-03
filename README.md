![LOGO](assets/site/logo.svg)
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
  *  [Segmentation](tutorials/annotations_image/segmentation/chapter.ipynb)
  *  [Setup](tutorials/annotations_image/setup/chapter.ipynb)
* Annotations video
  *  [Video annotations](tutorials/annotations_video/video_annotations/chapter.ipynb)
*  [Auto annotate service](tutorials/auto_annotate_service/chapter.ipynb)
* Data management
  * Cloud storage
    *  [Binding with aws](tutorials/data_management/cloud_storage/binding_with_aws/chapter.ipynb)
    *  [Binding with azure](tutorials/data_management/cloud_storage/binding_with_azure/chapter.ipynb)
    *  [Binding with gcs](tutorials/data_management/cloud_storage/binding_with_gcs/chapter.ipynb)
    *  [Create an external dataset](tutorials/data_management/cloud_storage/create_an_external_dataset/chapter.ipynb)
  *  [Data versioning](tutorials/data_management/data_versioning/chapter.ipynb)
  *  [Manage datasets](tutorials/data_management/manage_datasets/chapter.ipynb)
  *  [Modalities](tutorials/data_management/modalities/chapter.ipynb)
  * Sort and filter
    *  [Advanced sdk filters](tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.ipynb)
    *  [Annotation level](tutorials/data_management/sort_and_filter/annotation_level/chapter.ipynb)
    *  [Item level](tutorials/data_management/sort_and_filter/item_level/chapter.ipynb)
    *  [Pagination](tutorials/data_management/sort_and_filter/pagination/chapter.ipynb)
  *  [Upload and manage annotations](tutorials/data_management/upload_and_manage_annotations/chapter.ipynb)
  *  [Upload and manage items](tutorials/data_management/upload_and_manage_items/chapter.ipynb)
  *  [Working with metadata](tutorials/data_management/working_with_metadata/chapter.ipynb)
* Faas
  *  [Advance](tutorials/faas/advance/chapter.ipynb)
  *  [Auto annotate](tutorials/faas/auto_annotate/chapter.ipynb)
  *  [Concept](tutorials/faas/concept/chapter.ipynb)
  *  [Custom environment using docker](tutorials/faas/custom_environment_using_docker/chapter.ipynb)
  *  [Execution control](tutorials/faas/execution_control/chapter.ipynb)
  *  [Introduction](tutorials/faas/introduction/chapter.ipynb)
  *  [Multiple functions and modules](tutorials/faas/multiple_functions_and_modules/chapter.ipynb)
  *  [Single function rgb to gray](tutorials/faas/single_function_rgb_to_gray/chapter.ipynb)
  *  [Ui toolbars](tutorials/faas/ui_toolbars/chapter.ipynb)
* Model management
  *  [Create new model](tutorials/model_management/create_new_model/chapter.ipynb)
  *  [Dataloop dataloader](tutorials/model_management/dataloop_dataloader/chapter.ipynb)
  *  [Introduction](tutorials/model_management/introduction/chapter.ipynb)
  *  [Model metrics only](tutorials/model_management/model_metrics_only/chapter.ipynb)
  *  [Train dataloop models](tutorials/model_management/train_dataloop_models/chapter.ipynb)
  * Train models locally
    *  [Classification](tutorials/model_management/train_models_locally/classification/chapter.ipynb)
    *  [Object detection](tutorials/model_management/train_models_locally/object_detection/chapter.ipynb)
* Recipe and ontology
  *  [Concepts](tutorials/recipe_and_ontology/concepts/chapter.ipynb)
  *  [Ontology](tutorials/recipe_and_ontology/ontology/chapter.ipynb)
  *  [Recipe](tutorials/recipe_and_ontology/recipe/chapter.ipynb)
* Task workflows
  *  [Create a task](tutorials/task_workflows/create_a_task/chapter.ipynb)
  *  [Item status](tutorials/task_workflows/item_status/chapter.ipynb)
  *  [Redistributing and reassigning a task](tutorials/task_workflows/redistributing_and_reassigning_a_task/chapter.ipynb)

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
* Items
  *  [Add metadata to item](examples/items/add_metadata_to_item.py)
  *  [Add pdf viewer modality](examples/items/add_pdf_viewer_modality.py)
  *  [Filter by task status](examples/items/filter_by_task_status.py)
  *  [Move item](examples/items/move_item.py)
* Model mgmt
  * Snippets
    *  [Clone model](examples/model_mgmt/snippets/clone_model.py)
    *  [Deploy model](examples/model_mgmt/snippets/deploy_model.py)
    *  [Evaluate model](examples/model_mgmt/snippets/evaluate_model.py)
    *  [Train model](examples/model_mgmt/snippets/train_model.py)
* Pipelines
  *  [Create pipeline](examples/pipelines/create_pipeline.py)
* Reports
  *  [Create reports examples](examples/reports/create_reports_examples.py)
* Scoring
  *  [Create score](examples/scoring/create_score.py)
  *  [Feature set with score](examples/scoring/feature_set_with_score.py)
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
