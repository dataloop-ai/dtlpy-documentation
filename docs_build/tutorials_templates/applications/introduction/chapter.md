# Introduction
## What are Dataloop Applications?
Dataloop applications are extensions, which are add-ons that can work under the main platform of the Dataloop ecosystem (Dataloop OS) and receive access to the predefined panels and can useDataloop SDK and Components to create useful features for the end user.
Using applications, users can work more productively and efficiently by incorporating their custom functionality with the underlying platform.

### Start an App!
The best way to start is to visit out [GitHub Apps Space](https://github.com/dataloop-ai-apps) and see real and working examples.
However, if you want to start from scratch:
1. Install the [Dataloop SDK](https://developers.dataloop.ai/tutorials/getting_started/sdk_overview/chapter/#installing-prerequisite-software)
2. Create a directory where you wished to initialize the project in your terminal.
3. In the terminal, type:
```shell
dlp app init
```
4. Follow the steps and question or leave them empty for defaults.

5. The app is now ready for development!

### Installing apps
The Applications are installed into the platform (to a project or entire organization). To find an application, go to the App Store, search for an application by name, category, etc., select and click install.
Now all the application's components should be available to use.
You can change any settings or configuration (e.g. machine type, autoscaling) in the app settings.

Installing an app is also available in the SDK and CLI, simply:
```python
project = dl.projects.get('Apps Project')
dpk = dl.dpks.get(dpk_name='<app-name>')
project.apps.install(dpk=dpk)
```


### Parts of an application
#### DPK - Dataloop Package Kit
The Dataloop package kit is a zipped file of the entire application's code.
It holds all the required components of the application, the panels it is serving, the services it uses, and the source code of the application.
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

#### Panels and toolbars
A Panel represents the view the user is going to see.
The panel can be deployed into any available slot in the main platform, for example:
* Item Viewer - Overrides the Item viewer content with a custom-made layout to view an item from the task browser or the dataset browser.
* Floating Window - create a new window on top of the platform, which can be dragged and resized, and shows the panel.
* Data Browser - change the browsing view of items in a dataset
* Item Side Panel - Add a new side panel to the Annotation and Info panels in the item viewer.

A Toolbar is a panel that can be ***rendered*** into the platform slots and is NOT served, for example:
* Buttons in the item studio, data browser, task menu, etc.
* Configuration panels
* Project widgets


#### Modules and Functions
Python functions and modules can be used in the app, they are defined in the "modules" directory. For more information about our python modules go [here](https://developers.dataloop.ai/tutorials/faas/single_function_rgb_to_gray/chapter/).

#### Services
Services are the carriers of the app panels and backend. A service is responsible for running a panel and managing its lifecycle. The dl.Service entity represents the service, for more information about services, click [here](https://developers.dataloop.ai/tutorials/faas/single_function_rgb_to_gray/chapter/).

#### All the Others
You can use any other Dataloop entity (Models, Tasks, etc.) in the app. Simply define it in the manifest, and it will be created on installation.

### App Manifest - dataloop.json
The json to describe the app is saved at the root of the app directory and is named dataloop.json. Is contains all the definitions of the app components.
You can find real working manifests example in the [GitHub](https://github.com/dataloop-ai-apps)

### App Store
The App Store serves as a central repository for saving and publishing some custom applications, varying from a metadata viewer application through audio recording on the website to a completely new UI for the item viewer.

## Typical Workflow
1. Create an application (the FE and BE)
2. Initialize the application using the command line/python SDK (and maybe a template in the future)
3. Test your application locally, with the debugging tool in the platform
4. Tweak in the process the dataloop.json file to accommodate your needs.
5. Build your application and move the files into the appropriate panel directory. (NOTE: the application entry point is the index.html file)
6. CURRENTLY: add the directory to the path of the generated js/CSS files
7. Deploy your application.
8. Sample script can be found here, run it in the root folder of your application.


Note: Changing the application configuration to build in the right directory (instead of the default ‘/dist’):
Vue - change ‘vue.config.js’ outputDir property to the directory of the panel
React - and .env file to the root folder of your project, and add BUILDPATH='PATHTO_PANEL'
Angular - open the angular.json file and change projects.<APP_NAME>.architect.build.options.outputPath to the path of the panel.


