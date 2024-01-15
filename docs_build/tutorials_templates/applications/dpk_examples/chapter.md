# Dataloop JSON Examples

For end to end examples of Dataloop JSON files, Refer to
the [Table of Contents](https://github.com/dataloop-ai-apps/table-of-contents).

### Pipeline Node

```json
{
  "components": {
    "my-pipeline-node": {
      "type": "pipelineNode",
      "spec": {
        "name": "vision-face-detection-pipeline-node",
        "invoke": {
          "type": "function",
          "namespace": "service-name.module-name.function_name"
        },
        "categories": [
          "Node Category"
        ],
        "displayName": "Node Display Name",
        "description": "Node Description",
        "scope": "node",
        "configuration": {
          "fields": [
            {
              "name": "name",
              "title": "Node Name",
              "props": {
                "title": true,
                "type": "string",
                "default": "Default Node Name",
                "required": true,
                "placeholder": "Insert node name"
              },
              "rules": [
                {
                  "type": "required",
                  "effect": "error"
                }
              ],
              "widget": "dl-input"
            }
          ]
        }
      }
    }
  }
}
```

### Module

```json

{
  "my-module": {
    "type": "module",
    "spec": {
      "name": "module-name",
      "entryPoint": "path/to/main.py",
      "className": "ClassName",
      "computeConfig": "service-name",
      "initInputs": [
        {
          "type": "String",
          "name": "init_input_name"
        }
      ],
      "functions": [
        {
          "name": "function_name",
          "input": [
            {
              "type": "Item",
              "name": "item"
            }
          ],
          "output": [
            {
              "type": "Item",
              "name": "item"
            }
          ],
          "displayIcon": "display-icon"
        }
      ]
    }
  }
}
```

### Compute Config / Service

```json
{
  "gv-face-detection": {
    "type": "computeConfig",
    "spec": {
      "name": "service-name",
      "initParams": {
        "init_input_name": ""
      },
      "runtime": {
        "podType": "regular-xs",
        "runnerImage": "dataloopai/dtlpy-agent:cpu.py3.8.opencv4.7",
        "concurrency": 10,
        "autoscaler": {
          "type": "rabbitmq",
          "minReplicas": 0,
          "maxReplicas": 2,
          "queueLength": 100
        }
      },
      "executionTimeout": 600,
      "onReset": "failed",
      "maxAttempts": 3
    }
  }
}
```

### Toolbars

* *Invoke a panel or a function in an application*
* Supported Location:
    * `datasetsDashboard`
    * `datasetBrowserApps`
    * `datasetBrowserViewStyle`
    * `datasetBrowserSearchOption`
    * `datasetMenu`
    * `taskMenu`
    * `itemMenu`
    * `toolPlugin`

```json
{
  "components": {
    "my-toolbar-panel": {
      "displayName": "Run Dialog",
      "invoke": {
        "type": "panel",
        "namespace": "dialogPanel"
      },
      "icon": "icon-dl-add",
      "location": "datasetsDashboard",
      "conditions": {
        "resources": []
      }
    },
    "my-toolbar-function": {
      "displayName": "Run function",
      "invoke": {
        "type": "function",
        "namespace": "module-name.function_name"
      },
      "icon": "icon-dl-edit",
      "location": "itemMenu",
      "conditions": {
        "resources": []
      }
    }
  }
}
```

### Model

```json
{
  "components": {
    "models": {
      "type": "model",
      "spec": {
        "name": "model-name",
        "moduleName": "module-name",
        "scope": "project",
        "status": "",
        "configuration": {},
        "inputType": "",
        "outputType": "",
        "description": "Model Description"
      }
    }
  }
}
```

### Panel

```json
{
  "components": {
    "my-panel": {
      "type": "panel",
      "spec": {
        "name": "pipelineNodePanel",
        "icon": "dataloop-icon",
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
    }
  }
}
```

