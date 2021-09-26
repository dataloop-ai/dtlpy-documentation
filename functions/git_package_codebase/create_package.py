import dtlpy as dl

project_name = "insert your project name"
package_name = "package-git"  # this will be the name of the created package
git_repo_url = 'https://github.com/dataloop-ai/package_git_example.git'  # clone link of the git repo
git_repo_tag = 'main'  # tag/branch
# get the project that we want to use for the package creation
project = dl.projects.get(project_name=project_name)

# build the module for the package
module = dl.PackageModule(entry_point='main.py',
                          class_name='ServiceRunner',
                          functions=[
                              dl.PackageFunction(name='run',
                                                 inputs=[dl.FunctionIO(type="Item", name="item")],
                                                 description='example function that prints the item.name')
                          ])

package = project.packages.push(package_name=package_name,
                                modules=[module],
                                codebase=dl.GitCodebase(
                                    git_url=git_repo_url,
                                    git_tag=git_repo_tag))

# deploy the service for the first time
service = package.services.deploy(package=package,
                                  runtime=dl.KubernetesRuntime(concurrency=1,
                                                               autoscaler=dl.KubernetesRabbitmqAutoscaler(
                                                                   min_replicas=0,
                                                                   max_replicas=1,
                                                                   queue_length=10))
                                  )
