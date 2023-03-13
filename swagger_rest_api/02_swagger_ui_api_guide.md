# Swagger UI API Documentation

Dataloop's [Swagger UI](https://gate.dataloop.ai/api/v1/docs) offers the ability to perform API Requests such as ```GET```, ```POST```, ```PUT```, ```PATCH``` and 
```DELETE``` to different endpoints in our backend services like Projects, Datasets, Tasks, etc. It makes the process extremely easy and intuitive. With only a few clicks, you can run commands to get any information you may require about your Projects, Items, Datasets, Tasks or any other entity that is part of Dataloop.

In order to use the Swagger UI you will need to already be logged in to the Dataloop platform. If you haven't logged in yet, you need to [do that now](https://console.dataloop.ai/welcome) for the API requests to work. 

After logging in to the platform, the API authentication will be completed automatically.  If you logged in to Dataloop's Platform and then returned to the API page after completing the log in process, **refresh the page** and you will be able to run the API requests.
![image](https://user-images.githubusercontent.com/58508793/218516500-43b289ff-2e44-42e3-96be-5353cd1e7f76.png)

The image above is what you should see after logging in to Dataloop's platform, and going to the Swagger API UI. You can [find the Dataloop Swagger API here](https://gate.dataloop.ai/api/v1/docs/).

**Note:** This Swagger API guide will have the same structure as our [Developer Onboarding](../onboarding), which teaches you how to use the basic functions of Dataloop in Python code. Everything we'll cover in this guide can be done in Python code (in the Python SDK) as well as using the API.

## Projects 

This section explores the various API requests you can use to manage Projects in Dataloop. A Project in Dataloop is a high-level Organizational entity that represents a specific task or goal. It can be used to manage data, Tasks, and Annotations related to a particular Project, and often serves as the main unit of work in the system. It provides a centralized location for managing data and Tasks related to a specific goal or objective. This can help improve collaboration among team members, ensure consistency in the data and Annotations, and make it easier to track progress and results.

Here's a list of the most important Project requests:
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
- [Replace an account for a Project](https://gate.dataloop.ai/api/v1/docs/#/Projects/patch_projects__project_id__accounts);


## Datasets
This section will cover the most important API examples, using the API requests from the Datasets section. A Dataset is a collection of Items (files), their Metadata, and Annotations. A Dataset can have a file-system-like structure, with folders and subfolders at any level. There are different types of Datasets:

- Master - Original Dataset, managing the actual binaries;
- Clone - Contains pointers to original files, enabling management of virtual Items that do not replicate the binaries of the underlying storage once cloned or copied. When cloning a Dataset, users can decide if the new copy will contain Metadata and Annotations created over the original Dataset;
- Merge - Multiple Datasets can be merged into one, enabling multiple Annotations to be merged onto the same Item (for 2 Datasets to be successfully merged, they need to have the same Recipe and Ontology.

The most important API request can be seen below:
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
- [Get a Project's Datasets](https://gate.dataloop.ai/api/v1/docs/#/Datasets/DatasetsGetProjectDatasets);




## Items
The Items section of the API helps you do a variety of requests regarding Items. An Item in Dataloop, is a unit of data that represents a ‘single instance’ or ‘file’ of a larger Dataset. It can be an image, a video, a sound recording, a text document, or any other type of digital asset that needs to be labeled, annotated, or analyzed. Each Item in the Dataloop system is typically associated with one or more Tasks, which define the specific operations that need to be performed on the Item. For example, an Item may be labeled with Bounding Boxes to identify objects in an image, transcribed to convert speech-to-text, or classified based on its content. Items also have associated Metadata.

Here are some of the most important requests (with links) and their functionality:
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
- [Clone Item](https://gate.dataloop.ai/api/v1/docs/#/Items/DatasetItemsCloneItem);


## Annotations
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
- [List all Annotations of an item by Annotation ID](https://gate.dataloop.ai/api/v1/docs/#/Annotations/AnnotationsGetAnnotation);

## Tasks 
This section explore how to use the API to create and manage Annotation Tasks. A Task in Dataloop is a unit of work that needs to be completed by an individual or a team. A Task can represent any type of activity, such as annotating data, reviewing Annotations, labeling images, performing Quality Assurance (QA) checks, or any other data-related Task that requires human input. Tasks in the Dataloop system are created by Project managers, who define the specific requirements for each Task, such as the type of data to be labeled, the Annotation instructions, the deadline, and the number of annotators required. Tasks are then assigned to individual annotators or teams of annotators who complete the Task according to the specified requirements.

Here are the most important API requests for Tasks:
- [Create a new Task](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksCreateTask);
- [Find tasks by a Query](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksFindTasks);
- [Add work (or items to be annotated) to an existing Task](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksAddItemsToTask);
- [Update an existing Task](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksPatchTask);
- [Get a specific task by ID](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksGetTask);
- [Delete a task](https://gate.dataloop.ai/api/v1/docs#/Tasks/TasksDeleteTask);


## Assignments
An Assignment is a specific Task that is assigned to an individual, represents a unique instance of an Assignment, and contains all the information necessary for annotators to complete the work. As Annotators work on the Assignment, Annotators can communicate with Project Managers or team leaders and can ask for clarification on any aspects of the Task that are unclear. Once an Assignment is completed, the Dataloop system automatically aggregates the results and provides Project managers with real-time insights into the progress of each Assignment, the quality of the Annotations, and the overall status of the Project.

An Assigment may be an Item or collection of Items that are allocated to an Annotator for manual annotation and/or review. Items can be redistributed or reassigned between Assignments. The Annotator is also referred to as an “Assignee” or "Contributor".

Here are the most important API requests for Assignments:
- [Create a new Assignment](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsCreateAssignment);
- [Find Assignments using a Query](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsFindAssignments);
- [Update an existing Assignment](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsPatchAssignment);
- [Get a specific Assignment](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsGetAssignment);
- [Delete a assignment](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsDeleteAssignment);
- [Reassign Assignment to an Annotator](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsReassignAssignment);
- [Redistribute an Assignment to Annotators](https://gate.dataloop.ai/api/v1/docs#/Assignments/AssignmentsRedistributeAssignment);


## Organization
This section explores the most important API requests you can use to manage your Organization. In Dataloop, an Organization is an entity composed of one or more users who collaborate on data-related Projects and share Resources and data. An Organization is composed of multiple elements like Integration/Secrets, Members, Bots, and ComputerCache. The leader of an Organization is the Owner. An Owner in Dataloop represents the User who created the Organization.  An owner can delete/rename an Organization, create Projects, and add/remove Organization Members. The Owner cannot be removed from the Organization.

Here are the most important API request regarding Organizations:
- [List all of the Organization's Projects](https://gate.dataloop.ai/api/v1/docs#/Organization/get_orgs__org_id__projects);
- [List all of the Projects of an User in your Organization](https://gate.dataloop.ai/api/v1/docs#/Organization/get_orgs__org_id__members__user_id__projects);
- [Add a new member into the Organization](https://gate.dataloop.ai/api/v1/docs#/Organization/post_orgs__org_id__members);
- [Get a specific Organization by ID](https://gate.dataloop.ai/api/v1/docs#/Organization/get_orgs__org_id_);
- [Delete an Organization (must be Owner)](https://gate.dataloop.ai/api/v1/docs#/Organization/delete_orgs__org_id_);
- [Update an Organization](https://gate.dataloop.ai/api/v1/docs#/Organization/patch_orgs__org_id__plan);

## Services (FaaS)
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
- [Debug a Service's Stream](https://gate.dataloop.ai/api/v1/docs#/Services/Services_serviceStream);

## Packages
This section explores the most important API requests regrding Packages. A Package refers to an entity that is processed using the "Functions-as-a-Service" (FaaS) technology. FaaS Packages are used to automate the processing of data and can be used to perform a wide range of Tasks, such as data cleaning, data transformation, and data enrichment. FaaS Packages in the Dataloop system are created by Project managers or data scientists, who define the specific requirements for each Package, such as the data inputs, the functions to be executed, and the output data format. Once the FaaS Package is defined, it can be executed using the Dataloop FaaS engine, which automatically manages the Execution of the functions within the Package. The Package is a static code with a schema that holds all the Modules, functions, and the code base from which they can be taken.

A Package could also be thought as a bundle of code and definitions that can be used for creating models or deploying services. Code is a dl.Codebase entity, and definitions include modules, functions, IOs, and the code entry point. For now, it can be Python, nodeJS format. The main function of Packages is to deploy a Service and create an executable version of that code. Packages can be public, global, or specific to a particular Project.

Here are the most important API requests regarding Packages:
- [Get a list of Packages](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_listPackages);
- [Create a new Package](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_createPackage);
- [Get a Package by ID](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_getPackage);
- [Update Package](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_updatePackage);
- [Get Package revisions by ID](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_getPackageRevisions);
- [Delete a Package by ID](https://gate.dataloop.ai/api/v1/docs#/Packages/Packages_deletePackages).

## Executions
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


##











## Examples
### Datasets
### Example: Show all datasets
To show all of the datasets in your organization (or in a particular project, if you want to), you can use the ```GET/datasets``` API request. Go to the Datasets section, look for it and click it. It should look like this once selected:

![image](https://user-images.githubusercontent.com/58508793/224307707-27a41a69-9a95-4d0c-86e3-c9e2b245e829.png)

Click the "Try it out" button, and you will be able to complete the "name", "creator" and "projects" fields, to search for datasets matching specific criteria. You should firstly Execute without completing any of the fields. This will show you all of the Datasets you have access to, as seen below:

![image](https://user-images.githubusercontent.com/58508793/224308368-f0dcf9bc-0bd1-4baf-9e18-fb567a250790.png)

All of the information you requested, based on your Query should be in the "Response Body".

**Note**: If you have no dataset created, you can create one using the ```POST/datasets```, which is located just below the ```GET/datasets```.


### Example: GET a Dataset's Item count
By using a simple Query on the Datasets endpoint, you can use the Dataset ID and Query to get the requested items.

To do that, you must first find out the ```ID``` of the dataset you wish to Query. To find a Dataset ID, you can just click the ```Get\datasets``` API line (which we described above), which will return the details about all of the Datasets to which you have access in the Dataloop platform. You can also add the name of the Dataset as a parameter to the Query, search by Creator or by the Project name. Below, the Query is executed by using the Dataset name "Creatures", which is a Dataset used in one of [Dataloop's Python SDK Onboarding Exercises](../onboarding/11_onboarding_exercise.md) (be sure to use your own Dataset's name or ID):
![image](https://user-images.githubusercontent.com/58508793/219678882-765f6257-e92e-48dc-a0ad-70fba382227c.png)

The response to this ```GET``` Query can be seen below, including the dataset ID. Be sure to copy this ID, as we will use it in a moment (the ID you see after running the ```GET``` command on **your own dataset**):
![image](https://user-images.githubusercontent.com/58508793/219679455-89d26a5d-5303-43b8-b3af-86002bf3bb8d.png)

Filters can be used to specify diferent criteria that can be used to more accurately search for the information you want to find. In the image below, you can see how to input the Dataset ID and a specific Query.
![image](https://user-images.githubusercontent.com/58508793/218518081-65d657d6-a4c2-4443-8046-e1791b0fa2cd.png)

There are a lot more requests you can use in the [Dataset section of the API](https://gate.dataloop.ai/api/v1/docs/#/Datasets). Each request has a short description which will let you know what functionality it has. Feel free to explore and try out other Dataset API requests.




## Projects
### Example: GET Projects List

Let's get started with an example of a basic API request. Go ahead and scroll down until you find the "Projects" section. 

![image](https://user-images.githubusercontent.com/58508793/219648842-aba4b7ff-c26d-4315-ab71-2eaf719e8732.png)


Now,  select the first GET method, to get all of the projects and  then click "Try it out", like in the image below:
![image](https://user-images.githubusercontent.com/58508793/219650991-266730c4-debf-4fcc-9b37-a327b4af6145.png)


Click the big ```Execute``` button:
![image](https://user-images.githubusercontent.com/58508793/219651137-475d2a9d-cdd3-4c70-b98d-18a0f1d0daee.png)

You should now instantly recieve a response in JSON format that shows all Projects to which you have access, similar to the image below:

![image](https://user-images.githubusercontent.com/58508793/219651466-b6cc5956-440a-41f9-984d-d853d3c4ed85.png)

In the ```Response Body``` you will receive all of the details and inforamtion that the command you ran returns. Feel free to try more commands in the ```Projects``` section on your own.











## Custom Querries
Implementing  Custom Queries will allow you to better Search, Filer, Sort and Update your data. To do that, you will have to [learn more about the Dataloop Query Language (DQL) our proprietary Query Language](https://dataloop.ai/docs/api-dql).

Below, you can find some Queries we created for you, to search your Dataset for all a specific Annotation - in ths case "Bear". Just copy and paste it in the ```/datasets/{id}/query```. You should have the Dataset ```ID``` available from the API call we did above. Of course, you need to have at least an Annotated Item with the annotation "Bear" in your Dataset for this complete example to work.  To search for a specific Annotation you have, you can change the "Bear" string with the Annotation your Item in your Dataset. You would do the following:

```
copy{
   "resource":"items",
   "filter":{
      "$and":[
         {
            "type":"file"
         },
         {
            "hidden":false
         }
      ]
   },
   "join":{
      "on":{
         "resource":"annotations",
         "local":"itemId",
         "forigen":"id"
      },
      "filter":{
         "$and":[
            {
               "label":{
                  "$in":[
                     "Bear"
                  ]
               }
            },
            {
               "type":{
                  "$in":[
                     "box"
                  ]
               }
            }
         ]
      }
   }
}
```
The Response body for this query should show you the Items in your dataset that are Annotated with the specific Annotation you provided the Query. You will see the all of the detailed information for each Item under its Item Metadata, similar to the output seen below:
```
copy{
  "totalItemsCount": 2,
  "items": [
    {
      "id": "5e5fdae499d5538db88b8d5f",
      "datasetId": "5e5fdad764cab43156881739",
      "createdAt": "2020-03-04T16:44:20.000Z",
      "dir": "/",
      "filename": "/18407C.JPG",
      "type": "file",
      "hidden": false,
      "metadata": {
        "system": {
          "originalname": "18407C.JPG",
          "size": 340727,
          "encoding": "7bit",
          "mimetype": "image/jpeg",
          "annotationStatus": [],
          "refs": [],
          "executionLogs": {
            "image-metadata-extractor": {
              "default_module": {
                "run": {
                  "5e5fdae44eac5e41d231dbf4": {
                    "progress": 100,
                    "status": "success"
                  }
                }
              }
            }
          },
          "exif": {},
          "height": 1007,
          "width": 1600
        }
      },
      "name": "18407C.JPG",
      "url": "https://gate.dataloop.ai/api/v1/items/5e5fdae499d5538db88b8d5f",
      "dataset": "https://gate.dataloop.ai/api/v1/datasets/5e5fdad764cab43156881739",
      "annotated": true,
      "stream": "https://gate.dataloop.ai/api/v1/items/5e5fdae499d5538db88b8d5f/stream",
      "thumbnail": "https://gate.dataloop.ai/api/v1/items/5e5fdae499d5538db88b8d5f/thumbnail",
      "annotations": "https://gate.dataloop.ai/api/v1/items/5e5fdae499d5538db88b8d5f/annotations"
    },
    {
      "id": "5e5fdae4659f5f1a7b74901d",
      "datasetId": "5e5fdad764cab43156881739",
      "createdAt": "2020-03-04T16:44:20.000Z",
      "dir": "/",
      "filename": "/18407.JPG",
      "type": "file",
      "hidden": false,
      "metadata": {
        "system": {
          "originalname": "18407.JPG",
          "size": 238418,
          "encoding": "7bit",
          "mimetype": "image/jpeg",
          "annotationStatus": [],
          "refs": [],
          "executionLogs": {
            "image-metadata-extractor": {
              "default_module": {
                "run": {
                  "5e5fdae4b314cc1a13c399d7": {
                    "progress": 100,
                    "status": "success"
                  }
                }
              }
            }
          },
          "exif": {},
          "height": 1041,
          "width": 1291
        }
      },
      "name": "18407.JPG",
      "url": "https://gate.dataloop.ai/api/v1/items/5e5fdae4659f5f1a7b74901d",
      "dataset": "https://gate.dataloop.ai/api/v1/datasets/5e5fdad764cab43156881739",
      "annotated": true,
      "stream": "https://gate.dataloop.ai/api/v1/items/5e5fdae4659f5f1a7b74901d/stream",
      "thumbnail": "https://gate.dataloop.ai/api/v1/items/5e5fdae4659f5f1a7b74901d/thumbnail",
      "annotations": "https://gate.dataloop.ai/api/v1/items/5e5fdae4659f5f1a7b74901d/annotations"
    }
  ],
  "totalPagesCount": 1,
  "hasNextPage": false
}
```

## Example: POST Datasets Query for Annotations

In this example you learn how to get the Annotation count for all the Bounding Box with the Labels "dogs" from your dataset. You can also change the Label "dogs" with a Label that you have in your own Dataset.

First, you need to go to  ```POST/datasets/query``` from the ```Dataset``` section of the Swagger API, and click ```Try Out```:
![image](https://user-images.githubusercontent.com/58508793/219695497-83099e65-7881-4016-8886-fbf36ffc7cdb.png)

You can then add the the below request body (or your request body), in the Query area:
```
copy{
   "resource":"annotations",
   "filter":{
      "$and":[
         {
            "label":{
               "$in":[
                  "dogs"
               ]
            }
         },
         {
            "type":{
               "$in":[
                  "box"
               ]
            }
         }
      ]
   }
}
```
And then press execute, to apply your Query:
![image](https://user-images.githubusercontent.com/58508793/219695813-00cbe260-1c72-4749-b91c-e99d89ac2a43.png)

You should get all of the Items with the Annotation "dogs", and all of their Metadata details.

## Final Words

There are a lot more API Requests, Commands and Queries you can try on your own. Be sure to have a look around and learn how to use them.

If you have any troubles, be sure to [Contact Dataloop's Support](https://dataloop.ai/contact/).

You can also [Book a Demo](https://dataloop.ai/demo/), if you want to have someone teach you more about the API and the Dataloop platform in general.


