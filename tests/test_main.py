from taskman.model import TaskRequest, Task
from taskman.backends import MemoryBackend
from taskman.main import create_task, get_task, get_tasks


def test_save_and_get_item():
    backend = MemoryBackend()
    id = create_task(TaskRequest(
        name='Test Task',
        description='Demo',
    ), backend)
    assert get_task(id, backend) == Task(name='Test Task', description='Demo', id=id)


def test_save_and_get_items():
    backend = MemoryBackend()
    create_task(TaskRequest(
        name='Test Task',
        description='Demo',
    ), backend)
    create_task(TaskRequest(
        name='Test Task 2',
        description='Demo 2',
    ), backend)
    tasks = get_tasks(backend)
    assert len(tasks) == 2
    