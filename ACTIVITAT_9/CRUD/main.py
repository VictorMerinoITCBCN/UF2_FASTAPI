from fastapi import FastAPI
from pydantic import BaseModel
from . import users

app = FastAPI()

class User(BaseModel):
    name: str
    last_name: str
    age: int
    email: str
    phone: int

class Column(BaseModel):
    key: str
    value: str
        

@app.get("/user/{id}")
def get_user(id: int):
    return users.get(id)

@app.post("/user")
def create_user(user: User):
    return users.create(user)

@app.put("/user/{id}")
def update_user(id: int, user: User):
    return users.update(id, user)

@app.patch("/user/{id}")
def alter_user(id: int, columns: list[Column]):
    return users.alter(id, columns)

@app.delete("/user/{id}")
def delete_user(id: int):
    return users.delete(id)