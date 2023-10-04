# Deploy FaaS Using a Private GitHub Repository

## Configure Integrations for Authentication
Get the project and set up integrations for the username and password.
For the password, you’ll need to create an access token to serve as the password value.
Read [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to see how to create a fine-grained personal access token.


```python
project = dl.projects.get(project_id="project_id")
username_int = project.integrations.create(
    integrations_type=dl.IntegrationType.KEY_VALUE,
    name="username",
    options={"key": "username", "value": "github_username"},
)

password_int = project.integrations.create(
    integrations_type=dl.IntegrationType.KEY_VALUE,
    name="password",
    options={"key": "password", "value": "github_password"},
)

```


## Define the Package Module of Your FaaS
Define the required package module. This module serves as a description and structure of your codebase.

```python
module = [
    dl.PackageModule(
        class_name="ServiceRunner",
        entry_point="main.py",
        functions=[
            dl.PackageFunction(
                function_name="run",
                inputs=[dl.FunctionIO(name="item", type=dl.PackageInputType.ITEM)],
                outputs=[dl.FunctionIO(name="item", type=dl.PackageInputType.ITEM)],
            )
        ],
    )
]
```

## Push the Package with Credentials
Now, package your module and credentials together and push them to your project.
This ensures secure access to your private GitHub repository.

```python
package = project.packages.push(
    package_name="privategit",
    modules=module,
    codebase=dl.GitCodebase(
        git_url="git_url",
        git_tag="main",
        credentials={
            "username": {"key": "username", "id": username_int.id},
            "password": {"key": "password", "id": password_int.id},
        },
    ),
)
```

## Deploy the FaaS service
Finally, deploy your FaaS service using the package and module you've created.

```python
service = project.services.deploy(
    service_name="privategit", package=package, module_name=module[0].name
)
```

