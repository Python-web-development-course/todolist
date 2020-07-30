from http import HTTPStatus

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from model_Task import Task, StatusTask
from data_tasks import taskList, add_task, move_to_finished


import this

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name="static")
templates = Jinja2Templates(directory='templates')


@app.post("/add", status_code=HTTPStatus.CREATED.value)
def add(request: Request, title: str = Form(...)):
    new_task: Task = Task(title=title, status=StatusTask.active)
    add_task(new_task)
    return templates.TemplateResponse("addForm.html", {"request": request})


@app.post("/active/{title}")
def to_finished(request: Request, title: str):
    task: Task = Task(title=title, status=StatusTask.active)
    move_to_finished(task)
    return templates.TemplateResponse("active.html", {"request": request, "active": taskList})


@app.get("/add")
def get_form(request: Request):
    return templates.TemplateResponse("addForm.html", {"request": request})


@app.get("/")
def get_all_tasks(request: Request):
    return templates.TemplateResponse("all.html", {"request": request, "tasks": taskList})


@app.get("/active")
def get_actual_tasks(request: Request):
    return templates.TemplateResponse("active.html", {"request": request, "active": taskList})


@app.get("/finished")
def get_finished_tasks(request: Request):
    return templates.TemplateResponse("finished.html", {"request": request, "finished": taskList})
