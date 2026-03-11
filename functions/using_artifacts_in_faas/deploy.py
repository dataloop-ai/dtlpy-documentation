import os
import dtlpy as dl

project_name = 'COCO ors'

project = dl.projects.get(project_name=project_name)

script_dir = os.path.dirname(os.path.abspath(__file__))
dpk = project.dpks.publish(
    manifest_filepath=os.path.join(script_dir, 'dataloop.json'),
    local_path=script_dir
)
app = project.apps.install(dpk=dpk)

artifact_zip_file = os.path.join(script_dir, '..', '..', 'assets', 'artifacts', 'monkey-612x612.zip')
if os.path.isfile(artifact_zip_file):
    app.artifacts.upload(filepath=artifact_zip_file)

service = project.services.get(service_name='artifacts-package')
