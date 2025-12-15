# Extract Analytics

## Total Working Time - User Stats Studio Time and Annotation Classify Bulk Time

Total working time is derived by summing up the measure types `userStatsStudioTime` and `annotationClassifyBulkTime`.

Below is an example of tracking the total working time at the dataset level.

**Note**: Grouping is not supported for this metric in the payload, and dimensions must be passed in the context itself. If multiple dimensions, such as userId or datasetId, are passed in the context, the API will return aggregated data based on the provided dimensions.

**Code Description**

The following code is used to extract the total working time shown in the image above. In the `payload`, `datasetId` and `userId` are optional parameters.

- If neither parameter is provided: The aggregated data will be fetched for all datasets and users available in the `projectId`.

- If both parameters are provided: The aggregated data will be extracted specifically based on the given parameters.

```python
import dtlpy as dl

project = dl.projects.get(project_name='my project')
dataset = project.datasets.get(dataset_name='my dataset')

payload = {
    "startTime": project.created_at,
    "endTime": None,
    "context": {
        "projectId": [project.id],
        "datasetId": [dataset.id]
    },
    "measures": [
        {
            "measureType": "userStatsStudioTime", 
            "pageSize": 0
            },
        {
            "measureType": "annotationClassifyBulkTime",
            "pageSize": 0
            }
    ]
}

success, resp = dl.client_api.gen_request(req_type="post",
                                          path="/analytics/query",
                                          json_req=payload)
samples = resp.json()
total_time = 0
studio_time = samples[0]
bulk_time = samples[1]

if studio_time['response']:
    total_time += studio_time['response'][0]['activityDuration']

if bulk_time['response']:
    total_time += bulk_time['response'][0]['totalTime']

print(f'total_time in minutes: {int(total_time / (1000 * 60))}')

```

## Net Annotation Time | Avg Annotation on Item | Avg Annotation Time | Avg Annotation per Items | Total Annotation Time

The `annotationCounters` measureType is used for tracking the following metrics:

- **Net annotation time**
- **Average item time**
- **Average annotation time**
- **Annotations per item** (available in UI)

The `annotationWholeTime` measureType is used for tracking:

- **Total annotation time** (available in UI)

## Annotation Counter and Annotation Whole Time

**Note**: Grouping is not supported for these metrics in the payload, and dimensions must be passed in the context.

- If multiple dimensions such as `userId`, `datasetId`, etc., are passed in the context, the response will return aggregated data for the provided dimensions.
- If the parameters `datasetId` and `userId` are not passed, the aggregated data will be fetched for all datasets and users available in the `projectId`.

The following code is used to extract the metrics shown in the image above. In the payload, `datasetId` and `userId` are optional parameters.

- **If neither parameter is provided**: The aggregated data will be fetched for all datasets and users available in the `projectId`.

- **If both parameters are provided**: The aggregated data will be extracted specifically based on the given parameters.

```python
import dtlpy as dl
import math

project = dl.projects.get(project_name='my project')
dataset = project.datasets.get(dataset_name='my dataset')

payload = {
    "startTime": project.created_at,
    "endTime": None,
    "context": {
        "projectId": [project.id],
        "datasetId": [dataset.id]
    },
    "measures": [
        {
            "measureType": "annotationCounters",
             "pageSize": 0
             },
        {
            "measureType": "annotationWholeTime", 
            "pageSize": 0}
    ]
}

success, resp = dl.client_api.gen_request(req_type="post",
                                          path="/analytics/query",
                                          json_req=payload)
samples = resp.json()
net_annotation_time = 0
avg_item_time = 0
avg_annotation_time = 0
avg_annotations_per_item = 0
annotation_whole_time = 0

annotation_counters = samples[0]
annotation_wholetime = samples[1]

if annotation_counters['response']:
    net_annotation_time += annotation_counters['response'][0]['totalTime']
    avg_item_time += annotation_counters['response'][0]['avgItemAnnotationTime']
    avg_annotation_time += annotation_counters['response'][0]['avgAnnotationTime']
    avg_annotations_per_item += annotation_counters['response'][0]['avgAnnotationCountPerItem']

if annotation_wholetime['response']:
    annotation_whole_time += annotation_wholetime['response'][0]['totalTime']

print(f'net_annotation_time in minutes: {int(net_annotation_time/(1000*60))} \n'
        f'avg_item_time in minutes: {int(avg_item_time/(1000*60))} \n'
        f'avg_annotation_time in minutes: {int(avg_annotation_time/(1000*60))} \n'
        f'avg_annotations_per_item: {math.ceil(avg_annotations_per_item)} \n'
        f'annotation_whole_time in minutes: {int(annotation_whole_time/(1000*60))}')
```

## Annotations Count Per Task

Use the following code to extract the total annotations for items in a task.

