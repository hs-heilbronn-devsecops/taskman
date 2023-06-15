# -*- coding: utf-8 -*-
from os import getenv
from typing import List

from redis import Redis
from taskman import Task, TaskRequest
from .backend import Backend


class RedisBackend(Backend):
    def __init__(
            self,
            redis=Redis(host=getenv('REDIS_HOST', 'localhost'),
                        port=6379, decode_responses=True)
    ) -> None:
        self.redis = redis

    def keys(self) -> List[str]:
        return self.redis.keys()

    def get(self, task_id: str) -> Task:
        task = self.redis.json().get(f'tasks:{task_id}')
        return Task(
            id=task_id,
            name=task['name'],
            description=task['description'],
        )

    def set(self, task_id: str, request: TaskRequest):
        self.redis.json().set(f'tasks:{task_id}', '$', {
            'name': request.name,
            'description': request.description,
        })
