# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List
from taskman import Task, TaskRequest


class Backend(ABC):

    @abstractmethod
    def keys(self) -> List[str]:
        pass

    @abstractmethod
    def get(self, task_id: str) -> Task:
        pass

    @abstractmethod
    def set(self, task_id: str, request: TaskRequest):
        pass
