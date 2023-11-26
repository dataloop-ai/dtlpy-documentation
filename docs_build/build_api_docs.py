import requests
import json

def check():
    with open('./resources/rest_api/openapi.json', 'r') as f:
        data = json.load(f)

    def id_generator(dict_var):
        for k, v in dict_var.items():
            if k == "$ref":
                yield v
            elif isinstance(v, dict):
                for id_val in id_generator(v):
                    yield id_val


    path_refs = set([(lambda x: x.split('/')[-1])(x) for x in id_generator(data)])
    components_refs = set(list(data['components']['schemas'].keys()))
    path_refs.difference(components_refs)
    components_refs.difference(path_refs)


def build_api_docs():
    resp = requests.get('https://rc-gate.dataloop.ai/api/v1/collect-docs')
    resp = requests.get('https://rc-gate.dataloop.ai/api/v1/swagger-file')

    if resp.ok is True:
        with open('./resources/rest_api/openapi.json', 'w') as f:
            json.dump(resp.json(), f)
