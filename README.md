![LOGO](./assets/site/logo.svg)
[![Documentation Status](https://readthedocs.org/projects/dtlpy/badge/?version=latest)](https://sdk-docs.dataloop.ai/en/latest/?badge=latest)
[![pypi](https://img.shields.io/pypi/v/dtlpy.svg)](https://pypi.org/project/dtlpy/)
[![versions](https://img.shields.io/pypi/pyversions/dtlpy.svg)](https://github.com/dataloop-ai/dtlpy)
[![license](https://img.shields.io/github/license/dataloop-ai/dtlpy-documentation.svg)](https://github.com/dataloop-ai/dtlpy-documentation/blob/master/LICENSE)

# SDK Documentations and Tutorials for Dataloop's SDK

The following repository will gather Dataloop's SDK examples and best practices.

## Table of Content

- [SDK Documentations and Tutorials for Dataloop's SDK](#sdk-documentations-and-tutorials-for-dataloops-sdk)
  - [Table of Content](#table-of-content)
  - [Installation](#installation)
  - [Tutorials](#tutorials)
  - [Code Examples](#code-examples)
  - [Resources](#resources)
  - [Contributes](#contributes)

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

* Analytics
  *  [Extract analytics](tutorials/analytics/extract_analytics/chapter.ipynb)
  *  [Overview](tutorials/analytics/overview/chapter.ipynb)
* Annotations
  *  [Audio](tutorials/annotations/audio/chapter.ipynb)
  *  [Gis](tutorials/annotations/gis/chapter.ipynb)
  *  [Image](tutorials/annotations/image/chapter.ipynb)
  *  [Lidar](tutorials/annotations/lidar/chapter.ipynb)
  *  [Prompts](tutorials/annotations/prompts/chapter.ipynb)
  *  [Text](tutorials/annotations/text/chapter.ipynb)
  *  [Video](tutorials/annotations/video/chapter.ipynb)
* Applications
  *  [Dpk examples](tutorials/applications/dpk_examples/chapter.ipynb)
  *  [Faq](tutorials/applications/faq/chapter.ipynb)
  *  [Introduction](tutorials/applications/introduction/chapter.ipynb)
  *  [Pipeline library](tutorials/applications/pipeline_library/chapter.ipynb)
  *  [Python application](tutorials/applications/python_application/chapter.ipynb)
  *  [Web application](tutorials/applications/web_application/chapter.ipynb)
*  [Auto annotate service](tutorials/auto_annotate_service/chapter.ipynb)
* Data management
  * Dataloop query language
    *  [Introduction](tutorials/data_management/dataloop_query_language/introduction/chapter.ipynb)
    *  [More examples](tutorials/data_management/dataloop_query_language/more_examples/chapter.ipynb)
  *  [Datasets and versioning](tutorials/data_management/datasets_and_versioning/chapter.ipynb)
  * External storage drivers
    *  [Aws s3](tutorials/data_management/external_storage_drivers/aws_s3/chapter.ipynb)
    *  [Azure blob](tutorials/data_management/external_storage_drivers/azure_blob/chapter.ipynb)
    *  [Gcs](tutorials/data_management/external_storage_drivers/gcs/chapter.ipynb)
  *  [Feature vectors](tutorials/data_management/feature_vectors/chapter.ipynb)
  *  [Integrations and secrets](tutorials/data_management/integrations_and_secrets/chapter.ipynb)
  * Items and annotations
    *  [Introduction](tutorials/data_management/items_and_annotations/introduction/chapter.ipynb)
    *  [More examples](tutorials/data_management/items_and_annotations/more_examples/chapter.ipynb)
    * Other data types
      *  [Gis](tutorials/data_management/items_and_annotations/other_data_types/gis/chapter.ipynb)
      *  [Lidar](tutorials/data_management/items_and_annotations/other_data_types/lidar/chapter.ipynb)
* Faas applications
  *  [Building an app](tutorials/faas_applications/building_an_app/chapter.ipynb)
  *  [Execution control](tutorials/faas_applications/execution_control/chapter.ipynb)
  *  [Github examples](tutorials/faas_applications/github_examples/chapter.ipynb)
  *  [Service configurations](tutorials/faas_applications/service_configurations/chapter.ipynb)
  *  [Ui toolbars](tutorials/faas_applications/ui_toolbars/chapter.ipynb)
  *  [Using docker and private registries](tutorials/faas_applications/using_docker_and_private_registries/chapter.ipynb)
* Getting started
  *  [Sdk overview](tutorials/getting_started/sdk_overview/chapter.ipynb)
* Labeling workflows
  *  [Item status](tutorials/labeling_workflows/item_status/chapter.ipynb)
  *  [Quality control](tutorials/labeling_workflows/quality_control/chapter.ipynb)
  *  [Task and assignment](tutorials/labeling_workflows/task_and_assignment/chapter.ipynb)
* Model management
  *  [Create new model sdk](tutorials/model_management/create_new_model_sdk/chapter.ipynb)
  *  [Introduction](tutorials/model_management/introduction/chapter.ipynb)
  *  [Marketplace](tutorials/model_management/marketplace/chapter.ipynb)
  * More guides
    *  [Model adapter flows](tutorials/model_management/more_guides/model_adapter_flows/chapter.ipynb)
    *  [Model annotations](tutorials/model_management/more_guides/model_annotations/chapter.ipynb)
    *  [Model configurations](tutorials/model_management/more_guides/model_configurations/chapter.ipynb)
    *  [Model metrics](tutorials/model_management/more_guides/model_metrics/chapter.ipynb)
  *  [New model torchvision example](tutorials/model_management/new_model_torchvision_example/chapter.ipynb)
* Pipelines
  *  [Create a pipeline](tutorials/pipelines/create_a_pipeline/chapter.ipynb)
  *  [Pipeline executions](tutorials/pipelines/pipeline_executions/chapter.ipynb)
* Recipe and ontology
  *  [Instructions and validations](tutorials/recipe_and_ontology/instructions_and_validations/chapter.ipynb)
  *  [Introduction](tutorials/recipe_and_ontology/introduction/chapter.ipynb)

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
  *  [Polygon to segmentation annotations](examples/annotations/polygon_to_segmentation_annotations.py)
  *  [Show item and mask](examples/annotations/show_item_and_mask.py)
  *  [Upload annotation to dataset](examples/annotations/upload_annotation_to_dataset.py)
* Converters
  *  [Annotations convert to voc](examples/converters/annotations_convert_to_voc.py)
  *  [Annotations convert to yolo](examples/converters/annotations_convert_to_yolo.py)
  *  [Converter](examples/converters/converter.py)
  *  [Convert annotation types](examples/converters/convert_annotation_types.py)
* Data management
  * Scripts
    *  [Recursive export](examples/data_management/scripts/recursive_export.py)
  * Snippets
    * Datasets
      *  [Add labels](examples/data_management/snippets/datasets/add_labels.py)
      *  [Copy folder](examples/data_management/snippets/datasets/copy_folder.py)
      *  [Create dataset external storage](examples/data_management/snippets/datasets/create_dataset_external_storage.py)
      *  [Create dataset internal storage](examples/data_management/snippets/datasets/create_dataset_internal_storage.py)
    * Feature sets
      *  [From app](examples/data_management/snippets/feature_sets/from_app.py)
      *  [From external](examples/data_management/snippets/feature_sets/from_external.py)
    * Integrations
      *  [Create integration aws](examples/data_management/snippets/integrations/create_integration_aws.py)
      *  [Create integration azure](examples/data_management/snippets/integrations/create_integration_azure.py)
      *  [Create integration gcp](examples/data_management/snippets/integrations/create_integration_gcp.py)
    * Secrets
      *  [Create secret](examples/data_management/snippets/secrets/create_secret.py)
    * Storage drivers
      *  [Create storage driver blob](examples/data_management/snippets/storage_drivers/create_storage_driver_blob.py)
      *  [Create storage driver gcs](examples/data_management/snippets/storage_drivers/create_storage_driver_gcs.py)
      *  [Create storage driver s3](examples/data_management/snippets/storage_drivers/create_storage_driver_s3.py)
* Items
  *  [Add metadata to item](examples/items/add_metadata_to_item.py)
  *  [Add pdf viewer modality](examples/items/add_pdf_viewer_modality.py)
  *  [Filter by task status](examples/items/filter_by_task_status.py)
  *  [Move item](examples/items/move_item.py)
  *  [Random split to folders](examples/items/random_split_to_folders.py)
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
* Tasks
  *  [Recipe per task](examples/tasks/recipe_per_task.py)
* Uploads
  *  [Upload batch of items](examples/uploads/upload_batch_of_items.py)
  *  [Upload items and custom format annotations](examples/uploads/upload_items_and_custom_format_annotations.py)
  *  [Upload items with modalities](examples/uploads/upload_items_with_modalities.py)
  *  [Upload segmentation annotations from mask image](examples/uploads/upload_segmentation_annotations_from_mask_image.py)
  *  [Upload yolo format annotations](examples/uploads/upload_yolo_format_annotations.py)

## Resources

* [Dataloop Docs](https://docs.dataloop.ai/docs)
* [SDK Cheat Sheet](https://docs.dataloop.ai/docs/sdk-cheatsheet?highlight=cheat)
* [DTLPY source code](https://github.com/dataloop-ai/dtlpy)
* [Platform](https://console.dataloop.ai/)

## Contributes
