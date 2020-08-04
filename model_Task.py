from pydantic import BaseModel
from typing import Optional
from enum import Enum


class StatusTask(str, Enum):
    active = "active"
    finished = "finished"


class Task(BaseModel):
    id: Optional[int]
    title: str
    status: StatusTask
