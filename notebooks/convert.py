import os
import subprocess
from pathlib import Path
import nbformat

NOTEBOOKS_DIR = Path(__file__).parent
INDEX_MD = NOTEBOOKS_DIR / "notebooks.md"

# Helper to get all .ipynb files recursively
def find_notebooks(root):
    return [p for p in root.rglob("*.ipynb") if not p.name.startswith(".")]

def clean_notebook(nb_path):
    """Remove cell IDs that cause nbconvert issues"""
    nb = nbformat.read(str(nb_path), as_version=4)
    for cell in nb.cells:
        if 'id' in cell:
            del cell['id']
    return nb

# Helper to convert notebook to markdown
def convert_notebook_to_md(nb_path):
    md_path = nb_path.with_suffix(".md")
    try:
        # Clean the notebook first
        nb = clean_notebook(nb_path)
        temp_path = nb_path.with_suffix(".temp.ipynb")
        nbformat.write(nb, str(temp_path))
        
        subprocess.run([
            "jupyter", "nbconvert", "--to", "markdown", str(temp_path), "--output", md_path.stem
        ], check=True, cwd=nb_path.parent)
        
        # Clean up temp file
        temp_path.unlink()
        return md_path
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {nb_path}: {e}")
        return None

# Helper to extract notebook title/description (from metadata or fallback)
def get_notebook_metadata(nb_path):
    try:
        nb = nbformat.read(str(nb_path), as_version=4)
        title = nb.metadata.get("title") or nb_path.stem
        desc = nb.metadata.get("description") or ""
        return title, desc
    except Exception:
        return nb_path.stem, ""

# Helper to create GitHub/Colab links
def make_run_links(nb_rel_path):
    github_url = f"https://github.com/dataloop-ai/dtlpy-documentation/blob/main/notebooks/{nb_rel_path.as_posix()}"
    colab_url = f"https://colab.research.google.com/github/dataloop-ai/dtlpy-documentation/blob/main/notebooks/{nb_rel_path.as_posix()}"
    github_badge = f"[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)]({github_url})"
    colab_badge = f"[![Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"
    return f"{github_badge} {colab_badge}"

# Main script
def main():
    notebooks = find_notebooks(NOTEBOOKS_DIR)
    rows = []
    for nb_path in notebooks:
        md_path = convert_notebook_to_md(nb_path)
        nb_rel_path = nb_path.relative_to(NOTEBOOKS_DIR)
        md_rel_path = md_path.relative_to(NOTEBOOKS_DIR) if md_path else None
        title, desc = get_notebook_metadata(nb_path)
        run_links = make_run_links(nb_rel_path)
        if md_rel_path:
            name_link = f"[{title}]({md_rel_path.as_posix()})"
        else:
            name_link = title
        rows.append((name_link, desc, run_links))

    # Write notebooks.md
    with open(INDEX_MD, "w", encoding="utf-8") as f:
        f.write("# Notebooks\n\n")
        f.write("Explore interactive End-to-End Jupyter Notebooks for Dataloop Use Cases. Click the Colab or GitHub icons to run or view each notebook.\n\n")
        f.write("| Name | Description | Run |\n")
        f.write("| --- | --- | --- |\n")
        for name, desc, run in rows:
            f.write(f"| {name} | {desc} | {run} |\n")
    print(f"Converted {len(notebooks)} notebooks. Index written to {INDEX_MD}")

if __name__ == "__main__":
    main()
