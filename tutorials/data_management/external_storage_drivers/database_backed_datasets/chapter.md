# Database-Backed Datasets

A database-backed dataset exposes the rows of an external database (Elasticsearch) as Dataloop items. Instead of uploading files, you upload structured rows with the SDK and query them with Dataloop filters.

## Which Dataset Type Do I Need?

| You have | Use | Where to read |
|---|---|---|
| Files in Dataloop storage | A regular dataset | [Datasets and Versioning](/tutorials/data_management/datasets_and_versioning/chapter.md) |
| Files in NFS, PowerScale or S3, and you want their metadata indexed in Elasticsearch | A storage-analytics dataset (`metadata_driver_id`) | [Datasets and Versioning](/tutorials/data_management/datasets_and_versioning/chapter.md) |
| Rows that live in an Elasticsearch index | A database-backed dataset | This chapter |

## Step 1: Create the Elasticsearch Integration

The database driver reads its database access details from a Dataloop integration of type `dl.IntegrationType.ELASTICSEARCH`. Create it in the platform, or with the generic integrations API:

```python
import dtlpy as dl

project = dl.projects.get(project_name='project_name')

integration = project.integrations.create(
    integrations_type=dl.IntegrationType.ELASTICSEARCH,
    name='my-elasticsearch',
    options=elasticsearch_options,  # connection settings, loaded from a secret store - never hard-code them
)
```

There is no Elasticsearch-specific helper in the SDK. The keys expected in `options` are defined by the platform, not by the SDK. Keep credentials out of source code and out of notebooks.

## Step 2: Create a Database Driver

`project.drivers.create_database_driver()` creates a driver of type `database`. The database engine is taken from `integration_type`.

```python
driver = project.drivers.create_database_driver(
    name='events-driver',
    integration_id=integration.id,
    integration_type=dl.IntegrationType.ELASTICSEARCH,
    database_table={
        'collection': 'events',
        'schemaMapping': {
            'primaryKey': {'fields': ['_id'], 'composite': False, 'type': 'string'},
            'fieldMappings': [
                {'sourceField': 'event_type', 'targetPath': 'metadata.user.eventType', 'type': 'string'},
                {'sourceField': 'score', 'targetPath': 'metadata.user.score', 'type': 'number'},
            ],
        },
        'itemType': 'db_row',
    },
)
```

### `create_database_driver()` Inputs

| Input | Type | Required | Explanation |
|---|---|---|---|
| `name` | `str` | Yes | Driver name. |
| `integration_id` | `str` | Yes | ID of the integration that holds the database access details. |
| `integration_type` | `dl.IntegrationType` | Yes | The database engine, for example `dl.IntegrationType.ELASTICSEARCH`. |
| `database_table` | `dict` | Yes | The collection and how its fields map to Dataloop items. See the next table. |
| `project_id` | `str` | No | Defaults to the project you called the method from. |
| `dynamic_partitions` | `dict` | No | Dynamic partitions configuration. |
| `is_use_default_s2_schema` | `bool` | No | `True` replaces `schemaMapping` with the platform default unstructured S2 schema. Default `False`. |
| `disable_manual_sync` | `bool` | No | `True` hides the sync buttons in the UI, so the dataset can only be synced from the SDK or a direct API call. Default `False`. |

### `database_table` Keys

| Key | Explanation |
|---|---|
| `collection` | The Elasticsearch index to expose. |
| `schemaMapping.primaryKey` | `fields` (list of source fields), `composite` (bool) and `type`. For Elasticsearch, `composite` must be `False`. |
| `schemaMapping.fieldMappings` | List of `sourceField` (name in the database), `targetPath` (where it appears on the item) and `type`. |
| `itemType` | The item type for the rows, for example `db_row`. |

Platform rules for `schemaMapping`:

- Every `targetPath` must start with `metadata.user.`.
- Fields mapped with `type` `array` or `object` are skipped when the Elasticsearch index is built.

