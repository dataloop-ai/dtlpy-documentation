import dtlpy as dl

project_by_name = dl.projects.get(project_name='My Project')

project_by_id = dl.projects.get(project_id=project_by_name.id)

print(dl.client_api.last_curl)
