# 📦 Dataloop Package Kit Examples

## 📜 Complete DPK Manifest Example

Here is an example of a complete DPK manifest. 

NOTE: This is not supposed to be a real app, and publishing or installing it will probably result in some errors.

```json
{
  "name": "dpk-name",
  "displayName": "DPK Display Name",
  "version": "0.0.1",
  "scope": "project",
  "description": "Application description",
  "codebase": {
    "type": "git",
    "gitUrl": "repo-url",
    "gitTag": "0.0.1"
  },
  "components": {
    "panels": [
      {
        "name": "PanelName",
        "icon": "",
        "supportedSlots": [
          {
            "type": "pipelineNodeConfig",
            "configuration": {}
          }
        ],
        "conditions": {
          "resources": []
        }
      }
    ],
    "computeConfigs": [
      {
        "name": "compute-configs1",
        "runtime": {
          "podType": "highmem-xs",
          "concurrency": 1,
          "autoscaler": {
            "type": "rabbitmq",
            "minReplicas": 0,
            "maxReplicas": 2
          }
        }
      }
    ],
    "modules": [
      {
        "name": "my-module",
        "entryPoint": "my_entry_point.py",
        "className": "ClassName",
        "computeConfig": "compute-configs1",
        "description": "Module Desciption",
        "initInputs": [
          {
            "type": "DL Entity",
            "name": "param name"
          }
        ],
        "functions": [
          {
            "name": "func1",
            "input": [
              {
                "type": "DL Entity",
                "name": "param name"
              }
            ],
            "output": [
              {
                "type": "DL Entity",
                "name": "param name"
              }
            ],
            "displayName": "Function Display Name",
            "displayIcon": "",
            "description": "Function Description"
          }
        ]
      }
    ],
    "models": [
      {
        "name": "model-name",
        "moduleName": "my-module",
        "scope": "project",
        "status": "trained",
        "configuration": {},
        "description": "Model Description.",
        "labels": []
      }
    ],
    "pipelineNodes": [
      {
        "panel": "PanelName",
        "name": "Node Name",
        "invoke": {
          "type": "function",
          "namespace": "my-service.my-module.func1"
        },
        "categories": [
          "categoryName"
        ],
        "scope": "node"
      }
    ],
    "services": [
      {
        "name": "my-service",
        "panelNames": [
          "PanelName"
        ],
        "runtime": {
          "podType": "regular-xs",
          "concurrency": 10,
          "autoscaler": {
            "type": "rabbitmq",
            "minReplicas": 0,
            "maxReplicas": 2,
            "queueLength": 10
          }
        }
      }
    ],
    "toolbars": [
      {
        "displayName": "Toolbar Display Name",
        "invoke": {
          "type": "function",
          "namespace": "my-service.func1"
        },
        "location": "datasetBrowserApps",
        "icon": ""
      }
    ]
  }
}
```

## 🎯 Real-World DPK Examples

Let's explore some production-ready examples from our public repository! Here are some magical DPKs you can use as inspiration:

### 🤖 AI Model Adapters

* [Torch Models](https://github.com/dataloop-ai-apps/torch-models) - Collection of PyTorch model adapters for various tasks
* [NVIDIA Models](https://github.com/dataloop-ai-apps/nvidia-models) - Integration with NVIDIA's AI model ecosystem
* [Grounded SAM](https://github.com/dataloop-ai-apps/grounded-sam-adapter) - Adapter for Segment Anything Model with grounding

### 🔄 Pipeline & Data Processing

* [Pipeline Templates](https://github.com/dataloop-ai-apps/pipeline-templates) - Ready-to-use pipeline templates for common workflows
* [Dataset Clustering](https://github.com/dataloop-ai-apps/dataset-clustering) - Automated dataset organization using clustering techniques
* [Data Split](https://github.com/dataloop-ai-apps/data-split) - Smart dataset splitting for training/validation/testing
* [DTLPY Converters](https://github.com/dataloop-ai-apps/dtlpy-converters) - Tools for converting between different annotation formats

### 🔌 Integrations & Utilities

* [Export GCS](https://github.com/dataloop-ai-apps/export-gcs) - Export and import annotations to Google Cloud Storage
* [OpenCV Face Detection](https://github.com/dataloop-ai-apps/opencv-face-detection) - Simple face detection implementation using OpenCV

### 📊 Dataset Management

* [OSDAR23 Datasets](https://github.com/dataloop-ai-apps/osdar23-datasets) - Example datasets and tools for the OSDAR challenge

## 💡 Key Components in Real DPKs

Each of these DPKs demonstrates best practices for:

### 📝 Documentation
* Clear README files
* Installation instructions
* Usage examples
* API documentation

### 🏗️ Structure
* Well-organized code
* Proper manifest setup
* Clear dependency management
* Modular components

### ⚙️ Configuration
* Environment settings
* Runtime configurations
* Service definitions
* Panel layouts

### 🧪 Testing
* Test suites
* Example data
* Validation scripts
* Error handling

## 🎯 Example Use Cases

Here are some specific examples of how these DPKs are used:

### 1. Model Integration
```json
{
  "name": "yolov8-detector",
  "components": {
    "models": [
      {
        "name": "fasterrcnn",
        "moduleName": "model-adapter",
        "scope": "project",
        "status": "trained",
        "configuration": {
          "weights_url": "best.pt"
        }
      }
    ]
  }
}
```

### 2. Pipeline Node
```json
{
  "name": "data-splitter",
  "components": {
    "pipelineNodes": [
      {
        "name": "Split Dataset",
        "invoke": {
          "type": "function",
          "namespace": "data-split.splitter.split_dataset"
        },
        "categories": ["data"]
      }
    ]
  }
}
```

### 3. Custom UI Panel
```json
{
  "name": "annotation-viewer",
  "components": {
    "panels": [
      {
        "name": "AnnotationPanel",
        "supportedSlots": [
          {
            "type": "annotationStudio",
            "configuration": {}
          }
        ]
      }
    ]
  }
}
```

## 🚀 Getting Started with Examples

To use any of these example DPKs:

1. **Clone the Repository**
```bash
git clone https://github.com/dataloop-ai-apps/<dpk-name>
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure the DPK**
```python
import dtlpy as dl
project = dl.projects.get('your-project')
dpk = project.dpks.push(src_path='path/to/dpk')
```

4. **Install the App**
```python
project.apps.install(dpk=dpk)
```

## 💡 Pro Tips

* 📚 Study multiple examples to understand different patterns
* 🔍 Look at the manifest structure of similar apps
* 🧪 Test configurations locally before publishing
* 📝 Document your customizations
* 🔄 Keep your dependencies up to date

Need more inspiration? Visit our [Dataloop Apps Space](https://github.com/dataloop-ai-apps) for the latest examples and updates! ✨

