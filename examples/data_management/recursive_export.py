"""
Recursive Export

For large datasets, you may want to export a dataset recursively.
This example demonstrates how to recursively export a dataset.
"""

import concurrent.futures
import nest_asyncio
import logging
import asyncio
import json
import tqdm
import time
import os

import dtlpy as dl
import numpy as np

from bson import ObjectId
from pathlib import Path
from enum import Enum

from dtlpyconverters.coco import DataloopToCoco

nest_asyncio.apply()

logger = logging.getLogger('ExportBase')
logging.basicConfig(level=logging.INFO)


class ExportStatus(Enum):
    SUCCESS = "success"
    IN_PROGRESS = "in_progress"
    ERROR = "error"


class RecursiveExport:
    def __init__(self, dataset):
        """
        Initialize the RecursiveExport class.
        :param dataset: The dataset to export
        """
        self.dataset = dataset
        self.command_ids = []
        self.progress = 0
        self.output_item_ids = []
        self.export_files = []
        self.status = ExportStatus.IN_PROGRESS

    def recursive_export(
        self, from_id=None, to_id=None, from_operator='gte', to_operator='lte', depth=0, max_depth=10, max_items=100000
    ):
        """
        Recursive export of the dataset.
        :param from_id: The id of the first item to export
        :param to_id: The id of the last item to export
        :param from_operator: The operator to use for the from_id
        :param to_operator: The operator to use for the to_id
        :param depth: The current depth of the recursion
        :param max_depth: The maximum depth of the recursion
        :param max_items: The maximum number of items to export
        :return: None
        """
        if depth > max_depth:
            logger.error(f"Max depth reached: {max_depth}")
            payload = {
                'itemsQuery': {"filter": {"$and": [{"hidden": False}, {"type": "file"}]}},
                'includeItemVectors': False,
                # "itemsVectorQuery": {'select': {"datasetId": 1, 'featureSetId': 1, 'value': 1}},
                'exportType': 'json',
            }

            payload['itemsQuery']['filter']['$and'].append({"id": {f"${from_operator}": from_id}})
            payload['itemsQuery']['filter']['$and'].append({"id": {f"${to_operator}": to_id}})
            _id = self._start_export(payload)
            self.command_ids.append(_id)
            return
        if from_id is None:
            from_id = self._get_first_last_item(loc='first')
        if to_id is None:
            to_id = self._get_first_last_item(loc='last')

        filters = dl.Filters()
        filters.add(field="id", values=from_id, method=dl.FILTERS_METHOD_AND, operator=from_operator)
        filters.add(field='id', values=to_id, method=dl.FILTERS_METHOD_AND, operator=to_operator)
        filters.page_size = 0
        pages = self.dataset.items.list(filters=filters)

        if pages.items_count > max_items:
            from_id = self._get_first_last_item(filters=filters, loc='first')
            to_id = self._get_first_last_item(filters=filters, loc='last')
            mid_id = self._get_middle_id(from_id, to_id)
            self.recursive_export(
                from_id=from_id,
                to_id=mid_id,
                from_operator='gte',
                to_operator='lte',
                depth=depth + 1,
                max_items=max_items,
            )
            self.recursive_export(
                from_id=mid_id, to_id=to_id, from_operator='gt', to_operator='lte', depth=depth + 1, max_items=max_items
            )
        elif pages.items_count > 0:
            payload = {
                'itemsQuery': {"filter": {"$and": [{"hidden": False}, {"type": "file"}]}},
                'includeItemVectors': False,
                # "itemsVectorQuery": {'select': {"datasetId": 1, 'featureSetId': 1, 'value': 1}},
                'exportType': 'json',
            }

            payload['itemsQuery']['filter']['$and'].append({"id": {f"${from_operator}": from_id}})
            payload['itemsQuery']['filter']['$and'].append({"id": {f"${to_operator}": to_id}})
            _id = self._start_export(payload)
            self.command_ids.append(_id)
        else:
            # items_count = 0
            ...

    def _get_first_last_item(self, filters=None, loc='first') -> str:
        """
        Get the first or last item id in the dataset.
        :param filters: Filters to apply when getting the item
        :param loc: The location of the item to get. Can be 'first' or 'last'
        :return: The id of the item
        :raises AssertionError: If loc is not 'first' or 'last'
        """
        if filters is None:
            filters = dl.Filters()
        if loc == "first":
            filters.sort_by(field='id', value=dl.FILTERS_ORDERBY_DIRECTION_ASCENDING)
        elif loc == "last":
            filters.sort_by(field='id', value=dl.FILTERS_ORDERBY_DIRECTION_DESCENDING)
        else:
            assert False
        filters.page_size = 1
        pages = self.dataset.items.list(filters=filters)
        return pages.items[0].id

    def _start_export(self, payload):
        _, response = dl.client_api.gen_request(
            req_type='post', path=f'/datasets/{self.dataset.id}/export', json_req=payload
        )
        json_string = response.content.decode('utf-8')
        return json.loads(json_string)['id']

    @staticmethod
    def _get_middle_id(from_id, to_id):
        """
        Calculate the middle ObjectId between two given ObjectIds.
        :param from_id: The starting ObjectId as a string
        :param to_id: The ending ObjectId as a string
        :return: The middle ObjectId as a string
        """

        from_time = ObjectId(from_id).generation_time
        to_time = ObjectId(to_id).generation_time
        midpoint = from_time + (to_time - from_time) / 2
        # Convert to ObjectId
        return str(ObjectId.from_datetime(midpoint))

    def download_item_data(self, item_id):
        """
        Downloads item data and saves it as JSON.
        :param item_id: The ID of the item to be downloaded
        :return: The filepath where the item data was saved
        :raises Exception: If there is an error during the download or saving process
        """
        item = dl.items.get(item_id=item_id)
        filepath = os.path.join("tmp", self.dataset.name, f"{item_id}.json")
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        filepath = item.download(local_path=filepath, save_locally=True)
        return filepath

    def wait_and_process_data(self):
        """
        Waits for commands to finish processing and handles the export completion.
        This method monitors the progress of export commands and handles any exceptions
        that occur during the waiting period. It updates the status and progress of
        the export operation.
        :raises TimeoutError: If the command execution exceeds the timeout period
        :raises PlatformException: If a command fails or required data is missing
        :raises Exception: If any other error occurs while waiting for commands to finish
        """

        try:
            logger.info(f"Waiting for command {self.command_ids} to finish")

            timeout = 60 * 60 * 2
            max_sleep_time = 10
            backoff_factor = 1
            elapsed = 0
            start = time.time()
            if timeout is None or timeout <= 0:
                timeout = np.inf

            command = None
            num_tries = 1

            while elapsed < timeout:
                continue_loop = False
                progress = 0
                for command_id in self.command_ids:
                    command = dl.commands.get(command_id=command_id)
                    progress += command.progress
                    if command.in_progress():
                        continue_loop = True
                self.progress = (progress / len(self.command_ids)) // 2
                logger.info(f"Progress: {self.progress}")

                if not continue_loop:
                    break

                elapsed = time.time() - start
                sleep_time = np.min([timeout - elapsed, backoff_factor * (2**num_tries), max_sleep_time])
                num_tries += 1

                logger.debug(
                    f"Command {command.id} is running for {elapsed:.2f}[s] and now Going to sleep {sleep_time:.2f}[s]"
                )
                time.sleep(sleep_time)

            if elapsed >= timeout:
                raise TimeoutError(
                    f"command wait() got timeout. id: {command.id!r}, status: {command.status}, progress {command.progress}%"
                )
            for command_id in self.command_ids:
                command = dl.commands.get(command_id=command_id)
                if command.status != dl.CommandsStatus.SUCCESS:
                    raise dl.exceptions.PlatformException(
                        error='424', message=f"Command {command.id!r} {command.status}: '{command.error}'"
                    )
                if 'outputItemId' not in command.spec:
                    raise dl.exceptions.PlatformException(
                        error='400', message=f"outputItemId key is missing in command id: {command_id}"
                    )
                self.output_item_ids.append(command.spec['outputItemId'])
        except Exception as e:
            logger.error(f"Error while waiting for command {self.command_ids}: {e}")
            self.status = ExportStatus.ERROR
            raise e

    def get_and_process_data(self, **kwargs):
        """
        Downloads data for the items specified in output_item_ids using a thread pool executor.
        :param kwargs: Additional keyword arguments
        """
        self.export_files = []
        self.status = ExportStatus.IN_PROGRESS
        self.progress = 50

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(self.download_item_data, self.output_item_ids)
            for result in results:
                self.export_files.append(result)

        self.status = ExportStatus.SUCCESS
        self.progress = 100


