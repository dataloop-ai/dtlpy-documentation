# 🎨 UI Toolbars - Customize Your Dataloop Experience

Welcome to UI Toolbars! Learn how to add custom buttons and functionality throughout the Dataloop platform. Whether you want to trigger functions or open panels, toolbars make it possible!

## 🎯 When to Use Toolbars

Toolbars are perfect when you need to:

- Execute functions from buttons in the platform
- Open custom panels (UI Applications) from platform locations
- Add context-specific actions to datasets, tasks, or items

## 📍 Available Toolbar Locations

1. **`datasetsDashboard`** 📊

   - Available in Datasets and Project Overview pages
   - Perfect for dataset-wide operations

2. **`datasetBrowser`** 🗂️

   - For operations in the dataset browser interface
   - _Note: Limited availability for regular users_

3. **`datasetMenu`** 📁

   - Located in the dataset menu
   - Available in both Datasets and Project Overview pages

4. **`taskMenu`** ✅

   - Found in the task menu on the Tasks page
   - Ideal for task management operations

5. **`itemMenu`** 📄

   - Available in the right-click item menu
   - Perfect for item-specific operations

6. **`projectActions`** 🏗️
   - Located in the Project Actions menu
   - For project-level operations

## 🛠️ Toolbar Structure

### Basic Components

Every toolbar needs these key components:

```json
{
  "components": {
    "toolbars": [
      {
        "displayName": "My Action", // Button text
        "icon": "icon-dl-add", // Button icon
        "location": "datasetsDashboard", // Where it appears
        "invoke": {
          "type": "function", // or "panel"
          "namespace": "module.function" // What to execute
        }
      }
    ]
  }
}
```

### Complete Structure

Full configuration options:

```json
{
  "components": {
    "toolbars": [
      {
        "displayName": "Process Dataset",
        "icon": "icon-dl-play",
        "location": "datasetMenu",
        "invoke": {
          "type": "function",
          "namespace": "processing.start_process",
          "inputOptions": {
            "mode": "batch",
            "threshold": 0.5
          }
        },
        "conditions": {
          "resources": [
            {
              "entityType": "dataset",
              "filter": {
                "metadata.system.size": { "$gt": 0 }
              }
            }
          ]
        }
      }
    ]
  }
}
```

## 📝 Practical Examples

### 1. Function Button in Dataset Dashboard

Create a button to trigger a processing function:

```json
{
  "components": {
    "toolbars": [
      {
        "displayName": "Convert to Grayscale",
        "icon": "icon-dl-image",
        "location": "datasetsDashboard",
        "invoke": {
          "type": "function",
          "namespace": "image_processing.rgb2gray"
        }
      }
    ]
  }
}
```

### 2. Panel in Project Actions

Open a custom UI panel:

```json
{
  "components": {
    "toolbars": [
      {
        "displayName": "Analytics Dashboard",
        "icon": "icon-dl-dashboard",
        "location": "projectActions",
        "invoke": {
          "type": "panel",
          "namespace": "analyticsPanel"
        }
      }
    ]
  }
}
```

## 💡 Pro Tips & Best Practices

### UI/UX Design

- Use clear, action-oriented button names
- Choose intuitive icons from our [icon library](https://dataloop-ai.github.io/icons/)
- Group related actions in logical locations
- Consider the user's workflow when choosing button placement

### Conditions & Filters

- Use conditions to show/hide buttons based on context
- Filter by entity type and metadata
- Consider user permissions in your filters
- Test filters with various data scenarios

### Performance

- Keep function executions quick and responsive
- Show progress for long-running operations
- Consider caching for frequently used panel data
- Test with various network conditions

### Maintenance

- Document toolbar configurations
- Monitor usage patterns
- Update based on user feedback
- Regular testing across different locations

Need help? Check out our [icon library](https://dataloop-ai.github.io/icons/) for button icons, or reach out to our support team. Happy customizing! ✨
