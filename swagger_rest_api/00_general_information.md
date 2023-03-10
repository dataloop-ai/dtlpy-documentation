# About Dataloop's Rest API
The Dataloop platform offers a RESTful API HTTP interface that allows developers to perform full code language-agnostic automatic flows. In this section you will learn the basic intuition for what an API, REST and RESTful API is, and how Dataloop uses it to bring you quick and easy access to advanced development tools.

## What is an API?
An Application Programming Interface (API) establishes the rules that must be followed while communicating with other software systems. APIs are exposed or created by developers so that other applications can interface with their applications programmatically. For example, you could use the API of Dataloop to execute your Neural Network Model on our server, using an API request; our server would then process the Feedforward pass, and you would get the results back on your computer or website, without using any of your own resources or tools.

A web API can be thought of as a bridge between clients and web resources. In the scope of APIs, clients are people who want to get information from the internet. The client can be either a person or a software system that makes use of an API. Developers, for example, can create programs that automatically access various data from the API system. 

The information that various applications provide to their clients is referred to as *resources*. Images, videos, text, numbers, and other types of data can all be considered resources. The server is the machine that provides the resource to the client. APIs are used by businesses to share resources and deliver web services while maintaining security, control, and authentication. APIs also assist them in determining which clients have access to specific internal resources.

## What is REST?
Representational State Transfer (REST) is a software architecture that defines how an API should function. REST was developed initially as a guideline for managing communication on a complicated network such as the internet. REST-based architecture can be used to offer high-performance and reliable communication at scale. It is simple to implement and adapt, adding visibility and cross-platform portability to any API system.


## What is RESTful API?

API developers can create APIs using a variety of architectures. REST APIs are APIs that adhere to the REST architectural style. RESTful web services are online services that use the REST architecture. RESTful APIs are commonly referred to as RESTful web APIs. Nonetheless, the phrases REST API and RESTful API can be used interchangeably. There are several advantages to RESTful API that makes the process of developing AI solutions with Dataloop quick and easy:
 
- REST APIs enable systems to scale efficiently because they optimize client-server interactions. Statelessness decreases server load because the server does not have to keep past client request information. Certain client-server interactions are reduced or eliminated entirely by well-managed caching. All these features support scalability without causing communication bottlenecks that reduce performance;
- RESTful web services allow for complete client-server separation. They simplify and decouple distinct server components, allowing each component to evolve independently. Platform or technology changes at the server application do not affect the client application. The ability to layer application functions increases flexibility even further. For example, developers can make changes to the database layer without rewriting the application logic;
- REST APIs are unaffected by the technology employed. Client and server applications can be written in a variety of programming languages without compromising the API design. You can also change the underlying technology on either side without affecting the communication.

When the client requires a resource, it uses the API to communicate with the server. In the server application API documentation, API developers explain how their own custom implementation of REST API should be used by the client. Any REST API call generally follows these steps:

- A request is sent to the server by the client. In order to format the request so that the server can comprehend it, the client needs to follow the afferent API documentation.
- The client's authorization to make that request is confirmed by the server, which also authenticates the client.
- The request is processed internally by the server after it is received.
- The client receives a response from the server (in the example with the news website API, the client receives the news articles). The client will find information in the response indicating whether or not the request was granted. Any requested information is also included in the response.

## Key Features of Dataloop's API
Dataloop's platform gives users some very useful tools, because of the REST API it uses, such as:

- Editing Metadata - Add data to describe your Items and Datasets, such as unique or serial IDs for a sequence of frames or images, location of Item creation, sensor position and more.

- Bulk Uploads - Import millions of Items without compressing your data quality or separating Metadata from Items with the bulk upload capabilities.

- Direct M2M Integrations - Perform commands directly through your code, including the automatic creation of Projects, Datasets, Ontologies, and inferencing - all accessible via direct HTTP requests.

Now that you know the basics of the APIs in general and Dataloop's API, you can move on to learning how to [Authenticate on Dataloop's platform](./1.%20Authentication.md).
