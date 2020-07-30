import pytest
from data_tasks import add_task, taskList
from model_Task import Task, StatusTask


@pytest.mark.parametrize(
    'task',
    [Task(title="hello", status=StatusTask.active)]
)
def test_add_task(task):
    add_task(task)
    print(taskList)
    assert len(taskList) == 1
