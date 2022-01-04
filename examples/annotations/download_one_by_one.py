import dtlpy as dl
import traceback
import tqdm
import os
from concurrent.futures import ThreadPoolExecutor


def example(dataset_id, root_path):
    def download_single(w_item: dl.Item):
        try:
            annotation_path = os.path.join(root_path, w_item.dir[1:])
            if not os.path.isdir(annotation_path):
                os.makedirs(annotation_path)
            w_item.annotations.download(annotation_format=dl.VIEW_ANNOTATION_OPTIONS_JSON,
                                        filepath=annotation_path)
        except Exception:
            print(traceback.format_exc())
        finally:
            pbar.update()

    # This will download dataset annotation one by one, with relative path to the item's path
    if dl.token_expired():
        dl.login()
    dataset = dl.datasets.get(dataset_id=dataset_id)
    pages = dataset.items.list()
    pbar = tqdm.tqdm(total=pages.items_count)
    pool = ThreadPoolExecutor(max_workers=32)
    for page in pages:
        for item in page:
            pool.submit(download_single, w_item=item)
    pool.shutdown()


if __name__ == "__main__":
    dataset_id = "datasetId"
    root_path = '/local/download/path'
    example(dataset_id, root_path)
