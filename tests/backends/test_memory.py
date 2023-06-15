from fakeredis import FakeStrictRedis

from taskman.model import TaskRequest, Task
from taskman.backends import MemoryBackend, RedisBackend
from taskman.main import create_task, get_task, get_tasks


def test_save_and_get_item():
    backend = MemoryBackend()
    id = 'test12345'
    backend.set(id, TaskRequest(
        name='Test Task',
        description='Demo',
    ))
    assert backend.get(id) == Task(name='Test Task', description='Demo', id=id)


def test_save_and_get_items():
    backend = MemoryBackend()

    backend.set('test12345', TaskRequest(
        name='Test Task',
        description='Demo',
    ))
    backend.set('test67890',TaskRequest(
        name='Test Task 2',
        description='Demo 2',
    ))
    keys = backend.keys()
    assert len(keys) == 2