```python
import dtlpy as dl


# Configuration: Set your project name and dataset ID
project_name = 'your_project_name_here'
dataset_id = 'your_dataset_id_here'

# Initialize Project and Dataset
project = dl.projects.get(project_name=project_name)
dataset = project.datasets.get(dataset_id=dataset_id)


# Retrieve all tasks in the dataset
tasks = dataset.tasks.list()
task_ids = [task.id for task in tasks]

# Process each task and count total annotations
for task_id in task_ids:
    print(f"\nProcessing Task ID: {task_id}")

    # Filter items that belong to the current task
    filters = dl.Filters(field='metadata.system.refs.id', values=task_id)
    task_items = dataset.items.list(filters=filters)
    print(f"Items found: {task_items.items_count}")

    # Initialize total annotation counter
    total_annotations = 0

    # Count annotations for each item in the task
    for item in task_items.all():
        item_get = dataset.items.get(item_id=item.id)
        count = getattr(item_get, 'annotations_count', 0)
        print(f"Item {item.id} annotations_count = {count}")
        total_annotations += count

    # Fetch task details and print summary
    task = dataset.tasks.get(task_id=task_id)
    print(f"Task Name: {task.name}, Total Annotations: {total_annotations}")
```

## Average Annotation Time Per Label

`avgAnnotationTimePerLabel` measureType is used for tracking average annotation time per label.

Below code is an example of tracking the average annotation time per label at the dataset level.

**Note:** Grouping is not supported for this metric in the payload, and dimensions must be passed in the context itself.

**Code Description**

The following code is used to extract the metrics shown in the image above. In the payload, `datasetId` and `userId` are optional parameters.

- **If neither parameter is provided**: The data will be fetched for all labels available in the datasets for the `projectId`.

- **If both parameters are provided**: The data will be extracted specifically based on the given parameters.

```python
import dtlpy as dl
import pandas as pd

project = dl.projects.get(project_name='my project')
dataset = project.datasets.get(dataset_name='my dataset')

payload = {
    "startTime": project.created_at,
    "endTime": None,
    "context": {
        "projectId": [project.id],
        "datasetId": [dataset.id],
        "userId": ["e714acd9f43445e73c0a03752454c262e5d43f7a7a97542988b5d874190635af"]
    },
    "measures": [
        {
            "measureType": "avgAnnotationTimePerLabel",
            "sortDirection": "descending"
            }
    ]
}

success, resp = dl.client_api.gen_request(req_type="post",
                                          path="/analytics/query",
                                          json_req=payload)
samples = resp.json()
if samples[0]['response']:
    data = samples[0]['response']
    df = pd.DataFrame.from_dict(data=data)

```

## Item Annotation Duration

Use the following code to extract the item annotation duration at the dataset level.
Here we are using the `itemAnnotationDuration` measureType.

```python
import dtlpy as dl
import pandas as pd

project = dl.projects.get(project_name='my project')
dataset = project.datasets.get(dataset_name='my dataset')

payload = {
            "startTime": project.created_at,
            "endTime": None,
            "context": {
                        "projectId": [project.id],
                        "datasetId": [dataset.id],
                        "userId": ["e714acd9f43445e73c0a03752454c262e5d43f7a7a97542988b5d874190635af"]
            },
            "measures": [
                {
                    "measureType": "itemAnnotationDuration",
                    "sortDirection": "descending"
                    }
                ]
            }

success, resp = dl.client_api.gen_request(req_type="post",
                                          path="/analytics/query",
                                          json_req=payload)
samples = resp.json()
if samples[0]['response']:
    data = samples[0]['response']
    df = pd.DataFrame.from_dict(data=data)
```

## Annotation Timeline

The `annotationTimeline` measureType is used for tracking the annotation timeline.

Below is an example of tracking the annotation timeline at the dataset level.

**Note:** Grouping is not supported for this metric in the payload, and dimensions must be passed in the context itself.

The following code is used to extract the metrics shown in the image above. In the payload, `datasetId` and `userId` are optional parameters.

- **If `timeGranularity` is not provided**:  
  By default, it will pick "hour" as the `timeGranularity`. In the example code below, "hour" and "day" are passed as `timeGranularity`, and the response will include both hour-level and day-level data.

- **If neither `datasetId` nor `userId` is provided**: The data will be fetched for all items available in the datasets for the `projectId`.

- **If both parameters are provided**: The data will be extracted specifically based on the given parameters.

```python
import dtlpy as dl
import pandas as pd

project = dl.projects.get(project_name='my project')
dataset = project.datasets.get(dataset_name='my dataset')

payload = {
    "startTime": project.created_at,
    "endTime": None,
    "context": {
        "projectId": [project.id],
        "datasetId": [dataset.id]
    },
    "measures": [
        {
            "measureType": "annotationTimeline",
            "sortDirection": "descending",
            "timeGranularity": ["hour", "day"]}
    ]
}

success, resp = dl.client_api.gen_request(req_type="post",
                                          path="/analytics/query",
                                          json_req=payload)
samples = resp.json()
if samples[0]['response']:
    hour_data = samples[0]['response']
    hour_df = pd.DataFrame.from_dict(data=hour_data)

if samples[1]['response']:
    day_data = samples[1]['response']
    day_df = pd.DataFrame.from_dict(data=day_data)
```

