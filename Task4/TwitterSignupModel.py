from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
import datetime

app = FastAPI()

class User(BaseModel):
    name: str = Field(..., max_length=50)
    phone_no: int
    email: Optional[EmailStr] = None
    date_of_birth: datetime.date
    password: str = Field(..., min_length=8) 
    

@app.post("/users/{user_id}/")
async def signup(user_id: int, user: User):
    """Create your account"""
    return {"user_id": user_id, **user.dict()}

