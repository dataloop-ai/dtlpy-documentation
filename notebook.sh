echo "http://localhost:8888/notebooks/basics/basic_operations.ipynb"
echo "http://localhost:8888/notebooks/model_management/classification/inception_keras_training.ipynb"
jupyter notebook --NotebookApp.allow_origin=* --NotebookApp.allow_remote_access=1 --NotebookApp.token='' --NotebookApp.password='' --no-browser --port=8888 --config "jupyter_notebook_config.py"
