# Advanced Embedding Processing Tutorial

This notebook provides a comprehensive guide and a ready-to-use workflow for enhancing your datasets with advanced embedding techniques. By leveraging your existing data labels, you can generate more powerful and insightful data representations for visualization and similarity search.

You'll learn two powerful approaches: Label-Guided UMAP for creating visually clustered 3D embeddings, and Extended CLIP for enriching high-dimensional vectors with label information to improve similarity search performance.

### Prerequisites:
* **Dataloop Account:** You should have access to a Dataloop platform account.
* **Python Environment:** Python 3.7+ with pip for installing required packages.
* **Basic Knowledge:** Familiarity with machine learning concepts and embeddings is helpful but not required.

### Navigate through the following sections:
1. **[Setup and Configuration](#setup)** - Installing dependencies and establishing platform connection
2. **[Option A: Label-Guided UMAP Embedding](#option-a)** - Creating 3D embeddings for visualization
3. **[Option B: Extended CLIP Embedding](#option-b)** - Enriching CLIP vectors with label information
4. **[Conclusion and Next Steps](#conclusion)** - Summary and further actions

---

### 🎯 Embedding Options at a Glance

#### Option A: Label-Guided UMAP Embedding
- **Purpose**: Creates low-dimensional (3D) embeddings that visually group items with similar labels.
- **Best for**: Interactive visualization, understanding data structure, and discovering how labels relate to underlying features.
- **Output**: A new Dataloop feature set with 3D coordinates, viewable in the platform's 3D data viewer.

#### Option B: Extended CLIP Embedding  
- **Purpose**: Augments high-dimensional CLIP features with explicit label data.
- **Best for**: Powering more accurate similarity searches where both visual and label information are important.
- **Output**: A new Dataloop feature set with enriched, high-dimensional vectors.

<a id="setup"></a>
## 1. Setup and Common Configuration

**📌 Important:** This section must be run first, regardless of which embedding option you choose later. It handles package installation, connection to the Dataloop platform, and automated project setup.

### 1.1 Install Required Packages

First, we'll install the necessary Python packages. These libraries are essential for interacting with the Dataloop platform (`dtlpy`), handling data (`pandas`), processing embeddings (`scikit-learn`), and performing dimensionality reduction (`umap-learn`). This step may take a few minutes to complete.


```python
# Install necessary packages
%pip install dtlpy
%pip install pandas
%pip install bson
%pip install python-rapidjson
%pip install scikit-learn
%pip install umap-learn
```

### 1.2 Import Libraries and Define Helpers

Next, we import the required libraries and define a helper function. This function, `ensure_feature_set`, simplifies the process of creating or retrieving a feature set in your Dataloop project, preventing errors if the feature set already exists.


```python
# Import required libraries
import json
import random
import string
import dtlpy as dl
import numpy as np
import os
import umap
import matplotlib.pyplot as plt
from sklearn.preprocessing import MultiLabelBinarizer
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def ensure_feature_set(project: dl.Project, feature_set_name, dim, set_type):
    """
    Create or get an existing feature set in the project.
    
    Args:
        project: Dataloop project object
        feature_set_name: Name for the feature set
        dim: Dimension/size of the feature vectors
        set_type: Type of the feature set (e.g., '3d', 'embedding')
    
    Returns:
        dl.FeatureSet: The created or existing feature set
    """
    try:
        feature_set: dl.FeatureSet = project.feature_sets.create(
            name=feature_set_name, 
            size=dim, 
            set_type=set_type, 
            entity_type=dl.FeatureEntityType.ITEM
        )
    except Exception as e:
        feature_set: dl.FeatureSet = project.feature_sets.get(feature_set_name=feature_set_name)
    return feature_set
```

### 1.3 Automated Project and Dataset Setup

This section fully automates the setup process within the Dataloop platform. It is designed to run without any manual input.

**What this step does:**
1. **Connects to Dataloop:** Establishes a connection to the platform, handling authentication if needed.
2. **Creates a Project:** A new project named `My First Embeddings Project` is created to house our work.
3. **Installs a Dataset App:** The `dataset-images-animals` Dataloop App (DPK) is installed from the Marketplace. This app automatically creates a sample dataset with images, annotations, and pre-computed CLIP embeddings.
4. **Waits for Setup:** The script waits for the app's setup services to complete.
5. **Extracts Configuration:** Finally, it retrieves the newly created `dataset_id` and the existing `feature_set_id` (`'clip-feature-set'`), which are essential for the subsequent steps.


```python
# 🔗 Step 1: Connect to Dataloop Environment
print("🔗 Step 1: Connecting to Dataloop...")
dl.setenv('prod')  # Set environment to RC (adjust if needed)
if dl.token_expired():
    print("🔐 Token expired, logging in...")
    dl.login()
print("✅ Successfully connected to Dataloop environment")

# 📁 Step 2: Create New Project
print("\n📁 Step 2: Creating project...")
suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
project = dl.projects.create(project_name=f"My First Embeddings Project_{suffix}")
print(f"✅ Project loaded: '{project.name}' (ID: {project.id})")

# 📦 Step 3: Install DPK
print("\n📦 Step 3: Installing dataset app...")
dpk = dl.dpks.get(dpk_name='dataset-images-animals')
app = project.apps.install(dpk=dpk, app_name=dpk.display_name)
print(f"✅ DPK installed: '{dpk.display_name}' (Version: {dpk.version})")

# ⚙️ Step 4: Setup Services
print("\n⚙️ Step 4: Configuring services...")
# Create a filter to get services belonging to the app
filters = dl.Filters(resource=dl.FiltersResource.SERVICE)
filters.add(field='packageId', values=dpk.id)

# List the services with the specified filters
services = [ser for ser in project.services.list(filters=filters).all()]
service: dl.Service = services[0]
print(f"✅ Service configured: '{service.name}' (ID: {service.id})")

# 🔍 Step 5: Extract Configuration
print("\n🔍 Step 5: Wait for execution to complete...")
execution = service.executions.list()[0][0]
execution.wait()
dataset_id = execution.input['dataset']['dataset_id']
feature_set: dl.Feature = project.feature_sets.get(feature_set_name='clip-feature-set')

print(f"✅ Configuration extracted successfully!")
print(f"📊 Dataset ID: {dataset_id}")
print(f"🎯 Feature Set: '{feature_set.name}' (ID: {feature_set.id})")

print("\n" + "="*60)
print("🎉 Setup Complete! Use these values in the next steps:")
print(f"   📊 dataset_id: {dataset_id}")
print(f"   🎯 feature_set_id: {feature_set.id}")
print("="*60)
```

### 1.4 Download Dataset and Extracted Features

This final setup step brings the data from the Dataloop platform to our local notebook environment. We use the SDK's `export` functionality to download a JSON representation of our dataset, which includes all items, their annotations (labels), and their pre-computed feature vectors.

**What happens here:**
1. An export job is created for the entire dataset.
2. The job is configured to include feature vectors and annotations.
3. The resulting JSON file is downloaded to a local `./export` directory.
4. The script then loads this JSON file to confirm the export and count the number of items.


```python
# 📊 Configure export directory
save_dir = "./export"  # Local directory for exported data
os.makedirs(save_dir, exist_ok=True)

# 🔄 Get dataset and export data
dataset = dl.datasets.get(dataset_id=dataset_id)

print("🚀 Starting data export process...")
print(f"📁 Dataset: {dataset.name}")
print(f"💾 Save directory: {save_dir}")

# 📤 Export dataset with feature vectors and annotations using the simple export method
print("📤 Exporting dataset with feature vectors and annotations...")
export_result = dataset.export(
    local_path=save_dir,
    include_feature_vectors=True,
    include_annotations=True,
    export_type='json',
    timeout=0  # No timeout - wait until complete
)

print("⏳ Export completed...")
print(f"📥 Export result: {export_result}")

# The export returns the directory path, we need to find the actual JSON file
data_file = None

# Look for JSON files in the export directory
json_files = [f for f in os.listdir(export_result) if f.endswith('.json')]
data_file = os.path.join(export_result, json_files[0])
print(f"📊 Found JSON file: {data_file}")
print(f"📊 Data file: {data_file}")

# Count items in the export
with open(data_file, 'r') as f:
    exported_data = json.load(f)
    items_count = len(exported_data)

print("✅ Data export completed successfully!")
print(f"📊 Total items exported: {items_count}")
print("📋 You can now proceed to choose your embedding option below.")
```

---

<a id="option-a"></a>
## 2. Option A: Label-Guided UMAP Embedding

**Choose this option if your goal is to create meaningful 3D visualizations of your data.** This technique uses the UMAP algorithm in a supervised mode, leveraging your annotation labels to guide the dimensionality reduction process. The result is an embedding where items with similar labels are positioned closer together in the 3D space.

### How it Works:
1. **Input**: Takes the existing high-dimensional feature vectors (e.g., from CLIP) and the corresponding annotation labels for each item.
2. **Process**: The UMAP algorithm is trained on both the features and the labels simultaneously. The `target_weight` parameter controls how strongly the labels influence the final layout.
3. **Output**: A new 3D coordinate for each item, plus a set of 2D scatter plot images (one for each label) saved locally for quick inspection.
4. **Result**: A new Dataloop feature set containing these 3D embeddings, which can be visualized directly on the platform.

**💡 Tip**: Experiment with the UMAP parameters (`n_neighbors`, `min_dist`, `target_weight`) in the code to see how they affect the clustering and separation of your data.

### 2.1 Configure Feature Set Name

First, specify the name for the new UMAP feature set that will be created in your Dataloop project.


```python
# 🏷️ Configure the name for your new UMAP feature set
# This will be created in your Dataloop project
enhanced_feature_set_name = "umap-label-enhanced"

print(f"✅ Feature set name configured: {enhanced_feature_set_name}")
print("📋 This will create a new feature set with 3D UMAP embeddings in your project, optimized to separate by labels.")
```

### 2.2 Generate Label-Guided UMAP Embeddings

This code cell executes the entire UMAP generation workflow. It will:
1. **Load data** from the exported JSON file, extracting the features and labels.
2. **Prepare labels** by converting them into a binary format suitable for supervised UMAP.
3. **Run the UMAP algorithm** with the specified parameters to generate 3D embeddings.
4. **Generate and save visualizations** as PNG files, showing the distribution of each label in the 2D plane.
5. **Upload the new embeddings** back to your Dataloop project under the feature set name you configured.


```python
print("🔄 Step 1: Loading and processing data...")

# 📊 Load data from exported file
items = dict()
with open(data_file, 'r') as f:
    exported_data = json.load(f)
    
    # Handle different export formats
    if isinstance(exported_data, dict) and 'items' in exported_data:
        items_list = exported_data['items']
    elif isinstance(exported_data, list):
        items_list = exported_data
    else:
        raise ValueError("Unexpected export format")
    
    # Process each item
    for item in items_list:
        # Only process annotated items
        if not item.get('annotated', False):
            continue
        
        # Extract feature vectors and labels
        if item.get("itemVectors") and len(item.get("itemVectors", [])) > 0:
            # Find the feature vector for the current feature set
            feature_vector = None
            for vector in item["itemVectors"]:
                if vector.get('featureSetId') == feature_set.id:
                    feature_vector = vector.get('value')
                    break
            
            if feature_vector is None:
                # Try to get the first available vector if specific feature set not found
                feature_vector = item["itemVectors"][0].get('value')
            
            if feature_vector is not None:
                labels = [ann['label'] for ann in item.get("annotations", [])]
                items[item["id"]] = {"features": feature_vector, "labels": labels}

print(f"📋 Loaded {len(items)} annotated items with feature vectors")

# 🔄 Step 2: Prepare data for UMAP
print("🔄 Step 2: Preparing labels for supervised learning...")

# Convert to numpy arrays
features = np.array([v["features"] for v in items.values()])
labels = [v["labels"] for v in items.values()]  # keep as list for multi-label processing

# Convert labels to binary format for UMAP
mlb = MultiLabelBinarizer()
y = mlb.fit_transform(labels)

print(f"✅ Feature matrix shape: {features.shape}")
print(f"✅ Label matrix shape: {y.shape}")
print(f"✅ Unique labels found: {list(mlb.classes_)}")

# 🔄 Step 3: Run UMAP algorithm
print("🔄 Step 3: Running UMAP algorithm (this may take several minutes)...")

# Configure UMAP with label guidance
dumap = umap.UMAP(
    n_components=3,           # Create 3D embeddings
    n_neighbors=50,           # Controls local vs global structure (try 15, 30, 50, 100)
    min_dist=0.1,            # Controls cluster tightness (try 0.0, 0.1, 0.3, 0.5)
    metric="cosine",         # Distance metric for features
    target_metric="jaccard",  # Distance metric for labels
    target_weight=0.7,       # How much labels influence embedding (try 0.5, 0.7, 0.9)
    verbose=True,            # Show progress
    random_state=42          # For reproducible results
)

# Generate embeddings
embedding = dumap.fit_transform(features, y=y)
print(f"✅ Generated {embedding.shape[0]} embeddings with {embedding.shape[1]} dimensions")

# 🔄 Step 4: Create visualizations
print("🔄 Step 4: Creating visualization plots...")

# Create visualizations for each label
for idx, label in enumerate(mlb.classes_):
    mask = y[:, idx] == 1  # Items with this label
    
    plt.figure(figsize=(10, 8))
    plt.scatter(embedding[~mask, 0], embedding[~mask, 1], 
                c='lightgray', alpha=0.5, s=30, label=f'Other items')
    plt.scatter(embedding[mask, 0], embedding[mask, 1], 
                c='red', alpha=0.8, s=50, label=f'{label} items')
    
    plt.title(f"UMAP Embedding: '{label}' Distribution", fontsize=14)
    plt.xlabel("UMAP Dimension 1", fontsize=12)
    plt.ylabel("UMAP Dimension 2", fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save plot
    plot_filename = f"{save_dir}/umap_visualization_{label.replace(' ', '_')}.png"
    plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"  📊 Saved visualization for '{label}' -> {plot_filename}")

print("✅ All visualizations saved successfully!")

# 🔄 Step 5: Prepare embeddings for upload
print("🔄 Step 5: Preparing embeddings for upload to Dataloop...")

# Match embeddings back to item IDs
to_upload = {}
for indx, key in enumerate(items.keys()):
    to_upload[key] = embedding[indx].tolist()

# Create feature set in Dataloop
feature_set_label_enhanced = ensure_feature_set(project, enhanced_feature_set_name, 3, "3d")
print(f"✅ Feature set '{enhanced_feature_set_name}' ready in project")

# 🔄 Step 6: Upload embeddings
print("🔄 Step 6: Uploading embeddings to Dataloop...")

def upload_single(feature_set, item, value, pbar):
    """Upload a single feature vector to Dataloop"""
    try:
        feature_set_label_enhanced.features.create(value=value, entity=item)
        pbar.update(1)
        return True
    except Exception as e:
        print(f"❌ Error uploading feature for {item.id}: {e}")
        pbar.update(1)
        return False

# Upload with progress tracking
with tqdm(total=len(to_upload), desc="📤 Uploading UMAP embeddings") as pbar:
    pool = ThreadPoolExecutor(max_workers=50)
    futures = []
    
    for item_id, feature in to_upload.items():
        item = dataset.items.get(item_id=item_id, fetch=False)
        future = pool.submit(upload_single, feature_set_label_enhanced, item, feature, pbar)
        futures.append(future)
    
    # Wait for all uploads to complete
    successful_uploads = sum(1 for future in futures if future.result())
    pool.shutdown(wait=True)

print(f"✅ UMAP embedding generation completed!")
print(f"📊 Feature set '{enhanced_feature_set_name}' created with 3D embeddings")
print(f"📁 Visualizations saved in: {save_dir}")
print(f"🎯 Total items processed: {len(to_upload)}")
print(f"✅ Successfully uploaded: {successful_uploads}/{len(to_upload)}")
print("\n🎉 Your label-guided UMAP embeddings are now available in Dataloop!")
```

---

<a id="option-b"></a>
## 3. Option B: Extended CLIP Embedding

**Choose this option if your goal is to improve similarity search performance.** This technique enriches your existing high-dimensional CLIP vectors by appending binary information derived from your labels. This allows similarity searches to consider both visual features and explicit label data, leading to more accurate results.

### How it Works:
1. **Input**: Takes the existing high-dimensional CLIP feature vectors and the annotation labels for each item.
2. **Process**: First, all unique labels across the dataset are identified. For each item, a binary vector is created where each position corresponds to a unique label (1 if present, 0 if absent). This binary vector is then concatenated to the end of the item's original CLIP vector.
3. **Output**: A new, higher-dimensional feature vector for each item.
4. **Result**: A new Dataloop feature set containing these extended embeddings, ready to be used for enhanced similarity search.

**💡 Example**: If your original CLIP features are 512-dimensional and you have 10 unique labels in your dataset, the new extended features will be 522-dimensional (512 + 10).

### 3.1 Configure Feature Set Name

First, specify the name for the new extended CLIP feature set that will be created in your Dataloop project.


```python
# 🏷️ Configure the name for your new extended CLIP feature set
# This will be created in your Dataloop project
extended_feature_set_name = "extended-clip"

print(f"✅ Feature set name configured: {extended_feature_set_name}")
print("📋 This will create a new feature set with extended CLIP embeddings in your project.")
```

### 3.2 Generate Extended CLIP Embeddings

This code cell executes the entire workflow for creating extended CLIP embeddings. It will:
1. **Analyze the dataset** to find all unique labels available.
2. **Create a binary vector** for each item, representing the presence or absence of each unique label.
3. **Concatenate** the original CLIP feature vector with the new label binary vector for each item.
4. **Upload the new, extended embeddings** back to your Dataloop project under the feature set name you configured.

**⏱️ Processing time**: This process is generally much faster than UMAP as it does not involve complex model training.


```python
def labels_to_binary_vector(all_labels, sample_labels):
    """
    Create a binary vector indicating the presence of each label from all_labels
    in sample_labels.

    Args:
        all_labels (list): List of all possible labels.
        sample_labels (list): Labels for the current sample (may contain duplicates).

    Returns:
        list: Binary vector (list of 0/1).
    """
    sample_set = set(sample_labels)
    return [int(label in sample_set) for label in all_labels]

print("🔄 Step 1: Analyzing dataset to find all unique labels...")

# 📊 Load data from exported file
with open(data_file, 'r') as f:
    exported_data = json.load(f)
    
# Handle different export formats
if isinstance(exported_data, dict) and 'items' in exported_data:
    items_list = exported_data['items']
elif isinstance(exported_data, list):
    items_list = exported_data
else:
    raise ValueError("Unexpected export format")

# 🔍 Find all unique labels in the dataset
all_labels = set()
for item in items_list:
    for annotation in item.get("annotations", []):
        all_labels.add(annotation.get("label"))

all_labels = list(sorted(all_labels))  # Sort for consistent ordering
print(f"✅ Found {len(all_labels)} unique labels: {all_labels}")

print("🔄 Step 2: Processing items and creating extended embeddings...")

# 📊 Process each item and create extended embeddings
all_processed_data = {}
processed_count = 0
skipped_count = 0

for item in items_list:
    # Skip items without feature vectors
    if not item.get("itemVectors") or len(item.get("itemVectors", [])) == 0:
        skipped_count += 1
        continue
    
    # Extract original feature vector
    # Try to find the vector for the current feature set first
    original_vector = None
    for vector in item["itemVectors"]:
        if vector.get('featureSetId') == feature_set.id:
            original_vector = vector.get("value")
            break
    
    # If not found, use the first available vector
    if original_vector is None:
        original_vector = item["itemVectors"][0].get("value")
    
    if original_vector is None:
        skipped_count += 1
        continue
    
    # Extract labels for this item
    item_labels = [annotation.get("label") for annotation in item.get("annotations", [])]
    
    # Create binary label vector
    label_binary_vector = labels_to_binary_vector(all_labels, item_labels)
    
    # Concatenate original features with label binary vector
    extended_vector = np.concatenate([original_vector, label_binary_vector])
    
    # Store processed data
    all_processed_data[item.get("id")] = {
        "item_vector_data": extended_vector,
        "annotations_labels": item_labels,
        "id": item.get("id")
    }
    processed_count += 1

print(f"✅ Successfully processed {processed_count} items")
print(f"⚠️  Skipped {skipped_count} items (missing feature vectors)")

# Show dimension information
if all_processed_data:
    sample_vector = next(iter(all_processed_data.values()))["item_vector_data"]
    original_dim = len(sample_vector) - len(all_labels)
    print(f"📊 Original feature dimension: {original_dim}")
    print(f"📊 Label dimension: {len(all_labels)}")
    print(f"📊 Extended feature dimension: {len(sample_vector)}")
    print(f"💡 Extension ratio: {len(sample_vector)/original_dim:.2f}x original size")

print("\n🔄 Step 3: Creating extended feature set and uploading embeddings...")

# Create the extended feature set
original_feature_set = dl.feature_sets.get(feature_set_id=feature_set.id)
extended_dim = original_feature_set.size + len(all_labels)
extended_feature_set = ensure_feature_set(
    project, 
    extended_feature_set_name, 
    extended_dim, 
    original_feature_set.set_type + "-extended"
)

print(f"✅ Created feature set '{extended_feature_set_name}' with dimension {extended_dim}")

# Prepare data for upload
to_upload = {}
for item_id, data in all_processed_data.items():
    to_upload[item_id] = data["item_vector_data"].tolist()

# Upload function
def upload_single(feature_set, item, value, pbar):
    """Upload a single feature vector to Dataloop"""
    try:
        feature_set.features.create(value=value, entity=item)
        pbar.update(1)
        return True
    except Exception as e:
        print(f"❌ Error uploading feature for {item.id}: {e}")
        pbar.update(1)
        return False

# Upload with progress tracking
with tqdm(total=len(to_upload), desc="📤 Uploading extended embeddings") as pbar:
    pool = ThreadPoolExecutor(max_workers=50)
    futures = []
    
    for item_id, feature in to_upload.items():
        item = dataset.items.get(item_id=item_id, fetch=False)
        future = pool.submit(upload_single, extended_feature_set, item, feature, pbar)
        futures.append(future)
    
    # Wait for all uploads to complete
    successful_uploads = sum(1 for future in futures if future.result())
    pool.shutdown(wait=True)

print(f"\n✅ Extended CLIP embedding generation completed!")
print(f"📊 Feature set '{extended_feature_set_name}' created with {extended_dim} dimensions")
print(f"🎯 Successfully uploaded: {successful_uploads}/{len(all_processed_data)}")
print("\n🎉 Your extended CLIP embeddings are now available in Dataloop!")
```

---
<a id="conclusion"></a>
## 4. Conclusion and Next Steps

Congratulations! You have successfully walked through the process of enhancing a dataset with advanced, label-aware embedding techniques. You have created one or two new feature sets in your Dataloop project, each tailored for a specific purpose.

### Summary of Results

**If you chose Option A (Label-Guided UMAP):**
- You created a `3d` feature set (e.g., `umap-label-enhanced`).
- These embeddings are optimized for visualization, where items with similar labels are clustered together.
- **Next Step:** Navigate to the dataset in the Dataloop platform, go to the 'Embeddings' tab, select your new 3D feature set, and explore your data in the interactive 3D viewer.

**If you chose Option B (Extended CLIP):**
- You created a high-dimensional `embedding` feature set (e.g., `extended-clip`).
- These embeddings are enriched with label information, making them ideal for more accurate similarity searches.
- **Next Step:** Use the platform's similarity search feature (e.g., by right-clicking an item and selecting 'Find Similar'). Ensure you select your new extended feature set to power the search.

### Further Actions

*   **Downstream Tasks:** These new feature sets can be used as inputs for other machine learning models or pipelines.
*   **Parameter Tuning:** Experiment with the parameters in the UMAP and Extended CLIP generation cells to see how they affect your results.
*   **Automation:** Integrate this notebook's logic into a Dataloop FaaS (Function as a Service) to automatically generate enhanced embeddings whenever your dataset is updated.
