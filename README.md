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

* Task workflows
  *  [Redistributing and reassigning a task](tutorials/task_workflows/redistributing_and_reassigning_a_task/chapter.ipynb)
  *  [Create a task](tutorials/task_workflows/create_a_task/chapter.ipynb)
  *  [Item status](tutorials/task_workflows/item_status/chapter.ipynb)
*  [Auto annotate service](tutorials/auto_annotate_service/chapter.ipynb)
* Data management
  * Sort and filter
    *  [Pagination](tutorials/data_management/sort_and_filter/pagination/chapter.ipynb)
    *  [Annotation level](tutorials/data_management/sort_and_filter/annotation_level/chapter.ipynb)
    *  [Item level](tutorials/data_management/sort_and_filter/item_level/chapter.ipynb)
    *  [Advanced sdk filters](tutorials/data_management/sort_and_filter/advanced_sdk_filters/chapter.ipynb)
  *  [Secrets](tutorials/data_management/secrets/chapter.ipynb)
  *  [Upload and manage annotations](tutorials/data_management/upload_and_manage_annotations/chapter.ipynb)
  *  [Modalities](tutorials/data_management/modalities/chapter.ipynb)
  *  [Working with metadata](tutorials/data_management/working_with_metadata/chapter.ipynb)
  *  [Integrations](tutorials/data_management/integrations/chapter.ipynb)
  *  [Upload and manage items](tutorials/data_management/upload_and_manage_items/chapter.ipynb)
  *  [Data versioning](tutorials/data_management/data_versioning/chapter.ipynb)
  * Cloud storage
    * Azure
      *  [Storage driver](tutorials/data_management/cloud_storage/azure/storage_driver/chapter.ipynb)
      *  [Integration](tutorials/data_management/cloud_storage/azure/integration/chapter.ipynb)
      *  [Auto upstream sync](tutorials/data_management/cloud_storage/azure/auto_upstream_sync/chapter.ipynb)
    * Gcp
      *  [Storage driver](tutorials/data_management/cloud_storage/gcp/storage_driver/chapter.ipynb)
      *  [Integration](tutorials/data_management/cloud_storage/gcp/integration/chapter.ipynb)
      *  [Auto upstream sync](tutorials/data_management/cloud_storage/gcp/auto_upstream_sync/chapter.ipynb)
    * Aws
      *  [Storage driver](tutorials/data_management/cloud_storage/aws/storage_driver/chapter.ipynb)
      *  [Integration](tutorials/data_management/cloud_storage/aws/integration/chapter.ipynb)
      *  [Manual item upstream sync](tutorials/data_management/cloud_storage/aws/manual_item_upstream_sync/chapter.ipynb)
      *  [Auto upstream sync](tutorials/data_management/cloud_storage/aws/auto_upstream_sync/chapter.ipynb)
  *  [Manage datasets](tutorials/data_management/manage_datasets/chapter.ipynb)
* Recipe and ontology
  *  [Recipe](tutorials/recipe_and_ontology/recipe/chapter.ipynb)
  *  [Ontology](tutorials/recipe_and_ontology/ontology/chapter.ipynb)
  *  [Concepts](tutorials/recipe_and_ontology/concepts/chapter.ipynb)
* Faas
  *  [Ui toolbars](tutorials/faas/ui_toolbars/chapter.ipynb)
  *  [Multiple functions and modules](tutorials/faas/multiple_functions_and_modules/chapter.ipynb)
  *  [Single function rgb to gray](tutorials/faas/single_function_rgb_to_gray/chapter.ipynb)
  *  [Private git codebase](tutorials/faas/private_git_codebase/chapter.ipynb)
  *  [Custom environment using docker](tutorials/faas/custom_environment_using_docker/chapter.ipynb)
  *  [Execution control](tutorials/faas/execution_control/chapter.ipynb)
  *  [Advance](tutorials/faas/advance/chapter.ipynb)
  *  [Concept](tutorials/faas/concept/chapter.ipynb)
  *  [Auto annotate](tutorials/faas/auto_annotate/chapter.ipynb)
* Pipelines
  *  [Create a pipeline](tutorials/pipelines/create_a_pipeline/chapter.ipynb)
* Annotations
  *  [Video](tutorials/annotations/video/chapter.ipynb)
  * Image
    *  [Segmentation](tutorials/annotations/image/segmentation/chapter.ipynb)
    *  [Ellipse and item description](tutorials/annotations/image/ellipse_and_item_description/chapter.ipynb)
    *  [Classification point and pose](tutorials/annotations/image/classification_point_and_pose/chapter.ipynb)
    *  [Advance tutorials](tutorials/annotations/image/advance_tutorials/chapter.ipynb)
    *  [Polygon and polyline](tutorials/annotations/image/polygon_and_polyline/chapter.ipynb)
    *  [Bounding box and cuboid](tutorials/annotations/image/bounding_box_and_cuboid/chapter.ipynb)
