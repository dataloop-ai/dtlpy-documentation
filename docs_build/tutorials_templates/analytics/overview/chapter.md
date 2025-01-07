# Analytics Overview

In the Dataloop platform, we have an analytics screen where different metrics like Active users, Annotator's performance, Total working time, Item annotation time, etc. can be tracked at a project, dataset, or task level which would help the business.

## Analytics API Overview

The Analytics API has 3 parameters to be passed to it, and it’s a POST request type.

- **endpoint**: API endpoint that needs to be called.
- **headers**: Authentication to the API endpoint. This would remain the same.
- **json**: JSON payload needs to be passed, which would contain the list of metrics that the user wants to extract within a specific period. JSON payload is the key parameter for tracking the metrics.

### Example of Fetching Active Users in a Project

```python
import dtlpy as dl

project = dl.projects.get(project_name='my project')
payload = {
    "startTime": project.created_at,
    "endTime": None,
    "context": {"projectId": [project.id]},
    "measures": [{"measureType": "activeUsers"}]
}

success, resp = dl.client_api.gen_request(req_type="post", 
                                          path="/analytics/query", 
                                          json=payload)
samples = resp.json()
```

### Understanding the Payload

The JSON payload mainly has 4 keys:

- **startTime**: A mandatory key representing the time from which the metrics need to be fetched. The API throws an error if this key is missing.
- **endTime**: An optional key. If not provided, the API uses the `current_timestamp` by default.
- **context**: The context refers to the dimensions for which the metrics need to be fetched. Below is the list of dimensions that can be passed to the API for fetching the metrics. These dimensions are optional and may vary from query to query depending on the use case. The dimensions must be passed as a list of strings; otherwise, the API will throw an ERROR..

    **Dimensions for Context**

    - `userId`: string[]
    - `orgId`: string[]
    - `projectId`: string[]
    - `accountId`: string[]
    - `datasetId`: string[]
    - `taskId`: string[]
    - `assignmentId`: string[]
    - `itemId`: string[]
    - `serviceId`: string[]
    - `podId`: string[]
    - `modelId`: string[]
    - `snapshotId`: string[]
    - `pipelineId`: string[]
    - `triggerId`: string[]
    - `pipelineExecutionId`: string[]
    - `nodeId`: string[]
    - `ontologyId`: string[]

- **measures**: Specifies the metrics the users wish to fetch. It includes keys like `measureType`, `params`, `page`, `pageSize`, `sortDirection`, and `timeGranularity`.

    **TimeGranularity Type**

    - SECOND = 'second'
    - MINUTE = 'minute'
    - HOUR = 'hour'
    - DAY = 'day'
    - WEEK = 'week'
    - MONTH = 'month'

    **List of Measure Types**

    - ANNOTATION_TIMELINE = 'annotationTimeline'
    - ITEM_STATUS_TIMELINE = 'itemStatusTimeline'
    - AVG_ANNOTATION_TIME_PER_LABEL = 'avgAnnotationTimePerLabel'
    - ITEM_ANNOTATION_DURATION = 'itemAnnotationDuration'
    - COUNT_ITEM_IN_ANNOTATION_TIME_BUCKET = 'countItemInAnnotationTimeBucket'
    - AVG_ITEM_ANNOTATION_TIME_PER_ANNOTATOR = 'avgItemAnnotationTimePerAnnotator'
    - ASSIGNMENT_STATS_COMPLETED_STATUS = 'assignmentStatsCompletedStatus'
    - ASSIGNMENT_STATS_ITEM_ACTIVE_TIME_STATS = 'assignmentStatsItemActiveTimeStats'
    - ASSIGNMENT_STATS_ITEM_TOTAL_TIME = 'assignmentStatsItemTotalTime'
    - ASSIGNMENT_STATS_ANNOTATION_ACTION_TIME_STATS = 'assignmentStatsAnnotationActionTimeStats'
    - ASSIGNMENT_STATS_ANNOTATION_CLASSIFY_BULK_STATS = 'assignmentStatsAnnotationClassifyBulkStats'
    - ASSIGNMENT_STATS_ACTIVE_TIME = 'assignmentStatsActiveTime'
    - ASSIGNMENT_STATS_STUDIO_ACTIVE_TIME = 'assignmentStatsStudioActiveTime'
    - ASSIGNMENT_START_TIME = 'assignmentStartTime'
    - ACTIVE_USERS = 'activeUsers'
    - LABELING_COUNTERS = 'labelingCounters'
    - LABELING_ACTION_PER_LABEL = 'labelingActionsPerLabel'
    - LABELING_TIME_PER_LABEL = 'labelingTimePerLabel'
    - LABELING_AVG_TIME_PER_LABEL = 'labelingAvgTimePerLabel'
    - USER_STATS_TASK_ACTIVITY_TIME = 'userStatsTaskActivityTime'
    - USER_STATS_ACTIVITY_TIME = 'userStatsActivityTime'
    - USER_STATS_ACTIVITY_TIME_BY_ROLE = 'userStatsActivityTimeByRole'
    - USER_STATS_ACTIVITY_TIME_BY_FIELD = 'userStatsActivityTimeByField'
    - USER_STATS_TOTAL_ACTIVITY_TIME = 'userStatsTotalActivityTime'
    - USER_STATS_STUDIO_TIME = 'userStatsStudioTime'
    - ISSUE_COUNTERS = 'issueCounters'
    - ISSUE_CORRECTION_TIME = 'issueCorrectionTime'
    - ISSUE_RAISE_TIME = 'issueRaiseTime'
    - ISSUE_RESOLVE_TIME = 'issueResolveTime'
    - ISSUE_APPROVAL_TIME = 'issueApprovalTime'
    - ISSUE_TIMELINE = 'issueTimeline'
    - ISSUE_PER_LABEL = 'issuePerLabel'
    - ISSUE_PER_ANNOTATOR = 'issuePerAnnotator'
    - SERVICE_REPLICA_STATUS = 'serviceReplicaStatus'
    - SERVICE_QUEUE_SIZE = 'serviceQueueSize'
    - SERVICE_NUMBER_OF_REPLICAS = 'serviceNumberOfReplicas'
    - SERVICE_USAGE = 'serviceUsage'
    - SERVICE_USAGE_PROJECTS = 'serviceUsageProjects'
    - SNAPSHOT_DATA = 'snapshotData'
    - EXECUTION_OVER_TIME = 'executionOverTime'
    - EXECUTION_DURATION = 'executionDuration'
    - EXECUTION_COUNT_BY_FUNCTIONS = 'executionCountByFunction'
    - EXECUTION_AVG_DURATION_BY_NODE = 'executionAvgDurationByNode'
    - PIPELINE_EXECUTION_AVG_DURATION = 'pipelineExecutionAvgDuration'


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
        {"measureType": "countItemInAnnotationTimeBucket", 
            "sortDirection": "descending", 
            "timeGranularity": ["hour", "day"]}
    ]
}

success, resp = dl.client_api.gen_request(req_type="post", 
                                          path="/analytics/query", 
                                          json=payload)
samples = resp.json()
if samples[0]['response']:
    hour_data = samples[0]['response']
    hour_df = pd.DataFrame.from_dict(data=hour_data)

if samples[1]['response']:
    day_data = samples[1]['response']
    day_df = pd.DataFrame.from_dict(data=day_data)

```