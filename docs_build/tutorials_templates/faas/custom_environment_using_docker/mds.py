def func1():
    """
    # FaaS Docker Image

    Dataloop enables you to deploy in the FaaS module a custom docker image, to enrich your application with literally
    anything required for your project. Deploying a docker image is as easy as providing the Docker image path when
    deploying the service:
    """


def func2():
    """
    or if you want to update an existing service:
    """


def func3():
    """

    ## Our Docker Image

    We have our list of docker images publicly available in [Dockerhub](https://hub.docker.com/repository/registry-1.docker.io/dataloopai/dtlpy-agent/tags)
    You can see the env of each docker on the dockerfile [here](https://github.com/dataloop-ai/dtlpy-agent/tree/main/dockerfiles)

    ## Public Docker Images

    You can use any public docker image, and on runtime, the Dataloop agent will install:

    1. Package requirements
    2. dtlpy package (version as defined on the service)
    3. dtlpy-agent (same version as the SDK)

    For example, using `docker.io/python:3.9.13` will run the function with Python 3.9.

    ## Build Your Own Docker Image

    If you want other environment or need to add some apt-get installation, you can create any docker image and use it directly.
    You will need to set the HOME directory to `/tmp` and install the python packages with --user (or as USER 1000).
    For instance:
    ```
    FROM dockerhub.io/dataloopai/dtlpy-agent:latest.gpu.cuda11.5.py3.8.opencv

    RUN apt update && apt install -y zip ffmpeg

    USER 1000
    ENV HOME=/tmp
    RUN pip3 install --user \
        dtlpy==1.54.10 \
        dtlpy-agent==1.54.10 \
        torch \
        torchvision \
        imgaug \
        scikit-image==0.17.2
    ```

    ## Using Private Docker Registry

    To connect a private registry, you'll need to add the docker container registry credentials as an Organization Secret and just create use the runner image.

    ### Docker Hub
    You'll need to create the organization secret with the following credentials and encode everything as follows:

    """


def func4():
    """
    Now create the integration secret for the organization
    """


def func5():
    """
    That's it, now you can just add the container url to the dl.Service (`runner_image` in the runtime class) and run the service.

    """
