from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()


User_db = [ 
    {"Name":"Henshaw", "Location": "Lagos", "Hobby": "Python Programming", "Profession": "Student"},
    {"Name": "Daniel", "Location": "Akwa Ibom", "Hobby": "Graphics Designing", "Profession": "Student"}
    ]

#endpoint with path parameter
@app.get('/user/{user_id}')
async def get_user_details(user_id: int):
    return {"User Details": User_db[user_id]}


#endpoint with query parameter
@app.get('/user/')
async def checkUserDetails(name: Optional[str] = None):    
    for users in User_db:
        if users["Name"] == name:
            return {"User Details": users}
        