## Item Status Timeline

The `itemStatusTimeline` measureType is used for tracking the item status timeline.

Below is an example of tracking the Item Status Timeline at the dataset level.

**Note:** Grouping is not supported for this metric in the payload, and dimensions must be passed in the context itself.

The following code is used to extract the metrics shown in the image above. In the payload, `datasetId` and `userId` are optional parameters.

- **If `timeGranularity` is not provided**:  
  By default, it will pick "hour" as the `timeGranularity`. In the example code below, "hour" and "day" are passed as `timeGranularity`, and the response will include both hour-level and day-level data.

- **If neither `datasetId` nor `userId` is provided**:  
  The data will be fetched for all items available in the datasets for the `projectId`.

- **If both parameters are provided**:  
  The data will be extracted specifically based on the given parameters.

```python
import dtlpy as dl
import pandas as pd

project = dl.projects.get(project_name='my project')
dataset = project.datasets.get(dataset_name='my dataset')

payload = {
    "startTime": project.created_at,
    "endTime": None,
    "context": {
        "projectId": [project.id],
        "datasetId": [dataset.id]
    },
    "measures": [
        {
            "measureType": "itemStatusTimeline",
            "sortDirection": "descending",
            "timeGranularity": ["hour", "day"]
            }
    ]
}

success, resp = dl.client_api.gen_request(req_type="post",
                                          path="/analytics/query",
                                          json_req=payload)
samples = resp.json()
if samples[0]['response']:
    hour_data = samples[0]['response']
    hour_df = pd.DataFrame.from_dict(data=hour_data)

if samples[1]['response']:
    day_data = samples[1]['response']
    day_df = pd.DataFrame.from_dict(data=day_data)

```

## Average Annotation Time Per Annotator

The `avgItemAnnotationTimePerAnnotator` measureType is used for tracking the average annotation time per annotator.

Below is an example of tracking the Average Annotation Time Per Annotator at the dataset level.

**Note:** Grouping is not supported for this metric in the payload, and dimensions must be passed in the context itself.

The following code is used to extract the metrics shown in the image above. In the payload, `datasetId` and `userId` are optional parameters.

- **If neither `datasetId` nor `userId` is provided**: The data will be fetched for all items available in the datasets for the `projectId`.

- **If both parameters are provided**: The data will be extracted specifically based on the given parameters.

```python
import dtlpy as dl
import pandas as pd

project = dl.projects.get(project_name='my project')
dataset = project.datasets.get(dataset_name='my dataset')

payload = {
    "startTime": project.created_at,
    "endTime": None,
    "context": {
        "projectId": [project.id],
        "datasetId": [dataset.id]
    },
    "measures": [
        {
            "measureType": "avgItemAnnotationTimePerAnnotator",
            "sortDirection": "descending"
            }
    ]
}

success, resp = dl.client_api.gen_request(req_type="post",
                                          path="/analytics/query",
                                          json_req=payload)
samples = resp.json()
if samples[0]['response']:
    data = samples[0]['response']
    df = pd.DataFrame.from_dict(data=data)
```

## Count Items in Annotation Time Bucket

The `countItemInAnnotationTimeBucket` measureType is used for tracking the count of items in annotation time buckets.

Below is an example of tracking the Count Items in Annotation Time Bucket at the dataset level.

**Note:** Grouping is not supported for this metric in the payload, and dimensions must be passed in the context itself.

The following code is used to extract the metrics shown in the image above. In the payload, `datasetId` and `userId` are optional parameters.

- **If `timeGranularity` is not provided**:  
  By default, it will pick "hour" as the `timeGranularity`. In the example code below, "hour" and "day" are passed as `timeGranularity`, and the response will include both hour-level and day-level data.

- **If neither `datasetId` nor `userId` is provided**: The data will be fetched for all items available in the datasets for the `projectId`.

- **If both parameters are provided**: The data will be extracted specifically based on the given parameters.

```python
import dtlpy as dl
import pandas as pd

project = dl.projects.get(project_name='my project')
dataset = project.datasets.get(dataset_name='my dataset')

payload = {
    "startTime": project.created_at,
    "endTime": None,
    "context": {
        "projectId": [project.id],
        "datasetId": [dataset.id]
    },
    "measures": [
        {
            "measureType": "countItemInAnnotationTimeBucket",
            "sortDirection": "descending",
            "timeGranularity": ["hour", "day"]}
    ]
}

success, resp = dl.client_api.gen_request(req_type="post",
                                          path="/analytics/query",
                                          json_req=payload)
samples = resp.json()
if samples[0]['response']:
    hour_data = samples[0]['response']
    hour_df = pd.DataFrame.from_dict(data=hour_data)

if samples[1]['response']:
    day_data = samples[1]['response']
    day_df = pd.DataFrame.from_dict(data=day_data)

```
