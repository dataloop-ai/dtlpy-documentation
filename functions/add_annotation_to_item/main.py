import dtlpy as dl


class ServiceRunner(dl.BaseServiceRunner):

    @staticmethod
    def add_classification(item: dl.Item):
        """

        """
        # Create a builder
        builder = item.annotations.builder()
        # Add classification to the annotation builder
        builder.add(annotation_definition=dl.Classification(label='from-faas'))
        # Upload annotation to item
        item.annotations.upload(builder)
        return item
