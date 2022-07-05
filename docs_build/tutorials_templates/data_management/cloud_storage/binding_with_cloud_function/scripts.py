def section1():
    import dtlpy as dl

    DATASET_ID = ''
    DTLPY_USERNAME = ''
    DTLPY_PASSWORD = ''

    def create_gcs(event, context):
        """Triggered by a change to a Cloud Storage bucket.
        Args:
             event (dict): Event payload.
             context (google.cloud.functions.Context): Metadata for the event.
        """
        file = event
        dl.login_m2m(email=DTLPY_USERNAME, password=DTLPY_PASSWORD)
        dataset = dl.datasets.get(dataset_id=DATASET_ID,
                                  fetch=False  # to avoid GET the dataset each time
                                  )
        file_name = 'external://' + file['name']
        dataset.items.upload(local_path=file_name)


def section2():
    import dtlpy as dl

    DATASET_ID = ''
    DTLPY_USERNAME = ''
    DTLPY_PASSWORD = ''

    def delete_gcs(event, context):
        """Triggered by a change to a Cloud Storage bucket.
        Args:
             event (dict): Event payload.
             context (google.cloud.functions.Context): Metadata for the event.
        """
        file = event
        dl.login_m2m(email=DTLPY_USERNAME, password=DTLPY_PASSWORD)
        dataset = dl.datasets.get(dataset_id=DATASET_ID,
                                  fetch=False  # to avoid GET the dataset each time
                                  )
        file_name = file['name']
        dataset.items.delete(filename=file_name)
