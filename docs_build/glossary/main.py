import string

definitions = [
    {"name": "Entity",
     "description": "A Dataloop data model object. Represented by a json."},
    {"name": "Repository",
     "description": ""},
    {"name": "Item ($Entity)",
     "description": "An object representing some file and metadata"},
    {"name": "Binaries (Item)",
     "description": "The content of any type of file (image, video, pdf, etc)"},
    {"name": "Clone",
     "description": "A shallow copy of the item (with or without metadata and annotations) without copying the binaries."},
    {"name": "Annotation ($Entity)",
     "description": "A JSON format representing the objects and labels exists in an $Item."},
    {"name": "Label ($Entity)",
     "description": "A piece of text that gives information about an annotation instance. Contains also the color, display name and children of the anntoation."},
    {"name": "Attribute ($Entity)",
     "description": ""},
    {"name": "Box ($Entity)",
     "description": "A bounding box $Annotation type. Represented by 2 point for top-left and bottom-right. type=`box`"},
    {"name": "Polygon ($Entity)",
     "description": "A polygon $Annotation type. Represented by a list of (x,y) points. type=`segment`"},

    {"name": "Segmentation ($Entity)",
     "description": "A binary mask $Annotation type. Represented by mask with the same size as the image, 0 for background, 1 for the object. type=`binary`"},

    {"name": "Task ($Entity)",
     "description": "A set of items to be reviewed/annotated by human workers. A task is divided into assignments."
                    "Can be managed by a queue (Pulling Task) or by workload (percentage of items per assignee)."
                    "The task is connected to a recipe for instructions and world definitions (ontology)"},
    {"name": "Assignment ($Entity)",
     "description": "A single annotators’ items for manual review and/or annotation. Items can be redistributed or reassigned between assignments."
                    "The annotator is referred to as an “assignee”"},
    {"name": "Package ($Entity)",
     "description": "A package is the bundle of code and definitions that can be used for creating models or deploying services. Code is a dl.Codebase entity, and definitions include modules, functions, IOs, and the code entry point."
                    "Can be Python, nodeJS (maybe everything, we don't care)."
                    "Used to deploy a service and create an executable version of that code."
                    "Limited to 100MB"
                    "Can be public/global, or specific to a project"},
    {"name": "Module ($Entity)",
     "description": "A json representing the python class and functions (location, IOs etc.)"},
    {"name": "Function ($Entity)",
     "description": "definitions of where to find the class and how to load it"
                    "FaaS is the function"},
    {"name": "Codebase ($Entity)",
     "description": "-four types of code bases: item codebase vs git codebase vs local codebase vs filesystem (currently no one uses this, and is likely for when working in a remote container)"
                    "-limited to 100MB"},
    {"name": "Artifacts ($Entity)",
     "description": "Large files (binaries) that we don't want to pack inside a package (which should only contain code), but are still needed during the deployment of a package."
                    "They are uploaded separately and downloaded when the service is initiated.    "
                    "Usually need to be added to the .gitignore"
                    "There are three types: Item, Local, or Link"},
    {"name": "Service ($Entity)",
     "description": "A deployed $Package that serves the code. Given the matching input to a function, it will run it and return the output, e.g. if we have code in our $Package for converting RGB images to grayscale, the dl.Service would run the code and upload the grayed image."},
    {"name": "Execution ($Entity)",
     "description": ""},
    {"name": "Trigger ($Entity)",
     "description": ""},
    {"name": "Pod type",
     "description": ""},
    {"name": "Instance Catalog",
     "description": ""},
    {"name": "Model ($Entity)",
     "description": "A Dataloop Model is a combination of data (dl.Dataset), configurations (json dictionary), and code (dl.Package) to represent a learnable instance of the data."
                    "You can train, evaluate, compare, and deploy a dl.Model."
                    "Out-of-the-box models are available on the platform with the scope attribute “public”, as opposed to project specific models with “project” scope."},
    {"name": "LogSample",
     "description": ""},
    {"name": "Model Adapter",
     "description": "A python class to wrap a generic ML code (train, predict etc) for standardizing models (and frameworks) to match the requirements of the Dataloop API."
                    "Log Sample, Metric Sample, A single data point is used to measure and compare different models and metrics. e.g. saving the train/validation loss and accuracy of a training session"
                    "Offline Mode"
                    "For model management, only dl.Model is used to save configurations and training/evaluation metrics, while code and weights and biases are kept locally."
                    "Gives the ability to manage training runs, view live metrics, and compare dl.Models (configurations and metrics)"
                    "Online Mode"
                    "Allows integration into the Dataloop platform (after creating Model Adapter)."
                    "Gives the ability to create custom buttons (e.g. in the annotations studio), train, deploy and evaluate using the Model Management Pages, using models inside a pipeline etc.)"},
    {"name": "Model",
     "description": "The representation of what a machine learning algorithm has learned from the training data"
                    "Is a python (pytorch, tensorflow) representation of a NN architecture with or without loaded weights (pth, pb, hdf5 files)"},
    {"name": "Model Weights / Model Artifacts",
     "description": "Those are the files that are saved/created by training a machine learning algorithm on a dataset. They are adjusted using optimization algorithms and unique to each training session."},
    {"name": "Neural Network",
     "description": "A machine learning model that is composed of layers consisting of simple connected units or neurons followed by nonlinearities."},
    {"name": "Command",
     "description": ""},
    {"name": "Pipeline ($Entity)",
     "description": "A collection of functions (machine processing) and tasks (human processing) that creates a processing flow. Structured from nodes (processing units) and connections (to move data types between nodes)"},
    {"name": "Pipeline Cycle",
     "description": "A single run over the pipeline. From the first node to the last available node to run"},

    {"name": "Metadata",
     "description": "A dictionary object that contains metadata of the Dl object. Usually includes “system” and “user” in the metadata fields to distinguish between necessary and custom user metadata."},
    {"name": "DQL - Dataloop Query Language",
     "description": ""},
    {"name": "Dataset ($Entity)",
     "description": ""},
    {"name": "",
     "description": ""},

]


def create():
    md_string = "# Glossary\n"
    md_string += "\n"
    letters = list(string.ascii_uppercase)
    headers = [f"[{letter.upper()}](#{letter.lower()})" for letter in letters]
    md_string += " | ".join(headers)
    md_string += "\n"
    md_string += "\n"
    sorted_definitions = sorted(definitions, key=lambda d: d['name'].lower())
    for letter in letters:
        letter_definitions = [definition for definition in sorted_definitions if
                              definition["name"].lower().startswith(letter.lower())]
        md_string += f"## {letter.upper()}\n"
        for definition in letter_definitions:
            md_string += f"### {definition['name']}\n"
            md_string += f"{definition['description']}\n"

    with open('docs_build/glossary/glossary.md', 'w', encoding='utf8') as f:
        f.write(md_string)
