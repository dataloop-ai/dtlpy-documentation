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
  

```python
service = package.deploy(service_name='my-service',
                         runtime=dl.KubernetesRuntime(
                             runner_image='python:3.8'
                         ))
```
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
  

```python
service = package.deploy(service_name='my-service',
                         runtime=dl.KubernetesRuntime(
                             runner_image='python:3.8'
                         ))
```
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
  

```python
service = package.deploy(service_name='my-service',
                         runtime=dl.KubernetesRuntime(
                             runner_image='python:3.8'
                         ))
```
