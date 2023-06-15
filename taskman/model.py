# -*- coding: utf-8 -*-
from pydantic import BaseModel


class TaskRequest(BaseModel):
    name: str
    description: str


class Task(TaskRequest):
    id: str
