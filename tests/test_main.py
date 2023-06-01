from fakeredis import FakeStrictRedis
from taskman.main import create_task, get_task, get_tasks,TaskRequest, Task


def test_save_and_get_item():
    r = FakeStrictRedis()
    id = create_task(TaskRequest(
        name='Test Task',
        description='Demo',
    ), r)
    assert get_task(id, r) == Task(name='Test Task', description='Demo', id=id)


def test_save_and_get_items():
    r = FakeStrictRedis()
    create_task(TaskRequest(
        name='Test Task',
        description='Demo',
    ), r)
    create_task(TaskRequest(
        name='Test Task 2',
        description='Demo 2',
    ), r)
    tasks = get_tasks(r)
    assert len(tasks)==2

