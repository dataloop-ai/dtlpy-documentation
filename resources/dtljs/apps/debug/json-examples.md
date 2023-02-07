# Dataloop JSON Examples

* Examples for a `dataloop.json` file for developing stages ([Debug Applications](./index.md)).

### Floating Window
```json
{
  "components": {
    "panels": [
      {
        "name": "reference-viewer",
        "supportedSlots": [
          {
            "type": "floatingWindow",
            "configuration": {
              "layout": {
                "width": 455,
                "height": 340,
                "resizeable": true,
                "backgroundColor": "dl-color-studio-panel"
              }
            }
          }
        ],
        "conditions": {
          "resources": []
        }
      }
    ]
  }
}
```

### Item Viewer
```json

{
    "components": {
        "panels": [
            {
                "name": "item-viewer",
                "supportedSlots": [
                    {
                        "type": "itemViewer",
                        "configuration": {
                            "layout": {
                                "leftBar": false,
                                "rightBar": false,
                                "bottomBar": false
                            }
                        }
                    }
                ],
                "conditions": {
                    "resources": [
                        {
                            "entityType": "item",
                            "filter": {
                                "metadata.system.mimetype": "image/*"
                            }
                        }
                    ]
                }
            }
        ]
    }
}
```

### Pipeline Node
```json
{
    "components": {
        "panels": [
            {
                "name": "pipelineNodePanel",
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
        "pipelineNodes": [
            {
                "invoke": {
                    "type": "function",
                    "namespace": "custom_nodes.data_split"
                },
                "categories": ["data"]
            }
        ],
        "modules": [
            {
                "name": "custom_nodes",
                "entryPoint": "modules/main.py",
                "className": "Runner",
                "initInputs": [],
                "functions": [
                    {
                        "name": "data_split",
                        "description": "Data splitting custom node",
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
                        "displayIcon": "qa-sampling",
                        "displayName": "Data Split"
                    },
                    {
                        "name": "test",
                        "description": "Testing the waters",
                        "input": [],
                        "output": [],
                        "displayIcon": "node-train",
                        "displayName": "Test"
                    }
                ]
            }
        ]
    }
}
```

### Toolbars
* *Invoke a panel or a function in an application*
```json
{
  "components": {
    "panels": [
      {
        "name": "floatingWindowPanel",
        "supportedSlots": [
          {
            "type": "floatingWindow",
            "configuration": {
              "layout": {
                "width": 455,
                "height": 340,
                "resizeable": true,
                "backgroundColor": "dl-color-studio-panel"
              }
            }
          }
        ],
        "conditions": {
          "resources": []
        }
      }
    ],
    "toolbars": [
      {
        "displayName": "Floating Window",
        "invoke": {
          "type": "panel",
          "namespace": "floatingWindowPanel",
        },
        "icon": "icon-dl-add",
        "location": "datasetsDashboard",
        "conditions": {
          "resources": []
        }
      },
      {
        "displayName": "Run function",
        "invoke": {
          "type": "function",
          "namespace": "my_module.my_function"
        },
        "icon": "icon-dl-edit",
        "location": "itemMenu",
        "conditions": {
          "resources": []
        }
      }
    ],
    "modules": [
      {
        "name": "my_module",
        "entryPoint": "modules/main.py",
        "className": "Runner",
        "initInputs": [],
        "functions": [
          {
            "name": "my_function",
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
            ]
          }
        ]
      }
    ]
  }
}

```
