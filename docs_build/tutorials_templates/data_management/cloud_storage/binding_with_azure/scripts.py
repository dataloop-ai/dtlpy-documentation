def section1():
    import azure.functions as func
    import dtlpy as dl
    import os
    os.environ["DATALOOP_PATH"] = "/tmp"
    dataset_id = os.environ.get('DATASET_ID')
    dtlpy_username = os.environ.get('DTLPY_USERNAME')
    dtlpy_password = os.environ.get('DTLPY_PASSWORD')
    container_name = os.environ.get('CONTAINER_NAME')

    def main(event: func.EventGridEvent):
        url = event.get_json()['url']
        if container_name in url:
            dl.login_m2m(email=dtlpy_username, password=dtlpy_password)
            dataset = dl.datasets.get(dataset_id=dataset_id,
                                      fetch=False  # to avoid GET the dataset each time
                                      )
            # remove th Container name from the path
            file_name = url.split(container_name)[1]
            if 'BlobCreated' in event.event_type:
                file_name = 'external:/' + file_name
                dataset.items.upload(local_path=file_name)
            else:
                dataset.items.delete(filename=file_name)


def section2():
    import dtlpy as dl
    dl.login()
    project = dl.projects.get(project_name='project name')
    bot = project.bots.create(name='serviceAccount', return_credentials=True)
    print('username: ', bot.id)
    print('password: ', bot.password)
