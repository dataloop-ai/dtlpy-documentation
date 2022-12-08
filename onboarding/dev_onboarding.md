# Onboarding

## Introduction

### Platform overview

[Here](https://dataloop.ai/docs/dataloop-overview) you will find full overview of Dataloop platform. 

The main entities of the platform is the following: 

 - [Project](https://dataloop.ai/docs/project)
 - [Dataset](https://dataloop.ai/docs/dataset)
 - [Recipe](https://dataloop.ai/docs/ontology)
 - [Task](https://dataloop.ai/docs/tasks-assignments)
 - [Contributors](https://dataloop.ai/docs/contributor-roles)
 

### SDK overview

Python SDK that provides full control over your projects and code. It allows you to automate CRUD (Create, Read, Update, Delete) operations within the platform for all the main entities. 

In order to use our SDK, follow the steps below: 

1. [Installing](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/getting_started/sdk_overview/chapter.md#installing-prerequisite-software)
2. [Login](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/getting_started/sdk_overview/chapter.md#sdk-login)

**Project:** 

1. [Create project](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/getting_started/sdk_overview/chapter.md#to-create-a-new-project)
2. [Get project](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/getting_started/sdk_overview/chapter.md#to-select-the-new-project)
3. [Add contributors](https://sdk-docs.dataloop.ai/en/latest/repositories.html#dtlpy.repositories.projects.Projects.list_members)


**Dataset**

1. [Create dataset](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/getting_started/sdk_overview/chapter.md#to-create-a-new-dataset)
2. [Get dataset](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/getting_started/sdk_overview/chapter.md#to-select-the-dataset)
3. [Upload items](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/getting_started/sdk_overview/chapter.md#uploading-items)
4. [Get items](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/getting_started/sdk_overview/chapter.md#getting-items)
5. [Add metadata](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/upload_and_manage_items/chapter.md)

***Exercise:*** 

1. To create a project 
2. Add 2 contributors to the project ( one project owner and another annotator)
3. To create dataset 
4. To upload 2 images in "Folder 1" and upload 2 videos in "Folder 2"
5. Both images have to have item metadata
6. To delete one image from Folder 1


**Annotations**

There are different types of annotations that you can create on the platform. 
In this introduction section we will focus on [classificaton](https://dataloop.ai/docs/classify-item)
and [bounding box](https://dataloop.ai/docs/create-bounding-box) and [polilyne](https://dataloop.ai/docs/create-polygon)

1. [Setup](https://sdk-docs.dataloop.ai/en/latest/tutorials/annotations_image/setup/chapter.html)
2. [Upload annotations](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/getting_started/sdk_overview/chapter.md#annotating-items) ( review only box and classification)
3. [Classification](https://sdk-docs.dataloop.ai/en/latest/tutorials/annotations_image/classification_point_and_pose/chapter.html)
4. [Bounding box](https://sdk-docs.dataloop.ai/en/latest/tutorials/annotations_image/bounding_box_and_cuboid/chapter.html)
5. [Polygon and polyline](https://sdk-docs.dataloop.ai/en/latest/tutorials/annotations_image/polygon_and_polyline/chapter.html)


 
***Exercise:***

1. Get the dataset 
2. Get one specific image by its ID
3. Add a polygon
4. Get another image by its ID
5. Add a box


### Querying and Filtering

**Metadata**

Each entity in our system has a JSON code that represents its data within our system.
There are different json structure between [item](https://dataloop.ai/docs/en/item-json-format?highlight=metadata) and 
[annotations](https://dataloop.ai/docs/annotation-json-format). 

You can learn more [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/80f1e828ef6b27fe28e8c12ea5f2f4c53573b426/tutorials/data_management/working_with_metadata/chapter.ipynb) how to use the metadata for SDK. 

**Pagination**

We use pages instead of a list when we have an object that contains a lot of information. While in UI you would simply go page by page or in batches of pages. 

You can learn more [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/pagination/chapter.md) how to work with pages and use this concept with filters. 


**Filters**

[Filters](https://dataloop.ai/docs/sort-filter) are part of the Dataset and Task Browsers, enabling you to filter items based on every aspect of your files.

Filters are very powerful when using SDK and can help you build automatic flows based on different queries. 

You can learn basic queries [here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/tutorials/data_management/sort_and_filter/item_level/chapter.ipynb)

***Exercise:***

1. Get dataset 
2. Filter out only image that has annotation box 
3. Print how many images of this type you found



### Tasks & assignments

Annotation work in the Dataloop called [task](https://dataloop.ai/docs/tasks-assignments) that include main elements: 
data itself, team and instructions ( recipe & ontology).

You can [create tasks](https://sdk-docs.dataloop.ai/en/latest/tutorials/task_workflows/create_a_task/chapter.html#) from entire dataset or based on certain parameters by using filters.


***Exersice:***
1. Get a dataset
2. Filter out only not annotated items
3. Create an annotation task and assigned it to 2 different contributors


### Dataset advanced

Dataloop provides data [versioning tools](https://dataloop.ai/docs/clone-merge-dataset?highlight=clone) to manage your data that you can use for golden training 
sets management, reproducibility, experimentation and many more. 

You can use [merge](https://sdk-docs.dataloop.ai/en/latest/repositories.html#dtlpy.repositories.datasets.Datasets.merge) and [clone](https://sdk-docs.dataloop.ai/en/latest/tutorials/data_management/data_versioning/chapter.html#clone-datasets) also via SDK. 

***Exercise:***
1. Get a dataset
2. Clone dataset
3. Rename cloned dataset
4. Create a new dataset
5. Merge your original dataset with a new created one


## FAAS

Dataloop Function-as-a-Service ([FAAS](https://dataloop.ai/docs/faas))  is a compute service that automatically runs your code based on time patterns or in response to trigger events.
You can use this tool for pre annotation processing (resize, video assembler/dissember); post annotation processing (auto-parenting, augmentation); ML models (auto-detection), QA models (auto QA, consensus model, majority vote model)

**The main concepts in FAAS:**

- [Service](https://dataloop.ai/docs/service-runtime)
- [Docker image](https://dataloop.ai/docs/faas-docker-images)
- [Service analytics](https://dataloop.ai/docs/service-analytics)

**Advanced examples how to implemnet FAAS:**

1. Create and deploy [simple function](https://sdk-docs.dataloop.ai/en/latest/tutorials/faas/single_function_rgb_to_gray/chapter.html)
2. The function that extracts image Exif information and uploads it [to item's metadata](https://github.com/dataloop-ai/image-exif)
3. Add [classification](https://github.com/SewarDra/dtlpyTraining-Sessions/tree/main/Session%202-FaaS%26Pipelines/add_classification-basic%20FaaS)
4. Auto [annotation service](https://dataloop.ai/docs/auto-annotation-service)

**Video tutorials how to create FAAS in UI**

1. FAAS with [module](https://app.guidde.co/share/playbooks/j7iGAKHJas4iZjP8umCgK4?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)
2. FAAS [cron](https://app.guidde.co/share/playbooks/9pA98jkVBjScnYKbL1GcLK?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)


##Pipelines

The Dataloop pipeline process allows transitioning data between labeling tasks,
QA tasks, functions installed in Dataloop, code snippets, ML models. 
The data can be filtered by any criteria, split, merged, and change status in the process.

**Video tutorials how to create pipelines in UI**

1. [Simple pipeline](https://app.guidde.co/share/playbooks/p88yeiCCZYPJ5De92KRhNz?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)

2. [Task to task pipeline](https://app.guidde.co/share/playbooks/d4VKpz2wXkEfC3b8KtScoj?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)
3. [Task with FAAS and Filter](https://app.guidde.co/share/playbooks/uhQbzYGjMZjQoAWGMzcM3r?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)
4. [Task with Filter](https://app.guidde.co/share/playbooks/f94hGsB1CoURVjVUhD354B?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)















