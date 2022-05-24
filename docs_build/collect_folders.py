import pathspec
import os


def add_file(d, v):
    if len(v) == 1:
        d.append(v[0])
    elif len(v) == 2:
        if v[0] not in d:
            d[v[0]] = list()
        add_file(d[v[0]], v[1:])
    else:
        if v[0] not in d:
            d[v[0]] = dict()
        add_file(d[v[0]], v[1:])


def add_examples_line(md_lines, content, root, level):
    if isinstance(content, dict):
        for dirname, files in content.items():
            caption = dirname.replace("_", " ").capitalize()
            md_lines.append('  ' * level + f'* {caption}')
            add_examples_line(md_lines=md_lines,
                              content=content[dirname],
                              level=level + 1,
                              root=f'{root}/{dirname}')
    elif isinstance(content, list):
        for file in content:
            filename, ext = os.path.splitext(file)
            caption = filename.replace("_", " ").capitalize()
            filepath = f'{root}/{file}'
            md_lines.append('  ' * level + f'*  [{caption}]({filepath})')
    else:
        raise ValueError()


def add_tutorial_line(md_lines, content, root, level):
    """
    For tutorials, the file is always "chapter" so need to add the folder as the name and link the chapter.ipynb file

    """
    if isinstance(content, dict):
        for dirname, files in content.items():
            if isinstance(files, list):
                # v is the list of chapter files
                for file in files:
                    caption = dirname.replace("_", " ").capitalize()
                    filepath = f'{root}/{dirname}/{file}'
                    md_lines.append('  ' * level + f'*  [{caption}]({filepath})')
            else:
                caption = dirname.replace("_", " ").capitalize()
                md_lines.append('  ' * level + f'* {caption}')
                add_tutorial_line(md_lines=md_lines,
                                  content=content[dirname],
                                  level=level + 1,
                                  root=f'{root}/{dirname}')
    else:
        raise ValueError()


def collect_examples(root, git_spec):
    content = dict()
    for path, subdirs, files in os.walk(root):
        for filename in files:
            filepath = os.path.join(path, filename)
            if git_spec.match_file(filepath):
                # file in gitignore
                continue
            name, ext = os.path.splitext(filename)
            if ext not in ['.py', '.ipynb']:
                continue
            hierarchy = filepath.split(os.sep)[1:]
            print(f'Adding to {root}: {filepath}')
            add_file(content, hierarchy)
    md_lines = list()
    add_examples_line(md_lines=md_lines,
                      content=content,
                      level=0,
                      root=root)

    return md_lines


def collect_tutorials(root, git_spec):
    content = dict()
    for path, subdirs, files in os.walk(root):
        for filename in files:
            filepath = os.path.join(path, filename)
            if git_spec.match_file(filepath):
                # file in gitignore
                continue
            name, ext = os.path.splitext(filename)
            if ext not in ['.py', '.ipynb']:
                continue
            hierarchy = filepath.split(os.sep)[1:]
            print(f'Adding to {root}: {filepath}')
            add_file(content, hierarchy)
    md_lines = list()
    add_tutorial_line(md_lines=md_lines,
                      content=content,
                      level=0,
                      root=root)
    return md_lines


def main():
    with open('.gitignore', 'r') as f:
        spec_src = f.read()
    ignore_lines = spec_src.splitlines() + ['.git', '.dataloop']
    git_spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, ignore_lines)

    example_lines = collect_examples(root='examples', git_spec=git_spec)
    tutorial_lines = collect_tutorials(root='tutorials', git_spec=git_spec)

    with open(os.path.join('docs_build', 'readme_template.md'), 'r') as f:
        template_lines = f.readlines()

    new_lines = list()
    for line in template_lines:
        if line.startswith('$'):
            if 'tutorials' in line:
                md_lines = [f'{line}\n' for line in tutorial_lines]
                new_lines.extend(md_lines)
            elif 'examples' in line:
                md_lines = [f'{line}\n' for line in example_lines]
                new_lines.extend(md_lines)
            else:
                raise ValueError(f'unknown lines header: {line}')
        else:
            new_lines.append(line)
    with open('README.md', 'w') as f:
        f.writelines(new_lines)
    print('Done! Writing new README.md file')


if __name__ == "__main__":
    """
    Build the examples and tutorials directories into the README.md file.
    
    Run: 
    Need to run this file from the root folder:
    python docs_build/collect_folders.py
     
    """
    main()
