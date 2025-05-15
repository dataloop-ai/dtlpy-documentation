import dtlpy as dl

# Get the project and the dataset
project = dl.projects.get(project_id="<project-id>")
dataset = dl.datasets.get(dataset_id="<dataset-id>")

# Get the DPK and install the app
dpk = dl.dpks.get(dpk_name="clip-model-adapter")
app = project.apps.install(dpk=dpk)

# Get the model names from the DPK components
dpk_models = dpk.components.models
models_names = [model.get("name") for model in dpk_models]

# Get the embedder model
embedder = project.models.get(model_name=models_names[0])

# Embed the entire dataset
items = dataset.items.get_all_items()
embedder.embed_datasets([dataset.id])
