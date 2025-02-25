# Quality Control in Dataloop: Consensus, Honeypot, and Qualification Tasks 🎯

Welcome to your guide to quality control in Dataloop! Whether you're validating annotations, assessing annotator skills, or ensuring data quality, we've got you covered. Let's dive into the world of quality control tasks!

## Understanding Quality Control Tasks 🎓

Think of quality control tasks as your data quality toolkit. Each type serves a unique purpose:

### Task Types at a Glance 📊

| Task Type | Purpose | Best For | Key Feature |
|----------|---------|----------|-------------|
| 🤝 **Consensus** | Multiple annotators work together | High-value data | Majority voting |
| 🍯 **Honeypot** | Hidden quality checks | Ongoing monitoring | Mixed with real data |
| 📝 **Qualification** | Skill assessment | New annotators | Pre-task testing |

## Creating Consensus Tasks 🤝

Want multiple annotators to work on the same items? Consensus tasks are your friend! They help ensure quality through collaboration and agreement.

```python
import dtlpy as dl
import datetime

# Create a consensus task where multiple annotators work on the same items
consensus_task = dataset.tasks.create(
    task_name='Consensus Task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=[
        'annotator1@dataloop.ai',
        'annotator2@dataloop.ai',
        'annotator3@dataloop.ai'
    ],
    consensus_task_type=dl.entities.ConsensusTaskType.CONSENSUS,
    consensus_percentage=60,  # 60% of items will be reviewed by all annotators
    consensus_assignees=3     # Each consensus item gets 3 reviewers
)
```

### How Consensus Tasks Work 🔄

1. **Distribution**: 
   - 60% of items go to all annotators
   - 40% are divided among annotators normally
2. **Review Process**:
   - Multiple annotators work independently
   - Results are compared automatically
   - Differences can trigger additional review

## Setting Up Honeypot Tasks 🍯

Want to quietly monitor annotation quality? Honeypot tasks mix pre-annotated "truth" items with regular work.

```python
# Create a honeypot task with hidden quality checks
honeypot_task = dataset.tasks.create(
    task_name='Honeypot Task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=[
        'annotator1@dataloop.ai',
        'annotator2@dataloop.ai'
    ],
    consensus_task_type=dl.entities.ConsensusTaskType.HONEYPOT,
    consensus_percentage=5  # 5% of items will be honeypot items
)
```

### Honeypot Setup Requirements 📋

1. Create a `/honeypot` folder in your dataset root
2. Add your ground truth items there
3. They'll be randomly mixed into assignments
4. Performance is measured against these known items

💡 **Pro Tip**: Keep your honeypot percentage low (3-5%) to maintain natural workflow while ensuring quality.

## Creating Qualification Tasks 📝

Need to test annotator skills before a big project? Qualification tasks are your answer!

```python
# Create a qualification task to assess annotator skills
qualification_task = dataset.tasks.create(
    task_name='Qualification Task',
    due_date=datetime.datetime(day=1, month=1, year=2029).timestamp(),
    assignee_ids=[
        'annotator1@dataloop.ai',
        'annotator2@dataloop.ai'
    ],
    consensus_task_type=dl.entities.ConsensusTaskType.QUALIFICATION
)
```

### How Qualification Tasks Work 🎓

1. Each annotator gets the same set of pre-annotated items
2. They work without seeing the ground truth
3. Their work is compared against known correct annotations
4. Scores help you assess their skills

## Best Practices 💡

### Choosing the Right Task Type 🎯

1. **Use Consensus Tasks When**:
   - Working on critical data
   - Need high confidence in results
   - Have complex annotation guidelines

2. **Use Honeypot Tasks When**:
   - Managing large-scale operations
   - Need ongoing quality monitoring
   - Want unobtrusive quality checks

3. **Use Qualification Tasks When**:
   - Onboarding new annotators
   - Starting a new project type
   - Need to assess specific skills

### Quality Control Tips 🌟

1. **For Consensus Tasks**:
   - Start with a small consensus percentage
   - Increase based on disagreement rates
   - Use for training and standardization

2. **For Honeypot Tasks**:
   - Rotate honeypot items regularly
   - Keep honeypot items representative
   - Monitor trends over time

3. **For Qualification Tasks**:
   - Include various difficulty levels
   - Provide clear instructions
   - Set realistic passing thresholds

## Need More Help? 🤔

- Learn more about [Consensus Tasks](https://docs.dataloop.ai/docs/quality-task-types#consensus)
- Explore [Honeypot Tasks](https://docs.dataloop.ai/docs/quality-task-types#honeypot)
- Understand [Qualification Tasks](https://docs.dataloop.ai/docs/quality-task-types#qualification)

Happy quality controlling! 🚀
