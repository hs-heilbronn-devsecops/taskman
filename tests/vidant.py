Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@jeetpatel2059 
hhn-secops-projectgrp-vrock
/
taskman
Public
forked from hs-heilbronn-devsecops/taskman
Fork your own copy of hhn-secops-projectgrp-vrock/taskman
Code
Pull requests
Actions
Projects
Security
Insights
Settings
Beta Try the new code view
taskman/tests/jeet_main.py /
@jeetpatel2059
jeetpatel2059 Create jeet_main.py
Latest commit f68d408 2 minutes ago
 History
 1 contributor
25 lines (20 sloc)  640 Bytes
 

from taskman.main import create_task, get_task, get_tasks,TaskRequest, Task, delete_tasks


def test_save_and_get_item():
    delete_tasks()
    create_task(TaskRequest(
        name='Test Task',
        description='Demo',
    ))
    assert get_task('1') == Task(name='Assignemnt Task', description='Demo', item_id=1)


def test_save_and_get_items():
    delete_tasks()
    create_task(TaskRequest(
        name='Assignemnt Task',
        description='Assignemnt 1',
    ))
    create_task(TaskRequest(
        name='Assignemnt Task 2',
        description='Assignemnt 1 - second',
    ))
    tasks = get_tasks()
    assert len(tasks)==2
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
