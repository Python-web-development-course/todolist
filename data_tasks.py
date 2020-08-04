from typing import List
from model_Task import Task, StatusTask
from pydantic import BaseModel


class ToDoList(BaseModel):
    taskList: List[Task] = []

    def add_task(self, task: Task) -> None:
        self.taskList.append(task)

    def move_to_finished(self, task: Task) -> None:
        index: int = self.taskList.index(task)
        task.status = StatusTask.finished
        self.taskList[index].status = StatusTask.finished
