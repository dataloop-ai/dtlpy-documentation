# Chapter 1 - Python SDK Installation

### SDK Overview

Dataloop provides an end-to-end platform that supports the entire AI lifecycle, from development to production. By leveraging both a data management and annotation platform, training data generation is streamlined, resulting in accelerated automated pipeline production and reduced engineering time and costs.

The Dataloop platform is built upon an extensive Python SDK that provides full control over your projects and code. It allows you to automate CRUD (Create, Read, Update, Delete) operations within the platform for:

* Projects
* Datasets
* Items
* Annotations
* Metadata

Note - In this Onboarding, everything will be formatted in a specific way, as specified below:

* Dataloop, Python, Dataset, Items, etc.
  * Keywords that related to Dataloop entities you'll see and use in the Dataloop UI are always capitalized; same in this onboarding.
* `code`
  * Anything relating to code or a code block will appear as code within grey highlighting.
* **Bold text**
  * Heading and important things to note will be displayed in bold text.
* Words in \<angled brackets>
  * Denote words or phrases you need to replace with values you or someone else created and are relevant to the example and code being used.

### Installation

In order to use our Python SDK, you must first install it on your machine. To do that you need to follow the steps below.

#### 1. Prerequisites

**Python 3.6 or later** must be installed in order to use our Python SDK.

To download Python:

1. Visit https://www.python.org/downloads/
2. From the downloads page, select your desired OS and proceed with the download.
3. Once the download is complete, you can proceed to install the software.

If you already installed Python, but you are unsure about which version you have, you can [check your Python version](https://phoenixnap.com/kb/check-python-version) using the following command:

```shell
python --version
```

Or, if this doesn't work, you can do:

```shell
python3 --version
```

You can also use [Anaconda](https://www.anaconda.com/) to install both Python and the Dataloop SDK. Anaconda will give you many useful tools that will help you along the way, and a console that works similarly on Windows, Linux and MacOS.

Once you make sure your Python version is 3.6 or greater, you can move to the next step.

#### 2. Install Dataloop Python SDK

The package installer for Python is called `pip`. To install Dataloop's Python SDK package you need to have pip installed on your system. If you installed Python correctly, be it from python.org or by using Anaconda, `pip` should already be installed.

To make sure that `pip` is installed you can run the following command:

```shell
pip --version
```

Or, if that doesn't work, try:

```shell
pip3 --version
```

If `pip` isn’t already installed, but Python is installed, you can install `pip` from the standard library, by executing the following command in the Command Line:

```python
python3 -m ensurepip --default-pip
```

Now that you made sure both Python and its package installer, `pip`, are up-to-date, we can proceed to install Dataloop's Python SDK, using the following command:

```python
pip install dtlpy
```

Or, if that doesn't work, try:

```python
pip3 install dtlpy
```

If everything works well, you should see a confirmation, that the `dtlpy` package was successfully installed.

Congratulations! You finished the installation process! In the next chapter, we will look at how to sign up for an account on the Dataloop platform (if you haven't already), and how to sign in to the platform using Python code. Then, you will learn how to create a new project and a new dataset where you will be able to import data samples to populate it.
