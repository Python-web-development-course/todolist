from typing import List
from model_Task import Task, StatusTask


class Tasks:
    def __init__(self):
        self.taskList = []

    def add_task(self, task: Task) -> None:
        task.id = id(task)
        self.taskList.append(task)

    def move_to_finished(self, task: Task) -> None:
        index: int = self.taskList.index(task)
        task.status = StatusTask.finished
        self.taskList[index].status = StatusTask.finished

    def get_task_by_id(self, task_id):
        for task in self.taskList:
            if task.id == task_id:
                return task
