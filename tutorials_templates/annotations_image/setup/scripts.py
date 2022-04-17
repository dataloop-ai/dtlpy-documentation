def section1():
    import dtlpy as dl
    if dl.token_expired():
        dl.login()
    project = dl.projects.get(project_name='project_name')
    dataset = project.datasets.get(dataset_name='dataset_name')


def section2():
    import matplotlib.pyplot as plt
    plt.figure()
    plt.imshow(builder.show())
    for annotation in builder:
        plt.figure()
        plt.imshow(annotation.show())
        plt.title(annotation.label)
