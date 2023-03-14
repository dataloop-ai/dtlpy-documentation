# Swagger UI API Documentation

## Contents
### API Requests
[Projects](#Projects) | [Datasets](#Datasets) | [Recipes](#Recipes) | [Ontologies](#Ontologies) | [Items](#Items) | [Annotations](#Annotations)  |[Tasks](#Tasks) |[Assignments](#Assignments) | [Organization](#Organization) | [Services(FaaS)](#Services) | [Packages](#Packages) | [Executions](#Executions) | [Pipelines](#Pipelines) | [Composition](#Composition) | [Triggers](#Triggers) | [Features, Sets, Vectors](#Features) | [Models](#Models) | [Applications & DPK](#Applications) |

***[See API Request Examples here.](#Examples)***



## Intro
Dataloop's [Swagger UI](https://gate.dataloop.ai/api/v1/docs) offers the ability to perform API Requests such as ```GET```, ```POST```, ```PUT```, ```PATCH``` and 
```DELETE``` to different endpoints in our backend services like Projects, Datasets, Tasks, etc. It makes the process extremely easy and intuitive. With only a few clicks, you can run commands to get any information you may require about your Projects, Items, Datasets, Tasks or any other entity that is part of Dataloop.

In order to use the Swagger UI you will need to already be logged in to the Dataloop platform. If you haven't logged in yet, you need to [do that now](https://console.dataloop.ai/welcome) for the API requests to work. 

After logging in to the platform, the API authentication will be completed automatically.  If you logged in to Dataloop's Platform and then returned to the API page after completing the log in process, **refresh the page** and you will be able to run the API requests.
![image](https://user-images.githubusercontent.com/58508793/218516500-43b289ff-2e44-42e3-96be-5353cd1e7f76.png)

The image above is what you should see after logging in to Dataloop's platform, and going to the Swagger API UI. You can [find the Dataloop Swagger API here](https://gate.dataloop.ai/api/v1/docs/).

**Note:** This Swagger API guide will have the same structure as our [Developer Onboarding](../onboarding), which teaches you how to use the basic functions of Dataloop in Python code. Everything we'll cover in this guide can be done in Python code (in the Python SDK) as well as using the API.

## <a name="Projects"></a>Projects 

This section explores the various API requests you can use to manage Projects in Dataloop. A Project in Dataloop is a high-level Organizational entity that represents a specific task or goal. It can be used to manage data, Tasks, and Annotations related to a particular Project, and often serves as the main unit of work in the system. It provides a centralized location for managing data and Tasks related to a specific goal or objective. This can help improve collaboration among team members, ensure consistency in the data and Annotations, and make it easier to track progress and results.

Here's a list of the most important API requests for Projects:
- [List an User's Projects for the current Organization](https://gate.dataloop.ai/api/v1/docs/#/Projects/get_projects);
- [Create a new Project](https://gate.dataloop.ai/api/v1/docs/#/Projects/post_projects);
- [Show a Project's details](https://gate.dataloop.ai/api/v1/docs/#/Projects/get_projects__id_);
- [Delete a Project by ID](https://gate.dataloop.ai/api/v1/docs/#/Projects/delete_projects__id_);
- [Rename Project, using the Project's ID](https://gate.dataloop.ai/api/v1/docs/#/Projects/patch_projects__id_);
- [List all of the Project's Contributors using Project's ID](https://gate.dataloop.ai/api/v1/docs/#/Projects/get_projects__id__members);
- [List all of the Project's Contributors using Project's name](https://gate.dataloop.ai/api/v1/docs/#/Projects/get_projects__project_name__name_);
- [Add a new User to a specific Project](https://gate.dataloop.ai/api/v1/docs/#/Projects/post_projects__project_id__members__user_id_);
- [Remove a Member from a Project](https://gate.dataloop.ai/api/v1/docs/#/Projects/delete_projects__project_id__members__user_id_);
- [Change a User's Role and permissions usin Project ID and User ID](https://gate.dataloop.ai/api/v1/docs/#/Projects/patch_projects__project_id__members__user_id_);
- [Move the Project to another Organization](https://gate.dataloop.ai/api/v1/docs/#/Projects/patch_projects__project_id__org);
- [Add an account to a Project](https://gate.dataloop.ai/api/v1/docs/#/Projects/post_projects__project_id__accounts);
- [Remove an account from a Project](https://gate.dataloop.ai/api/v1/docs/#/Projects/delete_projects__project_id__accounts);
- [Replace an account for a Project](https://gate.dataloop.ai/api/v1/docs/#/Projects/patch_projects__project_id__accounts).


## <a name="Datasets"></a>Datasets
This section will cover the most important API examples, using the API requests from the Datasets section. A Dataset is a collection of Items (files), their Metadata, and Annotations. A Dataset can have a file-system-like structure, with folders and subfolders at any level. There are different types of Datasets:

- Master - Original Dataset, managing the actual binaries;
- Clone - Contains pointers to original files, enabling management of virtual Items that do not replicate the binaries of the underlying storage once cloned or copied. When cloning a Dataset, users can decide if the new copy will contain Metadata and Annotations created over the original Dataset;
- Merge - Multiple Datasets can be merged into one, enabling multiple Annotations to be merged onto the same Item (for 2 Datasets to be successfully merged, they need to have the same Recipe and Ontology.

The most important API request for Datasets can be seen below:
- [Get a names list of all existing Datasets](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsListDatasets);
- [Create a new Dataset](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsCreateDataset);
- [Get Dataset by ID](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsGetDataset);
- [Delete a Dataset](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsDeleteDataset);
- [Update a Dataset's properties](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsPatchDataset);
- [Clone a Dataset](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsCloneDataset);
- [Delete all expired Items](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsDeleteExpiredItems);
- [Merge Datasets](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsMergeDatasets);
- [Get a directory tree of the Dataset](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsGetDirectoryTree);
- [Download a JSON file representing all Annotations in the specified Dataset](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsGetAnnotationsAsJSON);
- [Download a .zip archive containing all Annotations in the specified Dataset](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsGetAnnotationsAsZIP); 
- [Get Annotations in .zip chunks (multiple segments, in case of huge Datasets)](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsGetAnnotationsZIPChunks);
- [Get a Dataset's Label Aggregation](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsGetDatasetLabelAggregation);
- [Get a Filtered Dataset Labe Aggregation](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsGetFilteredDatasetLabelAggregation);
- [Get a specific .zip chunk](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsStreamAnnotationsZIPChunk);
- [Annotate Items by RQL](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsAnnotateItemsByRQL);
- [Querry Dataset](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsQueryDatasets);
- [ Reset dataset counters for Item count, Annotation count, etc.](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsResetDatasetCounters);
- [Update an Item's Annotation;](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsRestoreAnnotation)
- [Synchronize missing files from storage](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsSync);
- [Import Items to the Dataset](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsImportItemsToDataset);
- [Detach Items from Dataset](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsDetachItemsFromDataset);
- [Get a Project's Datasets](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsGetProjectDatasets).

## <a name="Recipes"></a>Recipes
A "Recipe" refers to a set of instructions or rules that define how data should be processed, labeled, or analyzed within a Project. Recipes can be thought of as templates or workflows that provide a standardized way of working with data and can help to streamline the process of generating labeled Datasets for machine learning and other applications. Linked with an Ontology, the Recipe adds labeling instructions and settings, such as labeling tools to be used, mapping of tools to specific labels/Attributes, PDF instructions file, and more. Recipes in the Dataloop system can be customized and adapted to fit a wide range of use cases and data types.

Here are the most important API requests for Recipes:
- [Create a new Recipe](https://gate.dataloop.ai/api/v1/docs#/Recipes/RecipesCreateRecipe);
- [Find Recipes by Query](https://gate.dataloop.ai/api/v1/docs#/Recipes/RecipesFindRecipes);
- [Clone a Recipe](https://gate.dataloop.ai/api/v1/docs#/Recipes/RecipesCloneRecipe);
- [Update an existing Recipe](https://gate.dataloop.ai/api/v1/docs#/Recipes/RecipesPatchRecipe);
- [Get a specific Recipe](https://gate.dataloop.ai/api/v1/docs#/Recipes/RecipesGetRecipe);
- [Delete a Recipe](https://gate.dataloop.ai/api/v1/docs#/Recipes/RecipesDeleteRecipe).


## <a name="Ontologies"></a>Ontologies
An Ontology in Dataloop represents a set of definitions that describe the structure and relationships of your Labels. The Ontology of a Dataset is the building block of your Model and will help you define the object detection your trained model provides. Ontology holds 2 important components that are used in your Project:
- Labels (like classes) - are the names you use to classify your Annotations;
- Attributes - allow additional independent degrees of freedom while building a world definition.

Here are the most important API requests for Ontology:
- [Create a new Ontology](https://gate.dataloop.ai/api/v1/docs#/Ontologies/OntologiesCreateOntology);
- [Find Ontologies using a Query](https://gate.dataloop.ai/api/v1/docs#/Ontologies/OntologiesFindOntologies);
- [Update an existing Ontology](https://gate.dataloop.ai/api/v1/docs#/Ontologies/OntologiesUpdateOntology);
- [Get a specific Ontology by ID](https://gate.dataloop.ai/api/v1/docs#/Ontologies/OntologiesGetOntology);
- [Delete an Ontology](https://gate.dataloop.ai/api/v1/docs#/Ontologies/OntologiesDeleteOntology);
- [Update an existing Ontology](https://gate.dataloop.ai/api/v1/docs#/Ontologies/OntologiesAddLabels).


## <a name="Items"></a>Items
The Items section of the API helps you do a variety of requests regarding Items. An Item in Dataloop, is a unit of data that represents a ‘single instance’ or ‘file’ of a larger Dataset. It can be an image, a video, a sound recording, a text document, or any other type of digital asset that needs to be labeled, annotated, or analyzed. Each Item in the Dataloop system is typically associated with one or more Tasks, which define the specific operations that need to be performed on the Item. For example, an Item may be labeled with Bounding Boxes to identify objects in an image, transcribed to convert speech-to-text, or classified based on its content. Items also have associated Metadata.

Here are some of the most important API requests for Items:
- [List items in a dataset](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsGetItems);
- [Create a new item in a dataset](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsCreateItem);
- [Move files to a specified directory](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsMoveItems);
- [Get Item by ID](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsGetItem);
- [Delete Item by ID](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsRemoveItem);
- [Edit Item by ID](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsEditItem);
- [Remove Items by Query](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsRemoveItemsByQuery);
- [Create Item Revision using ID](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsCreateItemRevision);
- [Stream an Item](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsStreamItem);
- [Stream Item's Thumbnail](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsStreamItemThumbnail);
- [Get Directory Child Items](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsGetDirectoryChildItems);
- [Clone Item](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsCloneItem).


## <a name="Annotations"></a>Annotations
This section explores the various API requests you can use to manage Annotations in Datalop. An Annotation entity refers to a label, tag, or another piece of Metadata that is attached to an Item in a Dataset. Annotations are typically used to provide additional context or information about an Item, and to enable machine learning models to better understand and interpret the data. Annotations in the Dataloop system can take many forms, depending on the specific Task and type of data being annotated. Annotations in the Dataloop system are typically created by human annotators, who use the system's interface to draw bounding boxes, select Labels, or enter text. Annotations can also be reviewed and verified by other annotators or team Members, to ensure accuracy and consistency. Some common types of Annotations include:

- Bounding Boxes - Used to identify the location and size of objects within images or videos;
- Classification Labels - Used to categorize Items based on their content or characteristics;
- Text Transcriptions - Used to convert spoken words or written text into machine-readable formats;
- Semantic Segmentation Masks - Used to identify and segment different regions or objects within an image. Note: A JSON format representing the objects and labels exists in an Item.

Here's a list of the most important Annotation reqeusts:
- [List all Annotations of a specific Item, by ID](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetItemAnnotationsListAnnotations);
- [Create an Annotation for an Item](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetItemAnnotationsCreateAnnotation);
- [List an Annotation of an Item by Annotation ID](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetItemAnnotationsGetAnnotation);
- [Delete an Annotation from an Item](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetItemAnnotationsDeleteAnnotation);
- [Update an Item's Annotation](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetItemAnnotationsUpdateAnnotation);
- [Update an Item's Annotation status to issue](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetItemAnnotationsAnnotationIssues);
- [List the Log for all Annotations  of an Item](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetItemAnnotationsLogListAnnotationsLog);
- [List the Log for a specific Annotation  of an Item](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetItemAnnotationsLogGetAnnotation);
- [Delete Annotation Log for a specific Annotation](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetItemAnnotationsLogDeleteAnnotation);
- [Update an Item's Annotation Log](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetItemAnnotationsLogUpdateAnnotation);
- [Update an Item's Annotation status to issue](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetItemAnnotationsLogAnnotationIssues);
- [Query Annotations for a specified Dataset](https://gate.dataloop.ai/api/v1/docs/#/Annotations/DatasetAnnotationsQueryAnnotations);
- [List all Annotations of an item by Annotation ID](https://gate.dataloop.ai/api/v1/docs/#/Annotations/AnnotationsGetAnnotation).

## <a name="Tasks"></a>Tasks 
This section explore how to use the API to create and manage Annotation Tasks. A Task in Dataloop is a unit of work that needs to be completed by an individual or a team. A Task can represent any type of activity, such as annotating data, reviewing Annotations, labeling images, performing Quality Assurance (QA) checks, or any other data-related Task that requires human input. Tasks in the Dataloop system are created by Project managers, who define the specific requirements for each Task, such as the type of data to be labeled, the Annotation instructions, the deadline, and the number of annotators required. Tasks are then assigned to individual annotators or teams of annotators who complete the Task according to the specified requirements.

Here are the most important API requests for Tasks:
- [Create a new Task](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksCreateTask);
- [Find tasks by a Query](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksFindTasks);
- [Add work (or items to be annotated) to an existing Task](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksAddItemsToTask);
- [Update an existing Task](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksPatchTask);
- [Get a specific task by ID](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksGetTask);
- [Delete a task](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksDeleteTask).


## <a name="Assignments"></a>Assignments
An Assignment is a specific Task that is assigned to an individual, represents a unique instance of an Assignment, and contains all the information necessary for annotators to complete the work. As Annotators work on the Assignment, Annotators can communicate with Project Managers or team leaders and can ask for clarification on any aspects of the Task that are unclear. Once an Assignment is completed, the Dataloop system automatically aggregates the results and provides Project managers with real-time insights into the progress of each Assignment, the quality of the Annotations, and the overall status of the Project.

An Assigment may be an Item or collection of Items that are allocated to an Annotator for manual annotation and/or review. Items can be redistributed or reassigned between Assignments. The Annotator is also referred to as an “Assignee” or "Contributor".

Here are the most important API requests for Assignments:
- [Create a new Assignment](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsCreateAssignment);
- [Find Assignments using a Query](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsFindAssignments);
- [Update an existing Assignment](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsPatchAssignment);
- [Get a specific Assignment](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsGetAssignment);
- [Delete a assignment](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsDeleteAssignment);
- [Reassign Assignment to an Annotator](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsReassignAssignment);
- [Redistribute an Assignment to Annotators](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsRedistributeAssignment).


## <a name="Organization"></a>Organization
This section explores the most important API requests you can use to manage your Organization. In Dataloop, an Organization is an entity composed of one or more users who collaborate on data-related Projects and share Resources and data. An Organization is composed of multiple elements like Integration/Secrets, Members, Bots, and ComputerCache. The leader of an Organization is the Owner. An Owner in Dataloop represents the User who created the Organization.  An owner can delete/rename an Organization, create Projects, and add/remove Organization Members. The Owner cannot be removed from the Organization.

Here are the most important API request regarding Organizations:
- [List all of the Organization's Projects](https://gate.dataloop.ai/api/v1/docs#/Organization/get_orgs__org_id__projects);
- [List all of the Projects of an User in your Organization](https://gate.dataloop.ai/api/v1/docs#/Organization/get_orgs__org_id__members__user_id__projects);
- [Add a new member into the Organization](https://gate.dataloop.ai/api/v1/docs#/Organization/post_orgs__org_id__members);
- [Get a specific Organization by ID](https://gate.dataloop.ai/api/v1/docs#/Organization/get_orgs__org_id_);
- [Delete an Organization (must be Owner)](https://gate.dataloop.ai/api/v1/docs#/Organization/delete_orgs__org_id_);
- [Update an Organization](https://gate.dataloop.ai/api/v1/docs#/Organization/patch_orgs__org_id__plan).

## <a name="Services"></a>Services
This section explores the most important API reuqests you can use to manage Sevices. A Service or FaaS (Function-as-a-Service), is a cloud computing model where a cloud provider manages and runs individual functions in response to events or Triggers. In Dataloop, a FaaS Service is a serverless computing Service that allows users to run code without the need to manage servers or infrastructure. The FaaS Service is a key component of the system architecture, providing a platform for executing code and integrating with other Services in the system. The FaaS Service in Dataloop is designed to handle the Execution of small, isolated functions that can be triggered by a variety of events, such as data input from sensors or user actions.

A service can also be thought as a deployed Package that serves the code. Given the matching input to a function, it will run it and return the output, e.g. if we have code in our Package for converting RGB images to grayscale, the dl.Service would run the code and upload the grayed image (the processing would be done on the Cloud, and we would receive only the output of that Cloud processing).

Here are the most important API requests for Services:
- [Add a Service notification](https://gate.dataloop.ai/api/v1/docs#/Services/Services_notify);
- [Get all global services by using a list of Project ID and Service name](https://gate.dataloop.ai/api/v1/docs#/Services/Services_getGlobalServices);
- [Add or remove Cache for the Organization](https://gate.dataloop.ai/api/v1/docs#/Services/Services_cache);
- [Add or remove Fs-Cache for the Organization](https://gate.dataloop.ai/api/v1/docs#/Services/Services_fsCache);
- [Get a list of Services based on Query parameters](https://gate.dataloop.ai/api/v1/docs#/Services/Services_listServices);
- [Create new Service/Package](https://gate.dataloop.ai/api/v1/docs#/Services/Services_createService);
- [Get a Service by ID and version](https://gate.dataloop.ai/api/v1/docs#/Services/Services_getService);
- [Update a Service](https://gate.dataloop.ai/api/v1/docs#/Services/Services_updateService);
- [Delete a Service](https://gate.dataloop.ai/api/v1/docs#/Services/Services_deleteService);
- [Get service revisions by ID](https://gate.dataloop.ai/api/v1/docs#/Services/Services_getServiceRevisions);
- [Pause the execution of a Service](https://gate.dataloop.ai/api/v1/docs#/Services/Services_stopService);
- [Resume the execution of a Service](https://gate.dataloop.ai/api/v1/docs#/Services/Services_resumeService);
- [Get the logs for a Pipeline](https://gate.dataloop.ai/api/v1/docs#/Services/Services_getLogs);
- [Get the logs for a Service by using Service ID](https://gate.dataloop.ai/api/v1/docs#/Services/Services_getServiceLogs);
- [Update a Replica's Status](https://gate.dataloop.ai/api/v1/docs#/Services/Services_updateReplicaStatus);
- [Get the status of a Service](https://gate.dataloop.ai/api/v1/docs#/Services/Services_getServiceStatus);
- [Rollout a Service](https://gate.dataloop.ai/api/v1/docs#/Services/Services_rolloutService);
- [Debug a Service's Stream](https://gate.dataloop.ai/api/v1/docs#/Services/Services_serviceStream);\
- [Apply docker private registry credentials on the user's compute system](https://gate.dataloop.ai/api/v1/docs#/compute/Compute_registryCred);
- [Delete docker private registry credentials from the user compute system](https://gate.dataloop.ai/api/v1/docs#/compute/Compute_deleteRegistryCred).


## <a name="Packages"></a>Packages
This section explores the most important API requests regrding Packages. A Package refers to an entity that is processed using the "Functions-as-a-Service" (FaaS) technology. FaaS Packages are used to automate the processing of data and can be used to perform a wide range of Tasks, such as data cleaning, data transformation, and data enrichment. FaaS Packages in the Dataloop system are created by Project managers or data scientists, who define the specific requirements for each Package, such as the data inputs, the functions to be executed, and the output data format. Once the FaaS Package is defined, it can be executed using the Dataloop FaaS engine, which automatically manages the Execution of the functions within the Package. The Package is a static code with a schema that holds all the Modules, functions, and the code base from which they can be taken.

A Package could also be thought as a bundle of code and definitions that can be used for creating models or deploying services. Code is a dl.Codebase entity, and definitions include modules, functions, IOs, and the code entry point. For now, it can be Python, nodeJS format. The main function of Packages is to deploy a Service and create an executable version of that code. Packages can be public, global, or specific to a particular Project.

Here are the most important API requests regarding Packages:
- [Get a list of Packages](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_listPackages);
- [Create a new Package](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_createPackage);
- [Get a Package by ID](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_getPackage);
- [Update Package](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_updatePackage);
- [Get Package revisions by ID](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_getPackageRevisions);
- [Delete a Package by ID](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_deletePackages).

## <a name="Executions"></a>Executions
This section explores the most important API requests regrding Executions. An Execution refers to the process of executing a function within the FaaS Service. When a user submits a function for Execution, the FaaS Service creates a container to run the function and provides any necessary inputs. The function is executed within the container, and the results are returned to the user.

Here are the most important API requests regarding Packages:
- [Get an execution by ID](https://gate.dataloop.ai/api/v1/docs#/Executions/Executions_getExecution);
- [Update execution changes to Dataloop's platform](https://gate.dataloop.ai/api/v1/docs#/Executions/Executions_updateExecution);
- [Increment the number of attempts that an execution is allowed to try to run a Service that is not responding](https://gate.dataloop.ai/api/v1/docs#/Executions/Executions_incrementExecutionAttempts);
- [Get Execution Counters](https://gate.dataloop.ai/api/v1/docs#/Executions/Executions_getExecutionCounters);
- [List a Service's Executions](https://gate.dataloop.ai/api/v1/docs#/Executions/Executions_listExecutions);
- [Re-run an Execution](https://gate.dataloop.ai/api/v1/docs#/Executions/Executions_rerunExecution);
- [Re-run batch Execution](https://gate.dataloop.ai/api/v1/docs#/Executions/Executions_rerunExecutionQuery);
- [Execute a function on an existing Service](https://gate.dataloop.ai/api/v1/docs#/Executions/Executions_createExecution);
- [Update Execution progress](https://gate.dataloop.ai/api/v1/docs#/Executions/Executions_pushProgress);
- [Terminate an Execution using ID](https://gate.dataloop.ai/api/v1/docs#/Executions/Executions_terminateExecution).


## <a name="Pipelines"></a>Pipelines
Pipelines allow you to create automated flows that weave together humans and machines to process data in a Pipeline architecture. Pipelines consist of a series of Nodes, where each Node’s output is the input of the next one. They allow for transitioning of data between labeling and QA Tasks, FaaS (see entry for Package), and code snippets and, machine learning (ML) models. It is flexible and scalable and can be used for both training and production. Common examples of use cases include automatic pre-processing of data for Annotation workflows and deployment Pipelines for ML models.

Here are the most important API calls for Pipelines:
- [Create a Pipeline](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_create);
- [Get a Pipeline by ID](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_get);
- [Update a Pipeline](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_update);
- [Update a Pipeline's Settings](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_updateSettings);
- [Get a Pipeline's statistics](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_getStatistics);
- [Reset a Pipeline's counters](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_reset);
- [Delete the Pipeline - should also terminate the composition](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_terminate);
- [Execute a Pipeline and return the Pipeline execution as an object](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_execute);
- [Get one of Pipeline nodes by pipeline id and node id](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_getNode);
- [List Pipelines using a Query](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_list);
- [Install Pipeline](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_install);
- [Uninstall Pipeline](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_uninstall);
- [Purge Pipeline](https://gate.dataloop.ai/api/v1/docs#/pipelines/Pipeline_purge);
- [See a Pipeline's Executions](https://gate.dataloop.ai/api/v1/docs#/pipelines/PipelineExecution_executions);
- [See a Pipeline's logs](https://gate.dataloop.ai/api/v1/docs#/pipelines/PipelineLogs_logs);
- [Create Pipeline Template](https://gate.dataloop.ai/api/v1/docs#/pipelines%2Ftemplates/PipelineTemplates_create);
- [Querry Pipeline Template](https://gate.dataloop.ai/api/v1/docs#/pipelines%2Ftemplates/PipelineTemplates_query).


## <a name="Composition"></a>Composition
FaaS Functions give you the ability to quickly deploy services that have small functionality. But any more complex use cases requires multiple functions to work together. Function composition refers to combining single functions to create bigger, more complex functions. [Read more about Composing Pipelines here](https://dataloop.ai/docs/composing-pipelines).

Here are the most important API requests regarding Compositions:
- [Create a new Composition](https://gate.dataloop.ai/api/v1/docs#/compositions/Composition_create);
- [Get Compositions by Querry](https://gate.dataloop.ai/api/v1/docs#/compositions/Composition_list);
- [Get an Composition updated Object from the database](https://gate.dataloop.ai/api/v1/docs#/compositions/Composition_get);
- [Update an existing Composition](https://gate.dataloop.ai/api/v1/docs#/compositions/Composition_update);
- [Install an existing Composition](https://gate.dataloop.ai/api/v1/docs#/compositions/Composition_install);
- [Uninstall existing Composition](https://gate.dataloop.ai/api/v1/docs#/compositions/Composition_uninstall);
- [Delete the composition](https://gate.dataloop.ai/api/v1/docs#/compositions/Composition_terminate).


## <a name="Triggers"></a>Triggers
A Trigger is a rule-based mechanism that initiates an action when a specific event occurs. Triggers are used to automate workflows and streamline data processing. They are created by defining a set of conditions that must be met for the Trigger to be activated. These conditions can be based on a variety of factors, such as the content of data, the time of day, or the occurrence of specific events. Once a Trigger is activated, it can initiate a range of actions, such as sending notifications, generating reports, or Triggering the Execution of a specific Task or workflow. It can be of 2 types:

EventTrigger - contains a Project on which it monitors events, a Resource type such as Item, Annotation, Task, etc. The action that happened to the Resource such as created, updated, deleted status changed, etc. a DQL (The Data Query Engine) Filter that checks whether or not to invoke the operation based on the Resource JSON, and an operation.
CRONTrigger - enables you to run functions at specified time patterns with constant input using the Cron syntax. In the Cron Trigger specification, you specify when you want the Trigger to start, when you want it to end, specifying when it should run, and the input that should be sent to the action.

Here are the most important API requests for Triggers:
- [List Triggers and retrieves Services using a Query](https://gate.dataloop.ai/api/v1/docs#/Triggers/Triggers_listTriggers);
- [Create a Trigger - can create two types: a cron-trigger or an event-trigger](https://gate.dataloop.ai/api/v1/docs#/Triggers/Triggers_createTrigger);
- [Get Trigger by ID](https://gate.dataloop.ai/api/v1/docs#/Triggers/Triggers_getTrigger);
- [Update a Trigger](https://gate.dataloop.ai/api/v1/docs#/Triggers/Triggers_updateTrigger);
- [Delete a Trigger](https://gate.dataloop.ai/api/v1/docs#/Triggers/Triggers_deleteTriggers);
- [Querry a Trigger's resource information](https://gate.dataloop.ai/api/v1/docs#/TriggerResourceInformation/TriggerResourceInformation_queryTriggerResourceInformation).


## <a name="Features"></a>Features
A Feature vector is a numerical representation of an object or entity, typically used in machine learning and data analysis. It consists of a list of Features or Attributes that describe the object in a quantitative manner. A Feature set, on the other hand, is a collection of Feature vectors that are used to train a machine-learning algorithm. The Feature set contains all the necessary Features that are relevant to the problem being solved and is used to extract meaningful patterns and relationships from the data. The Dataloop system enables Feature vector augmentations on both Items and Annotations, this capability grants users the ability to search and Filter Annotations and Items according to their ‘similarity’ in the euclidean space.

Here are the most important API requests regarding Features:
- [Get Feature Vectors by creator](https://gate.dataloop.ai/api/v1/docs#/features/FeatureVectorsGetFeatureVectors);
- [Add new Feature Vector](https://gate.dataloop.ai/api/v1/docs#/features/FeatureVectorsAddFeatureVectors);
- [Get a Feature Vector by ID](https://gate.dataloop.ai/api/v1/docs#/features/FeatureVectorsGetFeatureVector);
- [Delete a Feature Vector by ID](https://gate.dataloop.ai/api/v1/docs#/features/FeatureVectorsDeleteFeatureVector);
- [Query Feature Vectors](https://gate.dataloop.ai/api/v1/docs#/features/FeatureVectorsQueryFeatures);
- [Get a feature set by ID](https://gate.dataloop.ai/api/v1/docs#/features/FeatureSetsGetFeatureSets);
- [Add a new feature set](https://gate.dataloop.ai/api/v1/docs#/features/FeatureSetsAddFeatureSets);
- [Get a feature set by ID](https://gate.dataloop.ai/api/v1/docs#/features/FeatureSetsGetFeatureSet);
- [Delete a feature set by ID](https://gate.dataloop.ai/api/v1/docs#/features/FeatureSetsDeleteFeatureSet);
- [Update a feature set by ID](https://gate.dataloop.ai/api/v1/docs#/features/FeatureSetsEditFeatureSet).

Feature API requests focused on Vectors:
- [Get Feature Vectors by creator](https://gate.dataloop.ai/api/v1/docs#/vectors/FeatureVectorsGetFeatureVectors);
- [Add anew Feature Vector](https://gate.dataloop.ai/api/v1/docs#/vectors/FeatureVectorsAddFeatureVectors);
- [Get a Feature Vector by ID](https://gate.dataloop.ai/api/v1/docs#/vectors/FeatureVectorsGetFeatureVector);
- [Delete a Feature Vector by ID](https://gate.dataloop.ai/api/v1/docs#/vectors/FeatureVectorsDeleteFeatureVector);
- [Query Feature Vectors](https://gate.dataloop.ai/api/v1/docs#/vectors/FeatureVectorsQueryFeatures).

Feature API requests focused on Feature Sets:
- [Get all Feature Sets](https://gate.dataloop.ai/api/v1/docs#/sets/FeatureSetsGetFeatureSets);
- [Add a new Feature Set](https://gate.dataloop.ai/api/v1/docs#/sets/FeatureSetsAddFeatureSets);
- [Get a Feature Set by ID](https://gate.dataloop.ai/api/v1/docs#/sets/FeatureSetsGetFeatureSet);
- [Delete a Feature Set by ID](https://gate.dataloop.ai/api/v1/docs#/sets/FeatureSetsDeleteFeatureSet);
- [Update a feature set by ID](https://gate.dataloop.ai/api/v1/docs#/sets/FeatureSetsEditFeatureSet).


## <a name="Models"></a>Models
A Model entity in Dataloop refers to a machine learning algorithm that has been trained on labeled data to make predictions or perform other Tasks. Models are a key component of the Dataloop system, as they enable users to apply machine-learning techniques to a wide range of data types, including images, text, and audio. The system has several pre-installed and publicly available model architectures, which can be installed in your Project and trained with your data to achieve the pre-annotation of your labels such as ResNet, Yolo-V5, U-net. A Dataloop Model is a combination of data (dl.Dataset), configurations (json dictionary), and code (dl.Package) to represent a learnable instance of the data. You can train, evaluate, compare, and deploy a dl.Model in Dataloop.

Here are the most important API requests for Models:
- [Get the details of a Model using ID](https://gate.dataloop.ai/api/v1/docs#/Models/Get%20Model);
- [Update a Model](https://gate.dataloop.ai/api/v1/docs#/Models/Update%20Model);
- [Delete a Model](https://gate.dataloop.ai/api/v1/docs#/Models/Delete%20Model);
- [Get models by using a Query](https://gate.dataloop.ai/api/v1/docs#/Models/List%20Models);
- [Create a new Model](https://gate.dataloop.ai/api/v1/docs#/Models/Create%20Model);
- [Query Models](https://gate.dataloop.ai/api/v1/docs#/Models/Query%20Models);
- [Train a Model](https://gate.dataloop.ai/api/v1/docs#/Models/Train%20Model);
- [Model Prediction](https://gate.dataloop.ai/api/v1/docs#/Models/Model%20Prediction);
- [Evaluate a Model](https://gate.dataloop.ai/api/v1/docs#/Models/Evaluate%20Model);
- [Deploy a Model](https://gate.dataloop.ai/api/v1/docs#/Models/Deploy%20Model);
- [Clone a Model](https://gate.dataloop.ai/api/v1/docs#/Models/Clone%20Model);
- [Show the latest Model executions](https://gate.dataloop.ai/api/v1/docs#/Models/Models%20Executions);
- [Show the latest Model Services](https://gate.dataloop.ai/api/v1/docs#/Models/Models%20Services);
- [Show all Dataset that the Model has been assigned to](https://gate.dataloop.ai/api/v1/docs#/Models/Models%20Datasets%20Count).

Model Metrics can also be used to analyse your Models and extract important insights from them, using these API requests:
- [Generate Model Metrics Report](https://gate.dataloop.ai/api/v1/docs#/Model%20Metrics/Generate%20Model%20Metrics%20Report);
- [Publish Model Metrics](https://gate.dataloop.ai/api/v1/docs#/Model%20Metrics/Publish%20Model%20Metrics);
- [Delete a Metric](https://gate.dataloop.ai/api/v1/docs#/Model%20Metrics/Delete%20Metric);
- [Query Model Metrics](https://gate.dataloop.ai/api/v1/docs#/Model%20Metrics/Query%20Model%20Metrics).

## <a name="Applications"></a>Applications
Here are the most important API requests for Applications:
- [Install a new Application](https://gate.dataloop.ai/api/v1/docs#/apps/App_install);
- [Update an existing Application](https://gate.dataloop.ai/api/v1/docs#/apps/App_update);
- [Get an Application updated object from the database](https://gate.dataloop.ai/api/v1/docs#/apps/App_get);
- [Uninstall a running Application(will remove all the components belonging to the app)](https://gate.dataloop.ai/api/v1/docs#/apps/App_uninstall);

DPK Applications API requests:
- [Publish an DPK Application](https://gate.dataloop.ai/api/v1/docs#/dpk/Dpk_publish);
- [Get an dpk updated object from the database](https://gate.dataloop.ai/api/v1/docs#/dpk/Dpk_get);
- [Delete an dpk Application](https://gate.dataloop.ai/api/v1/docs#/dpk/Dpk_deleteOne);
- [Get the revisions of a dpk by name](https://gate.dataloop.ai/api/v1/docs#/dpk/Dpk_getRevisions);
- [Querry DPK](https://gate.dataloop.ai/api/v1/docs#/dpk/Dpk_query).




## <a name="Examples"></a>Examples

### Example 1: Show all datasets
To show all of the datasets in your organization (or in a particular project, if you want to), you can use the ```GET/datasets``` API request. Go to the Datasets section, look for it and click it. It should look like this once selected:

![image](https://user-images.githubusercontent.com/58508793/224307707-27a41a69-9a95-4d0c-86e3-c9e2b245e829.png)

Click the "Try it out" button, and you will be able to complete the "name", "creator" and "projects" fields, to search for datasets matching specific criteria. You should firstly Execute without completing any of the fields. This will show you all of the Datasets you have access to, as seen below:

![image](https://user-images.githubusercontent.com/58508793/224308368-f0dcf9bc-0bd1-4baf-9e18-fb567a250790.png)

All of the information you requested, based on your Query should be in the "Response Body".

**Note**: If you have no dataset created, you can create one using the ```POST/datasets```, which is located just below the ```GET/datasets```.


### Example 2: GET a Dataset's Item count
By using a simple Query on the Datasets endpoint, you can use the Dataset ID and Query to get the requested items.

To do that, you must first find out the ```ID``` of the dataset you wish to Query. To find a Dataset ID, you can just click the ```Get\datasets``` API line (which we described above), which will return the details about all of the Datasets to which you have access in the Dataloop platform. You can also add the name of the Dataset as a parameter to the Query, search by Creator or by the Project name. Below, the Query is executed by using the Dataset name "Creatures", which is a Dataset used in one of [Dataloop's Python SDK Onboarding Exercises](../onboarding/11_onboarding_exercise.md) (be sure to use your own Dataset's name or ID):
![image](https://user-images.githubusercontent.com/58508793/219678882-765f6257-e92e-48dc-a0ad-70fba382227c.png)

The response to this ```GET``` Query can be seen below, including the dataset ID. Be sure to copy this ID, as we will use it in a moment (the ID you see after running the ```GET``` command on **your own dataset**):
![image](https://user-images.githubusercontent.com/58508793/219679455-89d26a5d-5303-43b8-b3af-86002bf3bb8d.png)

Filters can be used to specify diferent criteria that can be used to more accurately search for the information you want to find. In the image below, you can see how to input the Dataset ID and a specific Query.
![image](https://user-images.githubusercontent.com/58508793/218518081-65d657d6-a4c2-4443-8046-e1791b0fa2cd.png)

As you can observe in the Response Body, the "Creatures" Dataset has a total of 1132 Items. You can also observe that various other pieces of information can be found in the Response Body.


### Example 3: GET a list of Projects 

Let's now test an example of a basic Project API request. Go ahead and scroll down until you find the "Projects" section. 

![image](https://user-images.githubusercontent.com/58508793/219648842-aba4b7ff-c26d-4315-ab71-2eaf719e8732.png)


Now,  select the first GET method, to get all of the projects and  then click "Try it out", like in the image below:
![image](https://user-images.githubusercontent.com/58508793/219650991-266730c4-debf-4fcc-9b37-a327b4af6145.png)


Click the big ```Execute``` button:
![image](https://user-images.githubusercontent.com/58508793/219651137-475d2a9d-cdd3-4c70-b98d-18a0f1d0daee.png)

You should now instantly recieve a response in JSON format that shows all Projects to which you have access, similar to the image below:

![image](https://user-images.githubusercontent.com/58508793/219651466-b6cc5956-440a-41f9-984d-d853d3c4ed85.png)

In the ```Response Body``` you will receive all of the details and inforamtion that the command you ran returns. Feel free to try more commands in the ```Projects``` section on your own.

### Example 4: List a Project's Recipes
In this example, we will retrieve a list of all of the Recipes that are available in a given project, by using a Project's ID. [Click here to go to the "Get/recipes" section](https://gate.dataloop.ai/api/v1/docs#/Recipes/RecipesFindRecipes). Then, as usual, click on the "Try it out" button, and you should see this:

![image](https://user-images.githubusercontent.com/58508793/225086132-f19a65e4-498c-4281-857c-8f3bba90da4f.png)

As you can observe, there are multiple paramenters you can complete, but the most critical field  is the "Projects" in which you need to add an array representing the Project's ID. As you can see, that field was already filled using our "CreatureHun" Project's ID. In you case, you will need to find the ID of the Project you want to Querry and replace the ID you see in the image with your own Project ID. You can find a Project's ID using the [Get Projects] (https://gate.dataloop.ai/api/v1/docs#/Projects/get_projects) API request (which will list all active projects) - or you can go the web version of Dataloop, select your project and then look at the URL, where you will find the Project's ID:

![image](https://user-images.githubusercontent.com/58508793/225088107-e7566b7c-9552-4ed1-bb66-590b49f616a0.png)

After you complete the ID field (and any other fields you wish) and execute, you should see something similar to this, in the Response Body:

![image](https://user-images.githubusercontent.com/58508793/225087359-4d62a8bc-49f2-4a6c-bbec-d1cc62e8d1d5.png)


### Example 5: Show Items from a Dataset
In this example we will show all of the Items from a Dataset. To do so, you have to go to the ["Get Items" API request](https://gate.dataloop.ai/api/v1/docs#/Items/DatasetItemsGetItems) of the Items section. Once there , you should press "Try Out" and you will see this:

![image](https://user-images.githubusercontent.com/58508793/225089839-3f2f79f4-5aa0-4c46-81b3-63f1e982d238.png)

To execute the API request, you must at least provide the Dataset's ID. You can also use an URL encoded JSON Query, if you want to filter for specific Items. To find your Dataset's ID, you can either got  to the "Get/datasets" request and use it to list your Dataset and ID, you go to the web-version of Dataloop, and you will find the ID in the URL, as you can see below:
![image](https://user-images.githubusercontent.com/58508793/225090815-54e95e00-e6ff-4004-b425-9c2f14d59fcf.png)

The Dataset ID is found immediately after the "/datasets/". You can then use that ID to show all of the Items inside of the Dataset. After running the "Get/items" request, you should get something similar to what you can see below - which is a counter of all of the Items extracted and various details about each of those Items: 

![image](https://user-images.githubusercontent.com/58508793/225090358-44dd83b8-c8dd-47cc-a6c5-9be323827bf1.png)

### Example 6: Find all Tasks in a Project
In this examples, we will list all of the Tasks that were created as part of a specific Project. To do this, you must go to the ["Get/annotationtasks"](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksFindTasks). As usual, press the "Try Out" button, and a screen where you must provide various parameters will open up:

![image](https://user-images.githubusercontent.com/58508793/225092785-ecd8a6a6-c5f5-485f-ad62-7326272b06c4.png)
 
Here, you can use a Project's ID, and filter using other paramenters, like Dataset, Task Name, Creator, etc. which will help you filter so you can find the specific Task you are looking for. If you are using only the Project's ID as in the example above, you will get all of the Tasks that were assigned to that project. You can see that in the Response Body, below, after executing the request:

![image](https://user-images.githubusercontent.com/58508793/225093480-e2c513f7-4275-4839-b779-6332865e3ca3.png)

### Example 7: List all Projects from a specific Organization
In this example, we will add a new User to be a part of a specific Organization. To do that, you must first [go to the "GET/orgs/{org_id}/projects"](https://gate.dataloop.ai/api/v1/docs#/Organization/get_orgs__org_id__projects) in the Organization section. After that, use the "Try it out" button, and you should see something simmilar to what you see below:

![image](https://user-images.githubusercontent.com/58508793/225096445-c5381326-e174-4e05-8d94-46c37dbab348.png)

You will need to find out your Organization's ID to perform this request. To do that, you need to go to the web-version of Dataloop, select the Organization you want, and then go to the "Orgamization Overview" section. There, you will find the ID of the active Organization in the site URL, like you can observe below:

![image](https://user-images.githubusercontent.com/58508793/225097020-111fcdf0-3a62-4875-a147-aa778aafb71f.png)

You can then use that ID in the ["GET/orgs/{org_id}/projects"](https://gate.dataloop.ai/api/v1/docs#/Organization/get_orgs__org_id__projects) request and press the Execute button. You should then see a list of details about your Organization, and then a list of all of the Projects (and  Project details) of that Organization - as you can observe below:
![image](https://user-images.githubusercontent.com/58508793/225099630-0cd0001b-fa8b-4db4-a234-0c30b6f62523.png)

**Note:** You can also use this request to find the Project IDs for the projects of a specific Organization, when needed.





## Custom Querries
Implementing  Custom Queries will allow you to better Search, Filer, Sort and Update your data. If you want to do that, you can [learn more about the Dataloop Query Language (DQL), our proprietary Query Language](https://dataloop.ai/docs/api-dql).


## Final Words

There are a lot more API Requests, Commands and Queries you can try on your own. Be sure to have a look around and learn how to use them.

If you have any troubles, be sure to [Contact Dataloop's Support](https://dataloop.ai/contact/).

You can also [Book a Demo](https://dataloop.ai/demo/), if you want to have someone teach you more about the API and the Dataloop platform in general.


