# Glossary

[A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) | [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w) | [X](#x) | [Y](#y) | [Z](#z)

## A
### <a name="annotation"></a>Annotation ([Entity](#entity))
An Annotation entity refers to a label, tag, or another piece of Metadata that is attached to an Item in a Dataset. Annotations are typically used to provide additional context or information about an Item, and to enable machine learning models to better understand and interpret the data. Annotations in the Dataloop system can take many forms, depending on the specific Task and type of data being annotated. Annotations in the Dataloop system are typically created by human annotators, who use the system's interface to draw bounding boxes, select Labels, or enter text. Annotations can also be reviewed and verified by other annotators or team Members, to ensure accuracy and consistency.  Some common types of Annotations include:
- Bounding Boxes: Used to identify the location and size of objects within images or videos;
- Classification Labels: Used to categorize Items based on their content or characteristics;
- Text Transcriptions: Used to convert spoken words or written text into machine-readable formats;
- Semantic Segmentation Masks: Used to identify and segment different regions or objects within an image.


Note: A JSON format representing the objects and labels exists in an [Item](#item).


### <a name="artifacts"></a>Artifacts ([Entity](#entity))

Large files (binaries) that we don't want to pack inside a package (which should only contain code), but are still needed during the deployment of a package.  They are uploaded separately and downloaded when the service is initiated.  Usually need to be added to the ```.gitignore```.
There are three types of Artifacts: 
- Item; 
- Local; 
- Link.

### <a name="assignment"></a>Assignment ([Entity](#entity))
An Assignment is a specific Task that is assigned to an individual, represents a unique instance of an Assignment, and contains all the information necessary for annotators to complete the work. As Annotators work on the Assignment, Annotators can communicate with Project Managers or team leaders and can ask for clarification on any aspects of the Task that are unclear. Once an Assignment is completed, the Dataloop system automatically aggregates the results and provides Project managers with real-time insights into the progress of each Assignment, the quality of the Annotations, and the overall status of the Project.

An Assigment may be a single Annotators’ Items for manual review and/or annotation. Items can be redistributed or reassigned between Assignments.  The Annotator is also referred to as an “Assignee”.

### <a name="attribute"></a>Attribute ([Entity](#entity))
An Attribute refers to a specific property or characteristic that can be associated with an Annotation. Attributes can be thought of as additional pieces of information that provide context or Metadata about an Item, beyond what can be captured through Annotation Labels alone. Attributes have the following fields:
- Scope - where mapping to labels is done. The default applies any Attribute to all Labels, but individual selection can also be done.
- Mandatory - enforce annotators to answer Attributes in Studio 2.0 before clicking “Done” and moving to the next Item. The Feature is enabled from Recipe instructions and applies to any Attribute set as ‘Mandatory’.
- Type - selection and representation type of the Attribute.
- Subject - The guidance/question presented to the annotator, on how to fill this Attribute;
- Section ID - Allows referring to this Attribute via JSON exports and Metadata. It's auto-populated with a running number, but can be edited to any value.

## B

### <a name="binaries"></a>Binaries ([Item](#item))

The content of any type of file (image, video, pdf, etc.). The bineries are managed by the Master Dataset entity in Dataloop.

### <a name="box"></a>Bounding Box ([Entity](#entity))
A bounding box [Annotation](#annotation) type. Represented by 2 point for top-left and bottom-right. type=`box`
## C
### <a name="clone"></a>Clone
Dataset clones contain pointers to original files, enabling management of virtual Items that do not replicate the binaries (this clone is created without copying the file binaries) of the underlying storage once cloned or copied. When cloning a Dataset, users can decide if the new copy will contain Metadata and Annotations created over the original.

### <a name="codebase"></a>Codebase ([Entity](#entity))
The Package Codebase is the code you import to the platform containing all of the Modules and functions. When you upload the code to the platform, either from your computer or from Github, it is saved on the platform as an Item (in a zip file).

There are four types of code bases, which are all limited to 100MB: 
- Item Codebase
- git Codebase 
- local Codebase 
- filesystem (currently no one uses this, and is likely used when working in a remote container)  

### <a name="command"></a>Command

## D
### <a name="dataset"></a>Dataset ([Entity](#entity))
A Dataset is a collection of Items (files), their Metadata, and Annotations. A Dataset can have a file-system-like structure, with folders and subfolders at any level. There are different types of Datasets:
- Master - Original Dataset, managing the actual binaries;
- Clone - Contains pointers to original files, enabling management of virtual Items that do not replicate the binaries of the underlying storage once cloned or copied. When cloning a Dataset, users can decide if the new copy will contain Metadata and Annotations created over the original Dataset;
- Merge - Multiple Datasets can be merged into one, enabling multiple Annotations to be merged onto the same Item (for 2 Datasets to be successfully merged, they need to have the same Recipe and Ontology.

### <a name="dql"></a>DQL (Dataloop Query Language)
The Dataloop platform gives you different capabilities to organize your data in Datasets, folders, and versioning systems, you still need the ability to query your data. This is where our **Dataloop Query Language** becomes useful. When using the DQL in the SDK, additional fields such as sort, page, and pageSize can be defined to sort the data that is returned from the Query. Every DQL query has the following components:
- Resource: The target Resource for the Query. The Resource can be Items or Annotations.
- Filter: The Filter includes Attributes and logical operators to filter Items.
## E

### <a name="entity"></a>Entity
A Dataloop data model object. Represented by a json.

### <a name="execution"></a>Execution ([Entity](#entity))
Execution refers to the process of executing a function within the FaaS Service. When a user submits a function for Execution, the FaaS Service creates a container to run the function and provides any necessary inputs. The function is executed within the container, and the results are returned to the user.
### <a name="execution"></a>ExecutionIO ([Entity](#entity))
ExecutionIO or Execution input is the same input the function requires. The input will be provided to the method the Execution invokes. The input of Dataloop type (Item, Dataset, Annotation, etc.) should be passed with an ID of the corresponding entity or it can be an input of type Json that can have any JSON serializable value and will provide it as is to the method.

## F
### <a name="function"></a>Function ([Entity](#entity))
Functions are basic running units of the FaaS. You can define the Functions on the class and when the Service is deployed, you can run each of them. The functions are defined inside a Module, where multiple Functions can be an entrance point to the FaaS.
## G
## H
## I
### <a name="instance-catalog"></a>Instance Catalog

### <a name="item"></a>Item ([Entity](#entity))
An Item in Dataloop, is a unit of data that represents a ‘single instance’ or ‘file’ of a larger Dataset. It can be an image, a video, a sound recording, a text document, or any other type of digital asset that needs to be labeled, annotated, or analyzed. Each Item in the Dataloop system is typically associated with one or more Tasks, which define the specific operations that need to be performed on the Item. For example, an Item may be labeled with Bounding Boxes to identify objects in an image, transcribed to convert speech-to-text, or classified based on its content. Items also have associated Metadata.

### <a name="item"></a>Item Status ([Entity](#entity))
When a worker finishes working on an Item in their Assignment, they perform an action to set a status on the Item (e.g. Complete action on an Item so it will have "Completed" status). Users can customize their own status and later on use those as Trigger events, analytics reports or search and filter activities.
- In Annotation Tasks - the default statuses are "Discarded" (for disqualified Items) and "Completed" (for Items ready for the next phase).
- In QA (Quality Analysis) Tasks - the default statuses are "Discarded" and "Approved".
### <a name="item"></a>Item Links ([Entity](#entity))
Item Links are a way to connect files hosted in your external storage to the platform, using URL links. The Dataloop platform supports displaying JSON files over the Annotation Studios as Items that can be annotated, downloaded, and treated as Images. Links enable displaying an Image in the Dataloop platform without storing it on Dataloop servers. The JSON file acts as a pointer to the binary file that is stored on the customer's storage.


## J
## K
## L
### <a name="label"></a>Label ([Entity](#entity))
A piece of text that gives information about an Annotation instance. Contains also the color, display name and children of the annotation.
### <a name="logsample"></a>LogSample

## M
### <a name="metadata"></a>Metadata
A dictionary object that contains Metadata of the Dataloop object. Usually includes “system” and “user” in the Metadata fields to distinguish between necessary and custom user Metadata.

### <a name="model"></a>Model
The representation of what a machine learning algorithm has learned from the training data. Is a Python (pytorch, tensorflow) representation of a Neural Network's architecture with or without loaded weights (pth, pb, hdf5 files).

### <a name="model"></a>Model ([Entity](#entity))
A Model entity in Dataloop refers to a machine learning algorithm that has been trained on labeled data to make predictions or perform other Tasks. Models are a key component of the Dataloop system, as they enable users to apply machine-learning techniques to a wide range of data types, including images, text, and audio. The system has several pre-installed and publicly available model architectures, which can be installed in your Project and trained with your data to achieve the pre-annotation of your labels such as ResNet, Yolo-V5, U-net.
A Dataloop Model is a combination of data (dl.Dataset), configurations (json dictionary), and code (dl.Package) to represent a learnable instance of the data.  
You can train, evaluate, compare, and deploy a dl.Model.  
Out-of-the-box models are available on the platform with the scope attribute “public”, as opposed to project specific models with “project” scope.

### <a name="model-adapter"></a>Model Adapter
A python class to wrap a generic ML code (train, predict, etc.) for standardizing models (and frameworks) to match the requirements of the Dataloop API.  
- Log Sample: A single data point is used to measure and compare different models and metrics. e.g. saving the train/validation loss and accuracy of a training session.  
- Offline Mode: For local model management, only dl.Model is used to save configurations and training/evaluation metrics, while code and weights and biases are kept locally.  Gives the ability to manage training runs, view live metrics, and compare dl.Models (configurations and metrics) locally;
- Online Mode: Allows integration into the Dataloop platform (after creating Model Adapter). Gives the ability to create custom buttons (e.g. in the annotations studio), train, deploy and evaluate using the Model Management Pages, using models inside a pipeline etc.).

### <a name="model-weights-/-model-artifacts"></a>Model Weights / Model Artifacts
Those are the files that are saved/created by training a machine learning algorithm on a Dataset. They are adjusted using optimization algorithms and unique to each training session.

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

## P
### <a name="package"></a>Package ([Entity](#entity))
A Package refers to an entity that is processed using the "Functions-as-a-Service" (FaaS) technology. FaaS Packages are used to automate the processing of data and can be used to perform a wide range of Tasks, such as data cleaning, data transformation, and data enrichment. FaaS Packages in the Dataloop system are created by Project managers or data scientists, who define the specific requirements for each Package, such as the data inputs, the functions to be executed, and the output data format. Once the FaaS Package is defined, it can be executed using the Dataloop FaaS engine, which automatically manages the Execution of the functions within the Package. The Package is a static code with a schema that holds all the Modules, functions, and the code base from which they can be taken.


A Package could also be thought as a bundle of code and definitions that can be used for creating models or deploying services. Code is a dl.Codebase entity, and definitions include modules, functions, IOs, and the code entry point.  For now, it can be Python, nodeJS format.  The main function of Packages is to deploy a Service and create an executable version of that code.  Packages can be public, global, or specific to a particular Project.

**Note:** Packages are limited to a maximum of 100MB.


### <a name="pipeline"></a>Pipeline ([Entity](#entity))
Pipelines allow you to create automated flows that weave together humans and machines to process data in a Pipeline architecture. Pipelines consist of a series of Nodes, where each Node’s output is the input of the next one. They allow for transitioning of data between labeling and QA Tasks, FaaS (see entry for Package), and code snippets and, machine learning (ML) models. It is flexible and scalable and can be used for both training and production. Common examples of use cases include automatic pre-processing of data for Annotation workflows and deployment Pipelines for ML models.



### <a name="pipeline-cycle"></a>Pipeline Cycle
A Pipeline Cycle refers to all Node Executions performed on a single Pipeline run (usually over a specific Item); the Executions are listed in the order in which they occurred. Since some Items may be routed differently in the Pipeline based on Filters and user actions, each Cycle may have a different number of Executions.

### <a name="pipeline-cycle"></a>Pipeline Node
Node - The Pipeline can be made up of different Nodes, each with a different role in the Pipeline, such as storing data, executing functions, training models, or sending data to Annotation or QA Tasks. The main types are Dataset, Workflow, FaaS, Code, and Utilities.

### <a name="pod-type"></a>Pod type

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
A deployed [Package](#package) that serves the code. Given the matching input to a function, it will run it and return the output, e.g. if we have code in our [Package](#package) for converting RGB images to grayscale, the dl.Service would run the code and upload the grayed image.
## T
### <a name="task"></a>Task ([Entity](#entity))
A set of items to be reviewed/annotated by human workers. A task is divided into assignments.  
Can be managed by a queue (Pulling Task) or by workload (percentage of items per assignee).  
The task is connected to a recipe for instructions and world definitions (ontology)
### <a name="trigger"></a>Trigger ([Entity](#entity))

## U
## V
## W
## X
## Y
## Z
