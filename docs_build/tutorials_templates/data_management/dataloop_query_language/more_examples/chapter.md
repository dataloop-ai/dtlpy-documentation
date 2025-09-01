# DQL Cookbook: Practical Examples 🍳

Welcome to our DQL cookbook! Here you'll find tasty recipes for common filtering scenarios. Each example is ready to use - just copy, paste, and adjust to your needs!

## Filter Operators Toolbox 🧰

Let's start with the essential operators you'll need:

### Equal (eq) 🎯

Returns items where a field’s value is exactly equal to the specified value.

```python
# Example: Find items in a specific folder
filters = dl.Filters()
filters.add(field='dir', values='/DatasetFolderName', operator=dl.FILTERS_OPERATIONS_EQUAL)
filters.sort_by(field='filename')  # Optional: sort by name
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items in folder')
```

### Not Equal (ne) ❌

Returns items where a field’s value is different from the specified value.

```python
# Example: Find items without a specific label
filters = dl.Filters()
filters.add_join(field='label', values='cat', operator=dl.FILTERS_OPERATIONS_NOT_EQUAL)
filters.sort_by(field='filename')
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items without cat label')
```

### Greater Than (gt) and Less Than (lt) ⚖️

Return items where a field’s value is greater than or less than the specified value.

```python
# Example 1: Items with height > X pixels
filters = dl.Filters()
filters.add(field='metadata.system.height', values=height_number_in_pixels,
           operator=dl.FILTERS_OPERATIONS_GREATER_THAN)
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items taller than {height_number_in_pixels}px')

# Example 2: Items with width < X pixels
filters = dl.Filters()
filters.add(field='metadata.system.width', values=width_number_in_pixels, 
           operator=dl.FILTERS_OPERATIONS_LESS_THAN)
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items narrower than {width_number_in_pixels}px')
```

### In List (in) 📝

Returns items where a field’s value matches any value in a given list.

```python
# Example: Find items with multiple labels
filters = dl.Filters()
filters.add_join(field='label', values=['dog', 'cat'], operator=dl.FILTERS_OPERATIONS_IN)
filters.sort_by(field='filename')
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items with dog or cat labels')
```

### Exists ✨

Returns items where the specified field exists in the item’s metadata.

```python
# Example: Find items with user metadata
filters = dl.Filters()
filters.add(field='metadata.user', values=True, operator=dl.FILTERS_OPERATIONS_EXISTS)
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items with user metadata')
```

### Intersect

In Dataloop, the INTERSECT operator in DQL lets you create advanced queries by finding items that meet multiple conditions. It returns only the items that appear in all queries, making it useful for identifying data that satisfies several criteria across subsets.

```python
import dtlpy as dl

# Connect to the project and dataset
project = dl.projects.get(project_name="Vitalii Project")
dataset = project.datasets.get(dataset_name="cptn-intersect-operator-support")

# Build a custom filter:
#  - First filter: only visible items (hidden=False) and of type "file"
#  - Then apply the "intersect" operator to REQUIRE items to have BOTH "car" and "person" annotations
custom_filter = {
    "filter": {
        "$and": [
            {"hidden": False},     # Exclude hidden items
            {"type": "file"}       # Only include file-type items
        ]
    },
    "intersect": [
        {
            "query": {
                "join": {
                    "filter": {
                        "label": "car"    # Must include a "car" annotation
                    },
                    "on": {
                        "resource": "annotations",  # Join annotations
                        "local": "itemId",          # Match by itemId
                        "forigen": "id"             # Annotation linked to item
                    }
                }
            }
        },
        {
            "query": {
                "join": {
                    "filter": {
                        "label": "person" # Must ALSO include a "person" annotation
                    },
                    "on": {
                        "resource": "annotations",
                        "local": "itemId",
                        "forigen": "id"
                    }
                }
            }
        }
    ]
}

# Apply the filter
filters = dl.Filters(custom_filter=custom_filter)
pages = dataset.items.list(filters=filters)

print(f'Found {pages.items_count} items containing BOTH ' 
      f'"car" and "person" annotations')
```


### Except

