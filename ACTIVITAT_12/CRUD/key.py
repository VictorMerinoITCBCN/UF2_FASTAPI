from fastapi import APIRouter
from services import key_services
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class Key(BaseModel):
    id: Optional[int]
    lang_id: str
    character: str

@router.get("/keys")
def get():
    return key_services.get_keys()

@router.post("/key")
def post(key: Key):
    return key_services.add_key(key)

@router.put("/key")
def put(key: Key):
    return key_services.update_key(key)

@router.delete("/key/{key_id}")
def delete(key_id: int):
    return key_services.delete_key(key_id)