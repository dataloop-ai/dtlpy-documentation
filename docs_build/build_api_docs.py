import requests
import json


def build_api_docs():
    resp = requests.get('https://rc-gate.dataloop.ai/api/v1/collect-docs')
    resp = requests.get('https://rc-gate.dataloop.ai/api/v1/swagger-file')

    if resp.ok is True:
        with open('./resources/rest_api/openapi.json', 'w') as f:
            json.dump(resp.json(), f)
