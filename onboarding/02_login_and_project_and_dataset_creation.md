## Signing up and logging in to Dataloop

To be able to use our SDK or our other tools, you must first create a free account with dataloop and then log in.

To create an account you can <a href="https://dataloop-production.auth0.com/login?state=hKFo2SBYdnBxZUVLTHRhQlpRTXM5bXdDYWxQdWpOUE9KZFNabqFupWxvZ2luo3RpZNkgNjg3YnRKem5yV2NwSmJVN29UVnBTbGJtYUJFSURRNnCjY2lk2SBGckcwSFpnYTFDSzVVVlVTSkp1RGtTRHFJdFBpZVdHVw&client=FrG0HZga1CK5UVUSJJuDkSDqItPieWGW&protocol=oauth2&response_type=id_token%20code&response_mode=form_post&redirect_uri=https%3A%2F%2Fgate.dataloop.ai%2Fadmit%3Fdefault&scope=openid%20email%20profile%20offline_access&nonce=wy9u651zOeGnuAqKxk~-AfeIKo9hL9AP&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMS4zIn0%3D">click here</a>. You will be redirected to a Login/Signup form, which you can use to create an account using Google or by using your e-mail.

Once you do that, we can go on and try to login to the platform, in Python code. To do that, you need to either open Python in your console or open an IDE where you can run your Python code. Some examples of IDEs are <a href="https://www.spyder-ide.org/">Spyder</a> and <a href="https://visualstudio.microsoft.com/vs/">VisualStudio</a>.

Once you are ready to write Python code, you can use the following lines to log in into the platform:<br>
```python
import dtlpy as dl
dl.login()
```

After executing them, a browser tab will be opened where you can log in. If everything is good, you will see a banner saying that you can return to coding, which means you successfully logged in!

Just keep in mind that the login token lasts for 24 hours. After that, you will need to execute the login code again. Or, you can use the following code, so it will check everytime when your run your code if the login token expired or not, and also will allow you to run all of your code, without having to log in every time:<br>
```python
if dl.token_expired():
   dl.login()
```


### Machine-to-Machine Login
The M2M flow allows machines to obtain valid, signed JWT (authentication token) and automatically refresh it, without the need for a web browser login. M2M Login is recommended when you want to run commands on the platform without an ongoing internet connection or to run API commands directly from an external system to Dataloop.

To do that, you must use the following python code, completed with your login credentials (e-mail and password):<br>
```python
dl.login_m2m(email=email, password=password)
```


## Creating New Project

Now you can start creating a new project in dataloop, where you can work. This project will be accesible from both the SDK and from the dataloop online platform, which you can access by going to [dataloop.ai](https://dataloop.ai/) and logging in.

To create a new project, you can use the following line. Note that this line should be executed only once, as you can't create 2 projects having the same name. So you can use it once, and then comment it out.
```python
project = dl.projects.create(project_name='My-First-Project')
```

 Now the project should be created on the platform. To select this new project (so you can use it in code), you can use the following command:
 ```python
project = dl.projects.get(project_name='My-First-Project')
```

 Or you can select the new project using the project id. However, for this you need to find out your project ID first. To do that you can get a list of all of the projects you have, using the following line of code:
```python
dl.projects.list()
```
After that, you can import the project you want to work on, by using its id:

 ```python
 project = dl.projects.get(project_id='e4a5e5b3-a22a-4b59-9b76-30417a0859d9')
```

## Creating New Dataset

In Dataloop, a dataset is a collection of items (files), their respective metadata, and annotations. Datasets have a file system structure and are organized into folders and subfolders at multiple levels.

There are 3 types of datasets:
<ol>
  <li> Master - The original dataset which manages the actual binaries.</li>
  <li> Clone - Contains pointers to original files, which enables management of virtual items that do not replicate the binaries of the underlying storage once cloned or copied. When cloning a dataset, users can decide if the new copy will overwrite the original metadata and annotations.</li>
  <li> Merge - Several datasets can be merged into one, allowing multiple annotations to be combined into the same dataset.
</li>
</ol>

<br>
You can now create a new dataset inside this project. To do that, you can use the following command:
<br>

```python
project.datasets.create(dataset_name='My-First-Dataset')
```
<br>If the command was successful, you should get a log confirmation containing the dataset id, url, name, creator and other information.
```python
Dataset(id='632c24ae3444a86f029acb47', url='https://gate.dataloop.ai/api/v1/datasets/632c1194120a7571664d0de3', name='My-First-Dataset', creator='JohnDoe@gmail.com', items_count=0, expiration_options=None, index_driver='v1', created_at='2022-09-22T07:41:08.324Z')
```
To use this dataset you must select it first, using the following code: <br>
```python
dataset = project.datasets.get(dataset_name='My-First-Dataset')
```


You can now start to populate that dataset, by adding samples and annotating them. That's what we will do in the next chapter!

