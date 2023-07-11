# Creating a Python App

Python Applications use the same elements in the Dataloop FaaS Management.

You can look at [this simple app](https://github.com/dataloop-ai-apps/opencv-face-detection) for face detection.

Read more about modules, services and everything related to FaaS [here](https://developers.dataloop.ai/tutorials/faas/)

## Pre-launch Script

A pre-launch script is a customizable script that is executed before starting the application.
It serves as a preparatory step to ensure that the environment is properly set up and any required configurations are
performed prior to launching the application.
By adding a `build.sh` file to the root of the app, you can execute any command as part of the application's
initialization process.
For example, if you need to install some python packages, you can use something like this:

<h5 a><strong><code>build.sh</code></strong></h5>

``` shell
pip3 install my-package==1.0.0
```

You can also set a pre-launch script for a specific service by changing the name of the script
to `{service.name}-build.sh`.