* Model management
  *  [Create new model ui](tutorials/model_management/create_new_model_ui/chapter.ipynb)
  *  [Introduction](tutorials/model_management/introduction/chapter.ipynb)
  * Advance
    *  [Model metrics](tutorials/model_management/advance/model_metrics/chapter.ipynb)
    * Train models locally
      *  [Classification](tutorials/model_management/advance/train_models_locally/classification/chapter.ipynb)
      *  [Object detection](tutorials/model_management/advance/train_models_locally/object_detection/chapter.ipynb)
    *  [Dataloop dataset generator](tutorials/model_management/advance/dataloop_dataset_generator/chapter.ipynb)
  *  [Ai library](tutorials/model_management/ai_library/chapter.ipynb)
  *  [Create new model sdk](tutorials/model_management/create_new_model_sdk/chapter.ipynb)

## Code Examples

* Tasks
  *  [Recipe per task](examples/tasks/recipe_per_task.py)
* Data management
  * Snippets
    * Secrets
      *  [Create secret](examples/data_management/snippets/secrets/create_secret.py)
    * Datasets
      *  [Create dataset internal storage](examples/data_management/snippets/datasets/create_dataset_internal_storage.py)
      *  [Create dataset external storage](examples/data_management/snippets/datasets/create_dataset_external_storage.py)
      *  [Copy folder](examples/data_management/snippets/datasets/copy_folder.py)
      *  [Add labels](examples/data_management/snippets/datasets/add_labels.py)
    * Integrations
      *  [Create integration azure](examples/data_management/snippets/integrations/create_integration_azure.py)
      *  [Create integration aws](examples/data_management/snippets/integrations/create_integration_aws.py)
      *  [Create integration gcp](examples/data_management/snippets/integrations/create_integration_gcp.py)
    * Storage drivers
      *  [Create storage driver gcs](examples/data_management/snippets/storage_drivers/create_storage_driver_gcs.py)
      *  [Create storage driver s3](examples/data_management/snippets/storage_drivers/create_storage_driver_s3.py)
      *  [Create storage driver blob](examples/data_management/snippets/storage_drivers/create_storage_driver_blob.py)
* Converters
  *  [Convert annotation types](examples/converters/convert_annotation_types.py)
  *  [Annotations convert to yolo](examples/converters/annotations_convert_to_yolo.py)
  *  [Converter](examples/converters/converter.py)
  *  [Annotations convert to voc](examples/converters/annotations_convert_to_voc.py)
* Uploads
  *  [Upload items with modalities](examples/uploads/upload_items_with_modalities.py)
  *  [Upload segmentation annotations from mask image](examples/uploads/upload_segmentation_annotations_from_mask_image.py)
  *  [Upload yolo format annotations](examples/uploads/upload_yolo_format_annotations.py)
  *  [Upload items and custom format annotations](examples/uploads/upload_items_and_custom_format_annotations.py)
  *  [Upload batch of items](examples/uploads/upload_batch_of_items.py)
* Pipelines
  *  [Create pipeline](examples/pipelines/create_pipeline.py)
* Annotations
  *  [Play video annotation](examples/annotations/play_video_annotation.py)
  *  [Download one by one](examples/annotations/download_one_by_one.py)
  *  [Annotate items using model](examples/annotations/annotate_items_using_model.py)
  *  [Delete annotations](examples/annotations/delete_annotations.py)
  *  [Annotate video using model and tracker](examples/annotations/annotate_video_using_model_and_tracker.py)
  *  [Upload annotation to dataset](examples/annotations/upload_annotation_to_dataset.py)
  *  [Create video annotations](examples/annotations/create_video_annotations.py)
  *  [Show item and mask](examples/annotations/show_item_and_mask.py)
  *  [Create annotations](examples/annotations/create_annotations.py)
  *  [Copy annotations](examples/annotations/copy_annotations.py)
* Model mgmt
  * Snippets
    *  [Evaluate model](examples/model_mgmt/snippets/evaluate_model.py)
    *  [Train model](examples/model_mgmt/snippets/train_model.py)
    *  [Deploy model](examples/model_mgmt/snippets/deploy_model.py)
    *  [Clone model](examples/model_mgmt/snippets/clone_model.py)
* Items
  *  [Add pdf viewer modality](examples/items/add_pdf_viewer_modality.py)
  *  [Filter by task status](examples/items/filter_by_task_status.py)
  *  [Add metadata to item](examples/items/add_metadata_to_item.py)
  *  [Random split to folders](examples/items/random_split_to_folders.py)
  *  [Move item](examples/items/move_item.py)
* Reports
  *  [Create reports examples](examples/reports/create_reports_examples.py)

## Resources

* [Dataloop Docs](https://dataloop.ai/docs)
* [SDK Cheat Sheet](https://dataloop.ai/docs/sdk-cheatsheet?highlight=cheat)
* [DTLPY source code](https://github.com/dataloop-ai/dtlpy)
* [Platform](https://console.dataloop.ai/)

## Contributes
