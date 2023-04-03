### What are Dataloop Applications?

Dataloop applications are extensions, add-ons which can work under the main platform of the dataloop ecosystem (Dataloop
OS) and receive access to the predefined panels and can utilise Dataloop SDK and Components to create a useful features for
the end user.

*Using the applications, users can work more productively and efficiently, by incorporating their custom functionality
with the underlying platform.*

#### Start an App!
*The best way to start is to visit out [GitHub Apps Space](https://github.com/dataloop-ai-apps) and see real and working examples!*

But if you really want to start from scratch:
1. Install the Dataloop SDK
2. Create a directory where you wished to initialize the project in your terminal.
3. In the terminal, type:
```shell
dlp app init
```
4. Follow the steps and question or leave them empty for defaults.

Package is now ready to start the development!


#### Apps

The Applications are installed into the platform (to a project or entire organization).
From the App Store, search application (by name, categories, etc.) and just click install.
Now all the application's components should be available to use.
You can change any settings or configuration (e.g. machine type, autoscaling) in the app settings.

#### DPK - Dataloop Package

The dataloop package is a zipped file of the entire application's code.

It holds all the required components of the application, the panels it is serving, the services it uses, and the source
code of the application.

The base folder structure of the package is:
[]

##### Panels and Toolbars

A Panel represents the view the user is going to see.
The panel can be deployed into any available slot in the main platform, for example:

1. Item Viewer - Overrides the Item viewer content with a custom-made layout to view an item from the task browser or
   the dataset browser.
2. Floating Window - create a new window on top of the platform, which can be dragged and resized, and shows the panel.
3. Data Browser - change the browsing view of items in a dataset
4. Item Side Panel - Add a new side panel to the Annotation and Info panels in the item viewer.

A Toolbar is not *served*, it's a panel that can be rendered into the platform slots, for example:

1. Buttons in the item studio, data browser, task menu, etc.
2. Configuration panels
3. Project widgets
4.

##### Modules and Functions

Python functions and modules can be used in the app, they are defined in the "modules" directory.
For more information about our python modules go here.

##### Services

Services are the carriers of the app panels and backend.
A service is responsible for running a panel and managing its lifecycle.
The dl.Service entity represents the service, for more information about services, please refer to the documentation.

##### All the Others

You can use any other Dataloop entity (Models, Tasks, etc.) in the app.
Simply define it in the manifest, and it will be created on installation

#### App Manifest - dataloop.json

The json to describe the app is saved at the root of the app directory and is named dataloop.json.
Is contains all the definitions of the app components

#### Store

The App Store serves as a central repository for saving and publishing some custom applications,
varying from a metadata viewer application through audio recording on the website to a completely new UI for the item
viewer.

#### Typical Workflow

Create an application (the FE and BE)

Initialize the application using the command line/python SDK (and maybe a template in the future)

Test your application locally, with the debugging tool in the platform

Tweak in the process the dataloop.json file to accommodate your needs.

Build your application and move the files into the appropriate panel directory. (NOTE: the application entry point is
the index.html file)

CURRENTLY: add the directory to the path of the generated js/CSS files

Deploy your application. (You might need to change the env using dl.setenv() for Dataloop developers)

Sample script: (Run it in the root folder of your application)

*Note*
Changing the application configuration to build in the right directory (instead of the default ‘/dist’):

Vue - change ‘vue.config.js’ outputDir property to the directory of the panel

React - and .env file to the root folder of your project, and add BUILD_PATH='PATH_TO_PANEL'

Angular - open the angular.json file and change projects.<APP_NAME>.architect.build.options.outputPath to the path of
the panel.




