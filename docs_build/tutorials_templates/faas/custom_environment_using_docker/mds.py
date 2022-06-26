def func1():
    """
    # FaaS Docker Image

    On the service entity's runtime, we have a docker image configuration. This will deterime the docker we will

    ## Our default docker image

    We have our prepared docker images link to dockerhub

    the default env is:
    link to dtlpy-agent docker file

    You can use any public docker image you want and the Dataloop will install

    1. Package requirements
    2. dtlpy package (version as defined on the service)
    3. dtlpy-agent (same version as the SDK)

    ## Build you own docker image

    Dataloop enables you to deploy in the FaaS module a custom docker image, to enrich your application with literally
    anything required for your project. Deploying a docket image is as easy as providing the Docker image path when
    deploying the service:

    """


def func2():
    """
    or if you want to update an existing service:
    """


def func3():
    """
    If you want other environment or need to add some apt-get installation, you can create any docker image Dockerfile
    example need to public (for now)
    make sure to install everything with

    RUN pip3 install --user asynctest==0.13.0 boto3==1.21.45 dtlpy \

    1. USER 1000
    2. HOME /tmp

    For instance:
    ```
    FROM gcr.io/viewo-g/piper/agent/runner/gpu/main:latest

    RUN apt update && apt install -y zip ffmpeg

    USER 1000
    ENV HOME=/tmp
    RUN pip3 install --user \
        dtlpy==1.54.10 \
        dtlpy-agent==1.54.10 \
        torch \
        torchvision \
        imgaug \
        'scikit-image==0.17.2'
    ```
    """
