## FAAS
The Dataloop Function-as-a-Service ([FAAS](https://dataloop.ai/docs/faas)) allows users to deploy packages and run services from them, with access to the Dataloop system's computing resources and data. Overall, it serves as an incredibly powerful tool that provides exceptional flexibility, expands the platform's capabilities, and essentially allows meeting any needs and requirements while automating  processes.

You can use this tool for pre-annotation processing (resize, video assembler/dissembler), post-annotation processing (auto-parenting, augmentation), ML models (auto-detection), QA models (auto QA, consensus model, majority vote model), etc.

Our FaaS uses the [Kubernetes cluster](https://kubernetes.io/docs/concepts/overview/), to provide very low latency requests with minor operational costs.

## FAAS Concenpts
To work with FAAS, you first need to understand a few important concepts that will help you along the way.

### Services
Services are set up with a runtime driver and configuration that determines how to deploy the Service. The only supported driver is Kubernetes, which creates a Kubernetes deployment to control the number of replicas and resource allocation for the Service. The amount of resources and GPU type each replica has is determined by the instance type of the Service. The Agent, a pod running Dataloop code, manages the execution of the Service by loading the Module, listening to a Rabbitmq queue, processing messages, updating metrics and statuses, and monitoring the service overview. The Agent terminates when the Service goes down. When a manual execution or trigger occurs, a message is sent to Rabbitmq which invokes the function through one of the Agents.

To ensure zero downtime during Service updates, we use a rolling update approach. When a Service update is initiated, the backend selects a few Agents and instructs them to stop receiving new messages from RabbitMQ, wait for ongoing executions to finish, and then shut down. A new Agent with updated parameters is then created in place of the exiting one. If an Agent fails to shut down after being ordered, it will be forcibly terminated, even if it hasn't finished processing all its assigned executions.

If you want to find out more about Services in the SDK, you can look at our [documentation about Services](https://dataloop.ai/docs/service-runtime).

### Docker Images

A [Docker](https://docs.docker.com/get-started/) image is a file that acts as a blueprint for creating Docker containers. It functions as a set of instructions that tell Docker how to build and set up the container environment. Essentially, the Docker image is the foundation for creating containers, much like a snapshot in virtual machine environments. In fact, an image can be thought of as a sort of template, providing the starting point for creating containers that can run code and perform specific tasks. The use of Docker images makes it easier to manage, version, and distribute applications, providing consistency and reliability when deploying across various environments.

Dataloop enables you to deploy in the FaaS module a custom docker image, to enrich your application with literally anything required for your project. You can read more about [Dataloop's Docker here](https://dataloop.ai/docs/faas-docker-images).

## Working with FAAS
**Important!** To work with our FAAS function, you need to have a Premium Account. In case you don't know how get one, take a look at our [Pricing Plans](https://console.dataloop.ai/iam/8c8387a3-e771-4d2b-ad77-6a30294dbd01/account?tab=info).
If you don't have a premium account, you will get a 409 error, saying the FaaS function is for Premium accounts only!

If you have premium, we can proceed to create a simple function, that we can run on Dataloop's FaaS service.

Just copy paste the function below, which will convert RGB pictures to Greyscale:

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
You can now deploy the FaaS using Dataloop SDK. Once the service variable is defined and the service is deployed, you may execute the available function on any input you wish. In this case we ran the function on the "My-First-Project" dataset:
```python
project = dl.projects.get(project_name='My-First-Project')
service = project.services.deploy(func=rgb2gray,
                                  service_name='grayscale-item-service')
```

Execution refers to running a function on a service using specific inputs, known as arguments, which are provided to the function. The service can be executed either manually (on demand) or automatically based on a trigger, such as time or an event. In this tutorial, we will show you how to manually execute the "RGB to Gray" function.

To create a trigger, you can use the following code:
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

That's it for the FaaS Onboarding. If you want to find out more about FaaS functions and how to use it in more advanced ways, here are some useful links:
1. [Dataloop's FaaS documentation](https://dataloop.ai/docs/faas);
2. [Faas SDK Cheat-Sheet Section](https://dataloop.ai/docs/sdk-cheatsheet#:~:text=Copy-,FaaS,-To%20learn%20more)
3. [Advanced Auto-annotation Service](https://dataloop.ai/docs/auto-annotation-service)
4. [Pre-annotation service tutorial](https://dlportal-demo.redoc.ly/tutorials/faas/auto_annotate/chapter/#model-and-weights-files);
5. Tutorial and code for [extracting Exif (Exchangeable Image File Format) information](https://github.com/dataloop-ai/image-exif) from images and uploads it.

Now that you have learned how to work with the FaaS provided by Dataloop, let's move on and talk about pipelines - in the next chapter.

