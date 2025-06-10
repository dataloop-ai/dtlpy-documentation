# Quick Start: Run Notebooks Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/dataloop-ai/dtlpy-documentation.git
   cd dtlpy-documentation
   ```

2. **(Recommended) Create a virtual environment:**
   ```bash
   python -m venv venv
   # Activate:
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   pip install notebook  # if not already installed
   ```

4. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```
   - Open your browser to the Jupyter page if it doesn't open automatically.
   - Navigate to the `notebooks/` folder and open any `.ipynb` file.

---

### Tips & Troubleshooting
- Run cells with `Shift+Enter`.
- Install missing packages with `pip install <package>`.
- For a richer experience, try [VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) or [JupyterLab](https://jupyterlab.readthedocs.io/).
