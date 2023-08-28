def func1():
    service = package.deploy(service_name='my-service',
                             runtime=dl.KubernetesRuntime(
                                 runner_image='docker.io/python:3.8'
                             ))


def func2():
    service = dl.services.get('service-id-or-name')
    service.runtime.runner_image = 'python:3.8'
    service.update()


def func3():
    import base64
    import json
    # Credentials
    username = '<dokcer hub user name>'
    password = '<docker hub password>'
    mail = '<email>'

    # Create auth token
    auth_decoded = username + ":" + password
    auth_decoded_bytes = auth_decoded.encode('ascii')
    base64_auth_message_bytes = base64.b64encode(auth_decoded_bytes)
    base64_auth_message = base64_auth_message_bytes.decode('ascii')

    cred_payload = {
        "auths": {
            "docker.io": {
                "username": username,
                "password": password,
                "email": mail,
                "auth": base64_auth_message
            }
        }
    }
    encoded_cred = base64.b64encode(json.dumps(cred_payload).encode()).decode()
    print(encoded_cred)


def func4():
    org = dl.organizations.get(organization_name='<my organization name>')
    secret = org.integrations.create(integrations_type='private-registry',
                                     name='<my dockerhub secret>',
                                     options={"name": "_json_key",
                                              "spec": {"password": encoded_cred}})