In Dataloop, the EXCEPT operator in DQL lets you create advanced queries by excluding data from one set that also appears in another. It returns only the items unique to the first query, making it useful for filtering out specific results.



```python
import dtlpy as dl

# Connect to the project and dataset
project = dl.projects.get(project_name="Vitalii Project")
dataset = project.datasets.get(dataset_name="cptn-except-operator-support")

# Build a custom filter:
#  - First filter: only visible items (hidden=False) and of type "file"
#  - Then apply the "except" operator to EXCLUDE items with annotations labeled "person"
custom_filter = {
    "filter": {
        "$and": [
            {"hidden": False},     # Exclude hidden items
            {"type": "file"}       # Only include file-type items
        ]
    },
    "except": {
        "query": {
            "join": {
                "filter": {
                    "label": "person"   # Look for "person" annotations
                },
                "on": {
                    "resource": "annotations",  # Join annotations
                    "local": "itemId",          # Match by itemId
                    "forigen": "id"             # Annotation linked to item
                }
            }
        }
    }
}

# Apply the filter
filters = dl.Filters(custom_filter=custom_filter)
pages = dataset.items.list(filters=filters)

print(f'Found {pages.items_count} items (excluding items with "person" annotations)')
```





## Filtering by Annotations 🏷️

### Finding Items by Label

Need items with a specific label? Here's your go-to recipe:

```python
filters = dl.Filters()
filters.add_join(field='label', values='your_label_value')
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items with your label')
```

### Items Without a Specific Label

Want to find items that DON'T have a certain label? Here's a clever approach:

```python
# Get all items
all_items = set([item.id for item in dataset.items.list().all()])

# Get items WITH the label 'cat'
filters = dl.Filters()
filters.add_join(field='label', values='cat')
cat_items = set([item.id for item in dataset.items.list(filters=filters).all()])

# Find the difference - items without 'cat' label
no_cat_items = all_items.difference(cat_items)
print(f'Found {len(no_cat_items)} items without cat label')

# Process the results
for item_id in no_cat_items:
    item = dataset.items.get(item_id=item_id)
    print(f'Processing: {item.name}')
```

### OR Filtering of Annotations

Want items with either type of annotation? Here's how:

```python
filters = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
# Find box OR point annotations
filters.add(field='type', values='/box', method=dl.FiltersMethod.OR)
filters.add(field='type', values='/point', method=dl.FiltersMethod.OR)
filters.sort_by(field='createdAt', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
pages = dataset.annotations.list(filters=filters)
print(f'Found {pages.items_count} box or point annotations')
```

## Filtering by Status 📊

### Finding Items by Annotation Status

Want items that are completed or approved? Take your pick:

```python
# Both completed AND approved
filters = dl.Filters()
filters.add(field='metadata.system.annotationStatus', values=["completed", "approved"])
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} completed and approved items')

# Just completed (including approved)
filters = dl.Filters()
filters.add(field='metadata.system.annotationStatus', values="completed")
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} completed items')

# Only completed (excluding approved)
filters = dl.Filters()
filters.add(field='metadata.system.annotationStatus', values=["completed"])
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items with completed status only')
```

### Find Items With Status by Task

Need to find items assigned to a specific task with a specific status? Here's how:

```python
task_id = "my-task-id"
status_list = ['completed']

filters = dl.Filters()  # `resource` defaults to items
filters.add(
    field='metadata.system.refs',
    values={
        'id': {'$in': [task_id]},          # keep refs whose id == TASK_ID
        'metadata': {
            'status': {'$in': status_list}  # AND whose status == completed
        }
    },
)

pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items with completed status for task {task_id}')
```

### Check Remaining Items in Task

This will get all the items from a specific task that DOES NOT have any status set
```python
filetrs = dl.Filters()  # `resource` defaults to items
filetrs.add(
    field='metadata.system.refs',
    values={'id': {'$in': [task.id]}, 
            'metadata': {'status': {'$exists': False}}}, 
    operator=dl.FiltersOperations.MATCH
)
pages = item.dataset.items.list(filters=filetrs)
print(pages.items_count)
```

And the other way around, to get all the items WITH a status:

