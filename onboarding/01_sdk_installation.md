## SDK overview

Dataloop provides an end-to-end platform that supports the entire AI lifecycle, from development to production. By leveraging both a data management and annotation platform, deep learning data generation is streamlined, resulting in accelerated automated pipeline production and reduced engineering time and costs.

The Dataloop platform is built upon an extensive Python SDK that provides full control over your projects and code. It allows you to automate CRUD (Create, Read, Update, Delete) operations within the platform for:

<ul>
  <li>Projects</li>
  <li>Datasets</li>
  <li>Items</li>
   <li>Annotations</li>
   <li>Metadata</li>
</ul>

## Installation



In order to use our SDK, you must first install it on your machine. To do that you need to follow the steps below.

### 1. Prerequisites

To install a working version of our SDK package, you need to make sure you have the right python version installed.

**Python 3.6 or later** must be installed in order to use our SDK.

To download Python:
<ol>
  <li>Visit https://www.python.org/downloads/</li>
  <li>From the Downloads page, select your desired OS and proceed with the download.</li>
  <li>Once the download is complete, you can proceed to install the software.</li>
</ol>

If you aleady have python installed but you are unsure about which version it is, you can <a href="https://phoenixnap.com/kb/check-python-version">check your python version</a> using the following command:
```python
python --version
```


You can also use <a href="https://www.anaconda.com/">Anaconda</a> to install both python and the dataloop SDK. Anaconda will give you many useful tools that will help you along the way, and a console that works similarly on Windows, Linux and MacOS.

Once you make sure your python version is 3.6 or greater, you can move to the next step.

### 2. Install Dataloop SDK

 The package installer for Python is called pip. To install dataloop's SDK package you need to have pip installed on your system.  If you installed Python correctly, be it from python.org or by using Anaconda, pip should already be installed.

To make sure that pip is installed you can run the following command:
```python
pip --version
```


If pip isn’t already installed, but python is installed, you can install pip from the standard library, by executing the following command in the Command Line:
```python
python3 -m ensurepip --default-pip
```


Now that you made sure both Python and its package installer, pip, are up-to-date, we can proceed to install dataloop's SDK, using the following command:

```python
pip install dtlpy
```
If everything works well, you should have a confirmation, that the dtlpy package was successfully installed.


Congratulations! You finished the installation process! In the next chapter, we will look at how to sign up to dataloop (if you haven't already), and how to sign in to it using python code. Then you will learn how to create a new project and a new dataset where you will be able to import data samples to populate it.














