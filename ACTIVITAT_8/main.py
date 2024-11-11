from fastapi import FastAPI
from pydantic import BaseModel
import users

app = FastAPI()

class User(BaseModel):
    name: str
    last_name: str
    age: int
    gender: str
    email: str
    phone: int


@app.post("/create-user")
async def create_user(user: User):
    users.create_user(user.name, user.last_name, user.age, user.gender, user.email, user.phone)
    return {"msg": f"Usuari {user.name} create correctament"}

@app.get("/user/{id}")
def get_user(id: int):
    return users.get_user(id)