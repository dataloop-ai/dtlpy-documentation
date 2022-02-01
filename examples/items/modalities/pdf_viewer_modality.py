import dtlpy as dl


def example(project_name, dataset_name, local_image_filepath, local_pdf_filepath):
    # Preparation: get project & dataset
    project = dl.projects.get(project_name=project_name)
    dataset = project.datasets.get(dataset_name=dataset_name)

    # upload and claim item (image)
    item = dataset.items.upload(local_path=local_image_filepath)
    # or get item (image)
    item = dl.items.get(item_id=item.id)

    # upload and claim a PDF item
    item_pdf = dataset.items.upload(local_path=local_pdf_filepath)
    # or get a PDF item
    item_pdf = dataset.items.get(item_id=item_pdf.id)

    # create modality
    item.modalities.create(
        name="pdf-modality",
        ref_type=dl.MODALITY_REF_TYPE_ID,  # or dl.MODALITY_REF_TYPE_URL
        modality_type=dl.ModalityTypeEnum.PREVIEW,
        ref=item_pdf.id,  # or a link "http://www.africau.edu/images/default/sample.pdf"
        mimetype="application/pdf",
    )

    # Update item to apply changes to platform
    item.update(True)


def preparation():
    project_name = "My Project"
    dataset_name = "My Dataset"
    local_image_filepath = "assets/images/hamster.jpg"
    local_pdf_filepath = "assets/images/lorem-ipsum.pdf"
    return project_name, dataset_name, local_image_filepath, local_pdf_filepath


if __name__ == "__main__":
    project_name, dataset_name, local_image_filepath, local_pdf_filepath = preparation()
    example(project_name=project_name,
            dataset_name=dataset_name,
            local_image_filepath=local_image_filepath,
            local_pdf_filepath=local_pdf_filepath)
