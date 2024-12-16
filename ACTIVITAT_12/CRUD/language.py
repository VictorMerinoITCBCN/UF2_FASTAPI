from fastapi import APIRouter
from pydantic import BaseModel
from services import lang_services

router = APIRouter()

class Lang(BaseModel):
    id: str
    name: str

@router.get("/languages")
def get():
    return lang_services.get_languages()

@router.post("/language")
def post(lang: Lang):
    return lang_services.add_language(lang) 

@router.put("/language")
def put(lang: Lang):
    return lang_services.update_language(lang)

@router.delete("/language/{lang_id}")
def delete(lang_id: str):
    return lang_services.delete_language(lang_id)