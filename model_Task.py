from pydantic import BaseModel
from enum import Enum


class StatusTask(str, Enum):
    active = "active"
    finished = "finished"


class Task(BaseModel):
    title: str
    status: StatusTask
