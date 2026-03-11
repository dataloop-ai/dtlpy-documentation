import os
import dtlpy as dl

project_name = "insert your project name"

project = dl.projects.get(project_name=project_name)

script_dir = os.path.dirname(os.path.abspath(__file__))
dpk = project.dpks.publish(
    manifest_filepath=os.path.join(script_dir, 'dataloop.json'),
    local_path=script_dir
)
app = project.apps.install(dpk=dpk)

service = project.services.get(service_name='package-git')
