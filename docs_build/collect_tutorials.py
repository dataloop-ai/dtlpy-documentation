import json
import importlib.util
import inspect
import os

LINE_HEADER = '<func:'

TEMPLATES_PATH = 'docs_build/tutorials_templates'
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


def _build_md_block(func_string):
    # ignore 0 def line and the """
    source = list()
    for line in func_string[2:-1]:
        source.append(line[4:].rstrip() + '  \n')  # remove 4 spaces at the beginning
    return source


def load_templates(skeleton_filepath, mds_filepath, scripts_filepath):
    ####################
    # Load md function #
    ####################
    mds_spec = importlib.util.spec_from_file_location('mds', mds_filepath)
    mds_module = importlib.util.module_from_spec(mds_spec)
    mds_spec.loader.exec_module(mds_module)

    #######################
    # Load python scripts #
    #######################
    scripts_spec = importlib.util.spec_from_file_location('scripts', scripts_filepath)
    scripts_module = importlib.util.module_from_spec(scripts_spec)
    scripts_spec.loader.exec_module(scripts_module)
    indent_factor = 4
    # added support for class methods
    model_adapter_cls = getattr(scripts_module, 'Scripts', None)
    if model_adapter_cls is not None:
        scripts_module = model_adapter_cls()
        indent_factor = 8

    ######################
    # Load Skeleton file #
    ######################
    with open(skeleton_filepath, 'r') as f:
        skeleton = json.load(f)
    return skeleton, mds_module, scripts_module, indent_factor


def build_notebook(skeleton_filepath, mds_filepath, scripts_filepath):
    skeleton, mds_module, scripts_module, indent_factor = load_templates(skeleton_filepath=skeleton_filepath,
                                                                         mds_filepath=mds_filepath,
                                                                         scripts_filepath=scripts_filepath)
    cells = list()
    for cell_def in skeleton:
        if cell_def['type'] == 'md':
            cell = MD_CELL_TEMPLATE.copy()
            func_name = cell_def['name']
            func = getattr(mds_module, func_name)
            func_string, _ = inspect.getsourcelines(func)
            source = _build_md_block(func_string)
            # source = source# adding double space for new line
            cell['source'] = source

        elif cell_def['type'] == 'code':
            cell = CODE_CELL_TEMPLATE.copy()
            func_name = cell_def['name']
            func = getattr(scripts_module, func_name)
            func_string, _ = inspect.getsourcelines(func)
            # remove the "def" line
            func_string = func_string[1:]
            write_state = True
            source = list()
            for line in func_string[1:]:
                if line.strip().startswith('# DTLPY-STOP'):
                    write_state = False
                    continue
                if line.strip().startswith('# DTLPY-START'):
                    write_state = True
                    continue
                if write_state is False:
                    continue
                source.append(line[indent_factor:])
            cell['source'] = source
        else:
            raise ValueError('unknown cell type {!r}'.format(cell_def['type']))
        cells.append(cell)
    NOTEBOOK_TEMPLATE['cells'] = cells

    notebook_filepath = os.path.dirname(skeleton_filepath).replace(TEMPLATES_PATH, TUTORIALS_PATH)
    notebook_filepath = os.path.join(notebook_filepath, 'chapter.ipynb')
    os.makedirs(os.path.dirname(notebook_filepath), exist_ok=True)
    with open(notebook_filepath, 'w', encoding='UTF-8') as f:
        json.dump(NOTEBOOK_TEMPLATE, f)


def build_md_file(skeleton_filepath, mds_filepath, scripts_filepath):
    skeleton, mds_module, scripts_module, indent_factor = load_templates(skeleton_filepath=skeleton_filepath,
                                                                         mds_filepath=mds_filepath,
                                                                         scripts_filepath=scripts_filepath)
    lines = list()
    for cell_def in skeleton:
        if cell_def['type'] == 'md':
            func_name = cell_def['name']
            func = getattr(mds_module, func_name)
            func_string, _ = inspect.getsourcelines(func)
            lines.extend(_build_md_block(func_string))
        elif cell_def['type'] == 'code':
            func_name = cell_def['name']
            func = getattr(scripts_module, func_name)
            func_string, _ = inspect.getsourcelines(func)
            lines.append('\n```python\n')
            # ignore 0 def line and the """
            write_state = True
            for line in func_string[1:]:
                if line.strip().startswith('# DTLPY-STOP'):
                    write_state = False
                    continue
                if line.strip().startswith('# DTLPY-START'):
                    write_state = True
                    continue
                if write_state is False:
                    continue
                lines.append(line[indent_factor:])  # remove spaces at the beginning
            lines.append('```\n')
        else:
            raise ValueError('unknown cell type {!r}'.format(cell_def['type']))

    md_filepath = os.path.dirname(skeleton_filepath).replace(TEMPLATES_PATH, TUTORIALS_PATH)
    md_filepath = os.path.join(md_filepath, 'chapter.md')
    os.makedirs(os.path.dirname(md_filepath), exist_ok=True)
    with open(md_filepath, 'w', encoding='UTF-8') as f:
        f.writelines(lines)


def main():
    for path, subdirs, files in os.walk(TEMPLATES_PATH):
        for filename in files:
            if filename == 'skeleton.json':
                print('Preparing {!r} ...'.format(path))
                skeleton_filepath = os.path.join(path, filename)
                mds_filepath = os.path.join(os.path.dirname(skeleton_filepath), 'mds.py')
                scripts_filepath = os.path.join(os.path.dirname(skeleton_filepath), 'scripts.py')

                build_notebook(skeleton_filepath=skeleton_filepath,
                               mds_filepath=mds_filepath,
                               scripts_filepath=scripts_filepath)
                build_md_file(skeleton_filepath=skeleton_filepath,
                              mds_filepath=mds_filepath,
                              scripts_filepath=scripts_filepath)
                print('Done!')


if __name__ == "__main__":
    """
    Building MD files and Jupyter notebook from templates.
    loading skeleton.json file for the interleaving between code and text.
    
    Running build.py will OVERWRITE the "tutorials" folder with the new templates
    
    Ignoring code lines:
    you can use "# DTLPY-STOP" and "# DTLPY-START" to mark if you dont want some code to go in to the output file
    
    Run:
    Need to run this file from the root
    python docs_build/collect_tutorials.py
    
    """
    main()
