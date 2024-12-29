# Creating Consensus, Honeypot, and Qualification Tasks

Consensus tasks in Dataloop are a critical feature for ensuring annotation quality.
They enable validation, skill assessment, and collaborative annotations by involving multiple annotators in various task types: **Honeypot**,
**Qualification**, and **Consensus**. Each type serves distinct purposes and methodologies, as outlined below.

## Comparison of Consensus Task Types

| Task Type         | Purpose                               | Data Inclusion             | Evaluation Method        |
|-------------------|---------------------------------------|----------------------------|--------------------------|
| **Honeypot**      | Continuous quality monitoring         | Mixed raw and ground truth | Score on honeypot items  |
| **Qualification** | Pre-task skill assessment             | Ground truth only          | Compare with known truth |
| **Consensus**     | High-quality collaborative annotation | Raw data only              | Majority vote/custom     |

These task types allow for flexible, scalable annotation workflows tailored to project needs, ensuring data quality and
annotator performance.

## Standard Consensus Tasks

Read more about Consensus Tasks [here](https://docs.dataloop.ai/docs/consensus).

Standard consensus tasks involve multiple annotators working on the same items, enabling comparison and consolidation of
annotations based on majority votes or custom rules.
In the following example, we will duplicate 60% of the data to be annotated by all 3 assignees, the rest 40% will be
divided according to the distribution between the assignees:

### Example:

```python
task = dataset.tasks.create(
    task_name='Consensus Task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai', 'annotator3@dataloop.ai'],
    consensus_task_type=dl.entities.ConsensusTaskType.CONSENSUS,
    consensus_percentage=60,  # 50% of items will have consensus
    consensus_assignees=3  # Each consensus item is assigned to 3 annotators
)
```

## Honeypot Tasks

Read more about Honeypot Tasks [here](https://docs.dataloop.ai/docs/qualification-honeypot#honeypot).

Honeypot tasks are designed for continuous monitoring of annotators' performance during their regular work by planting
items with known ground truth among raw data.
These tasks help assess annotators' accuracy and ensure ongoing quality control.
**NOTE** There must be a `/honeypot` folder in the root of the dataset with the annotated items (that will be randomly cloned to
the different assignments).

### Example:

```python
task = dataset.tasks.create(
    task_name='Honeypot Task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    consensus_task_type=dl.entities.ConsensusTaskType.HONEYPOT,
    consensus_percentage=5,  # 5% of items are honeypot
)
```

## Qualification Tasks

Read more about Qualification Tasks [here](https://docs.dataloop.ai/docs/qualification-honeypot#qualification).

Qualification tasks evaluate annotators' skills before assigning them to production tasks.
These tasks simulate a test environment where annotators work on items with hidden ground truth.
Qualification tasks create an assignment **over entire selected data for each of the assignees**.
By having ground-truth annotations, a score is calculated and provided for each of the assignees.

### Example:

```python
task = dataset.tasks.create(
    task_name='Qualification Task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    consensus_task_type=dl.entities.ConsensusTaskType.QUALIFICATION
)
```
