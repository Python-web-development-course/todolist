import pytest
from data_tasks import taskList, move_to_finished, add_task
from model_Task import Task, StatusTask


@pytest.mark.parametrize(
    'task',
    [Task(title="hello", status=StatusTask.active), Task(title="no", status=StatusTask.finished)]
)
def test_move_to_finished(task):
    add_task(task)
    # print(taskList)
    for this_task in taskList:
        move_to_finished(this_task)
        assert this_task.status == StatusTask.finished
