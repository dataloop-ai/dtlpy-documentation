
# Advanced Onboarding Exercise using Dataloop's Python SDK
Welcome to the second step of Dataloop’s Python SDK onboarding process. If you are coming here from the first part of Dataloop’s Python SDK Onboarding, which teaches how to do basic operations using the Python SDK, this guide is the next step in your journey to learn how to use Dataloop without using the Dataloop UI.

If you haven’t yet checked the initial onboarding, you can [find it here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/onboarding/01_sdk_installation.md). 

Also, you can [visit the Dataloop Developer Community Getting Started repository]([https://github.com/dataloop-ai](https://github.com/dataloop-ai-apps/dataloop-devs) to get a look at Dataloop’s documentation, suggested tools, etc. and Open Source Solution repository.

This Onboarding exercise will take you through an interactive and fun guide meant to teach you how to use Dataloop to solve a “real-world” problem. 
Without further ado, you will now learn how to use Dataloop to find and categorize some escaped magical animals and then train a model to classify them.
## The story
Once upon a time, in a world not far from our own, there was a zoo teeming with magical creatures that made you believe in fairy tales. 
All visitors to the zoo adored these creatures, and the staff nurtured and groomed them.

But, one day all hell broke loose! The animals broke free from their cages and made their way into the city, led by a tiger smarter than Einstein. The zoo staff was hot on their tails, but the animals were as quick as a caffeine-fueled cheetah (or Python coder) and slipped through their fingers.

As the search for the missing animals continued, the zoo's staff realized they needed assistance. As a result, they enlisted the assistance of local authorities to complete the mission. One of the officers knew about Dataloop's AI data management and advanced annotation platform, and he immediately contacted them for help. The police sent all the zoo images of creatures to Dataloop’s AI department. 

You are one of Dataloop's Top Data Scientists, and you need to research how to help the zoo find all of the missing creatures. Let the hunt begin!

## First steps: Installation
If you came here from the previous Onboarding, you should already have Dataloop’s Python SDK installed, and know how to install it. If you don’t, you can learn about the [installation guide here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/onboarding/01_sdk_installation.md) and the [login guide here](https://github.com/dataloop-ai/dtlpy-documentation/blob/main/onboarding/02_login_and_project_and_dataset_creation.md). 

We highly recommend that you follow the first [onboarding guide](https://github.com/dataloop-ai/dtlpy-documentation/tree/main/onboarding) from beginning to end if you want to better understand what we will do next.
## Creating project and dataset
The first to do is to import Dataloop’s Python package and log in. After that, we will create a new project called “CreatureHunt” and a new dataset for that project, called “Creatures”. Copy the code below, and it should all work fine if you installed the platform correctly and logged in. The explanation for each of the lines of code can be found as comments in the code.


```python
import dtlpy as dl # importing Dataloop’s Python SDK
#Logging in to Dataloop - This should redirect you to a login page the first time you use it
if dl.token_expired():
    dl.login()


#Create a new project - run once and then comment out to avoid getting an (harmless) error each time you run your code
project = dl.projects.create(project_name='CreatureHunt')
# "get" the new project
project = dl.projects.get(project_name='CreatureHunt')
#Create a new dataset - run once and then comment out to avoid getting an (harmless) error each time you run your code
dataset = project.datasets.create(dataset_name='Creatures')       
# "get" the new dataset
dataset = project.datasets.get(dataset_name='Creatures')
```
Now that you've created the  project and dataset, you need to download our "magical creatures" dataset. It contains aprox. 100 samples for each of the 10 classes of magical creatures that escaped from the zoo.

[Download the dataset from here](https://drive.google.com/drive/u/0/folders/1eIHZgN0iHWG3vlmxQD7rvNhSeFg7BLPM).

After downloading these images, add them to an easily accesible folder as you will need to let the platform know where those images are. Then, you can copy and run the code below, after making sure you set the right path to the dataset. Make a folder called "MagicalCreatures" and then create 2 folders in it, one called "images_folder" which will contain the dataset images, and another called "annotations_folder" which will have the data you will annotate". The example below is for a windows path.
```python
#set local path (the location of the images) - Set your own path
local_items_path = r'C:\Users\User\Desktop\MagicalCreatures\images_folder\*'
#Set the local path to annotated data - Set your own path
local_annotations_path = r'C:\Users\User\Desktop\MagicalCreatures\annotations_folder'
```
Now, you should place the dataset you downloaded into the "images_folder" you created, so we can upload them to Dataloop's platform.

```python
	#upload annotated and un-annotated data
dataset.items.upload(local_path=local_items_path, local_annotations_path=local_annotations_path)
	#create filter to select all unannotated data
filters = dl.Filters(field='<annotated>', values=False)
	#create a new task and assign it to your mail
```

You can now create an annotation task and optionally assign yourself or other annotators to work the task.  We suggest you just assign yourself for this exercise, so just replace <annotator1@dataloop.ai> with your Dataloop user id then delete `, '<annotator2@dataloop.ai>'` from the code example.
```python
#create a task for the annotation of the imagaes
import datetime
task = dataset.tasks.create(
    task_name='annotate_creatures',
    due_date=datetime.datetime(day=11, month=3, year=2025).timestamp(),
    assignee_ids=['<annotator1@dataloop.ai>', '<annotator2@dataloop.ai>'],
    # The items will be divided equally between assignees
    filters=filters  # (optional) filter by folder directory or use other filters
)
```



After creating a project and dataset, we can open the project in the web version of the Dataloop platform.

```python
#Opening the new project in web view
dl.projects.open_in_web(project_name="CreatureHunt")
```

After executing that line of code, you may have to log in to the platform again. Just use your e-mail and password used to create your Dataloop account to log into the platform. You will then see the screen below:
![image](https://user-images.githubusercontent.com/58508793/218433304-084f12ed-3ce0-441c-92fd-992f20fa0a5f.png)

If you hover with your mouse on the left-side of your screen, a pannel should open up and you should have the active project "CreatureHunt", as seen below:
![image](https://user-images.githubusercontent.com/58508793/218434388-8bbf991a-7bd3-4d93-bed4-bb655268e098.png)

## Annotating Your Data

(Here will be placed Ira's section)




## Importing Model and Training


For this section, you will need to install an extra package, called Pytorch. You can install it from their [install page](https://pytorch.org/get-started/locally/), as your hardware and software setup allows. If you have a good Nvidia GPU, we highly advise you to install the CUDA version, as it will highly accelerate the training process. Otherwise, you can just use the basic CPU version, which will be slower, but will get the job done. If you have installed Python using Anaconda select Conda, otherwise select "pip". 
