from pathlib import Path
import requests
import re


def check_links():
    p = Path('./tutorials').glob('**/*.md')
    files = [x for x in p if x.is_file()]
    p = Path('./onboarding').glob('**/*.md')
    files.extend([x for x in p if x.is_file()])
    print(f'Found {len(files)} md files to check... ')
    for file in files:
        with open(file, 'r', encoding='UTF-8') as f:
            string = f.read()
        # res = re.findall(r'(https?://[^\s"]+)', string)
        res = re.findall(r'(https?://[a-zA-Z0-9./\-_#]+)', string)
        if res is not None:
            for url in res:
                if 'local.dataloop.ai' in url:
                    continue
                try:
                    resp = requests.get(url, timeout=3)
                    if not resp.ok:
                        print(f'    BROKEN: {url}, in {file}')
                        # assert False
                except requests.exceptions.HTTPError:
                    print(f'    BROKEN: {url}, in {file}: HTTPError')
                except requests.exceptions.ConnectionError as errc:
                    print(f'    BROKEN: {url}, in {file}: ConnectionError')
                except requests.exceptions.Timeout:
                    print(f'    BROKEN: {url}, in {file}: Timeout')
                except requests.exceptions.RequestException:
                    print(f'    BROKEN: {url}, in {file}: RequestException')


def check_dtlpy_links():
    p = Path('./dtlpy/dtlpy').glob('**/*.py')
    files = [x for x in p if x.is_file()]
    print(f'Found {len(files)} md files to check... ')
    for file in files:
        with open(file, 'r', encoding='UTF-8') as f:
            string = f.read()
        # res = re.findall(r'(https?://[^\s"]+)', string)
        res = re.findall(r'(https?://[a-zA-Z0-9./\-_#]+)', string)
        if res is not None:
            for url in res:
                if 'local.dataloop.ai' in url or 'gate.dataloop.ai':
                    continue
                try:
                    resp = requests.get(url, timeout=3)
                    if not resp.ok:
                        print(f'    BROKEN: {url}, in {file}')
                        # assert False
                except requests.exceptions.HTTPError:
                    print(f'    BROKEN: {url}, in {file}: HTTPError')
                except requests.exceptions.ConnectionError as errc:
                    print(f'    BROKEN: {url}, in {file}: ConnectionError')
                except requests.exceptions.Timeout:
                    print(f'    BROKEN: {url}, in {file}: Timeout')
                except requests.exceptions.RequestException:
                    print(f'    BROKEN: {url}, in {file}: RequestException')


if __name__ == "__main__":
    """
    Go over all the links in the xamples and tutorials and verify they are not broken
    """
    check_links()
    # check_dtlpy_links()
