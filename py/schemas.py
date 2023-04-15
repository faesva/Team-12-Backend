from typing import Optional
from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    id: Optional[int]
    is_admin: bool | None = None
    username: str
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: str
    password: str

    class Config:
        orm_mode = True


class Movie(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    category_id: Optional[int]
    title: str
    sipnosis: str
    director: str
    release_date: date

    class Config:
        orm_mode = True


class MovieUpdate(BaseModel):
    category_id: Optional[int]
    title: str
    sipnosis: str
    director: str
    release_date: str

    class Config:
        orm_mode = True


class Response(BaseModel):
    message: str