class CocoConverter(DataloopToCoco):
    async def on_dataset(self, **kwargs):
        """
        Callback to tun the conversion on a dataset.
        Will be called after on_dataset_start and before on_dataset_end.
        """
        kwargs = await self.on_dataset_start(**kwargs)
        if self.download_annotations:
            self.dataset.download_annotations(local_path=self.input_annotations_path, filters=self.filters)
            json_path = Path(self.input_annotations_path).joinpath('json')
        else:
            json_path = Path(self.input_annotations_path)
        if self.download_items:
            self.dataset.items.download(local_path=self.output_items_path)

        files = list(json_path.rglob('*.json'))
        self.categories = {
            cat['name']: cat
            for cat in self.gen_coco_categories(self.dataset.instance_map, self.dataset.recipes.list()[0])
        }
        self.pbar = tqdm.tqdm(total=len(files))
        futures = list()
        for annotation_json_filepath in files:
            with open(annotation_json_filepath, 'r') as f:
                data = json.load(f)
            if isinstance(data, list):
                for item_data in data:
                    json_annotations = item_data.pop('annotations')
                    item = dl.Item.from_json(_json=item_data, client_api=dl.client_api, dataset=self.dataset)
                    annotations = dl.AnnotationCollection.from_json(_json=json_annotations, item=item)
                    futures.append(
                        asyncio.create_task(self.on_item(item=item, dataset=self.dataset, annotations=annotations))
                    )
            else:
                json_annotations = data.pop('annotations')
                item = dl.Item.from_json(_json=data, client_api=dl.client_api, dataset=self.dataset)
                annotations = dl.AnnotationCollection.from_json(_json=json_annotations, item=item)
                futures.append(
                    asyncio.create_task(self.on_item(item=item, dataset=self.dataset, annotations=annotations))
                )
        await asyncio.gather(*futures)
        kwargs = await self.on_dataset_end(**kwargs)
        return kwargs


if __name__ == "__main__":
    dataset = dl.datasets.get(dataset_id="")
    recursive_export = RecursiveExport(dataset)
    recursive_export.recursive_export()
    recursive_export.wait_and_process_data()
    recursive_export.get_and_process_data()
    # convert to coco
    coco_converter = CocoConverter(
        dataset=dataset,
        output_annotations_path=f"tmp/{dataset.name}/coco",
        input_annotations_path=f"tmp/{dataset.name}",
        download_annotations=False,
        download_items=False,
    )

    asyncio.run(coco_converter.convert_dataset())

    # check data
    with open(f"tmp/{dataset.name}/coco/coco.json", "r") as f:
        data = json.load(f)
    print(f"Number of images: {len(data['images'])}")
    print(f"Number of annotations: {len(data['annotations'])}")
    print(f"Number of categories: {len(data['categories'])}")






