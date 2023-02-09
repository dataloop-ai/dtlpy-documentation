import string
import json
import re

with open('docs_build/glossary/glossary.json', 'r', encoding='utf8') as f:
    definitions = json.load(f)

def create():
    md_string = "# Glossary\n"
    md_string += "\n"
    letters = list(string.ascii_uppercase)
    headers = [f"[{letter.upper()}](#{letter.lower()})" for letter in letters]
    md_string += " | ".join(headers)
    md_string += "\n"
    md_string += "\n"
    sorted_definitions = sorted(definitions, key=lambda d: d['header'].lower())
    for letter in letters:
        letter_definitions = [definition for definition in sorted_definitions if
                              definition["header"].lower().startswith(letter.lower())]
        md_string += f"## {letter.upper()}\n"
        for definition in letter_definitions:
            header = definition['header']
            description = definition['description']

            ###
            # replace $ with the current link
            # header = "this is a $[test] with two $[dollars]"
            grps = re.finditer(r"\$\[([A-Za-z0-9_]+)\]", header)
            for grp in grps:
                txt = grp.group(1)
                header = header.replace(grp.group(), f'[{txt}](#{txt.lower()})')

            grps = re.finditer(r"\$\[([A-Za-z0-9_]+)\]", description)
            for grp in grps:
                txt = grp.group(1)
                description = description.replace(grp.group(), f'[{txt}](#{txt.lower()})')

            ###
            # set header name for the linking
            if header.find('(') == -1:
                tag_name = header
            else:
                tag_name = header[:(header.find('('))]
            tag_name = tag_name.strip().lower().replace(' ', '-')
            header = f'<a name="{tag_name}"></a>{header}'

            ###
            # add to the md strings
            md_string += f"### {header}\n"
            md_string += f"{description}\n"

    with open('docs_build/glossary/glossary.md', 'w', encoding='utf8') as f:
        f.write(md_string)


if __name__ == "__main__":
    create()
