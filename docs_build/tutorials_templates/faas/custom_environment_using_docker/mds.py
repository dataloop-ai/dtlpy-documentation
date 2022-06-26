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

    You can use any public docker image! On runtime, our agent will install:

    1. Package requirements
    2. dtlpy package (version as defined on the service)
    3. dtlpy-agent (same version as the SDK)

    For example, using `docker.io/python:3.9.13` will run the function with Python 3.9.

    ## Build Your Own Docker Image

    If you want other environment or need to add some apt-get installation, you can create any docker image and use it directly.
    You will to set the HOME directory to `/tmp` and install the python packages with --user (or as user 1000).
    For instance:
    ```
    FROM docker pull dockerhub.io/dataloopai/dtlpy-agent:latest.gpu.cuda11.5.py3.8.opencv

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
    <div style="background-color: lightblue; color: black; width: 50%; padding: 10px; border-radius: 15px 5px 5px 5px;"><b>Note</b><br>
    Using private images is NOT supported yet!</div>

    To connect a private registry, you'll need to add the credentials as Organization Secrets and use the secret in the runtime configuration:

    """
