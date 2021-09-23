import dtlpy as dl
import json

pipelines_json_file = ''
with open(pipelines_json_file, 'r') as f:
    pipeline_json = json.load(f)

pipeline = dl.pipelines.create(pipeline_json=pipeline_json)

composition = pipeline.install()
