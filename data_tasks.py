from typing import List
from model_Task import Task, StatusTask


taskList: List[Task] = []


def add_task(task: Task) -> None:
    taskList.append(task)


def move_to_finished(task: Task) -> None:
    index: int = taskList.index(task)
    taskList[index].status = StatusTask.finished
