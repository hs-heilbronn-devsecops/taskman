from typing import Dict, List

from .backend import Backend
from .. import TaskRequest, Task


class MemoryBackend(Backend):

    def __init__(self):
        self.tasks: Dict[str, Task] = {}

    def keys(self) -> List[str]:
        return self.tasks.keys()

    def get(self, task_id: str) -> Task:
        return self.tasks[task_id]

    def set(self, task_id: str, request: TaskRequest):
        self.tasks[task_id] = Task(
            id=task_id,
            name=request.name,
            description=request.description
        )
