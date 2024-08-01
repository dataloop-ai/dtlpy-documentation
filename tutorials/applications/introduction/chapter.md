# Introduction

## What are Dataloop Applications?

Dataloop applications are extensions, which are add-ons that can work under the main platform of the Dataloop
ecosystem (Dataloop OS) and receive access to the predefined panels and can useDataloop SDK and Components to create
useful features for the end user.
Using applications, users can work more productively and efficiently by incorporating their custom functionality with
the underlying platform.

## Publish a DPK (Dataloop Package Kit)

The Dataloop package kit is a zipped file of the entire application's code.
It holds all the required components of the application, the panels it is serving, the services it uses, and the source
code of the application.
The base folder structure of the package is:

```
├── modules
│   ├── __init__.py
│   └── main.py
├── panels
│   └── index.html
├── src
│   └── .gitkeep
├── tests
│   ├── __init__.py
│   └── index.html
├── dataloop.json
├── README.md
├── build.sh
└── requirements.txt
```

The best way to start is to visit out GitHub Apps Space and see real and working examples. However, if you want to start
from scratch:

```python
import dtlpy as dl

project = dl.projects.get('Project Name')
dpk = project.dpks.publish()

```

## Installing Apps

### Marketplace

The [Marketplace](https://docs.dataloop.ai/docs/marketplace) serves as a central repository for saving and publishing
some custom applications, varying from a metadata
viewer application through audio recording on the website to a completely new UI for the item viewer.
The Applications are installed into the platform (to a project or entire organization).
To find an application, go to the marketplace, search for an application by name, category, etc., select and click
install.
Now all the application's components should be available to use.
You can change any settings or configuration (e.g. machine type, autoscaling) in the app settings.

### Using SDK

Installing an app is also available in the SDK:

```python
import dtlpy as dl

project = dl.projects.get('Apps Project')
dpk = dl.dpks.get(dpk_name='<app-name>')
project.apps.install(dpk=dpk)
```

## DPK Components

### Scopes

A DPK can be available for installation at either the Project or Organization level:

* **Project Scope:** The DPK is only available for installation within the specific project where it’s published.
* **Organization Scope:** The DPK is accessible across all projects within the organization but must be installed
  individually for each project.

This setup gives you control over where the DPK can be installed based on your specific requirements.
The scope can be set in the manifest directly (see the examples below) or when publishing:

```python
import dtlpy as dl
import json

project = dl.projects.get('Project Name')
with open('dataloop.json', 'r') as file:
    manifest = json.load(file)

dpk = dl.Dpk.from_json(_json=manifest,
                       client_api=dl.client_api,
                       project=project)
dpk.scope = "project"  # or 'organization'
dpk = project.dpks.publish(dpk)

```

Applications are installed within the scope of individual projects.
If a DPK is set with `scope=organization`, it will be accessible for installation across all projects within the
organization, but each project requires a separate installation.

### Codebase

Codebase can be either directly from git repo and tag, or using Dataloop's Item Codebase.
Codebase can be set directly in the manifest file, or using the python SDK:

```python
import dtlpy as dl
import json
import os

project = dl.projects.get('Project Name')
with open('dataloop.json', 'r') as file:
    manifest = json.load(file)

dpk = dl.Dpk.from_json(_json=manifest,
                       client_api=dl.client_api,
                       project=project)

# Local codebase
codebase = project.codebases.pack(directory=os.getcwd(),
                                  name=dpk.name,
                                  description="some description")

# Git codebase
codebase = dl.GitCodebase(git_url='git_url',
                          git_tag='git_tag')

dpk.codebase = codebase
dpk = project.dpks.publish(dpk)

```

### Panels and toolbars

A Panel represents the view the user is going to see.
The panel can be deployed into any available slot in the main platform, for example:

* Item Viewer - Overrides the Item viewer content with a custom-made layout to view an item from the task browser or the
  dataset browser.
* Floating Window - create a new window on top of the platform, which can be dragged and resized, and shows the panel.
* Data Browser - change the browsing view of items in a dataset
* Item Side Panel - Add a new side panel to the Annotation and Info panels in the item viewer.

A Toolbar is a panel that can be ***rendered*** into the platform slots and is NOT served, for example:

* Buttons in the item studio, data browser, task menu, etc.
* Configuration panels
* Project widgets

### Modules and Functions

Python functions and modules can be used in the app, they are defined in the "modules" directory. For more information
about our python modules go [here](https://developers.dataloop.ai/tutorials/faas/single_function_rgb_to_gray/chapter/).

### Services

Services are the carriers of the app panels and backend. A service is responsible for running a panel and managing its
lifecycle. The dl.Service entity represents the service, for more information about services,
click [here](https://developers.dataloop.ai/tutorials/faas/single_function_rgb_to_gray/chapter/).

### All the Others

You can use any other Dataloop entity (Models, Tasks, etc.) in the app. Simply define it in the manifest, and it will be
created on installation.

## App Manifest - dataloop.json

The json to describe the app is saved at the root of the app directory and is named dataloop.json. Is contains all the
definitions of the app components.
More example in [this page](https://developers.dataloop.ai/tutorials/applications/dpk_examples/chapter/), and you can
find real working manifests example in the [GitHub](https://github.com/dataloop-ai-apps)

