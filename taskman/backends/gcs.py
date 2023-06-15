from json import dump, load
from os import getenv
from typing import List

from google.cloud import storage

from .backend import Backend
from .. import TaskRequest, Task


class GCSBackend(Backend):

    def __init__(self):
        self.storage_client = storage.Client()
        self.bucket = self.storage_client.bucket(self.get_bucket_name())

    def keys(self) -> List[str]:
        blobs = self.storage_client.list_blobs(self.get_bucket_name())
        return map(lambda blob: blob.name, blobs)

    def get(self, task_id: str) -> Task:
        blob = self.bucket.blob(task_id)
        with blob.open("r") as file:
            data = load(file)
            return Task(
                id=task_id,
                name=data["name"],
                description=data["description"],
            )

    def set(self, task_id: str, request: TaskRequest):
        blob = self.bucket.blob(task_id)
        with blob.open("w") as file:
            dump({
                "name": request.name,
                "description": request.description,
            }, file)

    def get_bucket_name(self):
        return getenv('BUCKET')
