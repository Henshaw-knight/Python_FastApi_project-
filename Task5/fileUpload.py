from fastapi import FastAPI, Form, UploadFile, HTTPException
from typing import Optional
from pydantic import BaseModel
import datetime

app = FastAPI()

#Getting the date and time of the upload 
date = datetime.datetime.now()

@app.post("/uploadfile/")
async def create_upload_file(file: Optional[UploadFile] = None, username: str = Form(...)):
    #validation
    if len(username) < 5:
        raise HTTPException(status_code = 422, detail = "Username should have at least 5 characters")
    if file == None:
        raise HTTPException(status_code = 404, detail = "No file found. Kindly upload a file")     
    return {"filename": file.filename, "username": username, "Date_and_time_of_upload": f"{date}"}
