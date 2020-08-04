import pytest
from data_tasks import ToDoList
from model_Task import Task, StatusTask


@pytest.fixture()
def todo_list():
    tdl = ToDoList()
    return tdl


@pytest.fixture()
def task():
    return Task(title="Hello", status=StatusTask.active)


def test_add_task(todo_list, task):
    todo_list.add_task(todo_list, task)
    print(todo_list.taskList)
    assert len(todo_list.taskList) == 1


def test_move_to_finished(todo_list, task):
    todo_list.add_task(task)
    todo_list.move_to_finished(task)
    assert task.status == StatusTask.finished
