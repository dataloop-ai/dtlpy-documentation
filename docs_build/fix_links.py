from pathlib import Path
import requests
import re


p = Path('docs_build').glob('**/mds.py')
files = [x for x in p if x.is_file()]

for file in files:
    print(f'Checking {file}')
    with open(file, 'r', encoding='UTF-8') as f:
        string = f.read()
    # res = re.findall(r'(https?://[^\s"]+)', string)
    res = re.findall(r'(https?://[a-zA-Z0-9./\-_#]+)', string)
    if res is not None:
        for url in res:
            resp = requests.get(url)
            if not resp.ok:
                print(f'    BROKEN: {url}, in {file}')
                # assert False


