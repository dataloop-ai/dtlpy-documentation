# Creating Consensus Tasks

Consensus tasks in Dataloop are a critical feature for ensuring annotation quality. They enable validation, skill assessment, and collaborative annotations by involving multiple annotators in various task types: **Honeypot**, **Qualification**, and **Consensus**. Each type serves distinct purposes and methodologies, as outlined below.

---

## **Honeypot Tasks**
Honeypot tasks are designed for continuous monitoring of annotators' performance during their regular work by planting items with known ground truth among raw data. These tasks help assess annotators' accuracy and ensure ongoing quality control.

### Key Features:
- **Ground Truth Integration**: Honeypot items are pre-annotated and inserted alongside raw items.
- **Performance Monitoring**: Annotators' scores are calculated based on their annotations of honeypot items.
- **Ongoing Process**: Honeypot tasks operate within regular tasks, providing constant evaluation.

### How to Set Up:
1. Prepare a folder `/honeypot` in the dataset containing the ground-truth items.
2. Create a new annotation task and enable the Honeypot feature in the **Quality** step.
3. Specify the percentage of honeypot items (e.g., 5% means 5 out of 100 items will be honeypot items).

### Example:
```python
task = dataset.tasks.create(
    task_name='Honeypot Task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    consensus_task_type=dl.entities.ConsensusTaskType.HONEYPOT,
    consensus_percentage=5,  # 5% of items are honeypot
    consensus_assignees=2     # Each honeypot item is assigned to 2 annotators
)
```

---

## **Qualification Tasks**
Qualification tasks evaluate annotators' skills before assigning them to production tasks. These tasks simulate a test environment where annotators work on items with hidden ground truth.

### Key Features:
- **Skill Assessment**: Helps identify annotators' proficiency using controlled datasets.
- **Custom Scoring**: Supports integration with custom scoring functions for detailed evaluation.
- **Continuous Testing**: Allows reusing the same qualification task for new annotators.

### How to Set Up:
1. Create an annotation task and enable the Qualification feature in the **Quality** step.
2. Include items with known ground truth.
3. Enable a scoring pipeline to calculate annotators' performance.

### Example:
```python
task = dataset.tasks.create(
    task_name='Qualification Task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai'],
    consensus_task_type=dl.entities.ConsensusTaskType.QUALIFICATION,
    consensus_percentage=100,  # All items are qualification items
    consensus_assignees=1      # Single annotator per item for evaluation
)
```

---

## **Standard Consensus Tasks**
Standard consensus tasks involve multiple annotators working on the same items, enabling comparison and consolidation of annotations based on majority votes or custom rules.

### Key Features:
- **Redundancy**: Ensures multiple annotators review the same data.
- **Data Merging**: Annotations are merged back into original items upon completion.
- **Custom Scoring**: Enables advanced analysis and scoring of annotations.

### How to Set Up:
1. Create a new annotation task and enable the Consensus feature in the **Quality** step.
2. Specify the percentage of items for consensus and the number of annotators per item.
3. Use custom scoring functions for advanced quality control.

### Example:
```python
task = dataset.tasks.create(
    task_name='Consensus Task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=['annotator1@dataloop.ai', 'annotator2@dataloop.ai', 'annotator3@dataloop.ai'],
    consensus_task_type=dl.entities.ConsensusTaskType.CONSENSUS,
    consensus_percentage=50,  # 50% of items will have consensus
    consensus_assignees=2     # Each consensus item is assigned to 2 annotators
)
```

---

## Comparison of Consensus Task Types

| Task Type      | Purpose                              | Data Inclusion            | Evaluation Method       |
|----------------|--------------------------------------|---------------------------|-------------------------|
| **Honeypot**   | Continuous quality monitoring        | Mixed raw and ground truth| Score on honeypot items |
| **Qualification** | Pre-task skill assessment            | Ground truth only         | Compare with known truth|
| **Consensus**  | High-quality collaborative annotation| Raw data only             | Majority vote/custom    |

---

These task types allow for flexible, scalable annotation workflows tailored to project needs, ensuring data quality and annotator performance.
