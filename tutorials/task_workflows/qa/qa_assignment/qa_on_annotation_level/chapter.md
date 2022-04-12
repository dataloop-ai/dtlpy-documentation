## QA on Annotation Level  
To reach the tasks and assignments repositories go to <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.tasks" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.assignments" target="_blank">assignments</a>.  
  
  
To reach the tasks and assignments entities go to <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.task" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.assignment" target="_blank">assignments</a>.  
### ItemAnnotations Review  
The Annotation Studio also enables direct feedback for specific annotations. To enable a realtime review, a Reviewer can open an issue on an Annotation.  
The Annotator (person who annotated the issued Annotation) then receives the issue, fixes it and sends it back for a second review.  
The Reviewer may approve the fix or return it as an issue.  
  
We also support a real-time dialog on items as an annotation, go to <a href="https://dataloop.ai/docs/note-annotation" target="_blank">Note Annotation</a> to learn more.  
#### Prep  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
```
### Single status update  

```python
# Mark a single annotation with an open issue
item = dataset.items.get(item_id='my-item-id')
annotation = item.annotations.get(annotation_id='your-annotation-id-number')
annotation.update_status(dl.AnnotationStatus.ISSUE)
# In the same way you can update to another status
annotation.update_status(dl.AnnotationStatus.APPROVED)
annotation.update_status(dl.AnnotationStatus.REVIEW)
annotation.update_status(dl.AnnotationStatus.CLEAR)  # Have the annotation without status
```
### Bulk status update  

```python
# Get Task
task = project.tasks.get(task_id='my_task_id')
# Add filters for items in the task who have annotations with issues
filters = dl.Filters()
filters.add_join(field='metadata.system.status', values='issue')
items = task.get_items(filters=filters)
# Go over all of the items
for page in items:
    for item in page:
        # Add filter for annotations with issues
        filters = dl.Filters()
        filters.resource = dl.FiltersResource.ANNOTATION
        filters.add(field='metadata.system.status', values='issue')
        annotations = item.annotations.list(filters=filters)
        # For every annotation that has issue in the item update the status to "for review"
        for annotation in annotations:           annotation.update_status(dl.AnnotationStatus.REVIEW)
```
