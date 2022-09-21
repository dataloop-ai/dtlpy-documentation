# Glossary

[A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) | [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w) | [X](#x) | [Y](#y) | [Z](#z)

## A
## B
### Binaries

## C
### Clone
A shallow copy of the item (with or without metadata and annotations) without copying the binaries.
### Command

## D
### dl.Annotation

### dl.Annotation

### dl.Artifacts
Large files (binaries) that we don't want to pack inside a package (which should only contain code), but are still needed during the deployment of a package.They are uploaded separately and downloaded when the service is initiated.    Usually need to be added to the .gitignoreThere are three types: Item, Local, or Link
### dl.Assignment
A single annotators’ items for manual review and/or annotation. A Task may consist of one or more assignments. Items can be redistributed or reassigned between assignments.The annotator is referred to as an “assignee”
### dl.Attribute

### dl.Box

### dl.Codebase
-four types of code bases: item codebase vs git codebase vs local codebase vs filesystem (currently no one uses this, and is likely for when working in a remote container)-limited to 100MB
### dl.Dataset

### dl.Execution (Entity)

### dl.Function
definitions of where to find the class and how to load itFaaS is the function
### dl.Item 

### dl.Label
A piece of text that gives information about an annotation instance
### dl.LogSample (Entity?)

### dl.Model (Entity)
A Dataloop Model is a combination of data (dl.Dataset), configurations (json dictionary), and code (dl.Package) to represent a learnable instance of the data.You can train, evaluate, compare, and deploy a dl.Model.Out-of-the-box models are available on the platform with the scope attribute “public”, as opposed to project specific models with “project” scope.
### dl.Module

### dl.Package
A package is the bundle of code and definitions that can be used for creating models or deploying services. Code is a dl.Codebase entity, and definitions include modules, functions, IOs, and the code entry point.Can be Python, nodeJS (maybe everything, we don't care).Used to deploy a service and create an executable version of that code.Limited to 100MBCan be public/global, or specific to a project
### dl.Pipeline
A collection of functions (machine processing) and tasks (human processing) that creates a processing flow. Structured from nodes (processing units) and connections (to move data types between nodes)
### dl.Polygon
“segment”
### dl.Segmentation
binary
### dl.Service (Entity)
A deployed dl.Package that serves the code. Given the matching input to a function, it will run it and return the output, e.g. if we have code in our dl.Package for converting RGB images to grayscale, the dl.Service would run the code and upload the grayed image.
### dl.Task
A set of items to be reviewed/annotated by human workers. A task is divided into assignments.Can be managed by a queue (Pulling Task) or by workload (percentage of items per assignee).The task is connected to a recipe for instructions and world definitions (ontology)
### dl.Trigger (Entity)

### DQL - Dataloop Query Language

## E
### Entity/Resource
A Dataloop model object. Represented by a json.
## F
## G
## H
## I
### Instance Catalog

## J
## K
## L
## M
### Metadata
A dictionary object that contains metadata of the Dl object. Usually includes “system” and “user” in the metadata fields to distinguish between necessary and custom user metadata.
### Model
The representation of what a machine learning algorithm has learned from the training dataIs a python (pytorch, tensorflow) representation of a NN architecture with or without loaded weights (pth, pb, hdf5 files)
### Model Adapter
A python class to wrap a generic ML code (train, predict etc) for standardizing models (and frameworks) to match the requirements of the Dataloop API.Log Sample, Metric Sample, A single data point is used to measure and compare different models and metrics. e.g. saving the train/validation loss and accuracy of a training sessionOffline ModeFor model management, only dl.Model is used to save configurations and training/evaluation metrics, while code and weights and biases are kept locally.Gives the ability to manage training runs, view live metrics, and compare dl.Models (configurations and metrics)Online ModeAllows integration into the Dataloop platform (after creating Model Adapter).Gives the ability to create custom buttons (e.g. in the annotations studio), train, deploy and evaluate using the Model Management Pages, using models inside a pipeline etc.)
### Model Weights / Model Artifacts
Those are the files that are saved/created by training a machine learning algorithm on a dataset. They are adjusted using optimization algorithms and unique to each training session.
## N
### Neural Network
A machine learning model that is composed of layers consisting of simple connected units or neurons followed by nonlinearities.
## O
## P
### Pipeline Cycle
A single run over the pipeline. From the first node to the last available node to run
### Pod type

## Q
## R
### Repository

## S
## T
## U
## V
## W
## X
## Y
## Z
