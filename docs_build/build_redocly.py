import os
import glob
import re
import yaml
import json
import pathlib
import random

import logging

logger = logging.getLogger(__name__)


def build_redocly():
    root = "./"

    subs_list = ['tutorials']
    mdx_lines, tut_dict = update_tutorials_redocly(root, subs_list)

    sidebars_yaml = os.path.join(root, "sidebars.yaml")
    update_yaml_file(tut_dict, sidebars_yaml)

    # mdx_file = os.path.join(root, 'tutorials/tutorials.mdx')
    # update_mdx_file(mdx_lines, mdx_file)


def update_tutorials_redocly(root, sub_folders_list):
    superdict = dict()
    superdict['contents'] = []
    mdx_str = []
    mydict = dict()
    for sub_folder in sub_folders_list:
        mylist = []
        directory = os.path.join(root, sub_folder)
        myjson = [os.path.basename(x)
                  for x in glob.glob(sub_folder + "/*.json", recursive=False)
                  if os.path.isfile(x)]
        if len(myjson) == 0:
            ...
        elif len(myjson) == 1:

            myjson = os.path.join(directory, myjson[0])
            mydict.update({'group': 'Tutorials',
                           'page': sub_folder + "/" + sub_folder + ".md",
                           'expanded': False,
                           'items': []})
            mdx_str = gen_sub_dict(myjson, mydict, directory, sub_folder, 0, mylist)
            superdict['contents'].append(mydict)
        else:
            raise ValueError(f"too many json files in directory: {len(myjson)}, {myjson}")
    return mdx_str, mydict


def gen_sub_dict(myjson, mydict, directory, mysubdir, level, str_list):
    with open(myjson) as json_file:
        data = json.load(json_file)
    yaml_str_list = []
    for content in data['content']:
        str_for_list = ""
        comp_dict = dict()
        display_name = content['displayName']
        location = content['location']
        page_location = mysubdir + "/" + location
        logger.info(f'Build redocly page for {location}')
        location_filepath = os.path.join(directory, location)
        md_file = "nofile"
        if not os.path.isfile(location_filepath):
            logger.warning(f"file does not exist: {location_filepath}")
            continue
        file_extension = pathlib.Path(location_filepath).suffix
        if file_extension == ".json":
            comp_dict['group'] = content['displayName']
            comp_dict['expanded'] = False
            comp_dict['items'] = []
            tabs = '&nbsp;' * (level-1) * 8
            str_for_list += f'| <div>{tabs}{display_name}</div> | {content["description"]} | |'
            if level > 0:
                str_list.append(str_for_list)
            gen_sub_dict(myjson=location_filepath,
                         mydict=comp_dict,
                         directory=directory,
                         mysubdir=mysubdir,
                         level=level + 1,
                         str_list=str_list)
        else:
            comp_dict['label'] = display_name
            comp_dict['page'] = page_location
            notebook_url = "https://github.com/dataloop-ai/dtlpy-documentation/blob/main/" + page_location.replace(
                ".md", ".ipynb")
            colab_url = "https://colab.research.google.com/github/dataloop-ai/dtlpy-documentation/blob/main/" + page_location.replace(
                ".md", ".ipynb")
            tabs = '&nbsp;' * (level-1) * 8
            str_for_list += f'| <div>{tabs}[{display_name}]({location})</div> | {content["description"]} | [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)]({notebook_url}) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url}) |'
            str_list.append(str_for_list)
        if level == 0:
            table_lines = ['| Name | Description | Notebook |', '| --- | --- | --- |']
            table_lines.extend(str_list)
            md_file = gen_md_file('\n'.join(table_lines), location, directory, content['displayName'])
            comp_dict['page'] = mysubdir + "/" + md_file
            str_list = []
        # else:
        #     str_list.append(str_for_list)

        get_mdx_str(header=content['displayName'],
                    md_file=md_file,
                    description=content['description'],
                    str_list=yaml_str_list)
        mydict['items'].append(comp_dict)
    return yaml_str_list


def get_mdx_str(header, md_file, description, str_list):
    # Map headers to their corresponding icons
    icon_mapping = {
        "Data Management": "dataManagementIcon",
        "Annotations": "annotationsIcon",
        "Recipe and Ontology": "recipeOntologyIcon",
        "Task and Workflows": "taskWorkflowsIcon",
        "Analytics": "analyticsIcon",
        "FaaS Tutorial": "faasIcon",
        "Pipelines": "pipelinesIcon",
        "Model Management": "modelManagementIcon",
        "Applications": "applicationsIcon",
        "Tutorials": "tutorialsIcon",
        "Resources": "resourcesIcon",
        "Onboarding": "onboardingIcon"
    }
    
    # Get the corresponding icon or use a default
    icon = icon_mapping.get(header, "tutorialsIcon")
    
    str_list.append(f'    <WideTile header="{header}" to="{md_file}" icon={{{icon}}}>\n')
    str_list.append(f'          {description}\n')
    str_list.append(f'    </WideTile>\n')


def gen_md_file(md_str, directory, mydest, h2):
    file_name = directory.split("/")[0] + ".md"
    file_path = mydest + "/" + file_name
    md_str = '# Tutorials\n\n## ' + h2 + "\n" + md_str
    with open(file_path, "w+") as f:
        f.write(md_str)
    return file_name


def get_yaml_data(yaml_filepath):
    with open(yaml_filepath) as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as exception:
            print(exception)
    return data


def update_yaml_file(tut_dict, yaml_filepath):
    data = get_yaml_data(yaml_filepath=yaml_filepath)
    for i in range(len(data)):
        mydict = data[i]
        if 'group' in mydict:
            if mydict['group'] == 'Tutorials':
                data[i] = tut_dict
                break
    with open(yaml_filepath, 'w') as file:
        yaml.dump(data, file, indent=2)


def update_mdx_file(mdx_lines, mdx_file):
    with open(mdx_file, "r+") as f:
        newlines = []
        inside = False
        for item in f.readlines():
            if re.search('^\s*<FlexSection', item):
                inside = True
                newlines.append(item)
                continue

            if re.search('^\s*</FlexSection', item):
                inside = False
                newlines.extend(mdx_lines)
                newlines.append(item)
                continue

            if inside:
                continue

            newlines.append(item)
    with open(mdx_file, "w") as f:
        f.writelines(newlines)


if __name__ == "__main__":
    """
    Building MD files and MDX files
    and update sidebar.yaml
    """
    build_redocly()
