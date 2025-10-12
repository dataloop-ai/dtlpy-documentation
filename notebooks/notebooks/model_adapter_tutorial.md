# Building a Custom Model Adapter Tutorial

This notebook provides a comprehensive guide on how to build, configure, and deploy a custom model adapter on the Dataloop platform. Model adapters are a powerful feature that allows you to integrate any model, including your own locally trained or fine-tuned models, into the Dataloop ecosystem for inference, annotation, and quality assurance.

Model adapters serve as the bridge between your custom models and the Dataloop platform, enabling seamless integration of machine learning workflows with data management and annotation processes.

### Prerequisites:
* **Dataloop Account:** You should have access to a Dataloop platform account.
* **Python Environment:** Ensure you have Python 3.7+ installed with pip.
* **Model Knowledge:** Basic understanding of machine learning models and their inference processes.
* **Docker (Optional):** For custom runtime environments and deployment optimization.

### Navigate through the following sections:
1. [Dependencies & Setup](#dependencies-setup)
2. [Building the Custom Model Adapter](#build-adapter)
3. [Configuring the Dataloop Application (DPK)](#configure-dpk)
4. [Publishing and Deploying the DPK](#publish-deploy)
5. [Conclusion and Next Steps](#conclusion)

## <a id='dependencies-setup'></a>1. Dependencies & Setup

First, let's ensure all required Python packages are installed and establish a connection to the Dataloop platform.


```python
!pip install dtlpy --upgrade --quiet
```

### Environment Setup and Dataloop Connection

With the dependencies installed, we'll import the necessary libraries and establish a connection to the Dataloop platform. If your Dataloop token is expired or not found, you will be prompted to log in.


```python
import dtlpy as dl
import warnings
warnings.filterwarnings('ignore')

if dl.token_expired():
    dl.login()
    
print(f"Successfully connected to Dataloop environment: {dl.client_api.environment}")
```

## <a id='build-adapter'></a>2. Building the Custom Model Adapter

The `dl.BaseModelAdapter` is the bridge between your model's code and the Dataloop platform. It's a Python class where you implement a few key methods to define how your model loads, trains, and predicts.

### Key Methods to Implement:

- **`load(self, local_path, **kwargs)`**: This function is responsible for loading your model's architecture and weights into memory. The `local_path` argument points to a directory where your model's artifacts (like weight files) are downloaded.

- **`predict(self, batch, **kwargs)`**: This is the core inference function. It takes a batch of prepared items (e.g., a list of NumPy arrays for images) and should return a list of `dl.AnnotationCollection` objects, with one collection for each item in the batch.

- **`train(self, data_path, output_path, **kwargs)`**: (Optional) If you want to enable training or fine-tuning from within the Dataloop platform, you'll implement this method to define your training loop.

- **`save(self, local_path, **kwargs)`**: (Optional) After training, this function is called to save the updated model weights and any other necessary artifacts to the specified `local_path`.

### Example: Creating a YOLOv20 Adapter

Let's create a model adapter for a hypothetical `YOLOv20` object detection model. We'll focus on the `load` and `predict` methods for this example. We will write this class to a file named `model_adapter.py`.


```python
%%writefile model_adapter.py
import dtlpy as dl
import torch
from ultralytics import YOLO
from PIL import Image
import os
import logging

logger = logging.getLogger('YOLOv20Adapter')

class Adapter(dl.BaseModelAdapter):

    def load(self, local_path, **kwargs):
        weights_filename = self.configuration.get('weights_filename', 'yolo20n.pt')
        model_filepath = os.path.join(local_path, weights_filename)
        
        # The YOLO class from ultralytics automatically handles downloads if the file doesn't exist
        self.model = YOLO(model_filepath)
        self.logger.info(f"Model loaded from {model_filepath}")
        
    def prepare_item_func(self, item: dl.Item):
        """
        This function is used to prepare an item for prediction.
        For our use case, we will use the item.download function to download the item and return a PIL image.
        """
        buffer = item.download(save_locally=False)
        image = Image.open(buffer).convert('RGB')
        return image
    
    def predict(self, batch, **kwargs):
        """
        Run inference on a batch of items.
        """
        logger.info(f'Predicting batch of size: {len(batch)}')
        batch_annotations = []
        for image in batch: # Batch is a list of PIL images from the prepare_item_func
            # YOLO model can take PIL image directly
            results = self.model(image)
            collection = dl.AnnotationCollection()
            
            # Process results for a single image
            for result in results:
                if result.boxes:
                    for box in result.boxes:
                        # Extract box coordinates, class, and confidence
                        left, top, right, bottom = box.xyxy[0].tolist()
                        confidence = box.conf[0].item()
                        label_id = int(box.cls[0].item())
                        label = self.model.names[label_id]
                        
                        # Add a box annotation to the collection
                        collection.add(
                            annotation_definition=dl.Box(
                                top=top,
                                left=left,
                                bottom=bottom,
                                right=right,
                                label=label
                            ),
                            model_info={
                                'name': self.model_entity.name,
                                'confidence': confidence
                            }
                        )
            
            batch_annotations.append(collection)
            
        return batch_annotations
```

## <a id='configure-dpk'></a>3. Configuring the Dataloop Application (DPK)

Every model and service on Dataloop is packaged as a Dataloop Application (DPK). The configuration for this app is defined in a manifest file called `dataloop.json`. This file contains all the necessary information for the platform to understand, display, and execute your model.

### Key sections in `dataloop.json`:

- **`name`, `displayName`, `version`, `description`**: Basic metadata about your app.
- **`codebase`**: Specifies the source of your code. For this tutorial we use a local codebase, but it can also be a Git repository.
- **`components`**: This is the core section where you define the building blocks of your app.
  - **`modules`**: Defines the code modules in your package. It specifies the entry point (e.g., `model_adapter.py`), the class name (`Adapter`), and the functions that can be executed.
  - **`computeConfigs`**: Defines named configurations for compute resources. This allows you to specify different hardware (like CPU or GPU types) and scaling behaviors for different tasks.
  - **`models`**: Here you define one or more models that your adapter can handle. Each model has its own configuration (`weights_filename`, `labels`, etc.), input/output types, and description.

### 3.1 `dataloop.json` Template

**Action Required:** In the template below, you would replace all placeholders like `<your-app-name>` with your specific details. For this tutorial, we will provide a complete `dataloop.json` in the next step.

```json
{
  "name": "<your-app-name>",
  "displayName": "<Your Model Display Name>",
  "version": "0.0.1",
  "scope": "public",
  "description": "<A brief description of your model>",
  "codebase": {
    "type": "local",
    "filePath": "model_adapter.py"
  },
  "components": {
    "computeConfigs": [
      {
        "name": "<your-deploy-config-name>",
        "runtime": {
          "podType": "regular-m",
          "concurrency": 1,
          "autoscaler": {
            "type": "rabbitmq",
            "minReplicas": 0,
            "maxReplicas": 1,
            "queueLength": 10
          }
        }
      }
    ],
    "modules": [
      {
        "name": "<your-module-name>",
        "entryPoint": "model_adapter.py",
        "className": "Adapter",
        "computeConfig": "<your-deploy-config-name>",
        "description": "<Module Description>",
        "initInputs": [
          {
            "type": "Model",
            "name": "model_entity"
          }
        ],
        "functions": [
          {
            "name": "predict_items",
            "input": [
              {
                "type": "Item[]",
                "name": "items"
              }
            ],
            "output": [
              {
                "type": "Annotation[]",
                "name": "annotations"
              }
            ],
            "displayName": "Predict Items"
          }
        ]
      }
    ],
    "models": [
      {
        "name": "<your-model-name>",
        "moduleName": "<your-module-name>",
        "scope": "project",
        "status": "pre-trained",
        "configuration": {
          "weights_filename": "<your_weights_file.pt>",
          "labels": [
             "label1", "label2", "..."
           ]
        },
        "inputType": "image",
        "outputType": "box",
        "description": "<Detailed description of the model variant>"
      }
    ]
  }
}
```

### 3.2 In-Depth Look at `computeConfigs`

The `computeConfigs` section in your `dataloop.json` is critical for defining the computational resources your service will use. It allows you to create named configurations that can be referenced by your modules, giving you fine-grained control over performance and cost.

#### Key Components:

-   **`name`**: A unique identifier for your compute configuration. You'll use this name to assign a specific configuration to a module (e.g., `"computeConfig": "your-deploy-config-name"`).

-   **`runtime`**: This object specifies the execution environment for your service.
    -   **`podType`**: This determines the size of the machine (pod) your service will run on. Dataloop offers a range of pod types with varying CPU, GPU, and memory resources.

| Pod Type | vCPU | Memory (GiB) | GPU | Description |
|---|---|---|---|---|
| `regular-xs` | 0.5 | 1.7 | - | Extra Small CPU instance |
| `regular-s` | 1 | 3.5 | - | Small CPU instance |
| `regular-m` | 2 | 7 | - | Medium CPU instance |
| `regular-l` | 4 | 14 | - | Large CPU instance |
| `gpu-k80` | 4 | 26 | 1x NVIDIA K80 | GPU instance for general purpose tasks |
| `gpu-t4` | 4 | 14 | 1x NVIDIA T4 | GPU instance with Turing architecture, good for inference |
| `gpu-v100` | 6 | 26 | 1x NVIDIA V100 | High-performance GPU for demanding training tasks |
| `gpu-a100` | 12 | 85 | 1x NVIDIA A100 | Top-tier GPU for large-scale training and inference |

-   **`concurrency`**: This sets the number of concurrent processes your service's replica can handle. For models that are not thread-safe or are resource-intensive per-task, this is typically set to `1`.

-   **`autoscaler`**: This object controls how your service scales in response to demand.
    -   `type`: The autoscaling trigger. `"rabbitmq"` is used for services that process jobs from a queue.
    -   `minReplicas`: The minimum number of service replicas to keep running, even with no load.
    -   `maxReplicas`: The maximum number of replicas that can be created to handle a surge in demand.
    -   `queueLength`: The number of messages in the RabbitMQ queue that will trigger the creation of a new replica.

### 3.3 Runner Image and Custom Environments

The optional `runnerImage` parameter allows you to specify a custom Docker image for your service's execution environment. This is extremely useful when your model requires specific system libraries, dependencies, or a particular version of Python that isn't available in the default Dataloop environment.

If you don't provide a `runnerImage`, Dataloop uses a default image. However, for production and reproducibility, it's highly recommended to build and use your own.

Here is a sample `Dockerfile` that you could use as a starting point:

#### Dockerfile:

```dockerfile
FROM dataloopai/dtlpy-agent:gpu.cuda.11.8.py3.8.pytorch2

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```

#### requirements.txt:

```txt
torch
ultralytics
dtlpy
```

For this tutorial, we are using a pre-built image specified in the final `dataloop.json`, but for your own projects, you would build this Docker image and push it to a container registry (like GCR, ECR, or Docker Hub) that your Dataloop organization is connected to.

### 3.4 Complete `dataloop.json` for YOLOv20

Below is the complete manifest for our YOLOv20 adapter. We'll write this to a `dataloop.json` file in our working directory.


```python
%%writefile dataloop.json
{
  "name": "yolo20",
  "displayName": "YOLOv20",
  "version": "0.0.1",
  "scope": "project",
  "description": "YOLOv20: Attention-Centric Object Detection",
  "codebase": {
    "type": "local",
    "localPath": "model_adapter.py"
  },
  "attributes": {
    "Provider": "Ultralytics",
    "License": "AGPL-3.0",
    "Category": "Model",
    "Computer Vision": "Object Detection",
    "Media Type": ["Image"],
    "Deployed By": "Dataloop"
  },
  "components": {
    "computeConfigs": [
      {
        "name": "yolov20-deploy",
        "runtime": {
          "podType": "regular-m",
          "concurrency": 1,
          "runnerImage": "gcr.io/viewo-g/piper/agent/runner/apps/yolo-world:0.0.1-dev",
          "autoscaler": {
            "type": "rabbitmq",
            "minReplicas": 1,
            "maxReplicas": 2,
            "queueLength": 100
          }
        }
      }
    ],
    "modules": [
      {
        "name": "yolov20-module",
        "entryPoint": "model_adapter.py",
        "className": "Adapter",
        "computeConfig": "yolov20-deploy",
        "description": "YoloV20 Module",
        "initInputs": [
          {
            "type": "Model",
            "name": "model_entity"
          }
        ],
        "functions": [
          {
            "name": "predict_items",
            "input": [
              {
                "type": "Item[]",
                "name": "items",
                "description": "List of items to run inference on"
              }
            ],
            "output": [
              {
                "type": "Annotation[]",
                "name": "annotations",
                "description": "The predicted annotations."
              }
            ],
            "displayName": "Predict Items",
            "displayIcon": "",
            "description": "Function to run YOLOv20 inference on items"
          }
        ]
      }
    ],
    "models": [
      {
        "name": "yolo20n",
        "moduleName": "yolov20-module",
        "scope": "project",
        "status": "pre-trained",
        "configuration": {
          "weights_filename": "yolo20n.pt",
          "labels": [
             "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", 
             "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", 
             "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", 
             "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", 
             "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", 
             "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", 
             "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", 
             "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", 
             "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", 
             "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
           ]
        },
        "inputType": "image",
        "outputType": "box",
        "description": "YOLO20 Nano model"
      }
    ]
  }
}
```

## <a id='publish-deploy'></a>4. Publishing and Deploying the DPK

Once you have your `model_adapter.py` and `dataloop.json` files ready, the final step is to publish your DPK to the Dataloop platform. This makes your model available as an app that can be installed in any project.

The following script automates this process:

1. **`project.dpks.publish()`**: This command reads your `dataloop.json`, finds your local codebase, and publishes it as a new DPK version in the app store.
2. **`project.apps.install()` or `app.update()`**: After publishing, this script checks if the app is already installed in your target project. If it is, it updates the app to the new version. If not, it installs it for the first time.

### 4.1 Define Project and Publish

**Action Required:** In the code cell below, replace `'{user_prefix}-model-adapter-tutorial'` with the name of the Dataloop project where you want to publish and install your model app.


```python
# Define a unique name for your project or change it to your own project name
user_email = dl.info()['user_email']
user_prefix = user_email.split('@')[0].replace('.', '').replace('-', '') # Simple prefix from email
project_name = f'{user_prefix}-model-adapter-tutorial'

# Check if the project exists, if not, create it
try:
    project = dl.projects.get(project_name=project_name)
    print(f"Successfully retrieved project: '{project.name}' (ID: {project.id})")
except dl.exceptions.NotFound:
    project = dl.projects.create(project_name=project_name)
    print(f"Successfully created project: '{project.name}' (ID: {project.id})")
```

### 4.2 Publish and Install the DPK

This cell will publish your DPK to the Dataloop platform and install it in your project.


```python
import os

# Publish the DPK to the Dataloop platform
dpk = project.dpks.publish(manifest_filepath='dataloop.json', 
                           local_path=os.getcwd())

print(f"DPK '{dpk.display_name}' published successfully. Version: {dpk.version}")

try:
    # If the app is already installed, update it to the new version
    app = project.apps.get(app_name=dpk.display_name)
    app.dpk_version = dpk.version
    app.update()
    print(f"App '{app.name}' updated successfully to version {dpk.version}.")
except dl.exceptions.NotFound:
    # If the app is not installed, install it
    app = project.apps.install(dpk=dpk, app_name=dpk.display_name)
    print(f"App '{app.name}' installed successfully.")
```

## <a id='conclusion'></a>5. Conclusion and Next Steps

Congratulations! You've now walked through the entire process of integrating a custom object detection model into the Dataloop platform.

### Summary of What You've Accomplished:
- **Brought Your Own Model**: Used the `BaseModelAdapter` to wrap any model for use on Dataloop
- **Handled Data**: Implemented the `predict` function to process items and generate Dataloop-standard annotations
- **Packaged Your App**: Defined your model, its functions, and configurations in the `dataloop.json` manifest
- **Deployed and Managed**: Published your DPK and installed it as a usable app within your Dataloop projects

### Next Steps:
- **Implement Training**: Add the `train` method to fine-tune your models directly on the platform
- **Create Complex Pipelines**: Build automated workflows that incorporate your custom models
- **Build Interactive UI**: Create custom panels and interfaces for your applications
- **Explore Advanced Features**: Investigate model versioning, A/B testing, and performance monitoring

For more examples and advanced model adapter patterns, you can explore the [Dataloop AI Apps GitHub repository](https://github.com/dataloop-ai-apps).
