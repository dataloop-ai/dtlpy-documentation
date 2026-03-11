import dtlpy as dl
import time

# Set project name and service name
service_name = 'custom-python'
project_name = 'My Project'

project = dl.projects.get(project_name=project_name)


# This is the function that we're going to run
def get_version():
    import sys
    print("Python version")
    print(sys.version)
    return sys.version


# Deploying the service
service = dl.Service.from_function(
    func=get_version,
    name=service_name,
    project=project,
    client_api=dl.client_api,
    runtime={"runnerImage": "python:3.9.7"}
)

# Executing the function - this should print the function output with the python version
execution = service.execute(function_name='get_version',
                            project_id=project.id)

time.sleep(10)  # maybe need to wait more. if empty - run next 3 lines again
execution = service.executions.get(execution_id=execution.id)
print(execution.latest_status)
print(execution.output)
