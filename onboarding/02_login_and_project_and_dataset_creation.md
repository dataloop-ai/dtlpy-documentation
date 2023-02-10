# 02\_login\_and\_project\_and\_dataset\_creation

### Sign up and log in to Dataloop

To be able to use our Python SDK or our other tools such as our API, you must first create an account on the Dataloop platform and then log in.  To get started, you can create a Free account which you can upgrade later to a paid account should you desire.

To create an account you can [click here](https://dataloop-production.auth0.com/login?state=hKFo2SBYdnBxZUVLTHRhQlpRTXM5bXdDYWxQdWpOUE9KZFNabqFupWxvZ2luo3RpZNkgNjg3YnRKem5yV2NwSmJVN29UVnBTbGJtYUJFSURRNnCjY2lk2SBGckcwSFpnYTFDSzVVVlVTSkp1RGtTRHFJdFBpZVdHVw\&client=FrG0HZga1CK5UVUSJJuDkSDqItPieWGW\&protocol=oauth2\&response\_type=id\_token%20code\&response\_mode=form\_post\&redirect\_uri=https%3A%2F%2Fgate.dataloop.ai%2Fadmit%3Fdefault\&scope=openid%20email%20profile%20offline\_access\&nonce=wy9u651zOeGnuAqKxk\~-AfeIKo9hL9AP\&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMS4zIn0%3D). You will be redirected to a Sign up/Login page, which you can use to create an account using your e-mail or Google sign-in as an option.

Once you do that, we can go on and try to login to the platform using the Python SDK. To accomplish this, you need to either open Python in your console or open an IDE where you can run the Python code. Some examples of IDEs are [Spyder](https://www.spyder-ide.org/) and [VisualStudio](https://code.visualstudio.com/) Code.

**Before you get started**:  Please note that all of these examples are proven to work when you are using the console or your IDE is running on your local machine.  If you're using an isolated environment on your local machine (example, Jupyter Notebook running in an Docker Container), things like the Login browser instantiation might not work.  The login call needs to pass cleanly from the console or IDE directly to the browser.  Isolated environments might not successfully make that round trip call.

When you are ready to write Python code in the IDE of your choice, you can use the following lines of code to log in into the platform:\


```python
import dtlpy as dl
dl.login()
```

After executing them, a browser tab will be opened where you can log in using the credentials you used at the Sign up step above.

\
![image](https://user-images.githubusercontent.com/58508793/216592564-635791c5-3004-46de-9dcf-5e1f059a97c7.png)

If everything is good, you will see a banner saying that you can return to coding, which means you successfully logged in!  You can close the browser tab.

\
![image](https://user-images.githubusercontent.com/58508793/216593171-4075acc5-9917-4ce6-9d1f-45c4feb3dfe1.png)

Keep in mind that the login token lasts for 24 hours. After that, you will need to execute the login code again.&#x20;

Optionally, you can use the following code, which will check every time when your run your code if the login token expired or not, and also will allow you to run all of your code, without having to log in every time:\


```python
import dtlpy as dl
if dl.token_expired():
   dl.login()
```

#### Machine-to-Machine (M2M) Login

The M2M login flow allows machines to obtain a valid, signed JWT (authentication token) and automatically refresh it without the need for a web browser login. M2M login is recommended when you want to run commands on the platform without an ongoing internet connection or to run API commands directly from an external system to Dataloop.

To do leverage M2M login, you first need to create a bot user with a unique name:

```python
import dtlpy as dl
dl.login() # use browser login to create the bot
project = dl.projects.get(project_name='myProject') # get your project
myBot = project.bots.create(name='my-unique-name', return_credentials=True)
```

A bot user on the Dataloop platform is similar to a user with Developer priveleges.  The difference is that it runs in the background vs being an interactive user via the Dataloop UI.  You can view the bot user via the UI under Contributors on the Project Dashboard.

<figure><img src="../.gitbook/assets/Screenshot 2023-02-10 at 10.22.34 AM.png" alt=""><figcaption><p>Bot user created during M2M login setup</p></figcaption></figure>

Make sure you save the log in credentials of the bot you just created for future logins. You can find them using these lines of code:

```python
print("the bot email is "+myBot.email)
print("the bot password is "+myBot.password)
```

Then, you can log in to the Dataloop platform using the Python SDK and you newly created M2M bot credentials:

```python
import dtlpy as dl
dl.login_m2m(email=email, password=password)
```

### Creating a New Project

Now that you're logged in, you can get started by creating a new Project in Dataloop.  Think of a Project as a container where you can complete work. This Project will be accessible from both the Python SDK and from the Dataloop online platform, which you can access by going to [dataloop.ai](https://dataloop.ai/) and logging in.

To create a new Project, you can use the line of code below. Note that this line should be executed only once, as you can't create 2 Projects having the same name. So, you can use it once, and then comment it out (place a `#` at the beginning of the line of code assuming you aren't running this on the console).

```python
project = dl.projects.create(project_name='My-First-Project')
```

Now the Project should be created on the platform. To select this new Project (so you can use it in code), you can use the following command:

```python
project = dl.projects.get(project_name='My-First-Project')
```

Or you can select the new Project using the Project ID. However, for this you need to find out your Project ID first. To do this you can get a list of all Projects you have, using the following line of code:

```python
dl.projects.list()
```

After running this command, you should get something like this:

```python
Project(created_at=1674492313392, creator='myfuncont@gmail.com', id='764803e6-af9b-4dde-8141-fea54231fb54', name='My-First-Project', feature_constraints=[{'name': 'downloadJsons', 'quota': 0, 'title': 'Download Annotation as Json'}, {'name': 'createGPUService', 'quota': 0, 'title': 'Create GPU service'}, {'name': 'createIntegration', 'quota': 0, 'title': 'Create Integrations'}, {'name': 'createDriver', 'quota': 0, 'title': 'Create Driver'}])
```

You should see above, that there is a variable called `id`. This is the ID you need to use to `get` the Project in the code below. Just replace the ID you see in the line of code below with your own Project ID, which you should get after executing the code above.

```python
project = dl.projects.get(project_id='764803e6-af9b-4dde-8141-fea54231fb54')
```

As a bonus, you can also open your project in the web UI using the following command:

```python
project.open_in_web()
```

In this case, a new tab will open, and you will be able to see the Project ID in your URL:\


![image](https://user-images.githubusercontent.com/58508793/216595924-89f522b4-6c59-4597-907f-f0c4a220d830.png)

### Creating New Dataset

In Dataloop, a Dataset is a collection of Items (files), their respective metadata, and annotations. Datasets have a file system structure and are organized into folders and subfolders which can have  multiple levels.

There are 3 types of Datasets:

1. Master - The original Dataset which manages the actual binaries.
2. Cloned - Contains pointers to original Dataset files, which enables management of virtual Items that do not replicate the file's binaries on the underlying storage once cloned or copied. When cloning a Dataset, users can decide if the new copy will overwrite the original metadata and annotations.
3. Merged - Several Datasets can be merged into one, allowing multiple annotations to be combined into the same Dataset.

\
You can now create a new Dataset inside this Project. To do this, you can use the following command:

```python
project.datasets.create(dataset_name='My-First-Dataset')
```

If the command was successful, you should get a log confirmation containing the Dataset ID, URL, name, creator and other information.

```python
Dataset(id='632c24ae3444a86f029acb47', url='https://gate.dataloop.ai/api/v1/datasets/632c1194120a7571664d0de3', name='My-First-Dataset', creator='JohnDoe@gmail.com', items_count=0, expiration_options=None, index_driver='v1', created_at='2022-09-22T07:41:08.324Z')
```

To use this Dataset you must select it first using the following code:\


```python
dataset = project.datasets.get(dataset_name='My-First-Dataset')
```

You can also open the Dataset in the web UI using the following line of code:

```python
dataset.open_in_web()
```

It should look something like this:

![image](https://user-images.githubusercontent.com/58508793/216603246-a06de404-5422-42fc-8c91-3cb46fcdc7f6.png)

You can now start to populate that Dataset by adding sample data files and annotating them. That's what we will do in the next chapter!
