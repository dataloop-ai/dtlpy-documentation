import dtlpy as dl
import tqdm
import torch
import clip
from PIL import Image

# Get the project and the dataset
project = dl.projects.get(project_id="<your-project-id>")
dataset = dl.datasets.get(dataset_id="<your-dataset-id>")

# Create the feature set
feature_set = project.feature_sets.create(name='clip-for-demo',
                                          entity_type=dl.FeatureEntityType.ITEM,
                                          project_id=project.id,
                                          set_type='clip',
                                          size=512)

# Load the embedder (CLIP)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model, preprocess = clip.load("ViT-B/32", device=device)

# List the items
items = dataset.items.list()
pbar = tqdm.tqdm(total=items.items_count)

for item in items.all():
    # Go over all the items and extract embeddings
    if 'image/' in item.mimetype:
        orig_image = Image.fromarray(item.download(save_locally=False, to_array=True))
        image = preprocess(orig_image).unsqueeze(0).to(device)
        features = model.encode_image(image)
    elif 'text/' in item.mimetype:
        text = item.download(save_locally=False).read().decode()
        tokens = clip.tokenize([text], context_length=77).to(device)
        features = model.encode_text(tokens)
    else:
        raise ValueError(f'Unsupported mimetype for clip: {item.mimetype}')
    output = features[0].cpu().detach().numpy().tolist()
    feature_set.features.create(value=output, entity=item)
    pbar.update()
