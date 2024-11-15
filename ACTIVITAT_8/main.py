from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import Union
import users

app = FastAPI()

class User(BaseModel):
    name: str
    last_name: str
    age: int
    gender: str
    email: str
    phone: int

class Modification(BaseModel):
    key: str
    value: Union [str, int]

@app.post("/create-user")
async def create_user(user: User):
    users.create_user(user.name, user.last_name, user.age, user.gender, user.email, user.phone)
    return {"msg": f"Usuari {user.name} creat correctament"}

@app.get("/user/{id}")
def get_user(id: int, response: Response):
    user = users.get_user(id)

    if user: return user
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "Usuari no trobat"}

@app.put("/user/{id}")
def update_user(id: int, user: User, response: Response):
    updated_user = users.update_user(id, user.name, user.last_name, user.age, user.gender, user.email, user.phone)

    if updated_user: return {"msg": f"Usuari amb id '{id}' actualitzat correctament"}
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "Usuari no trobat"}

@app.patch("/user/{id}")
def modify_user(id: int, modification: Modification, response: Response):
    modified_user = users.modify_user(id, modification.key, modification.value)

    if modified_user: return modified_user
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "Usuari no trobat"}