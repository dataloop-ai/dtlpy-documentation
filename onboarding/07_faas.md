# Chapter 7 - Function as a Service (FaaS)

The Dataloop Function-as-a-Service ([FAAS](07\_faas.md#faas)) allows users to deploy packages and run services from them leveraging the Dataloop platform's computing resources and data. Overall, it serves as an incredibly powerful tool that provides exceptional flexibility, expands the platform's capabilities, and essentially enables the technical users of the platform to meet a variety of backend automation needs and requirements.

You can use this tool for Dataset pre-annotation processing (Ex. resize, video assembler/dissembler, pre-labeling), post-annotation processing (Ex. auto-parenting, augmentation, reformatting output), ML model management and execution (Ex. auto-detection), QA model definition and execution (Ex. auto QA, consensus model, majority vote model), etc.

Dataloop FaaS uses [Kubernetes cluster](https://kubernetes.io/docs/concepts/overview/) technology to provide very low latency request fulfillment with minimal operational costs.

**Important!**  Currently FaaS is reserved for Dataloop customers subscribed at the Pro level or higher.  If you'd like to try FaaS before committing to a Pro level or higher subscription, email the [Dataloop Developer Community moderators](mailto:dataloop-devs@dataloop.ai?subject=\[Github]%20FaaS%20Access%20Request) from your company email address and one of the community moderators will connect with you to arrange a trial.

### FAAS Concepts

To start working with Dataloop's FaaS, you first need to understand a few important concepts that will help you along the way.

#### Services

Services are set up with a runtime driver and configuration that determines how to deploy the Service. The only supported driver is Kubernetes, which creates a Kubernetes deployment to control the number of replicas and resource allocation for the Service. The amount of resources and the GPU type each replica has is determined by the instance type of the Service. The Agent, a pod running Dataloop code, manages the execution of the Service by loading the Module, listening to a Rabbitmq queue, processing messages, updating metrics and statuses, and monitoring the Service overview. The Agent terminates when the Service goes down. When a manual execution or trigger occurs, a message is sent to Rabbitmq which invokes the function through one of the Agents.

To ensure zero downtime during Service updates, we use a rolling update approach. When a Service update is initiated, the backend selects a few Agents and instructs them to stop receiving new messages from RabbitMQ, wait for ongoing executions to finish, and then shut down. A new Agent with updated parameters is then created in place of the exiting one. If an Agent fails to shut down after being ordered to do so, it will be forcibly terminated even if it hasn't finished processing all its assigned executions.

If you want to find out more about Services in the Python SDK, you can look at our [FaaS Service documentation](https://dataloop.ai/docs/service-runtime).

#### Docker Images

A [Docker](https://docs.docker.com/get-started/) image is a file that acts as a blueprint for creating Docker containers. It functions as a set of instructions that tell Docker how to build and set up the container environment. Essentially, the Docker image is the foundation for creating containers, much like a snapshot in virtual machine environments. In fact, a Docker image can be thought of as a template that provides the starting point for creating containers that can run code and perform specific tasks. The use of Docker images makes it easier to manage, version, and distribute applications, providing consistency and reliability when deploying across various environments.

Dataloop enables you to deploy in the FaaS module a custom Docker image to enrich your Dataloop environment with literally anything required for your project. You can read more about [Dataloop's Docker image here](https://dataloop.ai/docs/faas-docker-images).

### Working with FaaS

**Reminder:** To work with FAAS you need to have a Pro level account or higher.  If you'd like to try FaaS before committing to a Pro level or higher subscription, email the [Dataloop Developer Community moderators](mailto:dataloop-devs@dataloop.ai?subject=\[Github]%20FaaS%20Access%20Request) from your company email address and one of the community moderators will connect with you to arrange a trial.

If you don't have a premium account, you will get the following error:

`dtlpy.exceptions.Conflict: ('409', 'Failed creating Trial users do not have permission to create services – premium account required. Please contact` [`info@dataloop.ai`](mailto:info@dataloop.ai) `for more information.')`

If you have your subscription or a trial sorted, we can proceed to create a simple function that we can run as a Dataloop FaaS service.

Just copy and paste the below function into your Python IDE.  This function converts RGB pictures to Greyscale:

```python
def rgb2gray(item: dl.Item):
    """
    Function to convert RGB image to GRAY
    Will also add a modality to the original item
    :param item: dl.Item to convert
    :return: None
    """
    import numpy as np
    import cv2
    buffer = item.download(save_locally=False)
    bgr = cv2.imdecode(np.frombuffer(buffer.read(), np.uint8), -1)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    bgr_equalized_item = item.dataset.items.upload(local_path=gray,
                                                   remote_path='/gray' + item.dir,
                                                   remote_name=item.name)
    # add modality
    item.modalities.create(name='gray',
                           ref=bgr_equalized_item.id)
    item.update(system_metadata=True)
```

You can now deploy the FaaS using Dataloop's Python SDK. Once the service variable is defined and the service is deployed, you may execute the available function on any input you wish. In this case we ran the function on the "My-First-Project" dataset:

```python
project = dl.projects.get(project_name='My-First-Project')
service = project.services.deploy(func=rgb2gray,
                                  service_name='grayscale-item-service')
```

Execution refers to running a function on a Service using specific inputs, known as arguments, which are provided to the function. The Service can be executed either manually (on demand) or automatically based on a trigger, such as time or an event. In this tutorial, we will show you how to manually execute the `rgb2gray` function.

To create a Trigger that runs the `rbg2gray` function, you can use the following code:

```python
trigger = service.triggers.create(name=package_name,
                                  filters=filters,
                                  actions=['Created'],
                                  execution_mode='Once',
                                  resource='Item')
```

To see the item we uploaded in web-view, run the following code:

```python
item.open_in_web()
```

That's it for the FaaS Onboarding. If you want to find out more about FaaS and how to use it in more advanced ways, here are some useful links:

1. [Dataloop's FaaS documentation](https://dataloop.ai/docs/faas);
2. [Faas SDK Cheat-Sheet Section](https://dataloop.ai/docs/sdk-cheatsheet)
3. [Advanced Auto-annotation Service](https://dataloop.ai/docs/auto-annotation-service)
4. [Pre-annotation service tutorial](https://dlportal-demo.redoc.ly/tutorials/faas/auto\_annotate/chapter/#model-and-weights-files);
5. Tutorial and code for [extracting Exif (Exchangeable Image File Format) information](https://github.com/dataloop-ai/image-exif) from images and uploading it.

Now that you have learned how to work with FaaS provided by Dataloop, let's move on and talk about Pipelines in the next chapter.
