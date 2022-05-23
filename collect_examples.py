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

    # return d


def add_line(md_lines, content, root, level):
    if isinstance(content, dict):
        for k, v in content.items():
            md_lines.append('  ' * level + f'* {k.capitalize()}')
            add_line(md_lines=md_lines,
                     content=content[k],
                     level=level + 1,
                     root=f'{root}/{k}')
    elif isinstance(content, list):
        for file in content:
            filename, ext = os.path.splitext(file)
            caption = filename.replace("_", " ").capitalize()
            filepath = f'{root}/{file}'
            md_lines.append('  ' * level + f'*  [{caption}](#{filepath})')
    else:
        raise ValueError()


def main():
    root = 'examples'
    content = dict()
    for path, subdirs, files in os.walk(root):
        for name in files:
            filename, ext = os.path.splitext(name)
            if ext not in ['.py', '.ipynb']:
                continue
            filepath = os.path.join(path, name)
            hierarchy = filepath.split(os.sep)[1:]
            add_file(content, hierarchy)

    # content = sorted(content)
    md_lines = list()
    add_line(md_lines=md_lines,
             content=content,
             level=0,
             root=root)

    with open('readme_template.md', 'r') as f:
        template_lines = f.readlines()

    new_lines = list()
    for line in template_lines:
        if line.startswith('$'):
            md_lines = [f'{line}\n' for line in md_lines]
            new_lines.extend(md_lines)
        else:
            new_lines.append(line)
    with open('README.md', 'w') as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    main()
