# Deploy FaaS Using a Private GitHub Repository

## Configure Integrations for Authentication

Get the required project and set up integrations for username and password.
To locate the username, refer to your GitHub URL:

```
https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

For the password, an access token is required to serve as authentication credentials.
Detailed instructions on generating a fine-grained personal access token can be
found [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

To grant read-only access to your repository, assign read only permissions to the repository “Contents”.
![alt text](../../../assets/images/faas/github.png)

```python
import dtlpy as dl

project = dl.projects.get(project_id="project_id")
username_integration = project.integrations.create(
    integrations_type=dl.IntegrationType.KEY_VALUE,
    name="username",
    options={"key": "username", "value": "<github_username>"},
)

password_integration = project.integrations.create(
    integrations_type=dl.IntegrationType.KEY_VALUE,
    name="password",
    options={"key": "password", "value": "<github_password>"},
)

print(f"Username integration id: {username_integration.id}")
print(f"Password integration id: {password_integration.id}")
```

## Update the DPKS Manifest

Copy the integration ID values to the Codebase object in the DPK manifest:

```json
  {
    "name": "private-git-dpk",
    "scope": "project",
    "codebase": {
        "type": "git",
        "gitUrl": "private-git-url",
        "gitTag": "main",
        "credentials": {
            "username": {
                "key": "username",
                "id": "<username integration id>"
            },
            "password": {
                "key": "password",
                "id": "<password integration id>"
            }
        }
    },
    "components": {}
}
```

Now you can publish the:

```python
dpk = project.dpks.publish()
```

