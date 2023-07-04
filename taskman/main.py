# -*- coding: utf-8 -*-
from uuid import uuid4
from typing import List, Optional
from os import getenv
from typing_extensions import Annotated

from fastapi import Depends, FastAPI
from starlette.responses import RedirectResponse
from .backends import Backend, RedisBackend, MemoryBackend, GCSBackend
from .model import Task, TaskRequest

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter
)


app = FastAPI()
FastAPIInstrumentor.instrument_app(app)

provider = TracerProvider()
provider.add_span_processor(BatchSpanProcessor(CloudTraceSpanExporter()))
provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

trace.set_tracer_provider(provider)

tracer = trace.get_tracer("tracer.taskman.premium")

my_backend: Optional[Backend] = None


def get_backend() -> Backend:
    global my_backend  # pylint: disable=global-statement
    if my_backend is None:
        backend_type = getenv('BACKEND', 'redis')
        if backend_type == 'redis':
            my_backend = RedisBackend()
        elif backend_type == 'gcs':
            my_backend = GCSBackend()
        else:
            my_backend = MemoryBackend()
    return my_backend


@app.get('/')
def redirect_to_tasks() -> None:
    with tracer.start_as_current_span("initial") as span:
        print("Initial")
    
        current_span = trace.get_current_span()
        current_span.set_attribute(SpanAttributes.HTTP_METHOD, "GET")

        return RedirectResponse(url='/tasks')


@app.get('/tasks')
def get_tasks(backend: Annotated[Backend, Depends(get_backend)]) -> List[Task]:
    with tracer.start_as_current_span("GetTasks"):
        keys = backend.keys()
        tasks = []
        for key in keys:
            tasks.append(backend.get(key))
        return tasks


@app.get('/tasks/{task_id}')
def get_task(task_id: str,
             backend: Annotated[Backend, Depends(get_backend)]) -> Task:
    
    with tracer.start_as_current_span("SpecificTask"):
        print("SpecificTask")

        return backend.get(task_id)


@app.put('/tasks/{item_id}')
def update_task(task_id: str,
                request: TaskRequest,
                backend: Annotated[Backend, Depends(get_backend)]) -> None:
    with tracer.start_as_current_span("UpdateTask"):
        print("UpdateTask")
        backend.set(task_id, request)
    


@app.post('/tasks')
def create_task(request: TaskRequest,
                backend: Annotated[Backend, Depends(get_backend)]) -> str:
    with tracer.start_as_current_span("PostTasks"):
        print("PostTasks")
        task_id = str(uuid4())
        backend.set(task_id, request)
        return task_id
