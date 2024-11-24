from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from . import users

app = FastAPI()

class Direction(BaseModel):
    city: str
    country: str
    addres: str

class User(BaseModel):
    name: str
    last_name: str
    age: int = Field(gt=0, description="The age must be positve")
    email: str = Field(pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    phone: int
    direction: Direction

class Column(BaseModel):
    key: str
    value: str
        

@app.get("/users/")
def get_all_users():
    return users.get_all()

@app.get("/user/{id}")
def get_user(id: int):
    return users.get(id)

@app.post("/user")
def create_user(user: Annotated[User, Body(embed=True)]):
    return users.create(user)

@app.put("/user/{id}")
def update_user(id: int, user: Annotated[User, Body(embed=True)]):
    return users.update(id, user)

@app.patch("/user/{id}")
def alter_user(id: int, columns: list[Column]):
    return users.alter(id, columns)

@app.delete("/user/{id}")
def delete_user(id: int):
    return users.delete(id)