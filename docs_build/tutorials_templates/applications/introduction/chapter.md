# 🎮 Welcome to Dataloop Applications - Level Up Your Platform!

## 🌟 What are Dataloop Applications?



These applications are extensions that plug right into the Dataloop ecosystem (we call it Dataloop OS), giving you access to:
* Custom panels that feel right at home in the platform 
* The mighty Dataloop SDK for crafting powerful features
* Special components that make your workflow smoother

Just like choosing the right tools for crafting in a game, applications let you customize your workspace with exactly what you need! 🛠️

## 📦 The Art of DPK (Dataloop Package Kit)

Think of a DPK as your application's treasure chest - it's a magical bundle that contains everything your application needs to work its wonders! Let's peek inside this chest:

```
📁 Your DPK Structure
├── 📂 modules/            # Your Python magic spells
│   ├── __init__.py
│   └── main.py
├── 📂 panels/            # Your UI enchantments
│   └── index.html
├── 📂 src/              # Your source code artifacts
│   └── .gitkeep
├── 📂 tests/            # Your quality assurance scrolls
│   ├── __init__.py
│   └── index.html
├── 📜 dataloop.json     # The sacred manifest
├── 📜 README.md         # Your application's story
├── 📜 build.sh         # Your building instructions
└── 📜 requirements.txt  # Your dependencies scroll
```

Want to see some real magic in action? Visit our [GitHub Apps Space](https://github.com/dataloop-ai-apps) for working examples! But if you're feeling adventurous and want to start from scratch:

```python
import dtlpy as dl

# Create your first DPK
project = dl.projects.get('Project Name')
dpk = project.dpks.publish()
```

## 🚀 Installing Your Applications

### 🏪 The Marketplace Way

Think of the [Marketplace](https://docs.dataloop.ai/docs/marketplace) as your app store - it's where all the cool applications hang out! Here you'll find everything from:
* 🔍 Metadata viewers
* 🎙️ Annotation Studios
* 🖼️ AI Model Adapters
* And many more magical tools!

To install an app:
1. 🏃‍♂️ Sprint to the marketplace
2. 🔍 Search for your desired application
3. 🎯 Click install
4. ✨ Watch the magic happen!

Need to tweak some settings? You can adjust machine types, autoscaling, and other configurations in the app settings.

### 🐍 The Python SDK Way

For those who prefer to wave their Python wand:

```python
import dtlpy as dl

# Get your project ready
project = dl.projects.get('Apps Project')

# Find your desired app
dpk = dl.dpks.get(dpk_name='<app-name>')

# Cast the installation spell
project.apps.install(dpk=dpk)
```

## 🧩 DPK Components - The Building Blocks

### 🎯 Scopes

Your DPK can cast its magic in two realms:
* 🏰 **Project Scope:** The app only works within its home project
* 🌍 **Organization Scope:** The app can work across all projects in your organization

Here's how to set your scope:

```json
{ 
    "name": "My App",
    "scope": "project"
    ...
}
```

### 💾 Codebase

Your application's brain can live in two places:
* 📦 Directly in a git repository with a specific tag
* 🗄️ In Dataloop's Item Codebase

Here's how to set it up:

```python
# For local codebase
codebase = project.codebases.pack(directory=os.getcwd(),
                                  name=dpk.name,
                                  description="My awesome app!")

# For git codebase
codebase = dl.GitCodebase(git_url='git_url',
                          git_tag='git_tag')

dpk.codebase = codebase
dpk = project.dpks.publish(dpk)
```

### 🎨 Panels and Toolbars

Think of panels as your app's face - they're what users see and interact with. You can place them in various spots:
* 🖼️ Item Viewer - Give items a fresh look
* 🪟 Floating Window - Create movable command centers
* 📂 Data Browser - Reimagine how users browse items
* ℹ️ Item Side Panel - Add helpful sidekicks to the viewer

Toolbars are like your app's quick actions - they can appear as:
* 🔘 Buttons in various places
* ⚙️ Configuration panels
* 📊 Project widgets

### 🐍 Modules and Functions

Your Python modules are like spell books - they hold all the powerful functions your app can perform. Find out more about crafting these spells in our [FaaS tutorial](https://developers.dataloop.ai/tutorials/faas/single_function_rgb_to_gray/chapter/).

### 🔧 Services

Think of services as your app's faithful servants - they keep your panels running and manage their lifecycle. Learn more about training these helpers in our [FaaS tutorial](https://developers.dataloop.ai/tutorials/faas/single_function_rgb_to_gray/chapter/).

### 🎁 And More!

You can use any other Dataloop entity (Models, Tasks, etc.) in your app - just define them in your manifest, and they'll spring to life during installation!

## 📜 The Sacred Manifest - dataloop.json

Your `dataloop.json` is like your app's spellbook - it contains all the instructions for how your app should work. Check out more examples in our [DPK Examples](https://developers.dataloop.ai/tutorials/applications/dpk_examples/chapter/) page, or explore real-world magic in our [GitHub](https://github.com/dataloop-ai-apps)!

Ready to create your own magical application? Let's get started! 🚀✨

