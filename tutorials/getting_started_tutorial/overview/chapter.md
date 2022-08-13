# Overview  
## About Dataloop  
The Dataloop platform allows managing unstructured data (images, video files, audio etc), annotating them with different annotation tools (box, polygon, classification etc) and using them with Dataloop services (compute running your code) and pipelines.  
  
## Data Management  
Data is managed in datasets, and can be arranged in folders. Datasets versioning is facilitated using cloning and merging, for an entire Dataset or partially for selected items. Datasets can use Dataloop storage, and then your binary files are actually uploaded, or you can connect your own cloud storage (GCS, S3, Azure). It requires first to set up an integration (secret) with IAM, and then creating a driver with region, bucket and folder information. As changes occur over time, synchronization can be triggered.  
Another option is using linked-items, where you create an item in a dataset that essentially points at a URL where your file resides. These can be quickly added using SDK or CSV file.  
Dataloop has strong data-management tools for filtering items by nearly any aspect, Filtering uses the Dataloop Query Language (DQL), and DQLs can be created and saved in the platform. You can add your own information into items’ user meta-data, and use it for filtering items.  
  
## Recipe & Ontology  
Labels & attributes are saved in the ontology, which is part of the recipe. In addition to that, the recipe contains labeling instructions, and various work configurations (options).  
  
## Annotation @ QA Workflow  
Annotation work is done in tasks. A task ties together the data (items), the assignees (annotators) and the work instructions (labels and attributes to use). An item is marked as done in a task by assigning it with a status. By default the status that marks an item as done in an annotation task is Completed, and in QA task - Approved. You can add your custom statuses to adjust the workflow for your needs, for example add “Expert review” status.  
A QA task is generated from all items with “Completed” status. You need to either create additional QA tasks as more items are completed, or work with a pipeline that flows these items regularly.  
## Annotations - Upload & Download (Export)  
Annotations created in tasks are saved as a section in the item JSON file, but can be downloaded separately. The Dataloop JSON format supports image annotations, video, LiDAR, audio etc.  
Annotations can be uploaded to items, if for example you need verification of model predictions or use pre-annotations. Items JSON and annotations can be exported from the system.  
The default format is Dataloop JSON format, and using converters you can have them in standard formats such as COCO, YOLO and VOC.  
  
  
## Automation - Services (FaaS)  
The Dataloop Function As A Service (FaaS) enables users to set up a service by deploying a package with one or more modules, and run functions from it. FaaS Services can access compute resources, and through SDK usage - to any data item and dataloop entity in the system.  
Services can be configured with triggers to run automatically on various events such as new items being created (for automatic preprocessing or pre-annotation), modified and more. CRON triggers can be configured for scheduled function executions.  
Services can also be deployed to a “UI slot” to make them available from the platform’s interface. For example allowing annotators to run your model or application on an item or an annotation, or allow custom operation on tasks etc.  
Altogether, it serves as a flexible platform that provides flexibility, increasing the platform’s capabilities, and essentially allows achieving any needs and requirements, and automating many processes.  
Through SDK you can upload and deploy packages, invoke executions or terminate them, assign to UI-slots, and control various aspects of the service.  
  
## Automation - Pipelines  
Pipelines allow you to compose a flow of items through various steps, weaving together services (FaaS), models and people (in annotation/QA tasks). Nearly any desired flow can be achieved with pipelines.  
Dataloop pipelines are designed for scale and production grade, starting from its ‘build’ mode with access to logs, execution history and pipeline cycle runs information, and with its ‘Production’ mode that can process high loads. Through SDK, you can create pipelines and control their various aspects.  
  
