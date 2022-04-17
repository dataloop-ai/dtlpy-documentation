## Note Annotation  
To reach the tasks and assignments repositories go to <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.tasks" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/repositories.html#module-dtlpy.repositories.assignments" target="_blank">assignments</a>.  
  
  
To reach the tasks and assignments entities go to <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.task" target="_blank">tasks</a> and <a href="https://sdk-docs.dataloop.ai/en/latest/entities.html#module-dtlpy.entities.assignment" target="_blank">assignments</a>.  
  
The Annotation Studio also enables real time dialog in the studio. The note annotation allows annotators and reviewers the option to add an issue directly to the item as an annotation.  
#### Prep  

```python
import dtlpy as dl
if dl.token_expired():
    dl.login()
```
### Init Note  
With message inside and top, bottom, left, right positioning  
Using the annotations definitions classes you can create, edit, view and  
upload platform annotations.  

```python
annotation_definition=dl.Note(top=10,left=10, bottom=100, right=100,label='my-label')
annotation_definition.assignee = "user@dataloop.ai"
annotation_definition.add_message("this is a message 1")
annotation_definition.add_message("this is a message 2")
```
### Create Note Annotation  
#### 1. Get project and dataset  

```python
project = dl.projects.get(project_name='project_name')
dataset = project.datasets.get(dataset_name='dataset_name')
```
#### 2. Get item from the platform  

```python
item = dataset.items.get(filepath='/your-image-file-path.jpg')
```
#### 3. Create a builder instance  

```python
builder = item.annotations.builder()
```
#### 4. Add a note  

```python
annotation_definition=dl.Note(top=10,left=10, bottom=100, right=100,label='my-label')
annotation_definition.assignee = "user@dataloop.ai" 
annotation_definition.add_message("this is a message 1")
annotation_definition.add_message("this is a message 2")
builder.add(annotation_definition=annotation_definition)
```
#### 5. Upload annotations to the item  

```python
item.annotations.upload(builder)
```
