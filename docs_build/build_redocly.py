from os.path import join, basename
import os
import glob
import re
import yaml
import json
import pathlib
import random


def build_redocly():
    root = "../"

    subs_list = ['tutorials']
    myndxlines, tut_dict = update_tutorials_redocly(root, subs_list)

    myyaml = join(root, "sidebars.yaml")
    update_yaml_file(tut_dict, myyaml)

    mdxfile = join(root, 'tutorials/tutorials.mdx')
    update_mdx_file(myndxlines, mdxfile)


def update_tutorials_redocly(root, subs_list):
    tutorials_folder = join(root, 'tutorials')
    superdict = dict()
    superdict['contents'] = []
    mymdxstr = []
    mydict = dict()
    for mysub in subs_list:
        mylist = []
        mydir = join(root, mysub)
        myjson = [basename(x) for x in glob.glob(glob.escape(tutorials_folder) + "/*.json", recursive=False) if
                  os.path.isfile(x)]
        if len(myjson) == 1:
            myjson = join(mydir, myjson[0])
            mydict.update({'group': 'Tutorials', 'page': mysub + "/" + mysub + ".mdx", 'expanded': False, 'pages': []})
            mymdxstr = gen_sub_dict(myjson, mydict, mydir, mysub, 0, mylist)
            superdict['contents'].append(mydict)
        else:
            print("too many json files in directory", len(myjson), myjson)
    return (mymdxstr, mydict)


def gen_sub_dict(myjson, mydict, mydir, mysubdir,level,strlist):
    with open(myjson) as json_file:
        data = json.load(json_file)
    tmpstrlist = []
    for subdict in data['content']:
        strforlist = "\t"*(level-1)
        tmpdict=dict()
        displayName = subdict['displayName']
        location = subdict['location']
        tmpfile = join(mydir,location)
        mdfile = "nofile"
        if not os.path.isfile(tmpfile):
            print("file does not exist:", tmpfile)
            continue
        file_extension = pathlib.Path(tmpfile).suffix
        if file_extension == ".json":
            tmpdict['group'] = subdict['displayName']
            tmpdict['expanded'] = False
            tmpdict['pages'] = []
            strforlist += f' - {displayName}'
            if level>0: strlist.append(strforlist)
            gen_sub_dict(tmpfile, tmpdict, mydir, mysubdir,level+1,strlist)
        else:
            tmpdict['label'] = subdict['displayName']
            tmpdict['page'] = mysubdir+"/"+subdict['location']
            strforlist += f' - [{displayName}]({location})'
            if level>0: strlist.append(strforlist)
        if level==0:
            mdfile = gen_md_file('\n'.join(strlist),location,mydir,subdict['displayName'])
            tmpdict['page'] = mysubdir+"/"+mdfile
            strlist=[]
        getmdxdtr(subdict['displayName'],mdfile,subdict['description'], tmpstrlist)
        mydict['pages'].append(tmpdict)
    return tmpstrlist


def getmdxdtr(header,tofile,description, mystr):
    r="{"
    l="}"
    nl='\n'
    mydict={1:"launchFastIcon",2:"icon1",3:"icon3"}
    myicon = mydict[random.randint(1,3)]
    mystr.append(f'    <WideTile header="{header}" to="{tofile}" icon={r}{myicon}{l}>{nl}')
    mystr.append(f'          {description}{nl}')
    mystr.append(f'    </WideTile>{nl}')


def gen_md_file(mdstr,mydir,mydest,h2):
    file_name = mydir.split("/")[0] + ".md"
    file_path = mydest + "/"+ file_name
    mdstr = '# Tutorials\n\n## ' + h2 + "\n" + mdstr
    fileh = open(file_path,"w+")
    fileh.write(mdstr)
    fileh.close()
    return file_name


def get_yaml_data(myyaml):
    with open(myyaml) as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as exception:
            print(exception)
    return data


def update_yaml_file(tut_dict, yaml_file):
    data = get_yaml_data(yaml_file)
    for i in range(len(data['contents'])):
        mydict = data['contents'][i]
        if 'group' in mydict:
            if mydict['group'] == 'Tutorials':
                data['contents'][i] = tut_dict
                break
    with open(yaml_file, 'w') as file:
        yaml.dump(data, file)


def update_mdx_file(mdxlines, mdxfile):
    file1 = open(mdxfile, "r+")
    newlines = []
    inside = False
    for item in file1.readlines():
        if re.search('^\s*<FlexSection', item):
            inside = True
            newlines.append(item)
            continue

        if re.search('^\s*</FlexSection', item):
            inside = False
            newlines.extend(mdxlines)
            newlines.append(item)
            continue

        if inside:
            continue

        newlines.append(item)
    file1.close()
    file2 = open(mdxfile, "w")
    file2.writelines(newlines)
    file2.close()


if __name__ == "__main__":
    """
    Building MD files and MDX files
    and update sidebar.yaml
    """
    build_redocly()