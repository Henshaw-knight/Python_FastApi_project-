from fastapi import FastAPI, Path, HTTPException
from typing import Optional, List
from pydantic import BaseModel
import datetime

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    message: str
    createDate: datetime.date

#Model to update existing user detail (message only)
class UpdateUserDetail(BaseModel):    
    message: Optional[str] = None
    


db =  [{"id":1, "name": "Henshaw", "age": 17, "message": "Hello", "createDate": "2022-03-19"}]


#Various fastAPI methods
@app.get("/")
def index():
    return db


#Only the message is meant to be updated
@app.put("/update-user/{user_id}")
def update_user(user_id: int, user: UpdateUserDetail):
    for each_user in db:
        user = user.dict() #converted to a dictionary
        if each_user['id'] == user_id:
            each_user['message'] = user['message'] 

            return db

        raise HTTPException(status_code= 404, detail=f'user with id {user_id} does not exist.')



# @app.post("/create-user/{user_id}")
# def create_user(user_id: int, user: User):
#     user = user.dict() #converted to a dictionary
#     for each_user in db:
#         if each_user["id"] == user_id:
#             raise HTTPException(status_code = 406, detail = f'user with id {user_id} already exists')
             
#     db.append(user)
#     return user  

    

# @app.delete("/delete-user/{user_id}")
# def delete_user(user_id: int):
#     for each_user in db:
#         if each_user['id'] == user_id:
#             del each_user
#             return {"Message": "User has been successfully deleted"}
#         raise HTTPException(status_code=404, detail=f"user with id {user_id} not found")    
    