`create_database_driver()` returns a `dl.DatabaseDriver`. In addition to the common driver fields it has `database_table`, `dynamic_partitions`, `read_only` and `is_use_default_s2_schema`.

## Step 3: Create the Dataset

```python
dataset = project.datasets.create(dataset_name='events', driver_id=driver.id)
print(dataset.is_database_backed)  # True
```

`dataset.is_database_backed` is set by the platform from the dataset's driver. It is a read-only field.

## Step 4: Upload Rows

On a database-backed dataset, `dataset.items.upload()` accepts structured rows instead of file paths: a `dict`, a list of `dict`, or a `pandas.DataFrame`.

```python
# One row
dataset.items.upload({'_id': 'e1', 'event_type': 'click', 'score': 0.91})

# Many rows
items = dataset.items.upload(
    [
        {'_id': 'e2', 'event_type': 'view', 'score': 0.43},
        {'_id': 'e3', 'event_type': 'buy', 'score': 0.77},
    ],
    return_as_list=True,
)

# A DataFrame - columns are field names
import pandas as pd

dataset.items.upload(pd.DataFrame([
    {'_id': 'e4', 'event_type': 'click', 'score': 0.12},
    {'_id': 'e5', 'event_type': 'view', 'score': 0.55},
]))
```

How row upload behaves:

- **Row identity**: each row needs an `_id` (or the driver's primary key field), or a `filename` to derive an id from. Rows with the same id overwrite each other.
- **Stored as-is**: the driver's `fieldMappings` are not applied on upload.
- **Chunking**: rows are sent in chunks of up to 1000 rows.
- **Return value**: the created items, not fetched from the platform. A single row returns one item, several rows return a generator, and `return_as_list=True` returns a list.
- **Ignored options**: `local_annotations_path`, `remote_name`, `file_types`, `overwrite`, `item_metadata` and `item_description` are ignored for rows. The SDK logs a warning that lists the ignored options.
- **Visibility**: uploaded rows may take a moment to appear in queries.

## Step 5: Query Rows

Query a database-backed dataset with regular filters, using the mapped `metadata.user.*` paths:

```python
filters = dl.Filters(field='metadata.user.eventType', values='click')
pages = dataset.items.list(filters=filters)
for item in pages.all():
    print(item.id)
```

For a database-backed dataset the platform decides whether the default item filters (type and hidden) apply, and leaves them out. Filters you create with `use_defaults=True` always send them.

### Get the Raw Rows

To read the rows exactly as stored in the database, set `database_driver_raw_data_only`:

```python
filters = dl.Filters()
filters.database_driver_raw_data_only = True

df = dataset.items.list(filters=filters, page_size=100)  # a pandas.DataFrame
print(df.columns)
```

In raw mode:

- `items.list()` returns a `pandas.DataFrame`, one row per database row, not a `PagedEntities`.
- The driver's field mappings are skipped, so the columns use the raw database names (for example `event_type`) rather than the mapped paths (`metadata.user.eventType`).

## Troubleshooting

| Symptom | Explanation |
|---|---|
| Warning: "Rows of a database-backed dataset are uploaded as-is, ignoring: ..." | File upload options were passed with row input. They have no effect on rows. |
| Error: "N of M rows were not uploaded by the platform" | The platform rejected some rows, for example a row whose primary key does not match the schema mapping. |
| Rows are missing right after upload | Uploaded rows may take a moment to appear in queries. |
| Columns differ between `items.list()` results | Raw mode (`database_driver_raw_data_only=True`) uses raw database column names, not the mapped `metadata.user.*` paths. |
| `create_database_driver()` fails for Elasticsearch | Check that `composite` is `False` and that every `targetPath` starts with `metadata.user.`. |

## Need More Help?

- [Dataloop Query Language: Introduction](/tutorials/data_management/dataloop_query_language/introduction/chapter.md)
- [Feature Vectors](/tutorials/data_management/feature_vectors/chapter.md) - to keep embeddings for this dataset in an external vector store
- [Python SDK reference: Drivers](https://sdk-docs.dataloop.ai/en/latest/repositories.html)
