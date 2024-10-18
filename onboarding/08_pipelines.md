# Chapter 8 - Pipelines

Dataloop’s Pipeline system integrates human and machine processing in a series of interconnected nodes to streamline data handling. The Pipeline architecture allows for data to flow through labeling tasks, quality assurance tasks, functions within the Dataloop system, code snippets, and machine learning models, allowing for data filtering, splitting, merging, and status changes as needed.

With Dataloop’s Pipeline, organizations can streamline any production pipeline, pre-process and label data, automate operations with applications and models, and post-process data for training machine learning models at optimal performance and availability standards.

As an example, a Pipeline may start with preprocessing data leveraging code snippets that perform a specific action (such as cutting a video into frames), then sending the output to multiple parallel tasks for labeling, quality assurance, or other processing. Completed Tasks can then be directed to a separate Task for review, while discarded Items get stored in a separate Dataset.

### Pipelines in the Python SDK

The Dataloop platform allows for the manipulation and use of Pipelines through both the user interface and the Dataloop Python SDK. In this section, we will focus on working with Pipelines through the Python SDK, but we will also provide additional resources at the end in the form of video tutorials for those who prefer to use the web version of Dataloop for managing Pipelines.

First, let's create a new Pipeline:

```python

pipeline = project.pipelines.create(name='My-First-Pipeline')

```

You have now defined a new Pipeline called "My-First-Pipeline". To see the details of this new Pipeline, you can simply `print` them:

```python
print(pipeline)
```

After doing so, you should see some details similar to this:

```python
Pipeline(id='63d93916845ca8a3f161d5fc', name='My-First-Pipeline', creator='email@gmail.com', org_id='8c8387a3-e771-4d2b-ad77-6a30294dbd01', connections=[], settings=<dtlpy.entities.pipeline.PipelineSettings object at 0x000002BB46FD36D0>, status='Created', created_at='2023-01-31T15:51:50.837Z', start_nodes=[], project_id='764803e6-af9b-4dde-8141-fea54231fb54', composition_id='63d93916845ca883da61d5fd', url='https://gate.dataloop.ai/api/v1/pipelines/63d93916845ca8a3f161d5fc', preview=None, description=None, revisions=None)
```

Now, you can take the Pipeline ID you got by printing the details of your Pipeline, and use it in the following line of code, to `get` your pipeline:

```python
pipeline = project.pipelines.get(pipeline_id='<pipeline_id>')
```

Next, you will use a line of code which will execute the Pipeline and return an object in the `pipeline_execution` variable we create:

```python
pipeline_execution= project.pipelines.execute(pipeline='pipeline_entity', execution_input= {'item': 'item_id'} )
```

To get the ID for an Item, Dataset, or Pipeline you can simply `print` it like this (using Item as an example):

```python
print(item_1)
```

In the example above, you printed the Item details of a Dataset sample file you defined in a previous chapter.  Assuming you followed all chapters and completed coding examples along the way this is how the output should look like (with ID and other details):

```python
Item(dataset_url='https://gate.dataloop.ai/api/v1/datasets/63cebc185bc9dbe3ed851dbe', created_at='2023-01-23T17:04:15.000Z', dataset_id='63cebc185bc9dbe3ed851dbe', filename='/test1.jpg', name='test1.jpg', type='file', id='63cebe0f6f60196b004423d9', spec=None, creator='myfuncont@gmail.com', _description=None, annotations_count=3)
```

Now you should have all the information needed to execute your Pipeline. Here are some other useful lines of code, that will help you when working with Pipelines in the Python SDK.

1. List all pipelines:&#x20;

`project.pipelines.list()`

2. Delete a Pipeline object:

```python
is_deleted = project.pipelines.delete(pipeline_id='<pipeline_id>')
```

2. Open Pipeline in web UI:

```python
project.pipelines.open_in_web(pipeline_id='<pipeline_id>')
```

4. Pause the Pipeline process:

```python
project.pipelines.pause(pipeline='pipeline_entity')
```

5. Reset Pipeline:

```python
project.pipelines.reset(pipeline='pipeline_entity')
```

6. Get a Pipeline's statistics:

```python
project.pipelines.stats(pipeline='pipeline_entity')
```

7. Execute Pipeline and return the execute in a variable:

```python
pipeline_execution = pipeline.pipeline_executions.create(pipeline_id='pipeline_id', execution_input={'item': 'item_id'})
```

8. Get Pipeline execution object:

```python
pipeline_executions = pipeline.pipeline_executions.get(pipeline_id='pipeline_id')
```

9. List project Pipeline executions objects:

```python
pipeline.pipeline_executions.list()
```

If you want to find out more about all of these commands, including descriptions of each parameter they take as input, [read more here](https://dlportal-demo.redoc.ly/resources/dtlpy/dl/).

### Creating Pipelines in the Dataloop Web UI

If you are interested in how you can work with Pipelines in the Dataloop web UI, here are some video tutorials to get you started:

1. [Simple Pipeline](https://app.guidde.co/share/playbooks/p88yeiCCZYPJ5De92KRhNz?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)
2. [Task to Task Pipeline](https://app.guidde.co/share/playbooks/d4VKpz2wXkEfC3b8KtScoj?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)
3. [Task with FaaS and Filter](https://app.guidde.co/share/playbooks/uhQbzYGjMZjQoAWGMzcM3r?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)
4. [Task with Filter](https://app.guidde.co/share/playbooks/f94hGsB1CoURVjVUhD354B?origin=jMK1qNxyBfeCaSgiUvBzFi9AfJb2)

The next chapter of this onboarding will show you what the next steps are in learning more about Dataloop's Python SDK. It will provide additional resources and redirect you to more advanced tutorials and exercises.
