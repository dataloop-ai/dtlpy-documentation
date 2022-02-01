import json
import importlib.util
import inspect
import os

LINE_HEADER = '<func:'

TEMPLATES_PATH = 'tutorials_templates'
TUTORIALS_PATH = 'tutorials'
NOTEBOOK_TEMPLATE = {"cells": [],
                     "metadata": {
                         "kernelspec": {
                             "display_name": "Python 3",
                             "language": "python",
                             "name": "python3"
                         },
                         "language_info": {
                             "codemirror_mode": {
                                 "name": "ipython",
                                 "version": 3
                             },
                             "file_extension": ".py",
                             "mimetype": "text/x-python",
                             "name": "python",
                             "nbconvert_exporter": "python",
                             "pygments_lexer": "ipython3",
                             "version": "3.7.7"
                         }
                     },
                     "nbformat": 4,
                     "nbformat_minor": 4}

MD_CELL_TEMPLATE = {
    "cell_type": "markdown",
    "metadata": {},
    "source": []
}
CODE_CELL_TEMPLATE = {
    "cell_type": "code",
    "execution_count": 0,
    "metadata": {},
    "outputs": [],
    "source": []
}


def build_notebook(skeleton_filepath):
    mds_filepath = os.path.join(os.path.dirname(skeleton_filepath), 'mds.py')
    scripts_filepath = os.path.join(os.path.dirname(skeleton_filepath), 'scripts.py')
    ####
    mds_spec = importlib.util.spec_from_file_location('mds', mds_filepath)
    mds_module = importlib.util.module_from_spec(mds_spec)
    mds_spec.loader.exec_module(mds_module)
    ####
    scripts_spec = importlib.util.spec_from_file_location('scripts', scripts_filepath)
    scripts_module = importlib.util.module_from_spec(scripts_spec)
    scripts_spec.loader.exec_module(scripts_module)

    with open(skeleton_filepath) as f:
        skeleton = json.load(f)

    cells = list()
    for cell_def in skeleton:
        if cell_def['type'] == 'md':
            cell = MD_CELL_TEMPLATE.copy()
            func_name = cell_def['name']
            func = getattr(mds_module, func_name)
            func_string, _ = inspect.getsourcelines(func)
            # remove the "def" line
            func_string = func_string[1:]
            source = [l[4:] for l in func_string]
            cell['source'] = source[1:-1]  # remove trtiple
        elif cell_def['type'] == 'code':
            cell = CODE_CELL_TEMPLATE.copy()
            func_name = cell_def['name']
            func = getattr(scripts_module, func_name)
            func_string, _ = inspect.getsourcelines(func)
            # remove the "def" line
            func_string = func_string[1:]
            source = [l[4:] for l in func_string]
            cell['source'] = source
        else:
            raise ValueError('unknown cell type {!r}'.format(cell_def['type']))
        cells.append(cell)
    NOTEBOOK_TEMPLATE['cells'] = cells

    notebook_filepath = os.path.dirname(skeleton_filepath).replace(TEMPLATES_PATH, TUTORIALS_PATH)
    notebook_filepath = os.path.join(notebook_filepath, 'chapter.ipynb')
    os.makedirs(os.path.dirname(notebook_filepath), exist_ok=True)
    with open(notebook_filepath, 'w') as f:
        json.dump(NOTEBOOK_TEMPLATE, f)


def build_md_file(skeleton_filepath):
    mds_filepath = os.path.join(os.path.dirname(skeleton_filepath), 'mds.py')
    scripts_filepath = os.path.join(os.path.dirname(skeleton_filepath), 'scripts.py')
    ####
    mds_spec = importlib.util.spec_from_file_location('mds', mds_filepath)
    mds_module = importlib.util.module_from_spec(mds_spec)
    mds_spec.loader.exec_module(mds_module)
    ####
    scripts_spec = importlib.util.spec_from_file_location('scripts', scripts_filepath)
    scripts_module = importlib.util.module_from_spec(scripts_spec)
    scripts_spec.loader.exec_module(scripts_module)

    with open(skeleton_filepath) as f:
        skeleton = json.load(f)

    lines = list()
    for cell_def in skeleton:
        if cell_def['type'] == 'md':
            func_name = cell_def['name']
            func = getattr(mds_module, func_name)
            func_string, _ = inspect.getsourcelines(func)
            # ignore 0 def line and the """
            for line in func_string[2:-1]:
                lines.append(line.strip() + '\n')  # remove spaces at the beginning
        elif cell_def['type'] == 'code':
            func_name = cell_def['name']
            func = getattr(scripts_module, func_name)
            func_string, _ = inspect.getsourcelines(func)
            lines.append('```\n')
            # ignore 0 def line and the """
            for line in func_string[1:]:
                lines.append(line[4:])  # remove spaces at the beginning
            lines.append('```\n')
        else:
            raise ValueError('unknown cell type {!r}'.format(cell_def['type']))

    md_filepath = os.path.dirname(skeleton_filepath).replace(TEMPLATES_PATH, TUTORIALS_PATH)
    md_filepath = os.path.join(md_filepath, 'chapter.md')
    os.makedirs(os.path.dirname(md_filepath), exist_ok=True)
    with open(md_filepath, 'w') as f:
        f.writelines(lines)


def main():
    for path, subdirs, files in os.walk(TEMPLATES_PATH):
        for filename in files:
            if filename == 'skeleton.json':
                print('Preparing {!r} ...'.format(path))
                # skeleton_filepath = "tutorials_templates/faas/multiple_functions/skeleton.json"
                skeleton_filepath = os.path.join(path, filename)
                build_notebook(skeleton_filepath=skeleton_filepath)
                build_md_file(skeleton_filepath=skeleton_filepath)
                print('Done!')


if __name__ == "__main__":
    main()
