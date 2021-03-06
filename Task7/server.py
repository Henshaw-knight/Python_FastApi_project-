"""A project to create JWT token and decode same"""

from fastapi import FastAPI
# from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from jose import jwt, JWTError
from datetime import datetime

app = FastAPI()

#for jose, we need the secret key, an algorithm and expiration time
SECRET_KEY = "6e9b583150caad16b6aa99063e148daf4fd6cd8a2683fba7ba8b3d050df4b2bb"  
ALGORITHM = "HS256"
EXPIRES_MINUTES = 90

class JWTCreateSchema(BaseModel):
    username: str
    email: EmailStr

class JWTDecodeSchema(BaseModel):
    jwt: str    
    
def create_jwt(data: JWTCreateSchema):
    data_dict = data.dict()
    encoded_token = jwt.encode(data_dict, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_token 

def decode_jwt(token):
    detail = jwt.decode(
        token, str(SECRET_KEY), algorithms = [ALGORITHM]
    )
    return detail    

@app.post("/jwt/")
async def verify(data: JWTCreateSchema):
    jwtdata = JWTCreateSchema(username = data.username, email = data.email)
    jwt = create_jwt(data=jwtdata)
    return {"jwt_token": jwt}

@app.get("/jwt/")
async def reveal(data: JWTDecodeSchema):
    data_dict = data.dict()
    jwtdata = data_dict["jwt"]
    detail = decode_jwt(jwtdata)
    return {"detail": detail}

