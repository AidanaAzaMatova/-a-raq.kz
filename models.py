# models.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    username: EmailStr
    phone: str
    password: str
    name: str
    city: str

class Token(BaseModel):
    access_token: str
    token_type: str
