from fastapi import FastAPI, HTTPException
from database import create_start_app_handler
from models import Task
from schemas import TaskCreate, TaskPublicSchema
from typing import List

def get_application():

    # start the application.
    app = FastAPI()

    #connect to database.
    app.add_event_handler("startup", create_start_app_handler(app))

    return app

app = get_application()


@app.post("/", response_model = TaskPublicSchema)
async def home(data: TaskCreate):     
    task = await Task.create(
        **data.dict(exclude_unset=True)
    )
    if data.is_completed == False:
        raise HTTPException(status_code= 400, detail= "Your task is incomplete, however the draft has been saved to the database.")
        
    return task

@app.get("/", response_model = List[TaskPublicSchema])
async def home():
    return await Task.all()