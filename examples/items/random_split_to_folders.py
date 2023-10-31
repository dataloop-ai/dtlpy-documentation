import tqdm
import dtlpy as dl
import numpy as np
from concurrent.futures import ThreadPoolExecutor


# Set the train indices
def split_items(items, train_size=0.8):
    n_items = len(items)
    n_train = int(train_size * n_items)
    is_train = np.zeros(n_items, dtype=bool)
    is_train[:n_train] = True
    np.random.shuffle(is_train)
    # Verify the numbers
    print(f'Train set with {np.sum(is_train)} items')

    return is_train


# Define the split function
def single_item(item, is_item_train, pbar):
    try:
        dest_dir = '/train/' if is_item_train else '/validation/'
        item.move(dest_dir + item.name)
    except Exception as e:
        print(e)
    finally:
        pbar.update()


# Main function
def main():
    # Get project and dataset
    project = dl.projects.get(project_name='Ninja Turtles')
    dataset = project.datasets.get(dataset_name='Splinter')

    # Get all items in the dataset
    filters = dl.Filters()
    pages = dataset.items.list(filters=filters)
    items = list(pages.all())

    is_train = split_items(items)

    pbar = tqdm.tqdm(total=len(items))

    with ThreadPoolExecutor(max_workers=32) as pool:
        for i_item, item in enumerate(items):
            pool.submit(single_item, is_item_train=is_train[i_item], item=item, pbar=pbar)


if __name__ == "__main__":
    main()
