# Glossary

[A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) | [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w) | [X](#x) | [Y](#y) | [Z](#z)

## A
### <a name="annotation"></a>Annotation ([Entity](#entity))
An Annotation entity refers to a Label, tag, or another piece of Metadata that is attached to an Item in a Dataset. Annotations are typically used to provide additional context or information about an Item, and to enable machine learning models to better understand and interpret the data. Annotations in the Dataloop system can take many forms, depending on the specific Task and type of data being annotated. Annotations in the Dataloop system are typically created by human annotators, who use the system's interface to draw bounding boxes, select Labels, or enter text. Annotations can also be reviewed and verified by other annotators or team Members, to ensure accuracy and consistency.  Some common types of Annotations include:
- Bounding Boxes - Used to identify the location and size of objects within images or videos;
- Classification Labels - Used to categorize Items based on their content or characteristics;
- Text Transcriptions - Used to convert spoken words or written text into machine-readable formats;
- Semantic Segmentation Masks - Used to identify and segment different regions or objects within an image.

**Note:** A JSON format representing the objects and labels exists in an [Item](#item).

### <a name="admin"></a>Admin
An Admin is simmilar to an [Owner](#owner).  An Admin can delete/rename an Organization, create Projects, and add/remove Organization Members. However Admin privileges can be removed, while Owner privileges cannot.


### <a name="artifacts"></a>Artifacts ([Entity](#entity))
Large files (binaries) that we don't want to pack inside a package (which should only contain code), but are still needed during the deployment of a package.  They are uploaded separately and downloaded when the service is initiated.  They usually need to be added to the ```.gitignore```.
There are three types of Artifacts: 
- Item; 
- Local; 
- Link.


### <a name="api"></a>API
APIs (Application Programming Interface) are mechanisms that enable two software components to communicate with each other using a set of definitions and protocols.


### <a name="assignment"></a>Assignment ([Entity](#entity))
An Assignment is a specific Task that is assigned to an individual, represents a unique instance of an Assignment, and contains all the information necessary for annotators to complete the work. As Annotators work on the Assignment, Annotators can communicate with Project Managers or team leaders and can ask for clarification on any aspects of the Task that are unclear. Once an Assignment is completed, the Dataloop system automatically aggregates the results and provides Project managers with real-time insights into the progress of each Assignment, the quality of the Annotations, and the overall status of the Project.

An Assigment may be an Item or collection of Items that are allocated to an Annotator for manual annotation and/or review. Items can be redistributed or reassigned between Assignments.  The Annotator is also referred to as an “Assignee” or "Contributor".

### <a name="autoscaler"></a>AutoScaler
The FaaS ([Service](#service)) Autoscaler is a component of the Dataloop system that automatically adjusts the number of serverless computing Resources allocated to the FaaS Service based on current demand. The purpose of the Autoscaler is to ensure that the system can handle spikes in demand without overprovisioning Resources and incurring unnecessary costs. The FaaS Autoscaler in Dataloop is designed to be flexible and configurable. Users can set thresholds for scaling up or down the number of Resources allocated to the FaaS Service, and they can also define scaling policies that govern how the Autoscaler responds to different types of demand. Dataloop autoscale runtime configuration is compound with the following Attributes:
- cooldown_period - Define how long to wait before scaling down (reducing the number of replicas) in case the queue is empty again. So that running Executions will have time to complete.
- polling_interval - Autoscaler polling interval of the Service queue (in seconds). This parameter defines how often a new Execution enters the queue.
- min_replicas & max_replicas - Maximum and Minimum number of replicas that can be initialized at a given time for the FaaS Service. 
- max_attempts_Attributes - Executions can fail due to Service termination (or other errors that can cause the Service to restart). In these cases, you can have the Execution try and run automatically as many times as you desire. To do so you need to set the Service max_attempts Attribute.

### <a name="attribute"></a>Attribute ([Entity](#entity))
An Attribute refers to a specific property or characteristic that can be associated with an Annotation. Attributes can be thought of as additional pieces of information that provide context or Metadata about an Item, beyond what can be captured through Annotation Labels alone. Attributes have the following fields:
- Scope - where mapping to labels is done. The default applies any Attribute to all Labels, but individual selection can also be done.
- Mandatory - enforce annotators to answer Attributes in Studio 2.0 before clicking “Done” and moving to the next Item. The Feature is enabled from Recipe instructions and applies to any Attribute set as ‘Mandatory’.
- Type - selection and representation type of the Attribute.
- Subject - The guidance/question presented to the annotator, on how to fill this Attribute;
- Section ID - Allows referring to this Attribute via JSON exports and Metadata. It's auto-populated with a running number, but can be edited to any value.


## B
### <a name="bot"></a>Bot
A Bot is a machine user that has Developer role permissions within a Project. In Dataloop, Bots are used to run Services. Once a Service has been deployed, it will log in using the Bot with which the Service was created or the Bot will be created automatically. All platform API requests will be made using the Bot’s token.

### <a name="binaries"></a>Binaries ([Item](#item))

The content of any type of file (image, video, pdf, etc.). Binaries are managed by the Master Dataset entity in Dataloop.

### <a name="box"></a>Bounding Box ([Entity](#entity))
A bounding box [Annotation](#annotation) type is used to identify the location and size of objects within images or videos.  A bounding box is represented by 2 points that define top-left and bottom-right.

**Note:** type=`box`


## C
### <a name="computercache"></a>ComputerCache
A ComputerCache or Cache in Dataloop can refer to a component that stores data temporarily in memory, making the data faster and easier to access. When data is requested by a user or an Application from within the FaaS (see entry for Package) namespace it is retrieved from the cache instead of being fetched from the Services - reducing API calls and improving performance.


### <a name="clone"></a>Clone
Dataset clones contain pointers to original file binaries, enabling management of virtual Items that do not replicate the binaries (this clone is created without copying the file binaries) in the underlying storage once cloned. When cloning a Dataset, users can decide if the new virtual copy will contain Metadata and Annotations created on the original.

### <a name="codebase"></a>Codebase ([Entity](#entity))
The Package Codebase is the code you import to the platform containing all of the Modules and functions. When you upload the code to the platform, either from your computer or from Github, it is saved on the platform as an Item (in a zip file).

There are four types of code bases, which are all limited to 100MB: 
- Item Codebase;
- git Codebase;
- local Codebase;
- filesystem (currently no one uses this, and is likely used when working in a remote container);  


### <a name="classificationlabel"></a>Classification Label
A type of [Annotation](#annotation) that is used to categorize Items based on the sum of characteristics it has. Usually text is attributed to a classification Label, describing the category in which the Item was classified.  For example, shirt, clouse, pants, coat would all fall under the classification of Clothing.

### <a name="command"></a>Command
A program or utility that runs from the command line is known as a **command**. An interface that accepts lines of text and converts them into instructions for your computer is known as a command line. A graphical user interface (GUI) is simply a command-line program abstraction.

## D
### <a name="dataset"></a>Dataset ([Entity](#entity))
A Dataset is a collection of Items (files), their Metadata, and Annotations. A Dataset can have a file-system-like structure, with folders and subfolders at any level. There are different types of Datasets:
- Master - Original Dataset, managing the actual binaries;
- Clone - Contains pointers to original files, enabling management of virtual Items that do not replicate the binaries of the underlying storage once cloned or copied. When cloning a Dataset, users can decide if the new copy will contain Metadata and Annotations created over the original Dataset;
- Merge - Multiple Datasets can be merged into one, enabling multiple Annotations to be merged onto the same Item (for 2 Datasets to be successfully merged, they need to have the same Recipe and Ontology.

### <a name="dql"></a>DQL (Dataloop Query Language)
The Dataloop platform gives you different capabilities to organize your data in Datasets, folders, and versioning systems, you still need the ability to query your data. This is where our **Dataloop Query Language** becomes useful. When using the DQL in the SDK, additional fields such as sort, page, and pageSize can be defined to sort the data that is returned from the Query. Every DQL query has the following components:
- Resource - The target Resource for the Query; the Resource can be Items or Annotations;
- Filter - The Filter includes Attributes and logical operators to filter Items.


## E
### <a name="entity"></a>Entity
A Dataloop data model object. Represented by a json. It contains information about the various Dataloop entities and their related functions/operations and data. For example for “Item” entities - Download, Update (e.g. update its metadata), or update its status in task.

### <a name="execution"></a>Execution ([Entity](#entity))
Execution refers to the process of executing a function within the FaaS Service. When a user submits a function for Execution, the FaaS Service creates a container to run the function and provides any necessary inputs. The function is executed within the container, and the results are returned to the user.

### <a name="executionio"></a>ExecutionIO ([Entity](#entity))
ExecutionIO or Execution input is the same input the function requires. The input will be provided to the method the Execution invokes. The input of Dataloop type (Item, Dataset, Annotation, etc.) should be passed with an ID of the corresponding entity or it can be an input of type Json that can have any JSON serializable value and will provide it as is to the method.


## F
### <a name="function"></a>Function ([Entity](#entity))
Functions are basic running units of the FaaS. You can define the Functions on the class and when the Service is deployed, you can run each of them. The functions are defined inside a Module, where multiple Functions can be an entrance point to the FaaS.

### <a name="features"></a>Features (Set/Vectors)
A Feature vector is a numerical representation of an object or entity, typically used in machine learning and data analysis. It consists of a list of Features or Attributes that describe the object in a quantitative manner.  A Feature set, on the other hand, is a collection of Feature vectors that are used to train a machine-learning algorithm. The Feature set contains all the necessary Features that are relevant to the problem being solved and is used to extract meaningful patterns and relationships from the data. The Dataloop system enables Feature vector augmentations on both Items and Annotations, this capability grants users the ability to search and Filter Annotations and Items according to their ‘similarity’ in the euclidean space.

### <a name="filter"></a>Filter
Filters are part of the [Dataset](#dataset) and Task Browsers, enabling you to Filter Items based on every aspect of your files. When multiple Filters are used, the relationship between them will be the AND logical operator. However, the relationship between multiple values in each Filter will be the OR logical operator. For example, entering "dog" and "cat" in the Labels Filter will result in all Items that have a "dog" label OR a "cat" label.


## G
### <a name="group"></a>Group
User Groups allow the forming of teams as a Resource, which can then be reused collectively in the Dataloop system, specifically with workflow Tasks. Groups can be granted Project roles.

## H


## I
### <a name="integration"></a>Integration/Secrets
Integration allows Dataloop Organizations to define Secrets for accessing cloud Resources, including cloud storage such as GCS/S3, Secure Token Service (STS), container registry Services (ECR/GCR), and others. Once an integration is defined for cloud storage, a storage driver must be created with storage details such as bucket, folder, etc.

### <a name="instance-catalog"></a>Instance Catalog

### <a name="item"></a>Item ([Entity](#entity))
An Item in Dataloop, is a unit of data that represents a ‘single instance’ or ‘file’ of a larger Dataset. It can be an image, a video, a sound recording, a text document, or any other type of digital asset that needs to be labeled, annotated, or analyzed. Each Item in the Dataloop system is typically associated with one or more Tasks, which define the specific operations that need to be performed on the Item. For example, an Item may be labeled with Bounding Boxes to identify objects in an image, transcribed to convert speech-to-text, or classified based on its content. Items also have associated Metadata.

### <a name="itemstatus"></a>Item Status ([Entity](#entity))
When a worker finishes working on an Item in their Assignment, they perform an action to set a status on the Item (e.g. Complete action on an Item so it will have "Completed" status). Users can customize their own status and later on use those as Trigger events, analytics reports or search and filter activities.
- In Annotation Tasks - the default statuses are "Discarded" (for disqualified Items) and "Completed" (for Items ready for the next phase).
- In QA (Quality Analysis) Tasks - the default statuses are "Discarded" and "Approved".
### <a name="itemlinks"></a>Item Links ([Entity](#entity))
Item Links are a way to connect files hosted in your external storage to the platform, using URL links. The Dataloop platform supports displaying JSON files over the Annotation Studios as Items that can be annotated, downloaded, and treated as Images. Links enable displaying an Image in the Dataloop platform without storing it on Dataloop servers. The JSON file acts as a pointer to the binary file that is stored on the customer's storage.


## J
## K
## L
### <a name="label"></a>Label ([Entity](#entity))
A piece of text that gives information about an Annotation instance. Contains also the color, display name and children of the annotation.

### <a name="logsample"></a>LogSample


## M

### <a name="modality"></a>Modality
Modalities in the Dataloop platform represent a Feature that allows defining relations between the main Item (where the relation is created) and other Items. There are 3 types of modalities:
- Overlay - modalities defined in the main Item are overlaid on top of each other in the image Annotation studio (only), with the option to set opacity level per layer or toggle visibility entirely. These are typically images from multiple sensors with the same content (for example day/night sensors). Items loaded as a Modality will load together when a source image is loaded.
- Replace - when the main Item is opened in an Annotation studio, the Item defined as “replace-modality” is opened in the studio instead. This is commonly used when converting between formats. The main Item in the unsupported format is used for data and Annotation management in its context, while Annotation work is done on a “replace-modality” in a supported format.
- Preview - Preview Modality allows presenting reference Items related to the main Item. A common use case is classifying retail-related photos, where related Items are photos of the product from various angles.

### <a name="member"></a>Member
A Member of an [Organization](#organization) can open new Projects and view the Organization's Members. Members cannot add/remove other Members or delete the Organization.

### <a name="metadata"></a>Metadata
A dictionary object that contains Metadata of the Dataloop object. Usually includes “system” and “user” in the Metadata fields to distinguish between necessary and custom user Metadata.


### <a name="model"></a>Model ([Entity](#entity))
A Model entity in Dataloop refers to a machine learning algorithm that has been trained on labeled data to make predictions or perform other Tasks. Models are a key component of the Dataloop system, as they enable users to apply machine-learning techniques to a wide range of data types, including images, text, and audio. The system has several pre-installed and publicly available model architectures, which can be installed in your Project and trained with your data to achieve the pre-annotation of your labels such as ResNet, Yolo-V5, U-net.
A Dataloop Model is a combination of data (dl.Dataset), configurations (json dictionary), and code (dl.Package) to represent a learnable instance of the data.  
You can train, evaluate, compare, and deploy a dl.Model.  
Out-of-the-box models are available on the platform with the scope attribute “public”, as opposed to project specific models with “project” scope.

### <a name="modelversion"></a>Model Version
A Model Version can be created as a baseline from a model architecture in the AI Library (usually untrained, and then begin training on selected data), or from an existing Model Version. Model version can have one of the statuses below:
- Created - The snapshot was created but was not yet trained
- Training - The Model Version is currently training
- Trained - The Model Version finished the training process
- Pending - The Model Version is pending training - training will begin when there are available Resources.
- Failed - Model training failed. This could be because of a problem with the model adaptor, the training method, configuration or compute Resources issues.
- Deployed - The model snapshot is running as a FaaS Service.


### <a name="modeladapter"></a>Model Adapter
A python class to wrap a generic ML code (train, predict, etc.) for standardizing models (and frameworks) to match the requirements of the Dataloop API.  
- Log Sample - A single data point is used to measure and compare different models and metrics. e.g. saving the train/validation loss and accuracy of a training session.  
- Offline Mode - For local model management, only dl.Model is used to save configurations and training/evaluation metrics, while code and weights and biases are kept locally.  Gives the ability to manage training runs, view live metrics, and compare dl.Models (configurations and metrics) locally;
- Online Mode - Allows integration into the Dataloop platform (after creating Model Adapter). Gives the ability to create custom buttons (e.g. in the Annotations studio), train, deploy and evaluate using the Model Management Pages, using Models inside a Pipeline etc.).

### <a name="modelweightsmodelartifacts"></a>Model Weights / Model Artifacts
Are the files that are saved/created by training a machine learning algorithm on a Dataset. They are adjusted using optimization algorithms and unique to each training session.

### <a name="module"></a>Module ([Entity](#entity))
Modules are a reference to a Python file containing the python class (ServiceRunner by default) with functions inside it(location, IOs etc.). Modules can contain functions, classes, or other components of code, and can be used to perform specific data-related Tasks.


## N
### <a name="neural-network"></a>Neural Network
A machine learning model that is composed of layers consisting of simple connected units or neurons followed by non-linearities.


## O
### <a name="ontology"></a>Ontology ([Entity](#entity))
A set of definitions that defines the structure and relationships of your Labels. The Ontology of a Dataset is the building block of your Model and will help you define the object detection your trained model provides. Ontology holds 2 important components that are used in your Project:
- Labels (like classes) - are the names you use to classify your Annotations;
- Attributes - allow additional independent degrees of freedom while building a world definition.


### <a name="organization"></a>Organization
Is an entity composed of one or more users who collaborate on data-related Projects and share Resources and data. An Organization is composed of multiple elements like Integration/Secrets, Members, Bots, and ComputerCache.

### <a name="owner"></a>Owner
An Owner in Dataloop represents the user who created the [Organization](#organization). This user cannot be removed. An owner can delete/rename an Organization, create Projects, and add/remove Organization Members.


## P
### <a name="package"></a>Package ([Entity](#entity))
A Package refers to an entity that is processed using the "Functions-as-a-Service" (FaaS) technology. FaaS Packages are used to automate the processing of data and can be used to perform a wide range of Tasks, such as data cleaning, data transformation, and data enrichment. FaaS Packages in the Dataloop system are created by Project managers or data scientists, who define the specific requirements for each Package, such as the data inputs, the functions to be executed, and the output data format. Once the FaaS Package is defined, it can be executed using the Dataloop FaaS engine, which automatically manages the Execution of the functions within the Package. The Package is a static code with a schema that holds all the Modules, functions, and the code base from which they can be taken.

A Package could also be thought as a bundle of code and definitions that can be used for creating models or deploying services. Code is a dl.Codebase entity, and definitions include modules, functions, IOs, and the code entry point.  For now, it can be Python, nodeJS format.  The main function of Packages is to deploy a Service and create an executable version of that code.  Packages can be public, global, or specific to a particular Project.

**Note:** Packages are limited to a maximum of 100MB.


### <a name="pipeline"></a>Pipeline ([Entity](#entity))
Pipelines allow you to create automated flows that weave together humans and machines to process data in a Pipeline architecture. Pipelines consist of a series of Nodes, where each Node’s output is the input of the next one. They allow for transitioning of data between labeling and QA Tasks, FaaS (see entry for Package), and code snippets and, machine learning (ML) models. It is flexible and scalable and can be used for both training and production. Common examples of use cases include automatic pre-processing of data for Annotation workflows and deployment Pipelines for ML models.


### <a name="pipelinecycle"></a>Pipeline Cycle
A Pipeline Cycle refers to all Node Executions performed on a single Pipeline run (usually over a specific Item); the Executions are listed in the order in which they occurred. Since some Items may be routed differently in the Pipeline based on Filters and user actions, each Cycle may have a different number of Executions.

### <a name="pipelinenode"></a>Pipeline Node
Node - The Pipeline can be made up of different Nodes, each with a different role in the Pipeline, such as storing data, executing functions, training models, or sending data to Annotation or QA Tasks. The main types are Dataset, Workflow, FaaS, Code, and Utilities.

### <a name="project"></a>Project
A Project is typically a high-level Organizational entity that represents a specific task or goal. It can be used to manage data, Tasks, and Annotations related to a particular Project, and often serves as the main unit of work in the system. It provides a centralized location for managing data and Tasks related to a specific goal or objective. This can help improve collaboration among team members, ensure consistency in the data and Annotations, and make it easier to track progress and results.
### <a name="projectcontributor"></a>Project Contributor
Project Contributors are users who have been granted access to a specific Project and are authorized to contribute to its data, Tasks, and Annotations. Project Contributors may have different levels of access and permissions. For example, some Contributors may be able to view and annotate data, while others may have the ability to train machine learning models or manage the overall workflow. Contributors can be added to the Project with one of the following roles: 
- Project Owner - this role has access to all. As a Project Owner, you can create Projects, manage Datasets, assign Contributors, change roles, export data, and more.
- Developer - as a developer, you can manage Datasets, set Recipes, create Tasks, and export data within a Project.
- Annotation Manager - as an Annotation manager you can create Annotations or QA Tasks, redistribute and reassign these Tasks to annotators, as well as review their Tasks.
- Annotator - annotators can only work on Annotation and QA Assignments assigned to them.

### <a name="pagination"></a>Pagination (SDK)
We use pages instead of a list when we have an object that contains a lot of information. The page object divides a large list into pages (with a default of 1000 items) in order to save time when going over the entries. You can redefine the number of entries per page with the ‘page_size’ attribute. When going over all entries in a page out of multiple pages, we use nested loops to first go to the pages and then go over the entities for each page.

### <a name="podtype"></a>Pod type

### <a name="polygon"></a>Polygon ([Entity](#entity))
A polygon [Annotation](#annotation) type. Represented by a list of (x,y) points. type=`segment`
## Q
## R
### <a name="recipe"></a>Recipe ([Entity](#entity))
A "Recipe" refers to a set of instructions or rules that define how data should be processed, labeled, or analyzed within a Project. Recipes can be thought of as templates or workflows that provide a standardized way of working with data and can help to streamline the process of generating labeled Datasets for machine learning and other applications. Linked with an Ontology, the Recipe adds labeling instructions and settings, such as labeling tools to be used, mapping of tools to specific labels/Attributes, PDF instructions file, and more. Recipes in the Dataloop system can be customized and adapted to fit a wide range of use cases and data types. 


### <a name="repository"></a>Repository
A collection of entities, which are usually queried (e.g. using a filter), or referred to (for example all Items in a Dataset entity). It allows performing bulk operations (for example Delete all items), or addressing each entity within the repository (for example every Item in an Items collection).

## S


### <a name="segmentation"></a>Semantic Segmentation Masks ([Entity](#entity))
A binary mask [Annotation](#annotation) type. Represented by mask with the same size as the image, 0 for background, 1 for the object. type=`binary`

### <a name="service"></a>Service ([Entity](#entity))
Service or FaaS (Function-as-a-Service), is a cloud computing model where a cloud provider manages and runs individual functions in response to events or Triggers. In Dataloop, a FaaS Service is a serverless computing Service that allows users to run code without the need to manage servers or infrastructure. The FaaS Service is a key component of the system architecture, providing a platform for executing code and integrating with other Services in the system. The FaaS Service in Dataloop is designed to handle the Execution of small, isolated functions that can be triggered by a variety of events, such as data input from sensors or user actions.

A service can also be thought as a deployed [Package](#package) that serves the code. Given the matching input to a function, it will run it and return the output, e.g. if we have code in our [Package](#package) for converting RGB images to grayscale, the dl.Service would run the code and upload the grayed image.


## T
### <a name="task"></a>Task ([Entity](#entity))
A "Task" is a unit of work that needs to be completed by an individual or a team. A Task can represent any type of activity, such as annotating data, reviewing Annotations, labeling images, performing quality assurance checks, or any other data-related Task that requires human input. Tasks in the Dataloop system are created by Project managers, who define the specific requirements for each Task, such as the type of data to be labeled, the Annotation instructions, the deadline, and the number of annotators required. Tasks are then assigned to individual annotators or teams of annotators who complete the Task according to the specified requirements. 

### <a name="trigger"></a>Trigger ([Entity](#entity))
A Trigger is a rule-based mechanism that initiates an action when a specific event occurs. Triggers are used to automate workflows and streamline data processing. They are created by defining a set of conditions that must be met for the Trigger to be activated. These conditions can be based on a variety of factors, such as the content of data, the time of day, or the occurrence of specific events. Once a Trigger is activated, it can initiate a range of actions, such as sending notifications, generating reports, or Triggering the Execution of a specific Task or workflow.
It can be of 2 types:
- EventTrigger - contains a Project on which it monitors events, a Resource type such as Item, Annotation, Task, etc. The action that happened to the Resource such as created, updated, deleted status changed, etc. a DQL (The Data Query Engine) Filter that checks whether or not to invoke the operation based on the Resource JSON, and an operation. 
- CRONTrigger - enables you to run functions at specified time patterns with constant input using the Cron syntax. In the Cron Trigger specification, you specify when you want the Trigger to start, when you want it to end, specifying when it should run, and the input that should be sent to the action.


### <a name="tasktranscriptions"></a>Text Transcriptions
A type of [Annotation](#annotation) used to convert spoken words or written text into machine-readable formats.


## U
### <a name="uislot"></a>UI Slot
UI slots create a button in the Dataloop platform, allowing users to invoke the FaaS function when needed. Once a Slot is activated, users can execute the function through the UI Slot in the Dataset browser, Task browser, or Annotation studio. 

## V
## W
### <a name="worker"></a>Worker
The Worker role as part of an [Organization](#organization) - a role designated for adding users with no permissions to the Organization itself. Typically used for adding Annotation workforce and arranging them into Task Groups, which can, later on, be added to Projects managed by the Organization. Accordingly, workers cannot view the list of Organization Members, access any Secrets, or open new Projects.

## X
## Y
## Z
