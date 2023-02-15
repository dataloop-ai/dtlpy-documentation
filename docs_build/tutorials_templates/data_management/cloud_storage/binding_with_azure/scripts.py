def section1():
    import azure.functions as func
    import os

    os.environ["DATALOOP_PATH"] = "/tmp"

    import dtlpy as dl

    dataset_id = os.environ.get('DATASET_ID')
    dtlpy_username = os.environ.get('DTLPY_USERNAME')
    dtlpy_password = os.environ.get('DTLPY_PASSWORD')
    container_name = os.environ.get('CONTAINER_NAME')

    def main(event: func.EventGridEvent):
        url = event.get_json()['url']
        if container_name in url:
            dl.login_m2m(email=dtlpy_username, password=dtlpy_password)
            dataset = dl.datasets.get(dataset_id=dataset_id)
            driver_path = dl.drivers.get(driver_id=dataset.driver).path
            # remove th Container name from the path
            file_name_to_upload = url.split(container_name)[1]
            if driver_path == '/':
                driver_path = None
            if driver_path is not None and driver_path not in url:
                return
            if driver_path:
                if not driver_path.startswith("/"):
                    driver_path = "/" + driver_path
                remote_path = file_name_to_upload.replace(driver_path, '')
            else:
                remote_path = file_name_to_upload
            if 'BlobCreated' in event.event_type:
                file_name = 'external:/' + file_name_to_upload
                dataset.items.upload(local_path=file_name, remote_path=os.path.dirname(remote_path))
            else:
                dataset.items.delete(filename=remote_path)


def section2():
    import dtlpy as dl
    dl.login()
    project = dl.projects.get(project_name='project name')
    bot = project.bots.create(name='serviceAccount', return_credentials=True)
    print('username: ', bot.id)
    print('password: ', bot.password)
