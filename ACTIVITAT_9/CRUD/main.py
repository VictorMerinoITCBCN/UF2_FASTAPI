from typing import Annotated

from fastapi import FastAPI, Body
from schemas import users_schemas
from . import users

app = FastAPI()
        
@app.get("/users/")
def get_all_users():
    return users_schemas.get_all()

@app.get("/user/{id}")
def get_user(id: int):
    return users.get(id)

@app.post("/user")
def create_user(user: Annotated[users_schemas.User, Body(embed=True)]):
    return users.create(user)

@app.put("/user/{id}")
def update_user(id: int, user: Annotated[users_schemas.User, Body(embed=True)]):
    return users.update(id, user)

@app.patch("/user/{id}")
def alter_user(id: int, columns: list[users_schemas.Column]):
    return users.alter(id, columns)

@app.delete("/user/{id}")
def delete_user(id: int):
    return users.delete(id)