def section1():
    import azure.functions as func
    import dtlpy as dl
    import os

    os.environ["DATALOOP_PATH"] = "/tmp"
    dataset_id = os.environ.get('DATASET_ID')
    dtlpy_username = os.environ.get('DTLPY_USERNAME')
    dtlpy_password = os.environ.get('DTLPY_PASSWORD')


    def main(myblob: func.InputStream):
        dl.login_m2m(email=dtlpy_username, password=dtlpy_password)
        dataset = dl.datasets.get(dataset_id=dataset_id,
                                  fetch=False  # to avoid GET the dataset each time
                                  )

        # remove th Container name from the path
        path_parser = myblob.name.split('/')
        file_name = '/'.join(path_parser[1:])

        file_name = 'external://' + file_name
        dataset.items.upload(local_path=file_name)
