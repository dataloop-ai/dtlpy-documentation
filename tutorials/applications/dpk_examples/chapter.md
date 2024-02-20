# Dataloop Manifest

Here is an example of a complete DPK manifest

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
        "supportedMethods": {
          "load": true,
          "predict": true,
          "train": true,
          "evaluate": true
        },
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

Here are some real DPKs example from our GitHub space, for more go check all our DPK repositories:
- [Model - YOLOv8](https://github.com/dataloop-ai-apps/yolov8/blob/main/dataloop.json)
- [Panel And Node - DataSplit](https://github.com/dataloop-ai-apps/data-split/blob/main/dataloop.json)
- [Toolbars - Dtlpy-Converters](https://github.com/dataloop-ai-apps/yolov8/blob/main/dataloop.json)

