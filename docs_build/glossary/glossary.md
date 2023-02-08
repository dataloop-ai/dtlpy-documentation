# Glossary

[A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) | [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w) | [X](#x) | [Y](#y) | [Z](#z)

## A
### <a name="annotation"></a>Annotation ([Entity](#entity))
A JSON format representing the objects and labels exists in an [Item](#item).
### <a name="artifacts"></a>Artifacts ([Entity](#entity))
Large files (binaries) that we don't want to pack inside a package (which should only contain code), but are still needed during the deployment of a package.They are uploaded separately and downloaded when the service is initiated.    Usually need to be added to the .gitignoreThere are three types: Item, Local, or Link
### <a name="assignment"></a>Assignment ([Entity](#entity))
A single annotators’ items for manual review and/or annotation. Items can be redistributed or reassigned between assignments.The annotator is referred to as an “assignee”
### <a name="attribute"></a>Attribute ([Entity](#entity))

## B
### <a name="binaries"></a>Binaries ([Item](#item))
The content of any type of file (image, video, pdf, etc)
### <a name="box"></a>Box ([Entity](#entity))
A bounding box [Annotation](#annotation) type. Represented by 2 point for top-left and bottom-right. type=`box`
## C
### <a name="clone"></a>Clone
A shallow copy of the item (with or without metadata and annotations) without copying the binaries.
### <a name="codebase"></a>Codebase ([Entity](#entity))
-four types of code bases: item codebase vs git codebase vs local codebase vs filesystem (currently no one uses this, and is likely for when working in a remote container)-limited to 100MB
### <a name="command"></a>Command

## D
### <a name="dataset"></a>Dataset ([Entity](#entity))

### <a name="dql"></a>DQL (Dataloop Query Language)

## E
### <a name="entity"></a>Entity
A Dataloop data model object. Represented by a json.
### <a name="execution"></a>Execution ([Entity](#entity))

## F
### <a name="function"></a>Function ([Entity](#entity))
definitions of where to find the class and how to load itFaaS is the function
## G
## H
## I
### <a name="instance-catalog"></a>Instance Catalog

### <a name="item"></a>Item ([Entity](#entity))
Data samples you upload to your dataset will be stored in something called an "item". Items are Dataloop objects that belong to the Dataloop "Item" class. They are stored as a "json" file and are represented as Dataloop data model objects. Items include the data sample you upload as well as the afferent metadata you add to that data sample. For example, each item has a "stream" method to get the data sample along with other json attributes, such as the metadata.
## J
## K
## L
### <a name="label"></a>Label ([Entity](#entity))
A piece of text that gives information about an annotation instance. Contains also the color, display name and children of the anntoation.
### <a name="logsample"></a>LogSample

## M
### <a name="metadata"></a>Metadata
A dictionary object that contains metadata of the Dl object. Usually includes “system” and “user” in the metadata fields to distinguish between necessary and custom user metadata.
### <a name="model"></a>Model
The representation of what a machine learning algorithm has learned from the training dataIs a python (pytorch, tensorflow) representation of a NN architecture with or without loaded weights (pth, pb, hdf5 files)
### <a name="model"></a>Model ([Entity](#entity))
A Dataloop Model is a combination of data (dl.Dataset), configurations (json dictionary), and code (dl.Package) to represent a learnable instance of the data.You can train, evaluate, compare, and deploy a dl.Model.Out-of-the-box models are available on the platform with the scope attribute “public”, as opposed to project specific models with “project” scope.
### <a name="model-adapter"></a>Model Adapter
A python class to wrap a generic ML code (train, predict etc) for standardizing models (and frameworks) to match the requirements of the Dataloop API.Log Sample, Metric Sample, A single data point is used to measure and compare different models and metrics. e.g. saving the train/validation loss and accuracy of a training sessionOffline ModeFor model management, only dl.Model is used to save configurations and training/evaluation metrics, while code and weights and biases are kept locally.Gives the ability to manage training runs, view live metrics, and compare dl.Models (configurations and metrics)Online ModeAllows integration into the Dataloop platform (after creating Model Adapter).Gives the ability to create custom buttons (e.g. in the annotations studio), train, deploy and evaluate using the Model Management Pages, using models inside a pipeline etc.)
### <a name="model-weights-/-model-artifacts"></a>Model Weights / Model Artifacts
Those are the files that are saved/created by training a machine learning algorithm on a dataset. They are adjusted using optimization algorithms and unique to each training session.
### <a name="module"></a>Module ([Entity](#entity))
A json representing the python class and functions (location, IOs etc.)
## N
### <a name="neural-network"></a>Neural Network
A machine learning model that is composed of layers consisting of simple connected units or neurons followed by nonlinearities.
## O
## P
### <a name="package"></a>Package ([Entity](#entity))
A package is the bundle of code and definitions that can be used for creating models or deploying services. Code is a dl.Codebase entity, and definitions include modules, functions, IOs, and the code entry point.Can be Python, nodeJS (maybe everything, we don't care).Used to deploy a service and create an executable version of that code.Limited to 100MBCan be public/global, or specific to a project
### <a name="pipeline"></a>Pipeline ([Entity](#entity))
A collection of functions (machine processing) and tasks (human processing) that creates a processing flow. Structured from nodes (processing units) and connections (to move data types between nodes)
### <a name="pipeline-cycle"></a>Pipeline Cycle
A single run over the pipeline. From the first node to the last available node to run
### <a name="pod-type"></a>Pod type

### <a name="polygon"></a>Polygon ([Entity](#entity))
A polygon [Annotation](#annotation) type. Represented by a list of (x,y) points. type=`segment`
## Q
## R
### <a name="repository"></a>Repository

## S
### <a name="segmentation"></a>Segmentation ([Entity](#entity))
A binary mask [Annotation](#annotation) type. Represented by mask with the same size as the image, 0 for background, 1 for the object. type=`binary`
### <a name="service"></a>Service ([Entity](#entity))
A deployed [Package](#package) that serves the code. Given the matching input to a function, it will run it and return the output, e.g. if we have code in our [Package](#package) for converting RGB images to grayscale, the dl.Service would run the code and upload the grayed image.
## T
### <a name="task"></a>Task ([Entity](#entity))
A set of items to be reviewed/annotated by human workers. A task is divided into assignments.Can be managed by a queue (Pulling Task) or by workload (percentage of items per assignee).The task is connected to a recipe for instructions and world definitions (ontology)
### <a name="trigger"></a>Trigger ([Entity](#entity))

## U
## V
## W
## X
## Y
## Z