```python
filetrs = dl.Filters()  # `resource` defaults to items
filetrs.add(
    field='metadata.system.refs',
    values={'id': {'$in': [task.id]}, 
            'metadata': {'status': {'$exists': True}}}, 
    operator=dl.FiltersOperations.MATCH
)
pages = item.dataset.items.list(filters=filetrs)
print(pages.items_count)
```

### Finding Unassigned Items

Looking for items nobody's working on?

```python
filters = dl.Filters()
filters.add(field='metadata.system.refs', values=[])
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} unassigned items')
```

## File and Folder Operations 📁

### Filtering by Folder

Want items from a specific folder?

```python
filters = dl.Filters()
filters.add(field='dir', values="/folderName")
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items in folder')
```

### Finding Specific Files

Looking for files with a particular name pattern?

```python
filters = dl.Filters()
filters.add(field='name', values='foo.bar.*')
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} matching files')
```

### Working with Hidden Items

Need to see hidden items and directories?

```python
# Method 1: Show directories
filters = dl.Filters()
filters.add(field='type', values='dir')

# Method 2: Remove type filter
filters = dl.Filters()
filters.pop(field='type')

# Method 3: Disable defaults
filters = dl.Filters(use_defaults=False)
```

## Advanced Sorting and Filtering 🎯

### Size-Based Sorting

Want to find and sort files within a specific size range?

```python
filters = dl.Filters()
# Between 0 and 5 MB
filters.add(field='metadata.system.size', values='0', operator='gt')
filters.add(field='metadata.system.size', values='5242880', operator='lt')
filters.sort_by(field='filename', value=dl.FILTERS_ORDERBY_DIRECTION_ASCENDING)
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} files between 0-5MB')
```

### Multi-Field Sorting

Need to sort by multiple criteria? We've got you covered:

```python
filters = dl.Filters()
filters.resource = dl.FiltersResource.ANNOTATION
# Sort by label (A-Z) then creation date (newest first)
filters.sort_by(field='label', value=dl.FILTERS_ORDERBY_DIRECTION_ASCENDING)
filters.sort_by(field='createdAt', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} sorted items')
```

## Time-Based Filtering ⏰

### Finding Items by Date Range

Need items from a specific time period? Here's how to handle UTC time properly:

```python
import datetime

# Option 1: Absolute dates (e.g., May 2-3, 2024)
earlier = datetime.datetime(year=2024, month=5, day=2, hour=0, minute=0, second=0).isoformat()
later = datetime.datetime(year=2024, month=5, day=3, hour=0, minute=0, second=0).isoformat()

# Option 2: Relative time (e.g., last hour)
earlier = (datetime.datetime.utcnow() - datetime.timedelta(hours=1)).isoformat()
later = datetime.datetime.utcnow().isoformat()

# Apply the filter
filters = dl.Filters()
filters.add(field='createdAt', values=earlier, operator=dl.FiltersOperations.GREATER_THAN)
filters.add(field='createdAt', values=later, operator=dl.FiltersOperations.LESS_THAN)
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items in time range')
```

## Working with Custom Filters 🛠️

### Using Platform-Generated DQL

Have a DQL JSON from the platform? Use it directly:

```python
filters = dl.Filters(
    custom_filter={
        "$and": [
            {"hidden": False},
            {"type": "file"},
            {"annotated": True}
        ]
    }
)
pages = dataset.items.list(filters=filters)
print(f'Found {pages.items_count} items matching custom filter')
```

### Opening Filters in the UI

Want to see your filter in action in the platform?

```python
filters = dl.Filters()
filters.add(field='annotated', values=True)
filters.open_in_web(dataset)
```

### Managing Filters

Need to remove a filter? Here's how:

```python
filters = dl.Filters()
# Add a filter
filters.add(field='to-delete-field', values='value')

# Remove it
filters.pop(field='to-delete-field')
# Or for annotation filters
filters.pop_join(field='to-delete-annotation-field')
```

## Need More Advanced Options? 🚀

For even more filtering power, check out our [Advanced SDK Filters](https://docs.dataloop.ai/docs/dql-operators) guide.

Happy filtering! 🎉
