from http import HTTPStatus

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from model_Task import Task, StatusTask
from data_tasks import Tasks


app = FastAPI()
tasks = Tasks()
app.mount('/static', StaticFiles(directory='static'), name="static")
templates = Jinja2Templates(directory='templates')


@app.post("/add", status_code=HTTPStatus.CREATED.value)
def add(title: str = Form(...)):
    tasks.add_task(Task(title=title, status=StatusTask.active))
    return RedirectResponse("/add", status_code=303)


@app.post("/active/{task_id}")
def to_finished(task_id: int):
    tasks.move_to_finished(tasks.get_by_id(task_id))
    return RedirectResponse("/active", status_code=303)


@app.get("/add")
def get_form(request: Request):
    return templates.TemplateResponse("addForm.html", {"request": request})


@app.get("/")
def get_all_tasks(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks.taskList})


@app.get("/active")
def get_actual_tasks(request: Request):
    return templates.TemplateResponse("active.html", {"request": request, "active": tasks.taskList})


@app.get("/finished")
def get_finished_tasks(request: Request):
    return templates.TemplateResponse("finished.html", {"request": request, "finished": tasks.taskList})
