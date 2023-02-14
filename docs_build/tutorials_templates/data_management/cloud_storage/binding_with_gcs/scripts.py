def section1():
    import dtlpy as dl
    dl.login()
    project = dl.projects.get(project_name='project name')
    bot = project.bots.create(name='serviceAccount', return_credentials=True)
    print('username: ', bot.id)
    print('password: ', bot.password)


def section2():
    import os
    os.environ["DATALOOP_PATH"] = "/tmp"

    import dtlpy as dl

    dataset_id = os.environ.get('DATASET_ID')
    dtlpy_username = os.environ.get('DTLPY_USERNAME')
    dtlpy_password = os.environ.get('DTLPY_PASSWORD')

    def create_gcs(event, context):
        """Triggered by a change to a Cloud Storage bucket.
        Args:
             event (dict): Event payload.
             context (google.cloud.functions.Context): Metadata for the event.
        """
        file = event
        dl.login_m2m(email=dtlpy_username, password=dtlpy_password)
        dataset = dl.datasets.get(dataset_id=dataset_id,
                                  fetch=False  # to avoid GET the dataset each time
                                  )
        file_name = 'external://' + file['name']
        dataset.items.upload(local_path=file_name)


def section3():
    import dtlpy as dl
    import os

    dataset_id = os.environ.get('DATASET_ID')
    dtlpy_username = os.environ.get('DTLPY_USERNAME')
    dtlpy_password = os.environ.get('DTLPY_PASSWORD')

    def delete_gcs(event, context):
        """Triggered by a change to a Cloud Storage bucket.
        Args:
             event (dict): Event payload.
             context (google.cloud.functions.Context): Metadata for the event.
        """
        file = event
        dl.login_m2m(email=dtlpy_username, password=dtlpy_password)
        dataset = dl.datasets.get(dataset_id=dataset_id,
                                  fetch=False  # to avoid GET the dataset each time
                                  )
        file_name = file['name']
        dataset.items.delete(filename=file_name)
